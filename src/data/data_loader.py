import os
import pandas as pd
from src.utils.config import DATA_DIR

class DataLoader:
    @staticmethod
    def load_data():
        """Load all required datasets"""
        try:
            # Print current directory and data directory for debugging
            print(f"Current directory: {os.getcwd()}")
            print(f"Looking for data in: {DATA_DIR}")
            
            # Check if files exist
            files = ['combine_data.csv', 'injuries.csv', 'rush.csv']
            for file in files:
                file_path = os.path.join(DATA_DIR, file)
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
            
            # Load the data
            combine_data = pd.read_csv(os.path.join(DATA_DIR, 'combine_data.csv'))
            injuries_data = pd.read_csv(os.path.join(DATA_DIR, 'injuries.csv'))
            rush_data = pd.read_csv(os.path.join(DATA_DIR, 'rush.csv'))
            
            return combine_data, injuries_data, rush_data
        except Exception as e:
            print(f"Error details: {str(e)}")
            raise Exception(f"Error loading data: {str(e)}") 