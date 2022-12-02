scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}
def main():
    main1()
    main2()
    
def main1():
    score = 0
    pairs = [line.split(" ") for line in get_input()]
    for pair in pairs:
        score += scores[pair[1]] + winscore(pair)
    print(f"Day 2 Challenge 1:\n  Score: {score}")

def main2():
    score = 0
    pairs = [line.split(" ") for line in get_input()]
    for pair in pairs:
        match pair[1]:
            case "X":
                score += 0 + scores[char_to_use(pair[0], "lose")] 
            case "Y":
                score += 3 + scores[char_to_use(pair[0], "tie")]
            case "Z":
                score += 6 + scores[char_to_use(pair[0], "win")]
    print(f"Day 2 Challenge 2:\n  Score: {score}")

def char_to_use(opponent: str, outcome: str) -> str:
    match outcome:
        case "win":
            return winchar(opponent)
        case "tie":
            return opponent
        case "lose":
            return losechar(opponent)

def winchar(opponent: str) -> str:
    match opponent:
        case "A":
            return "Y"
        case "B":
            return "Z"
        case "C":
            return "X"
def losechar(opponent: str) -> str:
    match opponent:
        case "A":
            return "Z"
        case "B":
            return "X"
        case "C":
            return "Y"
def winscore(pair: list[str]):
    pair = list(map(lambda x : scores[x], pair))
    if pair[0] == pair[1]:
        return 3
    if pair[1] - pair[0] == 1 or pair == [3,1]:
        return 6
    return 0
    

def get_input():
    with open("inputs/input-02.txt", "r") as f:
        lines = f.readlines()
        lines = map(lambda x: x.replace("\n",""), lines)
    return lines