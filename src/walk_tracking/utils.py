import yaml  # Import the PyYAML library for YAML parsing
import os    # Import the os library for file operations

def read_config(config_file: str = os.path.join("config", "config.yaml")) -> dict[str,dict]:
    """
    Reads a YAML configuration file and returns its contents as a dictionary.

    Args:
        config_file (str): The path to the YAML configuration file.

    Returns:
        dict: A dictionary containing the configuration settings.
    Raises:
        FileNotFoundError: If the specified config_file does not exist.
    """
    # Check if the specified configuration file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"config file not found: {config_file}")

    # Open and read the YAML configuration file
    with open(config_file, "r") as f:
        # Parse the YAML content and return it as a dictionary
        return yaml.safe_load(f)
