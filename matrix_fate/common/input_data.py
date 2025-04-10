import json

def normalize_input_data(data: dict) -> dict:
    return json.loads(json.dumps(data, sort_keys=True))
