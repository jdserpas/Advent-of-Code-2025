def solve(data):
        total = 0
        for line in data:
            i = 0
            highestLeft = line[i]
            highestRight = line[-1]
            for index, char in enumerate(line):
                if index == len(line) - 1:
                    break
                if char > highestLeft:
                    highestLeft = char
                    i = index
            for char in range(i + 1, len(line)):
                if line[char] > highestRight:
                    highestRight = line[char]
            total += int(highestLeft + highestRight)
        print(total) 

try:
    with open("example.txt", "r") as file:
        data = file.read().strip().splitlines()
        solve(data)

except FileNotFoundError:
    print("File not found. Please ensure 'example.txt' exists in the current directory.")

try:
    with open("input.txt", "r") as file:
        data = file.read().strip().splitlines()
        solve(data)
except FileNotFoundError:
    print("File not found. Please ensure 'input.txt' exists in the current directory.")