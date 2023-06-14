import sys

def print_script_and_variables():
    script_name = sys.argv[0]  # Get the name of the script
    
    if len(sys.argv) > 1:
        variables = " ".join(sys.argv[1:])  # Join the command line arguments excluding the script name
        print("Variables used:", variables)
    
    print("Script:", script_name)
    print("Script and Variables:", " ".join(sys.argv))
