import time
from source.device_simulator import ScooterSimulator

def create_fleet(count):
    fleet = []
    start_lat = 52.5200
    start_lon = 13.4050
    for i in range(count):
        scooter = ScooterSimulator(
            deviceId=f"scooter-{i+1}",
            start_lat=start_lat + (i * 0.0005),
            start_lon=start_lon + (i * 0.0005)
        )
        fleet.append(scooter)
    return fleet

def run_fleet_simulation(count=10, interval=1):
    fleet = create_fleet(count)
    while True:
        for scooter in fleet:
            payload = scooter.generate_payload()
            print(payload)
        time.sleep(interval)

if __name__ == "__main__":
    run_fleet_simulation(count=10, interval=1)