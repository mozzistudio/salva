#!/usr/bin/env python3
"""Fetch Apple product/device images from apple.com pages."""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

PRODUCT_KEYWORDS = [
    "iphone",
    "ipad",
    "mac",
    "macbook",
    "imac",
    "watch",
    "airpods",
    "vision",
    "homepod",
    "apple-tv",
    "appletv",
]

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Apple product images from apple.com.")
    parser.add_argument(
        "--output-dir",
        default="images/apple-products",
        help="Directory to store downloaded images.")
    parser.add_argument(
        "--base-url",
        default="https://www.apple.com/",
        help="Apple base URL to crawl.")
    parser.add_argument(
        "--sitemap-url",
        default="https://www.apple.com/sitemap.xml",
        help="Sitemap URL to discover product pages.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit the number of images to download (0 = no limit).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Limit the number of pages to crawl (0 = no limit).",
    )
    return parser.parse_args()


def fetch_html(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def fetch_xml(url: str) -> str:
    return fetch_html(url)


def extract_sitemap_urls(xml_text: str) -> list[str]:
    urls = []
    try:
        root = ElementTree.fromstring(xml_text)
    except ElementTree.ParseError:
        return urls
    for loc in root.iter():
        if loc.tag.endswith("loc") and loc.text:
            urls.append(loc.text.strip())
    return urls


def gather_sitemap_urls(sitemap_url: str) -> list[str]:
    xml_text = fetch_xml(sitemap_url)
    urls = extract_sitemap_urls(xml_text)
    sitemap_urls = [url for url in urls if url.endswith(".xml")]
    if sitemap_urls:
        nested = []
        for url in sitemap_urls:
            try:
                nested.extend(extract_sitemap_urls(fetch_xml(url)))
            except Exception:  # noqa: BLE001
                continue
        return nested
    return urls


def extract_image_urls(html: str, base_url: str) -> list[str]:
    urls = set()
    urls.update(re.findall(r'src="([^"]+)"', html))
    urls.update(re.findall(r'data-src="([^"]+)"', html))
    for match in re.findall(r'srcset="([^"]+)"', html):
        for part in match.split(","):
            candidate = part.strip().split(" ")[0]
            if candidate:
                urls.add(candidate)

    normalized = []
    for url in urls:
        if url.startswith("//"):
            url = f"https:{url}"
        else:
            url = urllib.parse.urljoin(base_url, url)
        normalized.append(url)
    return normalized


def is_product_page(url: str) -> bool:
    lowered = url.lower()
    return any(keyword in lowered for keyword in PRODUCT_KEYWORDS)


def is_image_url(url: str) -> bool:
    lowered = url.lower().split("?")[0]
    return lowered.endswith(IMAGE_EXTENSIONS)


def filter_product_images(
    urls: list[str],
    page_url: str,
) -> list[str]:
    filtered = []
    page_is_product = is_product_page(page_url)
    for url in urls:
        if not url.startswith("http"):
            continue
        lowered = url.lower()
        if not is_image_url(lowered):
            continue
        if page_is_product or any(keyword in lowered for keyword in PRODUCT_KEYWORDS):
            filtered.append(url)
    return filtered


def download_images(urls: list[str], output_dir: Path, limit: int) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded = 0

    for url in urls:
        if limit and downloaded >= limit:
            break
        parsed = urllib.parse.urlparse(url)
        filename = Path(parsed.path).name
        if not filename:
            filename = hashlib.md5(url.encode("utf-8")).hexdigest() + ".img"
        destination = output_dir / filename
        if destination.exists():
            continue
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120 Safari/537.36"
                    )
                },
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                destination.write_bytes(response.read())
            downloaded += 1
            print(f"Downloaded {url} -> {destination}")
        except Exception as exc:  # noqa: BLE001
            print(f"Failed to download {url}: {exc}", file=sys.stderr)
    return downloaded


def main() -> int:
    args = parse_args()
    try:
        sitemap_urls = gather_sitemap_urls(args.sitemap_url)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to fetch sitemap {args.sitemap_url}: {exc}", file=sys.stderr)
        sitemap_urls = []

    page_urls = [args.base_url]
    page_urls.extend([url for url in sitemap_urls if url.startswith(args.base_url)])
    page_urls = list(dict.fromkeys(page_urls))
    if args.max_pages:
        page_urls = page_urls[: args.max_pages]

    all_image_urls: list[str] = []
    for page_url in page_urls:
        if not page_url.startswith(args.base_url):
            continue
        if not is_product_page(page_url) and page_url != args.base_url:
            continue
        try:
            html = fetch_html(page_url)
        except Exception as exc:  # noqa: BLE001
            print(f"Failed to fetch {page_url}: {exc}", file=sys.stderr)
            continue
        urls = extract_image_urls(html, page_url)
        all_image_urls.extend(filter_product_images(urls, page_url))

    if not all_image_urls:
        print("No product image URLs found.")
        return 1

    unique_urls = sorted(set(all_image_urls))
    downloaded = download_images(unique_urls, Path(args.output_dir), args.limit)
    print(f"Downloaded {downloaded} images.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
