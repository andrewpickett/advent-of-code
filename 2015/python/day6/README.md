# Approach
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

# Original puzzle
### --- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at `0,0`, `0,999`, `999,999`, and `999,0`. The instructions include whether to `turn on`, `turn off`, or `toggle` various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like `0,0 through 2,2` therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

* `turn on 0,0 through 999,999` would turn on (or leave on) every light.
* `toggle 0,0 through 999,0` would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
* `turn off 499,499 through 500,500` would turn off (or leave off) the middle four lights.

After following the instructions, **how many lights are lit**?

### --- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase `turn on` actually means that you should increase the brightness of those lights by `1`.

The phrase `turn off` actually means that you should decrease the brightness of those lights by `1`, to a minimum of zero.

The phrase `toggle` actually means that you should increase the brightness of those lights by `2`.

What is the **total brightness** of all lights combined after following Santa's instructions?

For example:

* `turn on 0,0 through 0,0` would increase the total brightness by `1`.
* `toggle 0,0 through 999,999` would increase the total brightness by `2000000`.
