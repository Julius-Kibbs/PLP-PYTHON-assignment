def read_and_write():
    input_file = input("Input the file name:")
  
  #Opening and reading the file
    try:
        with open(input_file, 'r') as file:
            content = file.read()
    
        #Modifying the content    
        modified_content = content.upper()

        #Printing the modified content
        print(modified_content)

    except FileNotFoundError:
        print("file not found")

read_and_write()