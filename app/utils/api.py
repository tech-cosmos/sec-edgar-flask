import zipfile
from app.utils.storage import get_storage_client
import requests
import os
import tempfile
from tqdm import tqdm

import os

file_url = 'https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip'
BUCKET_NAME = os.getenv('CLOUD_STORAGE_BUCKET')
dest_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("/app", "/data")

def download_file():
    
  # Create a temporary file
  temp_file = tempfile.NamedTemporaryFile()

  # Set the User-Agent header
  headers = {'User-Agent': 'Cosmos Infinity shivam@cosmosinfinity.in'}
  
  # Download the file from the URL
  response = requests.get(file_url, stream=True, headers=headers)

  # Get the total size of the file
  total_size = int(response.headers.get('content-length', 0))
  
  # Print the progress bar
  with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:

    # Save the file to a temporary location on disk
    for chunk in response.iter_content(chunk_size=1024):
      temp_file.write(chunk)
      pbar.update(len(chunk))

    # Flush the data to the disk
    temp_file.flush()

  # Extract the contents of the zip file
  with zipfile.ZipFile(temp_file.name, 'r') as zip_ref:
    zip_ref.extractall(path=dest_path)

  # Get a Google Cloud Storage client
  client = get_storage_client()

  # Save the extracted files to Google Cloud Storage
  bucket = client.bucket(BUCKET_NAME)
  for file in zip_ref.namelist():
        # Check if the file already exists in the bucket
    blob = bucket.blob(file)
    if blob.exists():
      # Delete the file if it already exists
      blob.delete()
    # Read the contents of the file
    with open(file, 'rb') as f:
      file_data = f.read()
    # Save the file to Google Cloud Storage
    blob = bucket.blob(file)
    blob.upload_from_string(file_data)

  return 'Files successfully extracted and saved to Google Cloud Storage!'