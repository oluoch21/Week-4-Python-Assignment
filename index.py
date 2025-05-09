def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content by converting all text to uppercase
        modified_content = content.upper()
        
        # Open the output file to write the modified content
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"The file has been modified and saved to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for the filename
    input_filename = input("Enter the filename you want to read from: ")
    output_filename = input("Enter the filename to save the modified content: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)


# Run the program
if __name__ == "__main__":
    main()
