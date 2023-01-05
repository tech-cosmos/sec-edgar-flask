import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from app.models.submission import Submission

def index_files():
    
    dest_path_folder = os.path.join(os.getenv('DESTINATION_PATH'), 'submissions')
    
    for file in os.listdir(dest_path_folder):
        # Check if the file is a JSON file
        if file.endswith('.json'):
            file_path = os.path.join(dest_path_folder, file)
            
            # Open the file and parse the JSON data
            with open(file_path) as f:
                data = json.load(f)
                # Create a new object for the data and add it to the database
                obj = Submission(**data)
                db.session.add(obj)

    # Commit the changes to the database
    db.session.commit()
    
    return 'Files successfully stored to Postgres Database!'