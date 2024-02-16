# Approach
### Data format

Read in the input as an array of dance moves (just split on the commas). I then add those to a dictionary along with
the initial list of dance partners, so that I can do unit testing easier.

### Part 1
> _In what order are the programs standing after their dance?_

I originally was going to try to create a linked list because I assumed part 2 was going to somehow make this crazy hard
with an array implementation. I was struggling a little bit with getting a good implementation with a linked list, so
I decided to just write it as an array and see how it went. This was part just fine, and it ran nice and fast.

I did forget that in Python, you can swap elements in a list `L` by just doing `L[a], L[b] = L[b], L[a]`, so that made
my code a whole lot cleaner!

### Part 2
> _In what order are the programs standing after their billion dances?_

Well, my array implementation was going to work just fine, because at this point it was all about finding patterns.

My initial thought was to try to find a cycle, so I did a quick implementation and it just ran without finding any...
So I spent the next hour trying to find patterns for each individual character, because I assumed it would be something
with LCM or just taking each position one at a time to build the final string...but after I manually went through and
found the cycles for each position, it turns out it should have had a cycle every 63 positions!

So I revisited my code for detecting duplicates and found I had a bug...so I fixed that, re-ran my code, found the 63 cycle
and then I just had to divide `1,000,000,000` by `63` and take the remainder to determine which dance pattern would happen
on the billionth cycle.

I wasted so much time because of a silly little bug. Such is the life of a programmer.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               9 |
| **Part Two** |             641 |
