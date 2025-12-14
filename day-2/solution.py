def is_repeated_twice(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]

with open('input.txt') as f:
    input = []
    lines = f.readlines()
    for line in lines:
        input.append(tuple(map(int, line.strip().split('-'))))
    
    # Part 1
    invalid_ids = []
    for i in input:
        for j in range(i[0], i[1]+1):
            # Rule 1: If it's made up of two repeting digits
            str_j = str(j)
            invalid_ids.append(j) if is_repeated_twice(str_j) else None
    
    print(f"Solution #1: {sum(invalid_ids)}\n")

    # Part 2
    invalid_ids = []
    for i in input:
        for j in range(i[0], i[1]+1):
            # Rule 2: If it has any digit that appears exactly twice
            s = str(j)
            if s in (s + s)[1:-1]:
                invalid_ids.append(j)
    print(f"Solution #2: {sum(invalid_ids)}")