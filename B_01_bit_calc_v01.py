# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
-select file type
-enter the file info
-get the number of bits
''')



# asks users for file type (integer/image/text/xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

     # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

    # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's a text
        elif response in ['text', 't', 'txt']:
            return "Text"

        # check if it's an image
        elif response in ['image', 'p', 'img', 'picture']:
            return "image"

        # check if it's music
        elif response in ['music']:
            return "please enter a valid file type"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")


# Ask user for width and loop until they
#enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# calculate how many bits are needed to represent an integer
def image_calc():
    pass
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # calculate the number of pixels and * 24 to get number of bits
    num_pixels = width * height
    num_bits = num_pixels *24

    # Set up answer and return it
    answer = (f"Number o f pixels:  {width} x {height} = {num_pixels} "
              f"\nNumber of bits {num_pixels} x 24 = {num_bits}")

    return answer


# calculate how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter an integer (more than/equal to 0)
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

#   remove the 'OB' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it"

    return answer


# Calculates number of bits needed to9 represent text in ascii
def calc_text_bits():
    pass
    # Get text from user
    response = input("Enter some text: ")
    print()

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")
    return answer


# Main routine goes here

# Display instructions if requested
want_instructions = input("press enter to view instructions or any other key to not")

# Display instructions if requested
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type =="xxx":
        break

    # if user chose 'i', ask if img or int
    if file_type == 'i':

        want_image = input("press <enter> for an integer or any other key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)