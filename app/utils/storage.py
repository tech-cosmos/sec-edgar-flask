from google.cloud import storage
import google.auth
import os

def get_storage_client():
  # Get the current directory
  current_dir = os.path.dirname(os.path.abspath(__file__))

  # Construct the path to the key file
  key_path = os.path.join(current_dir, 'service_account.json')

  # Load the private key file
  credentials = google.oauth2.credentials.Credentials.from_service_account_file(key_path)

  # Create a client using the credentials
  client = storage.Client(credentials=credentials)
  
  return client