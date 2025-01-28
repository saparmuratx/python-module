line_to_append = ""

while not line_to_append:
    line_to_append = input("Enter line to append: ")

number_of_lines = 0

while number_of_lines <= 0:
    initial_input = input("Enter the number of lines: ")

    if not initial_input.isdigit() and not (initial_input[0] == '-' and initial_input[1:].isdigit()):
        print("WARNING: " + initial_input + " is not a number!")
        continue
    
    # TODO: give warning for negative numbers and 0

    number_of_lines = int(initial_input)


print("Line to append: " + line_to_append)
print("Number of lines to print: " + str(number_of_lines))

file = open("C:/Users/Saparmurat/Desktop/Python/L3/data.txt", "r+")


for i in range(number_of_lines):
    line = file.readline()
    print(line, end='')


file.write(line_to_append + "\n")

file.close()