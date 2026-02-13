def solve(data):
    # will be list of valid data split by empty new line
    count = 0
    fresh = []
    for i, x in enumerate(data):
        if x == '':
            data = data[i:]
            break
        t = tuple(map(int, x.split('-')))
        fresh.append(t)

    while(i := data.pop()):
        for a, b in fresh:
            if a <= int(i) <= b:
                count += 1
                break
    
    return count

def solve2(data):
    return 0
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