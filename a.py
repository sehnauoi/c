import pandas as pd
df = pd.read_json (r'character_data.json')
df.to_csv (r'character_data.csv')
