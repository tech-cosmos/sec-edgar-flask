import unittest
import os

# Import the necessary modules for the test case
from google.oauth2.credentials import Credentials
from google.cloud import storage
from tqdm import tqdm

class TestCloudStorageConnection(unittest.TestCase):
  def setUp(self):
        
    self.BUCKET_NAME = "sec-dataset"
      
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__)).replace("/app/tests", "/app/utils")

    # Construct the path to the key file
    key_path = os.path.join(current_dir, 'service_account.json')

    # Create a client for the Cloud Storage API
    self.client = storage.Client.from_service_account_json(key_path)

  def test_cloud_storage_connection(self):

    # List the buckets in the project
    buckets = self.client.list_buckets()

    # Check that the connection was successful
    self.assertTrue(buckets)
  
  def test_cloud_storage_upload(self):
    
    # Save the extracted files to Google Cloud Storage
    bucket = self.client.bucket(self.BUCKET_NAME)

    test_file = os.path.dirname(os.path.abspath(__file__)) + '/test.zip'
    
    # read the content of the zip file
    with open(test_file, 'rb') as file:    
    
      # create a new blob
      blob = bucket.blob('test.zip')

      # upload the file to the blob, with the progress callback function
      blob.upload_from_file(file)

if __name__ == '__main__':
  unittest.main()
