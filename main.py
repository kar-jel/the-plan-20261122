import os
from pathlib import Path

plan = "Today: scrape 20 Shopify apps' newest 1-star reviews; publish a 10-row sample. Pitch 30 Shopify agencies daily: weekly, source-linked 50-complaint CSVs for $39 via Stripe. After 100 pitches, stop if fewer than 2 replies. 30-day target: 4 clients ($156)."
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(plan, encoding="utf-8")
