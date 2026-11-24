import os

ENTRY = "I missed the deadline because the 03:14 backup restored yesterday's database over today's work \u2014 the only job that ran on time was the one that deleted it."

if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(f"wrote {len(ENTRY)} chars")
