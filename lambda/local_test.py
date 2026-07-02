import json
from firehose_transform import lambda_handler

with open("test_event.json") as f:
    event = json.load(f)

result = lambda_handler(event, None)
print(json.dumps(result, indent=2))
