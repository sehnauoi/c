import urllib.request
import os
import requests
import UnityPy

#data lists
raw = []
file = []
hash = []
id = []
name = []

def get_files(): # get data from url

    # Get manifest_bg.txt
    url1 = "https://raw.githubusercontent.com/esterTion/redive_master_db_diff/master/%2Bmanifest_bg.txt"
    read1 = requests.get(url1).content.decode('utf-8')
    
    # Get manifest_bg2.txt
    url2 = "https://raw.githubusercontent.com/esterTion/redive_master_db_diff/master/%2Bmanifest_bg2.txt"
    read2 = requests.get(url2).content.decode('utf-8')

    # Combine manifest_bg.txt & manifest_bg2.txt in one list
    url = read1+read2
    # print(url)

    # Save output data to bg.txt
    y = open("bg.txt", "a")
    print(url, file=y)
    print("                           === Extract Complete! ===                            ")
    y.close()

# get all values for extracting
def get_all(): # get all values for extracting with regex
  with open("bg.txt", "r") as f:
      for line in f:
          if 'a/bg_still_unit_' in line:
              start = line.index('bg_still_unit_')
              raw.append(line[start:start+47])
              file.append(line[start:start+28])
              hash.append(line[start+29:start+61])
              id.append(line[start+16:start+22])
              name.append(line[start+5:start+22])


def report(): # reporting
  print("""
                                 === Raw ===                                   
        """)
  print(raw[:10])
  print("""
                                 === Hash ===                                  
        """)
  print(hash[:10])
  print("""
                              === File Names ===                               
  """)
  print(file[:10])

def download_unity(): #Get Hash and files name (also raw)
  # downloading 3dUnity
  for x,y in zip(file,hash):
    link = "http://prd-priconne-redive.akamaized.net/dl/pool/AssetBundles/"+y[0:2]+"/"+y
    path = r'./raw/'+x
    urllib.request.urlretrieve(link, path)
    print("Downloading "+link+"\n"+y+"\nin "+path+"\nas "+x+"\n==========================")  
  print("Download Finished!")

  # w = r'/cards/'+x[14:21]+'png'
  # os.system("deserialize.py ")
  # subprocess.call(['python', 'deserialize.py', x, w])
  
def unpack_all_assets(source_folder : str, destination_folder : str):
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            # generate file_path
            file_path = os.path.join(root, file_name)
            # load that file via UnityPy.load
            env = UnityPy.load(file_path)

            # iterate over internal objects
            for obj in env.objects:
                # process specific object types
                if obj.type.name in ["Texture2D"]:
                    # parse the object data
                    data = obj.read()

                    # create destination path
                    dest = os.path.join(destination_folder, data.name[11:17])

                    # make sure that the extension is correct
                    # you probably only want to do so with images/textures
                    dest, ext = os.path.splitext(dest)
                    dest = dest + ".png"

                    img = data.image
                    img.save(dest)
                    print("Extracting "+data.name[11:17]+".png"+"\n==========================")
    print("Extract Completed!")

get_files()
get_all()
report()
download_unity()
unpack_all_assets('./raw/', './cards/')
