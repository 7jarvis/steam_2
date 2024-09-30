import json


class TestDataReader:
    with open('tests/test_data.json', 'r') as f:
        test_data = json.load(f)
