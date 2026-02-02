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
        return total 

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
    return sum(batteries)

def print_section(title, part1, part2):
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)
    print(f"  Part 1 Answer: {part1}")
    print(f"  Part 2 Answer: {part2}")
    print()

def run(filename, title):
    try:
        with open(filename, "r") as file:
            data = file.read().strip().splitlines()
            part1 = solve(data)
            part2 = solve2(data)
            print_section(title, part1, part2)
    except FileNotFoundError:
        print(f"File not found. Please ensure '{filename}' exists in the current directory.")

if __name__ == "__main__":
    run("example.txt", "EXAMPLE SOLUTION OUTPUT")
    run("input.txt", "SOLUTION OUTPUT")