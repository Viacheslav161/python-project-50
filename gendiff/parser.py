import json
import yaml
def load_data(file_path):
    """Loads data from a file based on its extension."""
    with open(file_path, 'r') as f:
        try:
            if file_path.endswith(('.yml', '.yaml')):
                return yaml.safe_load(f)
            elif file_path.endswith('.json'):
                return json.load(f)
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            print(f"Error loading file {file_path}: {e}")
            raise  # Повторно запускаем исключение
