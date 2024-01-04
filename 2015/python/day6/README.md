# Approach
### Data format

I read in each line of the input as an individual string with any whitespace removed. All stored in a single list.

I will then parse each line while processing them into tuples of coordinates, but that happens during the program execution...

### Part 1
> _After following the instructions, how many lights are lit?_

Ah, the first puzzle where creating the data structure and parsing the input is the most difficult part. I decided to just
implement this one exactly as described: create a 1000x1000 2-d array initialized to `0` and then run through all of the
instructions one by one changing the values in the grid.

Once the grid is initialized, we parse the input lines. The first step is to determine the coordinate range that will be
impacted, which I do through just a bunch of split/parse commands.

Once I have the coordinates, I check the command -- if it's "turn off" just iterate over those coordinates from start to end
and set the value to 0. If it's "turn on" set it to 1. If it's "toggle" just switch it.

It's not efficient in any capacity -- I imagine the "better" way to do this is to just keep a state or counter instead of
actually manipulating a 2-d array, but it finishes in about 5 seconds as is, which is fine with me.

### Part 2
> _What is the total brightness of all lights combined after following Santa's instructions?_

Exactly the same as part 1, but change the behavior based on the command. So instead of only having 0/1 values, we simply
use the command to determine how much to change the value (1, -1, or 2). By just updating that function that checks the commands,
the code worked as is. It's still super slow, but it works.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            5240 |
| **Part Two** |            8167 |
