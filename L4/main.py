number_of_lines = 0

while number_of_lines <= 0:
    initial_input = input("Enter the number of lines: ")

    if not initial_input.isdigit() and not (initial_input[0] == '-' and initial_input[1:].isdigit()):
        print("WARNING: " + initial_input + " is not a number!")
        continue
    
    number_of_lines = int(initial_input)
    if number_of_lines <= 0:
        print("WARNING: values must be > 0")

lines = []

for i in range(number_of_lines):
    line = input(f"Enter line #{i + 1} to append: ")

    lines.append(line)

print(f"Lines to append: {lines}")

print(len(lines))

file = open("data.txt", "a+")

for line in lines:
    file.write(line + "\n")

file.close()