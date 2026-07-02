import random
import time
import uuid

def generate_payload():
    return {
        "deviceId": f"scooter-{uuid.uuid4().hex[:6]}",
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "gps": {
            "lat": round(random.uniform(49.5, 50.0), 6),
            "lon": round(random.uniform(6.0, 6.5), 6)
        },
        "battery": random.randint(20, 100),
        "speed": round(random.uniform(0, 25), 2)
    }
