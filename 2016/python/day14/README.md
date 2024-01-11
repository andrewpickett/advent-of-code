# Approach
### Data format

Just read the input as a string.

### Part 1
> _Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?_

It wasn't efficient, but I just had some nested loops: the first just incrementing a counter and doing a hash. If it found
the hash had 3 repeated characters, I then started a new loop that went from 1-1000 and hashed the new index to see if it has
5 repeated characters. If so, increment a counter of how many I've found and then just keep doing that until my counter hit 64.
Once there, just return the last index. It was very simple, but definitely not efficient, and I knew it would bite me in
part 2...

### Part 2
> _Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?_

It's not pretty, but it finishes. It takes almost a minute to run, but that's way better than the original way I had it written
(which I never let run long enough to finish...). I changed how I was doing things for this part by just running through
the first X numbers and generating all of the relevant hashes for them. For every stretched hash, I checked if it had 3 or 5 repeated
numbers in it and saved those -- along with the index of it -- to two lists for triples and pentuples. Then I could just
iterate through my list of triples, and see if I could find any hashes in the pentuples list that were within the next
thousand indexes and had the same repeated character.

I know there are ways that this could be improved, but I'm just going to move on.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             130 |
| **Part Two** |           53547 |
