print("Running gendiff/parser.py")
import json
import yaml
def load_data(file_path):
    """Loads data from a file based on its extension."""
    print(f"Loading {file_path}...")
    with open(file_path, 'r') as f:
        if file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError("Unsupported file format")
