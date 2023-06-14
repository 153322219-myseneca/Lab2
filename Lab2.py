## Lab2.py

# check if at least two arguments are provided
if len(sys.argv) < 3:
    print("Please provide at least two arguments. Usage: script.py var1 var2")

# get the script name
script_name = sys.argv[0]

# get the variables from command line arguments
var1, var2 = sys.argv[1], sys.argv[2]

# print the script name and the variables separately
print("Script name: ", script_name)
print("Variables used: ", var1, var2)

# print the script name and variables together
print(f"{script_name} {var1} {var2}")
