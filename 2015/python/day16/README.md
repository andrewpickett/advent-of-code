# Approach
### Part 1
> _What is the number of the Sue that got you the gift?_

I hardcoded the ticker values so that I can reference them. I then read all of the sue values from the input into an array of
"sues". Just iterate over the array and check that the values that are present for a given sue match those values in the
ticker. I did a logical "AND" on the keys lists for the ticker and each sue to only have to compare the keys that are
needed. If all of the values for those given keys match, then we found our Sue.

### Part 2
> _What is the number of the real Aunt Sue?_

This is pretty much the same as part one, but since there is an extra check of "<" and ">" for specific keys, I expanded
the list comprehension I wrote in part one to be more explicit and allow me to interject the comparisons for specific keys.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               7 |
| **Part Two** |               1 |

# Original puzzle
### --- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

* `children`, by human DNA age analysis.
* `cats`. It doesn't differentiate individual breeds.
* Several seemingly random breeds of dog: `samoyeds`, `pomeranians`, `akitas`, and `vizslas`.
* `goldfish`. No other kinds of fish.
* `trees`, all in one group.
* `cars`, presumably by exhaust or gasoline or something.
* `perfumes`, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:
```
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
```
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the **number** of the Sue that got you the gift?

### --- Part Two ---
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the `cats` and `trees` readings indicates that there are **greater than** that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the `pomeranians` and `goldfish` readings indicate that there are **fewer than** that many (due to the modial interaction of magnetoreluctance).

What is the **number** of the real Aunt Sue?
