from functions.run_python_file import run_python_file

def run_tests():
    # Test case 1: Execute calculator/main.py (should produce STDOUT)
    print("Test 1: Executing calculator/main.py")
    result = run_python_file(".", "calculator/main.py")
    print(result)
    print("\n" + "-"*50 + "\n")

    # Test case 2: Execute a simple Python file that prints to STDOUT
    print("Test 2: Executing a simple Python file")
    result = run_python_file(".", "simple_test.py")
    print(result)
    print("\n" + "-"*50 + "\n")

    # Test case 3: Try to execute file outside working directory (should error)
    print("Test 3: Attempting to execute file outside working directory")
    result = run_python_file(".", "../main.py")
    print(result)
    print("\n" + "-"*50 + "\n")

    # Test case 4: Try to execute non-existent file (should error)
    print("Test 4: Attempting to execute non-existent file")
    result = run_python_file(".", "nonexistent.py")
    print(result)
    print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    run_tests()
    print("Ran 9 tests") 