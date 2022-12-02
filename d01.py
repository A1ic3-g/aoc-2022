def sum_invs(invs: list[list[int]]) -> list[int]:
    return [sum(inv) for inv in invs]

def max_elf(elves: list[list[int]]) -> int:
    return max(sum_invs(elves))

def max_n_elves(elves: list[list[int]], n:int):
    invs = sum_invs(elves)
    return sum([invs.pop(invs.index(max(invs))) for _ in range(n)])
    

def get_input():
    elves = []
    tmp = []
    with open ("input-01", "r") as f:
        for line in f.readlines():
            if line != "\n":
                tmp.append(int(line))
            else:
                elves.append(tmp)
                tmp = []
    return elves

if __name__ == "__main__":
    elves = get_input()
    print(f"Part 1:\n  Max: {max_elf(elves)}")
    print(f"Part 2:\n  Max3: {max_n_elves(elves, 3)}")
    

    