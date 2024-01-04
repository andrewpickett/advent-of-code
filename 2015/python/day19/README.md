# Approach
### Data format

I just read in the input as 2 parts: The molecule (which is the last line) and then the mappings which are every other line.

For the molecule, I store it as a list of individual elements, that way I can look them up in the mapping dictionary by their
key. This was a little trickier than all of the samples he gave, as elements can be multiple letters, so I use the fact that
new elements start with an upper case letter to determine each element in the molecule.

For the mapping, I just store it as the element to molecule mapping defined in the file.

### Part 1
> _How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?_

Loop through every element in the target molecule and perform every replacement one time on it. Add it to the set and
return the length of the set. Pretty simple.

### Part 2
> _Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?_

Holy cow -- this is the first problem that has caused me DAYS of troubleshooting, head scratching, and just general anger...

I spent a LONG time on this one, and honestly, looking back at it, I don't remember EVERYTHING that I did to make it work.

I do know I worked backwards from the target molecule and work from right to left to replace values keeping track of the shortest
path as I go...

I also think somehow my solution would only give the right answer like 50% of the time. I really don't care. I got it working,
I got the right answer, and I moved on. This one sucked.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |              23 |
