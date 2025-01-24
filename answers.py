def modify_file_content(content):
    #converting all text to uppercase
    return content.upper()  

def main():
    # Prompt the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Attempt to read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Prompt the user for the output filename
        output_filename = input("Enter the name of the new file to write: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read or write one of the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
