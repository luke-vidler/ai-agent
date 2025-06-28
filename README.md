# AI Agent with Function Calling

An intelligent AI agent built with Google Generative AI that can perform various file operations and code execution tasks through function calling capabilities.

## Features

- **File Operations**: Read file contents, list directory contents, and write files
- **Code Execution**: Run Python files with timeout and output capture
- **Multi-turn Conversations**: Maintain context across multiple interactions
- **Security**: Path validation to prevent directory traversal attacks
- **Error Handling**: Comprehensive error handling and user-friendly messages

## Available Functions

### 1. `get_files_info`
Lists files and directories in a specified path with size and type information.

**Parameters:**
- `directory` (optional): Subdirectory to list (defaults to working directory)

**Example:**
```
List all files in the current directory
```

### 2. `get_file_content`
Reads and returns the content of a file (up to 10,000 characters).

**Parameters:**
- `file_path`: Path to the file relative to working directory

**Example:**
```
Read the contents of main.py
```

### 3. `write_file`
Creates or overwrites a file with specified content.

**Parameters:**
- `file_path`: Path to the file relative to working directory
- `content`: Content to write to the file

**Example:**
```
Create a new file called hello.py with print("Hello, World!")
```

### 4. `run_python_file`
Executes a Python file and returns the output.

**Parameters:**
- `file_path`: Path to the Python file relative to working directory

**Example:**
```
Run the hello.py file
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/luke-vidler/ai-agent.git
   cd ai-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_google_generative_ai_api_key_here
   ```

## Usage

1. **Start the AI agent:**
   ```bash
   python main.py
   ```

2. **Interact with the agent:**
   The agent will prompt you for input. You can ask it to:
   - List files in directories
   - Read file contents
   - Create or modify files
   - Execute Python code
   - Perform complex multi-step tasks

3. **Example conversation:**
   ```
   User: List the files in the current directory
   Agent: [Lists all files and directories with sizes]
   
   User: Read the contents of main.py
   Agent: [Shows file contents]
   
   User: Create a simple calculator function
   Agent: [Creates a calculator.py file with the function]
   
   User: Run the calculator
   Agent: [Executes the calculator.py file]
   ```

## Project Structure

```
ai_agent/
├── main.py                 # Main application entry point
├── call_function.py        # Function dispatcher and schema definitions
├── functions/              # Individual function implementations
│   ├── get_files_info.py   # Directory listing functionality
│   ├── get_file_content.py # File reading functionality
│   ├── write_file.py       # File writing functionality
│   └── run_python_file.py  # Python execution functionality
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Security Features

- **Path Validation**: All file operations are restricted to the working directory
- **Directory Traversal Protection**: Prevents access to files outside the permitted directory
- **Timeout Protection**: Python file execution is limited to 30 seconds
- **Error Handling**: Graceful handling of permission errors and missing files

## Dependencies

- `google-genai==1.12.1`: Google Generative AI client library
- `python-dotenv==1.1.0`: Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Google Generative AI
- Inspired by the need for intelligent file and code management assistants