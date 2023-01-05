from app.utils.storage import Storage

LocalStorage = Storage()

    
def download_file():
    
  # Download & Create a temporary file
  LocalStorage.download_zip_file()

  # Extract the contents of the zip file
  LocalStorage.extract_zip_file()

  # Upload to Google Cloud Storage
  LocalStorage.upload_file_to_bucket()
  

  return 'Files successfully extracted and saved to Google Cloud Storage !'