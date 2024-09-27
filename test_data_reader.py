import json


class TestDataReader:
    with open('test_data.json', 'r') as f:
        test_data = json.load(f)
