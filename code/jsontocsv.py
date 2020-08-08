import pandas as pd
df = pd.read_json (r'C:\Users\bryanseah\Downloads\singapore-postal-codes-master\buildings.json')
df.to_csv (r'C:\Users\bryanseah\Downloads\singapore-postal-codes-master\buildings.csv', index = None)
