# Word Searcher

A rudimentary word search solver that I made for funsies. Able to solve word searches with hundreds of words in fractions of a second.

## `word-searcher.py`

Star of the show. Reads the puzzle data from `puzzle.txt` and the words to search for from `words.txt`. Here is some example output on a small word search:

<img src="https://github.com/jaxsonp/word-searcher/blob/main/example_output.png?raw=true" alt="example output" width="300"/>

## `generate.py`

This python file generates a word search using a given width, height, and number of words. It saves the generated puzzle and word list to `puzzle.txt` and `words.txt`, ready to be solved. The random words are taken from [a repo containing a list of the 10,000 most common English words](https://github.com/first20hours/google-10000-english/tree/master), more specifically the medium and long words from the no-swears category.
