import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
from datetime import datetime
import re
import random
from collections import deque
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
]

PRIORITY_PATHS = [
    "/", "/about", "/company", "/team",
    "/products", "/solutions", "/features", "/services",
    "/pricing", "/contact", "/careers", "/jobs",
    "/blog", "/customers", "/case-studies"
]

MAX_PAGES = 15
REQUEST_DELAY = 1.0

EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|io|co|edu)'
PHONE_REGEX = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
ADDRESS_KEYWORDS = ["street", "road", "avenue", "blvd", "lane", "drive", "suite", "floor", "building"]

SIGNAL_KEYWORDS = ["client", "customer", "partner", "case study", "testimonial", "award", "certification"]

def get_headers():
    return {"User-Agent": random.choice(USER_AGENTS)}

def is_same_domain(base, url):
    return urlparse(url).netloc == urlparse(base).netloc

def fetch(url):
    time.sleep(REQUEST_DELAY)
    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        if response.status_code in [403, 429]:
            return None, f"Blocked: {response.status_code}"
        response.raise_for_status()
        return response.text, None
    except Exception as e:
        return None, str(e)

def extract_social(soup, base_url):
    social = {}
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if "linkedin.com" in href and "linkedin" not in social:
            social["linkedin"] = urljoin(base_url, a["href"])
        elif "twitter.com" in href or "x.com" in href and "twitter" not in social:
            social["twitter"] = urljoin(base_url, a["href"])
        elif "youtube.com" in href and "youtube" not in social:
            social["youtube"] = urljoin(base_url, a["href"])
        elif "instagram.com" in href and "instagram" not in social:
            social["instagram"] = urljoin(base_url, a["href"])
        elif "github.com" in href and "github" not in social:
            social["github"] = urljoin(base_url, a["href"])
    return social

def extract_list_items(soup, heading_keywords):
    items = []
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
        if any(kw in heading.get_text().lower() for kw in heading_keywords):
            next_ul = heading.find_next(['ul', 'ol'])
            if next_ul:
                for li in next_ul.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    if text and len(text) < 200:
                        items.append(text)
    return items[:10] if items else "Not found"

def scrape_website(start_url):
    base_url = f"{urlparse(start_url).scheme}://{urlparse(start_url).netloc}"
    to_visit = deque([start_url])
    visited = set()
    pages_visited = []
    errors = []
    all_text = ""
    social_links = {}

    for path in PRIORITY_PATHS:
        full = urljoin(base_url, path)
        if full not in to_visit and full != start_url:
            to_visit.append(full)

    while to_visit and len(visited) < MAX_PAGES:
        url = to_visit.popleft()
        if url in visited or not is_same_domain(base_url, url):
            continue

        html, err = fetch(url)
        if err:
            errors.append(f"{url}: {err}")
            continue

        visited.add(url)
        pages_visited.append(url)
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(separator=" ", strip=True)
        all_text += " " + text

        social_links.update(extract_social(soup, base_url))

        for a in soup.find_all("a", href=True):
            link = urljoin(base_url, a["href"])
            parsed = urlparse(link)
            if (is_same_domain(base_url, link) and
                not parsed.fragment and
                link not in visited and
                link not in to_visit and
                not any(skip in parsed.path.lower() for skip in ['login', 'signup', 'cart'])):
                to_visit.append(link)

    homepage_html, _ = fetch(start_url)
    home_soup = BeautifulSoup(homepage_html, 'html.parser') if homepage_html else None

    company_name = (home_soup.title.string.strip() if home_soup and home_soup.title else "Not found")
    tagline = (home_soup.find("meta", {"name": "description"})["content"]
               if home_soup and home_soup.find("meta", {"name": "description"}) else "Not found")

    what_they_do = all_text[:600].strip() + "..." if all_text else "Not found"

    offerings = extract_list_items(home_soup, ["product", "solution", "feature", "service", "offering", "platform"])
    segments = extract_list_items(home_soup, ["industry", "sector", "customer", "market", "serve"])

    emails = list(set(re.findall(EMAIL_REGEX, all_text)))
    phones = list(set([p.strip() for p in re.findall(PHONE_REGEX, all_text) if p.strip()]))

    signals_found = [kw for kw in SIGNAL_KEYWORDS if kw in all_text.lower()]

    key_pages = [path for path in PRIORITY_PATHS if urljoin(base_url, path) in visited]

    contact_url = urljoin(base_url, "/contact") if "/contact" in [p.lower() for p in key_pages] else "Not found"
    careers_url = urljoin(base_url, "/careers") if any(c in [p.lower() for p in key_pages] for c in ["/careers", "/jobs"]) else "Not found"

    roles = extract_list_items(home_soup, ["opening", "position", "role", "hiring"]) if careers_url != "Not found" else "Not found"

    result = {
        "identity": {
            "company_name": company_name,
            "website_url": start_url,
            "tagline": tagline
        },
        "business_summary": {
            "what_they_do": what_they_do,
            "primary_offerings": offerings,
            "target_segments": segments
        },
        "evidence_proof": {
            "key_pages_detected": key_pages,
            "signals_found": signals_found,
            "social_links": social_links
        },
        "contact_location": {
            "emails": emails,
            "phones": phones,
            "contact_page_url": contact_url
        },
        "team_hiring": {
            "careers_page_url": careers_url,
            "open_roles_sample": roles
        },
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "pages_crawled": pages_visited,
            "total_pages": len(pages_visited),
            "errors": errors
        }
    }

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="General Company Website Scraper")
    parser.add_argument("url", help="Website URL to scrape (e.g., https://hubspot.com)")
    args = parser.parse_args()

    data = scrape_website(args.url)
    print(json.dumps(data, indent=4, ensure_ascii=False))