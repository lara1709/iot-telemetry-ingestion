import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    output = []
    for record in event["records"]:
        data = json.loads(record["data"])
        lat = round(data.get("lat", 0), 6)
        lon = round(data.get("lon", 0), 6)
        speed = data.get("speed", 0)
        battery = data.get("battery", 0)
        events = data.get("events", [])
        
        if battery < 10:
            battery_status = "CRITICAL"
        elif battery < 20:
            battery_status = "LOW"
        else:
            battery_status = "OK"

        if speed > 20:
            speed_status = "OVERSPEED"
        else: 
            speed_status = "NORMAL"

        if battery_status == "CRITICAL" or "crashDetected" in events:
            device_health = "CRITICAL"
        elif battery_status == "LOW" or "hardBrake" in events:
            device_health = "WARNING"
        else:
            device_health = "GOOD"

        enriched = {
            "deviceId": data.get("deviceId"),
            "lat": lat,
            "lon": lon,
            "speed": speed,
            "battery": battery,
            "events": events,
            "batteryStatus": battery_status,
            "speedStatus": speed_status,
            "deviceHealth": device_health,
            "ingestedAt": datetime.now(timezone.utc).isoformat()
        }

        output.append({
            "recordId": record["recordId"],
            "result": "Ok",
            "data": enriched
        })

    return {"records": output}