from google.cloud import storage
import google.auth
import os
import tempfile
import datetime
import requests
from tqdm import tqdm
import zipfile
import shutil


class Storage:
      
  def __init__(self):
         
    # Instance Variable
    self.submission_url='https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip'
    self.dest_path_submission = os.path.join(os.getenv('DESTINATION_PATH'), 'submissions')  
      
  def get_storage_client(self):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the key file
    key_path = os.path.join(current_dir, 'service_account.json')

    # Load the private key file
    self.client = storage.Client.from_service_account_json(key_path)
    

  def upload_file_to_bucket(self):
        
    self.get_storage_client()

    # Get the bucket that the file will be uploaded to
    bucket = self.client.get_bucket(os.getenv('CLOUD_STORAGE_BUCKET'))
    
    now = datetime.datetime.now()
    filename = 'sec-submissions-{}.zip'.format(now.strftime('%Y%m%d%H%M%S'))
    
    # create a new blob
    blob = bucket.blob(filename)
    
    # move the pointer to the beginning of the file
    self.temp_file.seek(0)

    # upload the file to the blob, with the progress callback function
    blob.upload_from_file(self.temp_file)
    

  def download_zip_file(self):
    
    
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(dir='/media/shivam/backup/data')

    # Set the User-Agent header
    headers = {'User-Agent': 'Cosmos Infinity shivam@cosmosinfinity.in'}
    
    # Download the file from the URL
    response = requests.get(self.submission_url, stream=True, headers=headers)

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
    
    self.temp_file = temp_file
  
  def prepare_folders(self):
        # Create the destination path if it doesn't exist
    if os.path.exists(self.dest_path_submission):
        # delete the folder
      shutil.rmtree(self.dest_path_submission)
      os.makedirs(self.dest_path_submission)
  
  def extract_zip_file(self):
    
    self.prepare_folders()        
     
    with zipfile.ZipFile(self.temp_file.name, 'r') as zip_ref:
      
      # get the list of files in the zip file
      file_list = zip_ref.infolist()

      # iterate over the list of files using a tqdm progress bar
      for file in tqdm(file_list, desc='Extracting files', total=len(file_list)):
        # extract the file
        zip_ref.extract(file, path=self.dest_path_submission)