import pandas as pd
from influxdb import DataFrameClient
import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルから環境変数をロードします

username = os.getenv('INFLUXDB_USERNAME')  # ユーザー名を取得します
password = os.getenv('INFLUXDB_PASSWORD')  # パスワードを取得します
# CSV ファイルを読み込む
df = pd.read_csv('/tmp/influxdb_data_all_result.csv')

# 必要に応じて DataFrame を調整する

# InfluxDBへの接続
client = DataFrameClient('localhost', 8086, username, password, 'data_all_result')

# DataFrameをInfluxDBに書き込む
client.write_points(df, 'buoy_surroundings', protocol='line')
