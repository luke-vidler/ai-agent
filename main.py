import os
import google.generativeai as genai
from dotenv import load_dotenv
from call_function import available_functions, call_function

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the model
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    tools=[available_functions]
)

def main():
    """
    Main function to run the AI agent with function calling capabilities.
    """
    print("🤖 AI Agent with Function Calling")
    print("=" * 40)
    print("Available functions:")
    print("- List files and directories")
    print("- Read file contents")
    print("- Write files")
    print("- Execute Python code")
    print("=" * 40)
    print("Type 'quit' to exit\n")
    
    # Initialize conversation
    conversation = model.start_chat(history=[])
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break
            
            if not user_input:
                continue
            
            # Send message to the model
            response = conversation.send_message(user_input)
            
            # Handle function calls if present
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                
                # Execute the function
                function_response = call_function(function_call)
                
                # Send function response back to the model
                response = conversation.send_message(function_response)
            
            # Print the response
            print(f"Agent: {response.text}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()