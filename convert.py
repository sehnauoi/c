from glob import glob
import os
# import pandas as pd

# list = glob.glob("*.json")
# for files in list:  

  
list = [os.path.splitext(val)[0] for val in glob('*.json')]
print(list)
# df = pd.read_json (r"common.json")
# df.to_csv (r"common.csv")
for x in list:
    # Process each file here
    # os.system("a.py")
    os.system("a.py "+x+".json"+" "+x+".csv")
