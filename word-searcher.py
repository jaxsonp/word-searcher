
def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip().split(" ") for line in f.readlines()]
    for row in puzzle:
        for letter in row:
            letter = letter.lower()
            print(letter + " ", end="")
        print()

    with open("words.txt", "r") as f:
        words = set([line.strip().lower() for line in f.readlines()])
    print(words)

    width = len(puzzle[0])
    height = len(puzzle)
    for y in range(height):
        for x in range(width):
            print(f"char")


if __name__ == "__main__":
    main()