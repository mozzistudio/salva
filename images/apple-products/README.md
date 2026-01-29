# Apple Product Images

This folder is intended to store images of Apple devices/products sourced from `apple.com`.

## Fetching images

Run the helper script from the repository root:

```bash
python scripts/fetch_apple_images.py
```

You can also limit the number of images and pages:

```bash
python scripts/fetch_apple_images.py --limit 10 --max-pages 50
```

The script crawls the Apple sitemap for product-related pages (e.g. `iphone`, `ipad`, `mac`, `watch`, `airpods`) and downloads images referenced on those pages. Adjust `--max-pages` if you need a smaller crawl.

If network access to `apple.com` is blocked in your environment, the script will report a fetch error and no images will be downloaded.
