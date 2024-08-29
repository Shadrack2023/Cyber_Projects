# Open a file called ids.txt in write mode
with open('ids.txt', 'w') as file:
    # Loop through numbers 0 to 1000
    for number in range(1001):
        # Write each number followed by a newline character
        file.write(f"{number}\n")
