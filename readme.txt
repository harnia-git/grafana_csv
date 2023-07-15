csvファイルをブラウザ経由でinfluxにアップロードする
timeレンジを絞る
クエリ(1行消す)
influx2の認証は基本的にトークンで行う
influxDBのHTTPエンドポイントは、docker-compose psでNAMEを確認して、設定する
http://localhost:8086 ではとおらず、
http://local-influxdb:8086 のようにNAMEを使うととおる
configure?か何か認証は、トークンで行う

grafana→datasource settingは次のとおり
Name　influxDB
QueryLanguage　Flux
Connection　url:http://local-influxdb:8086
Organizastion,token,buckt  ->influxDBのmember-aboutで調べて入力する


----
from(bucket: “weather-data”)
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == “temperature”)

.\influx query 'from(bucket:\"buoy-sample\") |> range(start:-30m)'
----
from(bucket: "weather-data")
  |> range(start: -10m)
  |> filter(fn: (r) => r.measurement == "temperature")
  |> mean()

  .\influx query 'from(bucket:\"buoy-sample\") |> range(start:-30m) |> mean()'
  ------

  from(bucket: "buoy_monitor")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "buoy_surroundings")
  |> filter(fn: (r) => r["_field"] == "Rssi")
  |> yield(name: "mean")