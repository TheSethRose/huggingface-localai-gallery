import requests
import yaml
import os

HUGGING_FACE_API = "https://huggingface.co/api/models"
OUTPUT_FILE = "models/index.yaml"

def generate_gallery():
    # Fetch models from Hugging Face API
    response = requests.get(HUGGING_FACE_API)

    if response.status_code != 200:
        print(f"Failed to fetch models. Status code: {response.status_code}")
        return False

    models = response.json()

    # Convert to LocalAI YAML format
    yaml_data = []
    for model in models:
        model_entry = {
            'name': model['id'],
            'config_file': {
                'backend': model.get('pipeline_tag', 'unknown'),
                'parameters': {
                    'model': f"huggingface://{model['id']}"
                }
            }
        }
        yaml_data.append(model_entry)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Write to YAML file
    with open(OUTPUT_FILE, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False, sort_keys=False)

    print(f"YAML gallery generated at {OUTPUT_FILE}")
    return True

if __name__ == "__main__":
    generate_gallery()
