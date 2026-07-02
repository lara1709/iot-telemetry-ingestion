import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    output = []
    for record in event["records"]:
        data = record["data"]
        if not isinstance(data, dict):
            output.append({
                "recordId": record["recordId"],
                "result": "Dropped",
                "data": record["data"] 
            })
            continue
        data["ingestedAt"] = datetime.now(timezone.utc).isoformat()
        data["deviceType"] = "scooter"
        data["city"] = "Berlin"

        output.append({
            "recordId": record["recordId"],
            "result": "Ok",
            "data": data
        })

    return {"records": output}