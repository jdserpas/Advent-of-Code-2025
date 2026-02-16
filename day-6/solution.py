import functools
import operator
import math

def solve(data):
    nums = []
    ops = []
    for line in data:
        clean_up = line.split()
        nums.append(clean_up)

    ops = nums[-1]
    nums = nums[:-1]    
    dataW = len(nums[0])
    dataH = len(nums)
    count = 0

    for i in range(dataW):
        temp = []
        for j in range(dataH):
            temp.append(int(nums[j][i]))
        
        if ops[i] == '*':
            count += math.prod(temp)
        elif ops[i] == '+':
            count += sum(temp)
    print(count)
            

    return count

def solve2(data):
    #TODO
    return 0

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