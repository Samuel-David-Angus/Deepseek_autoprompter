import json
import re

def remove_enumeration(json_response):
    pattern = r'^Question\s+\d+:\s*'
    all_processed = [re.sub(pattern, '', item["processed"]) for item in json_response["PREPROCESSED_TEXT"]]
    return all_processed

with open("raw.json", "r") as file:
    data = json.load(file)

results = {}

for category, unprocessed in data.items():
    all_processed = []
    for raw_json in unprocessed:
        processed = remove_enumeration(raw_json)
        for text in processed:
            all_processed.append(text)
    results[category] = all_processed

with open("processed.json", "w") as file:
    json.dump(results, file, indent=4)
