# Approach
### Part 1
> _In the output values, how many times do digits `1`, `4`, `7`, or `8` appear?_

There's a lot of words to describe everything here...and a lot of it is very confusing at first read (but the main CONCEPT is pretty simple).

The funny part with part 1, here, is that by the time you get to the end, you realize you don't care about 90% of what was said above (for now).

So for this part, just loop over all of the output values (everything after the `|` on the input lines) and just count how many have words
that are 2, 3, 4, or 7 characters long...add them up and that's the answer.

### Part 2
> _What do you get if you add up all of the output values?_

So, I looked at this and thought it was going to take a long time and brain power to figure out, so I decided to just
go to sleep and tackle it first thing in the morning.

As I started working on it, I started just writing down everything that I knew or could find out. I started having so many maps
show up in my code, because I was tracking all the configurations, locations of each line for each number, etc...etc...

While I was doing that, I was also just looking at what numbers overlap others (which became the key).

Now, after I was in map-hell, I decided to scrap everything and started looking at another approach: permutations.
I figure there are only 5040 possible arrangements of lines to letters, so I thought it would probably be easiest to just
loop over all permutations and then just check all the input values to find the permutation that results in all valid
values for the input. It would make it really easy and not have to worry about any logic around overlapping numbers.
I briefly started writing it this way, but realized the actual implementation of it was a little more cumbersome than I
wanted...so I decided to just go back to my "old" way...

But I had already realized the following:

* **1, 4, 7, 8**: are numbers for which we already know all the values.
* **0, 6, 9**: we can figure all of these out just by knowing the above!
  * Whichever number doesn't overlap with "1" completely is "6"
  * Whichever number doesn't overlap with "4" completely is "0"
  * The remaining one is "9"
* **2, 3, 5**: We can figure these out once we have the above!
  * Whichever number overlaps with "6" completely is "5"
  * Whichever number overlaps with "9" completely is "3"
  * The remaining one is "2"

So given that, we know all the numbers' mappings! In order to then decode the outputs, I just sort all of the mappings
alphabetically, sort the outputs alphabetically, and lookup the index of the output value in my mapping to determine the
actual number represented. Add it all up and it works.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|-------:|---------:|----------------:|----------------------:|------:|
| **Part One** |    421 |        1 |               0 |              00:12:39 |  3027 |
| **Part Two** | 986163 |        1 |              11 |             ~01:00:00 | 21655 |

# Original puzzle

### --- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named `a` through `g`:
```
0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```
So, to render a `1`, only segments `c` and `f` would be turned on; the rest would be off. To render a `7`, only segments `a`, `c`, and `f` would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires `a` through `g`, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires `b` and `g` are turned on, but that doesn't mean segments `b` and `g` are turned on: the only digit that uses two segments is `1`, so it must mean segments `c` and `f` are meant to be on. With just that information, you still can't tell which wire (`b`/`g`) goes to which segment (`c`/`f`). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:
```
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
```
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a `|` delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because `7` is the only digit that uses three segments, `dab` in the above example means that to render a `7`, signal lines `d`, `a`, and `b` are on. Because `4` is the only digit that uses four segments, `eafb` means that to render a `4`, signal lines `e`, `a`, `f`, and `b` are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (`cdfeb fcadb cdfeb cdbaf`) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:
```
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
```
Because the digits `1`, `4`, `7`, and `8` each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits `1`, `4`, `7`, or `8` appear?

### --- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:
```
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
```
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:
```
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
```
So, the unique signal patterns would correspond to the following digits:

* `acedgfb`: `8`
* `cdfbe`: `5`
* `gcdfa`: `2`
* `fbcad`: `3`
* `dab`: `7`
* `cefabd`: `9`
* `cdfgeb`: `6`
* `eafb`: `4`
* `cagedb`: `0`
* `ab`: `1`

Then, the four digits of the output value can be decoded:

* `cdfeb`: `5`
* `fcadb`: `3`
* `cdfeb`: `5`
* `cdbaf`: `3`

Therefore, the output value for this entry is `5353`.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

* `fdgacbe cefdb cefbgd gcbe`: `8394`
* `fcgedb cgb dgebacf gc`: `9781`
* `cg cg fdcagb cbg`: `1197`
* `efabcd cedba gadfec cb`: `9361`
* `gecf egdcabf bgf bfgea`: `4873`
* `gebdcfa ecba ca fadegcb`: `8418`
* `cefg dcbef fcge gbcadfe`: `4548`
* `ed bcgafe cdgba cbgef`: `1625`
* `gbdfcae bgc cg cgb`: `8717`
* `fgae cfgab fg bagce`: `4315`

* Adding all of the output values in this larger example produces `61229`.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
