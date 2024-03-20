
def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip().split(" ") for line in f.readlines()]
    width = len(puzzle[0])
    height = len(puzzle)
    for y in range(height):
        for x in range(width):
            puzzle[y][x] = puzzle[y][x].lower()
            print(puzzle[y][x] + " ", end="")
        print()

    with open("words.txt", "r") as f:
        all_words = set([line.strip().lower() for line in f.readlines()])
    print(all_words)

    undiscovered_words = set(all_words)
    word_locations = {}
    for y in range(height):
        for x in range(width):
            for x_offset, y_offset in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                possible_words = set(undiscovered_words)
                y_pos = y
                x_pos = x
                i = 0
                while len(possible_words) > 0:
                    for word in [x for x in possible_words]:
                        if puzzle[y_pos][x_pos] != word[i]:
                            possible_words.remove(word)
                        elif i + 1 == len(word):
                            # matched word
                            undiscovered_words.remove(word)
                            word_locations[word] = ((x, y), (x_offset, y_offset))
                            possible_words.remove(word)
                    y_pos += y_offset
                    x_pos += x_offset
                    i += 1
                    if x_pos < 0 or x_pos >= width or y_pos < 0 or y_pos >= height:
                        break



if __name__ == "__main__":
    main()