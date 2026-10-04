#!/usr/bin/env python3
"""Add a Google review-volume confidence check to a pipeline CSV.

Brad's volume rule (4 Oct 2026). Star rating alone is not trusted; it is
weighed against how many reviews stand behind it:

  Strong        rating >= 4.5 and reviews >= 50   (robust social proof)
  Moderate      everything between the other bands
  Questionable  reviews < 10, including no rating at all (too little
                statistical weight, or a dormant listing), unless Poor
  Poor          rating < 3.0 with reviews >= 10   (bad reputation with
                meaningful volume)

How it affects triage (only rows already marked "Send to Clay" change):
  Strong        -> Send to Clay, priority 1
  Moderate      -> Send to Clay, priority 2
  Questionable  -> Send to Clay, priority 3 (last in the queue), flag L11
  Poor          -> Hold for Brad (no Clay spend), flag L12

Review confidence never sets the tier: tiers come only from staff counts.

Usage:
  python3 scripts/review_confidence.py <in.csv> [--out <out.csv>]
The input needs `rating` and `reviews_count` columns (scraper or triage
format). Without --out the file is updated in place.
"""

import argparse
import csv
import sys

STRONG_MIN_RATING = 4.5
STRONG_MIN_REVIEWS = 50
LOW_SIGNAL_MAX_REVIEWS = 10   # fewer than this is "extremely low"
POOR_MAX_RATING = 3.0
POOR_MIN_REVIEWS = 10         # "meaningful volume"

PRIORITY = {"Strong": 1, "Moderate": 2, "Questionable": 3, "Poor": ""}
FLAG = {"Questionable": "L11_low_review_signal", "Poor": "L12_poor_reputation"}


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def classify(rating, reviews):
    """Return (band, reason) for one listing."""
    rating = to_float(rating)
    reviews = int(to_float(reviews) or 0)
    if rating is None or reviews == 0:
        return "Questionable", "no Google reviews"
    if rating < POOR_MAX_RATING and reviews >= POOR_MIN_REVIEWS:
        return "Poor", "{:g} stars across {} reviews".format(rating, reviews)
    if reviews < LOW_SIGNAL_MAX_REVIEWS:
        return "Questionable", "only {} review(s) behind {:g} stars".format(reviews, rating)
    if rating >= STRONG_MIN_RATING and reviews >= STRONG_MIN_REVIEWS:
        return "Strong", "{:g} stars across {} reviews".format(rating, reviews)
    return "Moderate", "{:g} stars across {} reviews".format(rating, reviews)


def append_note(existing, extra):
    existing = (existing or "").strip()
    return "{}; {}".format(existing, extra) if existing else extra


def apply(rows):
    for row in rows:
        band, reason = classify(row.get("rating"), row.get("reviews_count"))
        row["review_confidence"] = band
        row["review_confidence_reason"] = reason
        sending = row.get("next_step", "").startswith("Send to Clay")
        row["clay_priority"] = PRIORITY[band] if sending else ""
        if sending and band in FLAG:
            if "precheck_flag" in row:
                row["precheck_flag"] = append_note(row.get("precheck_flag"), FLAG[band])
            if band == "Poor":
                row["next_step"] = "Hold for Brad"
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("csv_in")
    parser.add_argument("--out", default="")
    args = parser.parse_args(argv)

    with open(args.csv_in, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    missing = {"rating", "reviews_count"} - set(fields)
    if missing:
        sys.exit("ERROR: input is missing column(s): {}".format(", ".join(sorted(missing))))

    rows = apply(rows)
    for col in ("review_confidence", "review_confidence_reason", "clay_priority"):
        if col not in fields:
            fields.append(col)

    out = args.out or args.csv_in
    with open(out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["review_confidence"]] = counts.get(row["review_confidence"], 0) + 1
    print("Review confidence: " + ", ".join("{} {}".format(k, v) for k, v in sorted(counts.items())))
    print("Written: {}".format(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
