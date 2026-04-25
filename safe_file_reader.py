# Program to open a file safely and handle common exceptions

filename = input("Enter the filename to open: ")

try:
    file = open(filename, 'r')
    content = file.read()
    
    print("\nFile opened successfully. File content:\n")
    print(content)
    
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")

except PermissionError:
    print("Error: You do not have permission to read this file.")
