import os
from google.genai import types

def write_file(working_directory, file_path, content):
    """
    Write content to a file in the working directory.
    """
    try:
        file_path = os.path.join(working_directory, file_path)
        
        # Check if file is outside permitted working directory
        if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
        with open(file_path, 'w') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except PermissionError:
        return f'Error: Permission denied to write to "{file_path}"'
    except IsADirectoryError:
        return f'Error: "{file_path}" is a directory, not a file'
    except Exception as e:
        return f'Error: An unexpected error occurred while writing to "{file_path}": {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)