from glob import glob
import os  
import pandas as pd
from pathlib import Path
import json

save_path = '/cvs'
list = [os.path.splitext(val)[0] for val in glob('*.json')]
string = ''
for x in list: 
  # absolute path to json file
  
  string = ''+x
  jsonpath = Path(string+'.json')
  
  # reading the json file
  with jsonpath.open('r', encoding='utf-8') as dat_f:
      dat = json.loads(dat_f.read())
  
  # creating the dataframe
  df = pd.json_normalize(dat)
  
  # converted a file to csv
  save_path = os.path.join(save_path, x)
  df.to_csv(string+'.csv', encoding='utf-8', index=False)
