# Approach
### Data format

Read the full line as a string from the file...that's it.

### Part 1
> _Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?_

The code isn't pretty, but it works. I didn't really do anything fancy to solve it. The idea was to just keep a map
of both bots and outputs. Whenever a value gets assigned, just push the value into the bucket with the id of the bot, and
whenever a bot gives values, we just need to pop the low/high (using `min`/`max` functions) to whichever target it says.

I then also just kept track of which bot does the given comparison so that when the instructions completed, I could just
return that bot number to get the answer to this first part.

The "tricky" part was actually just understanding the instructions. Once I finally realized -- after reading it 20 times --
that I just have to keep looping over the data until all of the instructions have been run, it wasn't too bad. But that part
alone took quite a bit of time.

### Part 2
> _What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?_

There really wasn't any different on this one. Since I already had the maps containing all of the values, I just had to
multiply the first 3 outputs.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              23 |
| **Part Two** |              22 |
