# Approach
### Data format

So the crux of this problem is that we don't actually care about the numbers ON the stones, but more the NUMBER of stones
themselves. So as we divide and build and everything we can just keep a map of the counts of the number of stones for
any given number. So my data format for this puzzle is just that: a simple map of `number` to `count`.

### Part 1
> _How many stones will you have after blinking 25 times?_

Like most people, I solved this one by doing exactly what the instructions said. Just build an array by replacing
the values based on the rules. It was quick, it ran fast, and I was done in a couple minutes...but obviously I knew
what was coming in part 2...

### Part 2
> _How many stones would you have after blinking a total of 75 times?_

The problem with this, is if you try to brute force it, it slows to a crawl very quickly (around 30 blinks or so).
I'm sure you could let it run for a LONG time (hours?) and it would finish and work...but clearly there's a trick.

As mentioned in the data format above, we just need to know the number of stones, not the numbers ON the stones.
So by keeping a map of the numbers, and how many we have, we can easily then just add up the counts to get the total
number of stones.

So, all I do is keep a map of the numbers on the stones with how many there are. This doesn't actually explode as quickly
or easily as you might think. In fact for part 1, there are only 474 distinct numbers in the map after all 25 blinks,
and for part 2, there are 3777 for my input. It's then very trivial to just add up 3777 values from a map and that's
the answer! Fun little puzzle!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              10 |
| **Part Two** |             270 |
