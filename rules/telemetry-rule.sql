SELECT 
  deviceId,
  timestamp,
  gps.lat AS latitude,
  gps.lon AS longitude,
  battery,
  speed
FROM
'scooter/+/telemetry'
INSERT INTO
  'FirehoseDeliveryStream'