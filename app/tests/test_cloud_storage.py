import unittest
import os

# Import the necessary modules for the test case
from google.oauth2.credentials import Credentials
from google.cloud import storage


class TestCloudStorageConnection(unittest.TestCase):
  def setUp(self):
      
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__)).replace("/app/tests", "/app/utils")

  # Construct the path to the key file
    key_path = os.path.join(current_dir, 'service_account.json')

    # Load the service account key file
    self.key_path = key_path

  def test_cloud_storage_connection(self):
    # Create a client for the Cloud Storage API
    client = storage.Client.from_service_account_json(self.key_path)

    # List the buckets in the project
    buckets = client.list_buckets()

    # Check that the connection was successful
    self.assertTrue(buckets)

if __name__ == '__main__':
  unittest.main()
