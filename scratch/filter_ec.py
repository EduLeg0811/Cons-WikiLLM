import json
import os

file_path = r"d:\APPS\SIMPLE\_Wiki LLM\Wiki - v1\corpus\ec.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

original_count = len(data["records"])
print(f"Original records count: {original_count}")

# Print unique authors to see who is there
authors = set()
for r in data["records"]:
    author = r.get("metadata", {}).get("author")
    if author:
        authors.add(author)
print(f"Unique authors found: {authors}")

# Filter records
filtered_records = [
    r for r in data["records"]
    if r.get("metadata", {}).get("author") == "Waldo Vieira"
]

new_count = len(filtered_records)
print(f"Filtered records count: {new_count}")

data["records"] = filtered_records
# Let's count unique rows (or semantic rows)
data["semantic_rows"] = new_count
# Let's count how many unique row IDs there are to estimate source_rows
unique_rows = len(set(r.get("row") for r in filtered_records))
data["source_rows"] = unique_rows

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Finished filtering.")
