import os
from pathlib import Path
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    """
    Get the content of a file in the working directory.
    """
    try:
        file_path = os.path.join(working_directory, file_path)
        
        # Check if file is outside permitted working directory
        if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        with open(file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    except FileNotFoundError:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    except PermissionError:
        return f'Error: Permission denied to read "{file_path}"'
    except IsADirectoryError:
        return f'Error: "{file_path}" is a directory, not a file'
    except Exception as e:
        return f'Error: An unexpected error occurred while reading "{file_path}": {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
    ),
)