# Approach
### Part 1
> _What is the sum of the priorities of those item types?_

Well I fell asleep...at 11:30pm...and didn't wake up until 12:10. Because of that, my solve time below for part 1 wasn't great,
when it really only took me about 5 minutes. Oh well.

This one ended up being fun to reduce. The idea is really simple and followed exactly what the instructions said:

* For each item in the data, split it in half.
* Check both halves to see which letter is common in both of them
* Take that letter and lookup the value associated with it
* Keep a running sum and return it.

The only "tricky" thing that I did to solve the above is to just use a string index to get the value. Since a-z corresponds to 1-26,
and A-Z corresponds to 27-52, I just wrote a single string that starts with a space (index 0), and every letter after that.
Then I can just do a `find()` with a character to get its value.

When I first wrote it, I wrote it out using full for loops and if-statements and it ended up being about 8-9 lines of code.
However, I then noticed it was just that: a for-loop with an if-statement to calculate a sum. So I just collapsed it all into a
comprehension, and voila -- solved it in one line! Pretty slick!

### Part 2
> _What is the sum of the priorities of those item types?_

Exactly the same as part 1, but the for loop is just iterating over groups of three, and we don't have do any halving of
the strings. So instead we change the range on the for-loop, change the condition on the if-statement, and it's done.

I wish I could say more here, but there really isn't much more!

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |   7967 |        1 |               4 |              00:14:58 | 5150 |
| **Part Two** |   2716 |        1 |               1 |              00:04:48 | 3705 |

# Original puzzle
### --- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf
didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The
Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the
errors. Every item type is identified by a single lowercase or uppercase letter (that is, `a` and `A` refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of
items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the
second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

* The first rucksack contains the items `vJrwpWtwJgWrhcsFMMfFFhFp`, which means its first compartment contains the items `vJrwpWtwJgWr`, while the second compartment contains the items `hcsFMMfFFhFp`. The only item type that appears in both compartments is lowercase `p`.
* The second rucksack's compartments contain `jqHRNqRjqzjGDLGL` and `rsFMfFZSrLrFZsSL`. The only item type that appears in both compartments is uppercase `L`.
* The third rucksack's compartments contain `PmmdzqPrV` and `vPwwTWBwg`; the only common item type is uppercase `P`.
* The fourth rucksack's compartments only share item type `v`.
* The fifth rucksack's compartments only share item type `t`.
* The sixth rucksack's compartments only share item type `s`.

To help prioritize item rearrangement, every item type can be converted to a priority:

* Lowercase item types `a` through `z` have priorities `1` through `26`.
* Uppercase item types `A` through `Z` have priorities `27` through `52`.

In the above example, the priority of the item type that appears in both compartments of each rucksack is `16` (`p`), `38` (`L`),
`42` (`P`), `22` (`v`), `20` (`t`), and `19` (`s`); the sum of these is `157`.

Find the item type that appears in both compartments of each rucksack.

### --- Part Two ---

As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency,
within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item
type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any
other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be
pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the
right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the
above example, the first group's rucksacks are the first three lines:

```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
```

And the second group's rucksacks are the next three lines:

```
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

In the first group, the only item type that appears in all three rucksacks is lowercase `r`; this must be their badges.
In the second group, their badge item type must be `Z`.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are `18` (`r`) for the
first group and `52` (`Z`) for the second group. The sum of these is `70`.

Find the item type that corresponds to the badges of each three-Elf group.
