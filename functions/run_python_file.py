import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    """
    Execute a Python file in the working directory.
    """
    try:
        full_file_path = os.path.join(working_directory, file_path)
        
        # Check if file is outside permitted working directory
        if not os.path.abspath(full_file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        # Check if file exists
        if not os.path.exists(full_file_path):
            return f'File "{file_path}" not found.'
            
        # Check if file ends with .py
        if not full_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
            
        # Execute the Python file
        result = subprocess.run(['python', full_file_path], 
                              capture_output=True, 
                              text=True, 
                              cwd=working_directory,
                              timeout=30)
        
        # Format the output
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
        
    except subprocess.TimeoutExpired:
        return f'Error: executing Python file: timeout after 30 seconds'
    except PermissionError:
        return f'Error: Permission denied to execute "{file_path}"'
    except Exception as e:
        return f'Error: executing Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)   