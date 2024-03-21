import random

def main():

    width = int(input("Puzzle width: "))
    height = int(input("Puzzle height: "))
    n_words = int(input("Number of words: "))
    print()

    print("Generating words")
    with open("dictionary.txt", "r") as f:
        dictionary = [line.strip() for line in f.readlines() if line != ""]
    words = random.sample(dictionary, n_words + 1)

    # initialization
    print("Generating puzzle")
    puzzle = []
    for y in range(height):
        puzzle.append([])
        for x in range(width):
            puzzle[y].append('-')
    all_placements = set()
    [[[all_placements.add((x, y, orientation)) for orientation in range(8)] for y in range(height)] for x in range(width)]
    orientation_offsets = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    # generating placements
    def place_words(puzzle: list, words: list) -> list:
        """
        Recursively attempts to put all words into the puzzle
        """
        possible_placements = all_placements.copy()
        if len(words) == 0:
            return puzzle
        word = words.pop()
        while True:
            if len(possible_placements) <= 0:
                return []

            placement = random.choice(list(possible_placements))
            possible_placements.remove(placement)

            x, y, orientation = placement
            x_offset, y_offset = orientation_offsets[orientation]
            valid_placement = True
            for i in range(len(word)):
                y_pos = y + (i * y_offset)
                x_pos = x + (i * x_offset)
                if y_pos < 0 or y_pos >= height or x_pos < 0 or x_pos >= width or (puzzle[y_pos][x_pos] != '-' and puzzle[y_pos][x_pos] != word[i]):
                    valid_placement = False
                    break
            if not valid_placement:
                continue
            # inserting word into puzzle
            new_puzzle = []
            for _y in range(height):
                new_puzzle.append([])
                for _x in range(width):
                    new_puzzle[_y].append(puzzle[_y][_x])
            for i in range(len(word)):
                new_puzzle[y + (i * y_offset)][x + (i * x_offset)] = word[i]
            result = place_words(new_puzzle, words.copy())
            if result != []:
                return result
    print("Placing words")
    puzzle = place_words(puzzle, words)
    if puzzle == []:
        print("Failed to generate puzzle :(")
        return

    print("Filling puzzle")
    for y in range(height):
        for x in range(width):
            if puzzle[y][x] == '-':
                puzzle[y][x] = chr(random.randrange(97, 123))

    print("Writing output to file")
    with open("puzzle.txt", "w") as f:
        for y in range(height):
            for x in range(width):
                f.write(puzzle[y][x] + " ")
            f.write("\n")
    with open("words.txt", "w") as f:
        f.write("\n".join(words))

    print("Done")

if __name__ == "__main__":
    main()

