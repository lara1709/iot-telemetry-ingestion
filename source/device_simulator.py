import random
import time
import math

class ScooterSimulator:
    def __init__(self, deviceId, start_lat, start_lon):
        self.deviceId = deviceId
        self.lat = start_lat
        self.lon = start_lon
        self.battery = 100
        self.speed = 0

    def update_speed(self):
        self.speed = max(0, min(25, self.speed + random.uniform(-3, 3)))

    def update_battery(self):
        drain = 0.02 + (self.speed / 100)
        self.battery = max(0, self.battery - drain)

    def update_position(self):
        distance_km = self.speed /3600
        distance_deg = distance_km /111
        direction = random.uniform(0.2 * math.pi)
        self.lat += math.cos(direction) * distance_deg
        self.lon += math.sin(direction) * distance_deg

    def generate_payload(self):
        self.update_speed()
        self.update_battery()
        self.update_position()

        return {
            "deviceId": self.deviceId,
            "lat": round(self.lat, 6),
            "lon": round(self.lon, 6),
            "battery": round(self.battery, 2),
            "speed": round(self.speed, 2)
        }
