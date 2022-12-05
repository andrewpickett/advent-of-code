# Approach
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

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |     98 |        1 |              23 |                   N/A |  N/A |
| **Part Two** |   4042 |        1 |              22 |                   N/A |  N/A |


# Original puzzle
### --- Day 10: Balance Bots ---
You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

```
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
```

* Initially, bot `1` starts with a value-`3` chip, and bot `2` starts with a value-`2` chip and a value-`5` chip.
* Because bot `2` has two microchips, it gives its lower one (`2`) to bot `1` and its higher one (`5`) to bot `0`.
* Then, bot `1` has two microchips; it puts the value-`2` chip in output `1` and gives the value-`3` chip to bot `0`.
* Finally, bot `0` has two microchips; it puts the `3` in output `2` and the `5` in output `0`.

In the end, output bin `0` contains a value-`5` microchip, output bin `1` contains a value-`2` microchip, and output bin `2` contains a value-`3` microchip. In this configuration, bot number `2` is responsible for comparing value-5 microchips with value-`2` microchips.


### --- Part Two ---
What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
