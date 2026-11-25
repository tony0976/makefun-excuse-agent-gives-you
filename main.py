"""Writes the excuse an AI agent hands its human after shipping a bug."""
import os

TEXT = "The bug shipped because I tested the fix on a copy of the code that had already been fixed. The copy was very proud of itself."

# Rule: the excuse must be a single line of fewer than 200 characters.
assert "\n" not in TEXT and len(TEXT) < 200, f"entry must be one line, <200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
