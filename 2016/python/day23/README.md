# Approach
### Data format

Read the input as a program into my AssembunnyProgram class. That will take care of all the parsing and reading of it.

### Part 1
> _What value should be sent to the safe?_

I just added a new `tgl` instruction to my Assembunny program code. Implemented exactly how it's described. Once I did that,
I was able to just run the code on the input, and it worked exactly as expected.

### Part 2
> _Anyway, what value should actually be sent to the safe?_

Alright, well, I knew I would have to do something tricky and clever here to identify loops or something. Obviously the
clue about "multiply" was important. However, I ended up just kicking off my normal code and started working on the
optimizations.

I ended up leaving, forgetting that I had it running, and after about an hour or 2, I came back and saw that it came back
with an answer...so...I just tried it out and it was correct.

Eventually I need to go back and actually code this the way it's supposed to, but for now, I'll take the W.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              70 |
| **Part Two** |         4262220 |
