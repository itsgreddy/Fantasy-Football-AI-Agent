import os
from src.utils.config import DATA_DIR, STORAGE_DIR, ROOT_DIR

def verify_setup():
    """Verify the project setup and data files"""
    print("Verifying project setup...")
    
    # Check directories
    print(f"\nChecking directories:")
    print(f"Root directory: {ROOT_DIR}")
    print(f"Data directory: {DATA_DIR}")
    print(f"Storage directory: {STORAGE_DIR}")
    
    # Check if Dataset folder exists
    dataset_dir = os.path.join(ROOT_DIR, "src", "data", "Dataset")
    print(f"Dataset directory: {dataset_dir} {'✓' if os.path.exists(dataset_dir) else '✗'}")
    
    # Check data files
    required_files = ['combine_data.csv', 'injuries.csv', 'rush.csv']
    print("\nChecking data files:")
    for file in required_files:
        file_path = os.path.join(DATA_DIR, file)
        exists = os.path.exists(file_path)
        print(f"{file}: {'✓' if exists else '✗'} ({file_path})")
        
    # Print current working directory for debugging
    print(f"\nCurrent working directory: {os.getcwd()}")
        
    # Check environment
    print("\nChecking environment:")
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"OPENAI_API_KEY: {'✓' if api_key else '✗'}")

    print("\nVerifying API keys:")
    api_key_valid = verify_api_key()
    if not api_key_valid:
        print("\nPlease update your OpenAI API key in .env file")
        return False
    
    return True

def verify_api_key():
    """Verify OpenAI API key"""
    from src.utils.config import OPENAI_API_KEY
    from llama_index.llms.openai import OpenAI
    
    try:
        llm = OpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY
        )
        # Try a simple completion to verify the key
        response = llm.complete("Test")
        print("✓ OpenAI API key is valid")
        return True
    except Exception as e:
        print(f"✗ OpenAI API key error: {str(e)}")
        return False

if __name__ == "__main__":
    verify_setup() 