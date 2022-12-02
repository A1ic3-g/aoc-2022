from itertools import takewhile

def sum_invs(invs: list[list[int]]) -> list[int]:
    return [sum(inv) for inv in invs]

def max_elf(elves: list[list[int]]) -> int:
    return max(elves)

def max_n_elves(invs: list[list[int]], n:int):
    return sum([invs.pop(invs.index(max(invs))) for _ in range(n)])
    

def get_input():
    elves = []
    with open ("inputs/input-01.txt", "r") as f:
        lines = f.readlines()
    while len(lines):
        tmp = list(map(int,list(takewhile(lambda x : x!="\n", lines))))
        elves += [tmp]
        lines = lines[len(tmp)+1:]
    return elves

def main():
    elves = sum_invs(get_input())
    print(f"Part 1:\n  Max: {max_elf(elves)}\nPart 2:\n  Max3: {max_n_elves(elves, 3)}")

if __name__ == "__main__":
    main()
