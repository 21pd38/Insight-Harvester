# Insight-Harvester

## Overview

This is a lightweight, reliable web scraper built in Python that takes a single company website URL as input and outputs a structured JSON profile containing key business information.

The scraper follows the assignment guidelines:
- Crawls only publicly accessible pages (no logins)
- Limits crawling to a maximum of 15 pages
- Prioritises key pages (`/about`, `/products`, `/solutions`, `/pricing`, `/contact`, `/careers`, etc.)
- Handles errors gracefully and logs them
- Extracts signals heuristically without hallucination (uses "Not found" when data is absent)
- Is polite: rotates User-Agents and adds a 1-second delay between requests

## How to Run

1. Save the script as `scraper.py`
2. Install dependencies:
   pip install requests beautifulsoup4

# Run the scraper with a url

python scraper.py https://www.example.com

# Demo for DigitalOcean.com
{
    "identity": {
        "company_name": "DigitalOcean: AI-Powered Unified Agentic Cloud Infrastructure",
        "website_url": "https://www.digitalocean.com",
        "tagline": "Build on DigitalOcean's unified agentic AI cloud infrastructure. AI-powered development, instant deployment, easy management. Simple and affordable."
    },
    "business_summary": {
        "what_they_do": "DigitalOcean: AI-Powered Unified Agentic Cloud Infrastructure Blog Docs Get Support Contact Sales DigitalOcean Products Featured Products Droplets Scalable virtual machines Kubernetes Scale more effectively Gradient™ AI Agentic Cloud Build and scale with AI Cloudways Managed cloud hosting App Platform Get apps to market faster Managed Databases Fully-managed database hosting Compute Droplets Kubernetes CPU-Optimized Droplets Functions App Platform Gradient™ AI Agentic Cloud GPU Droplets 1-Click Models Platform Bare Metal GPUs Backups & Snapshots Backups Snapshots SnapShooter Networking Virtua...",
        "primary_offerings": [
            "About",
            "Leadership",
            "Blog",
            "Careers",
            "Customers",
            "Partners",
            "Referral Program",
            "Affiliate Program",
            "Press",
            "Legal"
        ],
        "target_segments": [
            "About",
            "Leadership",
            "Blog",
            "Careers",
            "Customers",
            "Partners",
            "Referral Program",
            "Affiliate Program",
            "Press",
            "Legal"
        ]
    },
    "evidence_proof": {
        "key_pages_detected": [
            "/",
            "/about",
            "/company",
            "/products",
            "/solutions",
            "/pricing",
            "/contact",
            "/careers",
            "/blog",
            "/customers"
        ],
        "signals_found": [
            "client",
            "customer",
            "partner",
            "case study",
            "award",
            "certification"
        ],
        "social_links": {
            "youtube": "https://www.youtube.com/playlist?list=PLseEp7p6Ewibnv09L_48W3bi2HKiY6lrx",
            "twitter": "https://twitter.com/digitalocean",
            "instagram": "https://www.instagram.com/thedigitalocean/",
            "linkedin": "https://www.linkedin.com/company/digitalocean/",
            "github": "https://github.com/digitalocean"
        }
    },
    "contact_location": {
        "emails": [
            "com"
        ],
        "phones": [],
        "contact_page_url": "https://www.digitalocean.com/contact"
    },
    "team_hiring": {
        "careers_page_url": "https://www.digitalocean.com/careers",
        "open_roles_sample": "Not found"
    },
    "metadata": {
        "timestamp": "2025-12-19T12:22:39.648968",
        "pages_crawled": [
            "https://www.digitalocean.com",
            "https://www.digitalocean.com/",
            "https://www.digitalocean.com/about",
            "https://www.digitalocean.com/company",
            "https://www.digitalocean.com/products",
            "https://www.digitalocean.com/solutions",
            "https://www.digitalocean.com/pricing",
            "https://www.digitalocean.com/contact",
            "https://www.digitalocean.com/careers",
            "https://www.digitalocean.com/blog",
            "https://www.digitalocean.com/customers",
            "https://www.digitalocean.com/support",
            "https://www.digitalocean.com/company/contact/sales?referrer=tophat",
            "https://www.digitalocean.com/products/droplets",
            "https://www.digitalocean.com/products/kubernetes"
        ],
        "total_pages": 15,
        "errors": [
            "https://www.digitalocean.com/team: 404 Client Error: Not Found for url: https://www.digitalocean.com/team",
            "https://www.digitalocean.com/features: 404 Client Error: Not Found for url: https://www.digitalocean.com/features",
            "https://www.digitalocean.com/services: 404 Client Error: Not Found for url: https://www.digitalocean.com/services",
            "https://www.digitalocean.com/jobs: 404 Client Error: Not Found for url: https://www.digitalocean.com/jobs",
            "https://www.digitalocean.com/case-studies: 404 Client Error: Not Found for url: https://www.digitalocean.com/case-studies"
        ]
    }
}

# Demo for Vercel.com
{
    "identity": {
        "company_name": "Vercel: Build and deploy the best web experiences with the AI Cloud",
        "website_url": "https://vercel.com",
        "tagline": "Vercel gives developers the frameworks, workflows, and infrastructure to build a faster, more personalized web."
    },
    "business_summary": {
        "what_they_do": "Vercel: Build and deploy the best web experiences with the AI Cloud Products AI Cloud v0 Build applications with AI AI SDK The AI Toolkit for TypeScript AI Gateway One endpoint, all your models Vercel Agent An agent that knows your stack Sandbox AI workflows in live environments Core Platform CI/CD Helping teams ship 6× faster Content Delivery Fast, scalable, and reliable Fluid Compute Servers, in serverless form Observability Trace every step Security Bot Management Scalable bot protection BotID Invisible CAPTCHA Platform Security DDoS Protection, Firewall Web Application Firewall Granular,...",
        "primary_offerings": [
            "CI/CDHelping teams ship 6× faster",
            "Content DeliveryFast, scalable, and reliable",
            "Fluid ComputeServers, in serverless form",
            "ObservabilityTrace every step",
            "AI",
            "Enterprise",
            "Fluid Compute",
            "Next.js",
            "Observability",
            "Previews"
        ],
        "target_segments": "Not found"
    },
    "evidence_proof": {
        "key_pages_detected": [
            "/",
            "/about",
            "/company",
            "/team",
            "/products",
            "/features",
            "/services",
            "/pricing",
            "/contact",
            "/careers",
            "/jobs",
            "/blog",
            "/customers",
            "/case-studies"
        ],
        "signals_found": [
            "customer",
            "partner",
            "award",
            "certification"
        ],
        "social_links": {
            "github": "https://github.com/vercel",
            "linkedin": "https://linkedin.com/company/vercel",
            "twitter": "https://x.com/vercel",
            "youtube": "https://youtube.com/@VercelHQ"
        }
    },
    "contact_location": {
        "emails": [],
        "phones": [],
        "contact_page_url": "https://vercel.com/contact"
    },
    "team_hiring": {
        "careers_page_url": "https://vercel.com/careers",
        "open_roles_sample": "Not found"
    },
    "metadata": {
        "timestamp": "2025-12-19T12:23:27.965523",
        "pages_crawled": [
            "https://vercel.com",
            "https://vercel.com/",
            "https://vercel.com/about",
            "https://vercel.com/company",
            "https://vercel.com/team",
            "https://vercel.com/products",
            "https://vercel.com/features",
            "https://vercel.com/services",
            "https://vercel.com/pricing",
            "https://vercel.com/contact",
            "https://vercel.com/careers",
            "https://vercel.com/jobs",
            "https://vercel.com/blog",
            "https://vercel.com/customers",
            "https://vercel.com/case-studies"
        ],
        "total_pages": 15,
        "errors": [
            "https://vercel.com/solutions: 404 Client Error: Not Found for url: https://vercel.com/solutions"
        ]
    }
}
