import requests
import os

url = "https://raw.githubusercontent.com/nsethi31/Kaggle-Data-Credit-Card-Fraud-Detection/master/creditcard.csv"
dest_dir = "data"
dest_file = "creditcard.csv"
dest_path = os.path.join(dest_dir, dest_file)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

print(f"Downloading to {dest_path}...")
try:
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(dest_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download Done.")
except Exception as e:
    print(f"Error: {e}")
