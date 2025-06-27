CREATE EXTERNAL TABLE plc_analytics.daily_logs (
    record string,
    date string,
    time string,
    vibration float
)
PARTITIONED BY (
    year string,
    month string,
    day string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
) 
LOCATION 's3://your-bucket-name/plc-logs/'
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
    'storage.location.template'='s3://your-bucket-name/plc-logs/year=${year}/month=${month}/day=${day}/'
);