import os
import yaml
import uuid

# Specify the directory to walk through
directory = "/path/to/directory"

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    # Initialize an empty string to store the concatenated contents for the current subdirectory
    subdirectory_contents = ""

    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Open the file in read mode and read its contents
            with open(file_path, "r") as f:
                file_contents = f.read()

            # Concatenate the file contents to the existing string for the current subdirectory
            subdirectory_contents += file_contents

    # Generate a UUID for the new YAML file name
    file_uuid = str(uuid.uuid4())

    # Create a new file with the UUID as the name and write the concatenated contents
    new_file_path = os.path.join(root, f"{file_uuid}.yaml")
    with open(new_file_path, "w") as f:
        yaml.dump(subdirectory_contents, f)
