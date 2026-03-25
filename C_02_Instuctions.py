# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
-instruction 1
-instruction 2
-instruction 3
''')


# Main routine goes here
want_instructions = input("press enter to view instructions or any other key to not")

# Display instructions if requested
if want_instructions == "":
    instructions()

print("program continues")
