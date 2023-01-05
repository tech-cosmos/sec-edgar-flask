import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from app.models.submission import Submission
from tqdm import tqdm

def index_files():
    
    dest_path_folder = os.path.join(os.getenv('DESTINATION_PATH'), 'submissions')
    
    # Get a list of all the files in the folder
    files = os.listdir(dest_path_folder)

    # Use tqdm to show the progress of the file processing
    with tqdm(total=len(files)) as pbar:

        # Divide the files into batches of 100
        batch_size = 100
        for i in range(0, len(files), batch_size):
            batch = files[i:i + batch_size]
        
            for file in batch:
                # Check if the file is a JSON file
                if file.endswith('.json') and "submissions" not in file:
                    file_path = os.path.join(dest_path_folder, file)
                    
                    # Open the file and parse the JSON data
                    with open(file_path) as f:
                        data = json.load(f)
                        
                        try:
                            obj = Submission(**data)
                            db.session.add(obj)
                        except Exception as e:
                            print('Error in : ',file)
                            print('Error : ',e)
                        
                        pbar.update(1)

            # Commit the changes to the database
            db.session.commit()
    
    return 'Files successfully stored to Postgres Database!'