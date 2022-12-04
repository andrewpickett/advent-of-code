# Approach
### Part 1
> _In how many assignment pairs does one range fully contain the other?_

Got a couple minute delay because my dog decided she needed to go out at EXACLTY 11:59pm tonight. But after that, this puzzle
was pretty much just parsing the data into the right format and doing some quick comparisons. Basically to check if one of the
data ranges fully encompasses another in any given pair, just check if the start of one is less than or equal to the start of another while
the end of the same one is greater than or equal to the end of the other.

This was really fast to implement, but my first guess was incorrect. Turns out I forgot to parse the values into integers,
so my `<=` and `>=` operators were comparing strings, not ints...which led me to an incorrect answer. It took me a
couple of minutes to debug and find that, so my overall time wasn't great, but it was still not too bad. I then just collapsed
my for/if statements into a comprehension and extracted my comparisons to a separate function.

### Part 2
> _In how many assignment pairs do the ranges overlap?_

For this I just needed to create a new comparison function. In order to check if there is ANY overlap of the two sections,
I just check to see if the start OR end point of either point resides in the range of the other. It's 4 "between" comparisons,
but it's still very fast and pretty straightforward.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |    441 |        2 |               5 |              00:10:16 | 4765 |
| **Part Two** |    861 |        1 |               6 |              00:04:00 | 4431 |

# Original puzzle
### --- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the
job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap.
To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for
each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```

For the first few pairs, this list means:

* Within the first pair of Elves, the first Elf was assigned sections `2-4` (sections `2`, `3`, and `4`), while the second Elf was assigned sections `6-8` (sections `6`, `7`, `8`).
* The Elves in the second pair were each assigned two sections.
* The Elves in the third pair were each assigned three sections: one got sections `5`, `6`, and `7`, while the other also got `7`, plus `8` and `9`.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

```
.234.....  2-4
.....678.  6-8
```

```
.23......  2-3
...45....  4-5
```

```
....567..  5-7
......789  7-9
```

```
.2345678.  2-8
..34567..  3-7
```

```
.....6...  6-6
...456...  4-6
```

```
.23456...  2-6
...45678.  4-8
```

Some of the pairs have noticed that one of their assignments fully contains the other. For example, `2-8` fully contains `3-7`,
and `6-6` is fully contained by `4-6`. In pairs where one assignment fully contains the other, one Elf in the pair would be
exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration.
In this example, there are `2` such pairs.

### --- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that
overlap at all.

In the above example, the first two pairs (`2-4,6-8` and `2-3,4-5`) don't overlap, while the remaining four pairs
(`5-7,7-9`, `2-8,3-7`, `6-6,4-6`, and `2-6,4-8`) do overlap:

* `5-7,7-9` overlaps in a single section, `7`.
* `2-8,3-7` overlaps all of the sections `3` through `7`.
* `6-6,4-6` overlaps in a single section, `6`.
* `2-6,4-8` overlaps in sections `4`, `5`, and `6`.

So, in this example, the number of overlapping assignment pairs is `4`.
