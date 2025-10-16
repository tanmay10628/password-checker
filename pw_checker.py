# pw_checker.py

# --- 1. Imports ---
import sys   # Required to read command-line arguments

# --- 2. Function Definitions ---

def analyze(password):
    """
    Performs a basic analysis of the password.
    Checks if password is at least 8 characters long.
    """
    is_strong = len(password) >= 8
    
    return {
        "password": password,
        "length": len(password),
        "is_strong": is_strong,
        "message": "Strong enough" if is_strong else "Too short"
    }

def pretty_print(res, show_pw=False):
    """
    Prints the analysis results in a readable format.
    """
    print("-" * 30)
    if show_pw:
        print(f"Password: {res['password']}")
    else:
        print(f"Password: {'*' * res['length']}") 
        
    print(f"Length:   {res['length']}")
    print(f"Status:   {'GOOD' if res['is_strong'] else 'WEAK'}")
    print(f"Message:  {res['message']}")

def analyze_file(file_name):
    """Handles the logic of opening and processing a single file."""
    passwords_to_check = []
    print(f"\n--- Checking Passwords from: {file_name} ---")

    try:
        # 'r' mode opens the file for reading
        with open(file_name, 'r') as file:
            for line in file:
                # .strip() removes whitespace, including the newline character
                password = line.strip() 
                if password: # Only process non-empty lines
                    passwords_to_check.append(password)
                    
    except FileNotFoundError:
        print(f"ERROR: The file '{file_name}' was not found in the current directory.")
        return 

    # Process all passwords read from the file
    for pw in passwords_to_check:
        res = analyze(pw) 
        pretty_print(res, show_pw=True)


# --- 3. The main function ---
def main():
    # Check if a filename was provided as an argument
    if len(sys.argv) < 2:
        print("\nError: No file name provided.")
        print("Usage: python pw_checker.py <filename.txt>")
        return

    # Get the file name from the command-line argument (sys.argv[1])
    file_to_check = sys.argv[1]
    
    # Optional: Basic check to ensure the file looks like a text file
    if not file_to_check.lower().endswith('.txt'):
        print(f"\nWarning: File '{file_to_check}' does not end with .txt. Attempting to check anyway.")
    
    # Process the specified file
    analyze_file(file_to_check)


# --- 4. Execution Block ---
if __name__ == "__main__":
    main()