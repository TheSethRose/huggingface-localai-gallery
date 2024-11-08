# HuggingFace Gallery Generator for LocalAI

This tool automatically generates a YAML gallery of HuggingFace models for use with [LocalAI](https://github.com/go-skynet/LocalAI). It fetches model information from the HuggingFace API and formats it in a way that's compatible with LocalAI's configuration system.

## Automatic Updates

The gallery is automatically updated every 24 hours with the latest models from HuggingFace. You can always find the most recent version in `models/index.yaml`.

## How It Works

The generator:

1. Fetches the latest models from HuggingFace's API
2. Converts the data into LocalAI-compatible YAML format
3. Organizes models by their pipeline tags (text-generation, image-to-text, etc.)
4. Updates automatically every 24 hours via GitHub Actions

## Usage

### With LocalAI

1. Clone this repository
2. Copy the generated `models/index.yaml` into your LocalAI configuration directory
3. Use the models as defined in the LocalAI documentation

### Manual Generation

If you want to generate the gallery yourself:

```bash
# Install dependencies
pip install requests pyyaml

# Run the generator
python generate_gallery.py
```

The script will create a `models/index.yaml` file containing all available models.

## Output Format

Each model entry in the YAML file follows this structure:

```yaml
- name: organization/model-name
  config_file:
    backend: model-type
    parameters:
      model: huggingface://organization/model-name
```

Where:

- `name`: The model identifier on HuggingFace
- `backend`: The model's pipeline tag (e.g., text-generation, text-to-image)
- `model`: The HuggingFace path to the model

## GitHub Actions Automation

This repository uses GitHub Actions to:

- Run every 24 hours automatically
- Fetch the latest models from HuggingFace
- Update the gallery only when changes are detected
- Commit and push changes automatically

You can also trigger a manual update anytime through the GitHub Actions tab.

## Contributing

Contributions are welcome! Feel free to:

- Open issues for bugs or suggestions
- Submit pull requests for improvements
- Share how you're using this tool

## License

MIT License - Feel free to use this tool however you'd like!
