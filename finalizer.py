import json

def extract_LOs(json_response):
    all_processed = [value["LO"] for key, value in json_response.items()]
    return all_processed


def process_raw():
    with open("raw.json", "r") as file:
        data = json.load(file)

    results = {}
    for category, unprocessed in data.items():
        all_processed = []
        for raw_json in unprocessed:
            processed = extract_LOs(raw_json)
            for text in processed:
                all_processed.append(text)
        results[category] = all_processed

    with open("processed.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "main":
    process_raw()
    print("finished. your results are now in processed.py")