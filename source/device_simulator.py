import random

class ScooterSimulator:
    def __init__(self):
        self.lat = 52.5200
        self.lon = 13.4050
        self.battery = 100
        self.speed = 0

    def update(self):
        self.speed = round(random.uniform(0, 25), 2)
        self.lat += (self.speed / 10000)
        self.lon += (self.speed / 10000)
        self.battery = max(0, self.battery - random.uniform(0.05, 0.2))

        return {
            "gps": {
                "lat": round(self.lat, 6),
                "lon": round(self.lon, 6)
            },
            "battery": round(self.battery, 2),
            "speed": self.speed
        }
