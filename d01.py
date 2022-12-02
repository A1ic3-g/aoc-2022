def max_elf(elves: list[list[int]]) -> int:
    return max([sum(elf) for elf in elves])

if __name__ == "__main__":
    elves = []
    tmp = []
    with open ("input-01", "r") as f:
        for line in f.readlines():
            if line != "\n":
                tmp.append(int(line))
            else:
                elves.append(tmp)
                tmp = []
    print(max_elf(elves))

    