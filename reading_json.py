# Reading a JSON file in Python

# 1
import json
with open('data.json') as f:
  data = json.load(f)
print(data)

# 2
import pandas as pd
df=pd.read_json('data.json')
print(df)