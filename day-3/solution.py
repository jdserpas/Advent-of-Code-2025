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

def solve2(data):
    k = 12
    batteries = []
    for line in data:
        # How many digits do we need to drop?
        drop = len(line) - 12
        stack = []
        for num in list(line):
            while(len(stack) > 0 and drop > 0 and stack[-1] < num):
                stack.pop()
                drop -= 1
            stack.append(num)
        if drop > 0:
            stack = stack[0:-drop]
        batteries.append(int(''.join(stack)))
    print(sum(batteries))

try:
    with open("example.txt", "r") as file:
        data = file.read().strip().splitlines()
        print(">>>>>>>>>>>>>>>>>>>> EXAMPLE SOLUTION OUTPUT: >>>>>>>>>>>>>>>>>>>>>>>>>")
        print(" PART 1: ") 
        solve(data)
        print(" PART 2: ")
        solve2(data)

except FileNotFoundError:
    print("File not found. Please ensure 'example.txt' exists in the current directory.")

try:
    with open("input.txt", "r") as file:
        data = file.read().strip().splitlines()
        print(">>>>>>>>>>>>>>>>>>>> SOLUTION OUTPUT: >>>>>>>>>>>>>>>>>>>>>>>>>")
        print(" PART 1: ") 
        solve(data)
        print(" PART 2: ")
        solve2(data)
except FileNotFoundError:
    print("File not found. Please ensure 'input.txt' exists in the current directory.")