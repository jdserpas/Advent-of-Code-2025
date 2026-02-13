def solve(data):
    dataH = len(data)
    dataW = len(data[0])

    padded = [
        [0] * (dataW + 2)
        for _ in range(dataH + 2)
    ]

    for i in range(dataH):
        for j in range(dataW):
            padded[i + 1][j + 1] = 1 if data[i][j] == '@' else 0

    count = 0

    for i in range(1, dataH + 1):
        for j in range(1, dataW + 1):
            if padded[i][j] == 0:
                continue
            rolls = 0
            # check 3 above
            rolls += padded[i - 1][j - 1]
            rolls += padded[i - 1][j]
            rolls += padded[i - 1][j + 1]
            # check 2 on row
            rolls += padded[i][j - 1]
            rolls += padded[i][j + 1]
            #check 3 bellow
            rolls += padded[i + 1][j - 1]
            rolls += padded[i + 1][j]
            rolls += padded[i + 1][j + 1]

            if rolls < 4:
                count+=1
             

    return count 
    

def solve2(data):
    print("Solution 2 not implemented")
    # TODO

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