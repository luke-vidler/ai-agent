import os
from pathlib import Path
from google.genai import types

def get_files_info(working_directory, directory=None):
    """
    Get information about files in a directory, ensuring we only access files within the permitted working directory.
    
    Args:
        working_directory (str): The root directory that we're allowed to access
        directory (str, optional): The subdirectory to list. If None, uses working_directory.
    
    Returns:
        str: A formatted string listing the contents of the directory or an error message
    """
    try:
        # Convert paths to absolute paths for comparison
        working_dir = os.path.abspath(working_directory)
        if directory is None:
            target_dir = working_dir
        else:
            # Store original directory for error messages
            original_dir = directory
            target_dir = os.path.abspath(os.path.join(working_dir, directory))
        
        # Ensure the target directory is within the working directory
        if not target_dir.startswith(working_dir):
            return f'Error: Cannot list "{original_dir}" as it is outside the permitted working directory'
        
        # Check if the target path is a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{original_dir}" is not a directory'
        
        # Get list of files and directories
        items = os.listdir(target_dir)
        # Sort items alphabetically
        items.sort()
        
        # Build the output string
        output_lines = []
        for item in items:
            try:
                item_path = os.path.join(target_dir, item)
                # Skip if not accessible
                if not os.access(item_path, os.R_OK):
                    continue
                    
                # Get file stats
                stats = os.stat(item_path)
                is_dir = os.path.isdir(item_path)
                output_lines.append(
                    f"- {item}: file_size={stats.st_size} bytes, is_dir={is_dir}"
                )
            except (PermissionError, OSError) as e:
                # Skip files we can't access
                continue
            
        return "\n".join(output_lines)
            
    except PermissionError:
        return "Error: Permission denied"
    except FileNotFoundError:
        return f'Error: Directory "{directory}" not found'
    except OSError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: Unexpected error occurred: {str(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)