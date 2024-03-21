from datetime import datetime

def colorize(s: str, color: int) -> str:
    if color == -1:
        return s
    return f"\033[48;5;{color}m{s}\033[00m"

def main() -> None:
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip().split() for line in f.readlines()]
    width = len(puzzle[0])
    height = len(puzzle)
    print(f"Puzzle: ({width}x{height})")
    for y in range(height):
        for x in range(width):
            puzzle[y][x] = puzzle[y][x].lower()
            print(puzzle[y][x] + " ", end="")
        print()

    with open("words.txt", "r") as f:
        all_words = set([line.strip().lower() for line in f.read().split() if line != ""])
    print(f"{len(all_words)} words: {", ".join(all_words)}\n")

    colors = list(range(1, 15))
    color_index = 0

    start_t = datetime.now()
    undiscovered_words = set(all_words)
    discovered_words = set()
    word_locations = {}
    for y in range(height):
        for x in range(width):
            print(f"\rSolving: {100 * (y * width + x) / (width * height):.0f}%", end="")
            for x_offset, y_offset in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                possible_words = all_words - discovered_words
                y_pos = y
                x_pos = x
                i = 0
                while len(possible_words) > 0:
                    for word in [x for x in possible_words]:
                        if puzzle[y_pos][x_pos] != word[i]:
                            possible_words.remove(word)
                        elif i + 1 == len(word):
                            # matched word
                            discovered_words.add(word)
                            word_locations[word] = ((x, y), (x_offset, y_offset), colors[color_index % len(colors)])
                            color_index += 1
                            possible_words.remove(word)
                    y_pos += y_offset
                    x_pos += x_offset
                    i += 1
                    if x_pos < 0 or x_pos >= width or y_pos < 0 or y_pos >= height:
                        break
    print()
    print(f"(completed in {(datetime.now() - start_t).total_seconds():.4f} seconds)\n")

    # coloring map
    color_map = []
    for y in range(height):
        color_map.append([])
        for x in range(width):
            color_map[y].append(-1)

    for word in discovered_words:
        (x, y), (x_offset, y_offset), color = word_locations[word]
        for i in range(len(word)):
            color_map[y + (i * y_offset)][x + (i * x_offset)] = color

    for y in range(height):
        for x in range(width):
            print(colorize(puzzle[y][x], color_map[y][x]), end=" ")
        print()
    print(f"Found {len(discovered_words)}/{len(all_words)} words:")
    for word in discovered_words:
        print(f" {colorize("  ", word_locations[word][2])} {word}")
    print(f"Undiscovered words:")
    for word in (all_words - discovered_words):
        print(f"    \033[09m{word}\033[00m")


if __name__ == "__main__":
    main()