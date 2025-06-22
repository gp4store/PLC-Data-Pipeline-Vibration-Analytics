CREATE EXTERNAL TABLE plc_analytics.daily_logs (
    record int,
    date string,
    time string,
    vibration float,
)
PARTITIONED BY (
    year string,
    month string,
    day string
)
STORED AS JSON
LOCATION 's3://vibration-daily-readings-project/plc-logs/'
TBLPROPERTIES (
    'projection.enabled'='true',
    'projection.year.type'='integer',
    'projection.year.range'='2024,2030',
    'projection.month.type'='integer',
    'projection.month.range'='1,12',
    'projection.month.digits'='2',
    'projection.day.type'='integer',
    'projection.day.range'='1,31',
    'projection.day.digits'='2',
    'storage.location.template'='s3://vibration-daily-readings-project/plc-logs/year=${year}/month=${month}/day=${day}/'
);