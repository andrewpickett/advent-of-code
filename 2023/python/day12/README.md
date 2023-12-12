# Approach
### Part 1
> _What is the sum of those counts?_

I had a couple of thoughts going into this one. The first thought I had was almost creating a bitmask out of the spring
data. Then creating all possible groups out of the group numbers and doing a logical `AND` type of operation to find
which groupings actually worked on the given map.

I started down that road, and promptly gave up...it was going to be quite difficult.

The next idea I had was to use some dynamic programming with recursion to go character by character and find valid
spring groupings.

Ok...so I started the recursive approach. The first way I did this ended up not working out so well for me (worked for all
of the samples, but got the wrong answer multiple times on the actual input). Basically I started scanning through the
spring mapping and if I came across any `?` or `#` values, I checked if I would be able to fit the next spring grouping
on there before I reached the next `.`. I did this by using the grouping numbers as a stack, and so when I recursed,
I passed in a substring of the mapping and the remaining stack of group numbers. Like I said, I got this working for
everything on the samples, but just kept having some edge case not work on the real thing -- so I re-designed it.

I decided to just move one character at a time through and handle each of the use cases individually. So I need to keep
track of a position marker (where I am in the input string), a group number (which group I'm currently trying to work on),
and then the two pieces of data.

With that, I can just check the 3 cases:
1. `.` -- This is basically pointless, and I can just move my pointer forward...
2. `#` -- I must be starting a group, so check if I can insert the next group. If not, move the pointer to the next `.`...but if I can, then go ahead and do that.
3. `?` -- Here's where you need to recurse twice: once assuming it's a `.` and once for a `#`.

Then I just needed to handle the base cases to actually determine if it was valid or not.

Once that was set up, I ran it, got the answer and moved to part 2!

### Part 2
> _Unfold your condition records; what is the new sum of possible arrangement counts?_

So, I had actually assumed it was going to be something like this, so during part 1, I decided to just keep a record
of any sub-use-cases I ran into in a giant map. That way if I ever ran into those same problems, I already had the
answer without needing to recurse over and over.

I'm glad I did that, because once I multiplied my input by 5 and ran it, I got the answer right away...and it was FAST.

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        3 |              40 |              00:40:02 | 2776 |
| **Part Two** |        1 |             419 |              00:41:07 |  631 |


# Original puzzle
### --- Day 12: Hot Springs ---
You finally reach the hot springs! You can see steam rising from secluded areas attached to the primary, ornate building.

As you turn to enter, the researcher stops you. "Wait - I thought you were looking for the hot springs, weren't you?" You indicate that this definitely looks like hot springs to you.

"Oh, sorry, common mistake! This is actually the onsen! The hot springs are next door."

You look in the direction the researcher is pointing and suddenly notice the massive metal helixes towering overhead. "This way!"

It only takes you a few more steps to reach the main gate of the massive fenced-off area containing the springs. You go through the gate and into a small administrative building.

"Hello! What brings you to the hot springs today? Sorry they're not very hot right now; we're having a **lava shortage** at the moment." You ask about the missing machine parts for Desert Island.

"Oh, all of Gear Island is currently offline! Nothing is being manufactured at the moment, not until we get more lava to heat our forges. And our springs. The springs aren't very springy unless they're hot!"

"Say, could you go up and see why the lava stopped flowing? The springs are too cold for normal operation, but we should be able to find one springy enough to launch **you** up there!"

There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure which springs would even be **safe** to use! Worse yet, their **condition records of which springs are damaged** (your puzzle input) are also damaged! You'll need to help them repair the damaged records.

In the giant field just outside, the springs are arranged into **rows**. For each row, the condition records show every spring and whether it is **operational** (`.`) or **damaged** (`#`). This is the part of the condition records that is itself damaged; for some springs, it is simply **unknown** (`?`) whether the spring is operational or damaged.

However, the engineer that produced the condition records also duplicated some of this information in a different format! After the list of springs for a given row, the size of each **contiguous group of damaged springs** is listed in the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size of its contiguous group (that is, groups are always separated by at least one operational spring: `####` would always be `4`, never `2,2`).

So, condition records with no unknown spring conditions might look like this:
```
#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
```
However, the condition records are partially damaged; some of the springs' conditions are actually **unknown** (`?`). For example:
```
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
```
Equipped with this information, it is your job to figure out **how many different arrangements** of operational and broken springs fit the given criteria in each row.

In the first line (`???.### 1,1,3`), there is exactly **one** way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (`#.#`), making the whole row `#.#.###`.

The second line is more interesting: `.??..??...?##. 1,1,3` could be a total of **four** different arrangements. The last `?` must always be broken (to satisfy the final contiguous group of three broken springs), and each `??` must hide exactly one of the two broken springs. (Neither `??` could be both broken springs or they would form a single contiguous group of two; if that were true, the numbers afterward would have been `2,3` instead.) Since each `??` can either be `#.` or `.#`, there are four possible arrangements of springs.

The last line is actually consistent with **ten** different arrangements! Because the first number is `3`, the first and second `?` must both be `.` (if either were `#`, the first number would have to be `4` or higher). However, the remaining run of unknown spring conditions have many different ways they could hold groups of two and one broken springs:
```
?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
```
In this example, the number of possible arrangements for each row is:

* `???.### 1,1,3` - **`1`** arrangement
* `.??..??...?##. 1,1,3` - **`4`** arrangements
* `?#?#?#?#?#?#?#? 1,3,1,6` - **`1`** arrangement
* `????.#...#... 4,1,1` - **`1`** arrangement
* `????.######..#####. 1,6,5` - **`4`** arrangements
* `?###???????? 3,2,1` - **`10`** arrangements

Adding all of the possible arrangement counts together produces a total of **`21`** arrangements.

For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. **What is the sum of those counts?**

### --- Part Two ---
As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually **folded up** this whole time!

To **unfold the records**, on each row, replace the list of spring conditions with five copies of itself (separated by `?`) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by `,`).

So, this row:
```
.# 1
```
Would become:
```
.#?.#?.#?.#?.# 1,1,1,1,1
```
The first line of the above example would become:
```
???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
```
In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

* `???.### 1,1,3` - **`1`** arrangement
* `.??..??...?##. 1,1,3` - **`16384`** arrangements
* `?#?#?#?#?#?#?#? 1,3,1,6` - **`1`** arrangement
* `????.#...#... 4,1,1` - **`16`** arrangements
* `????.######..#####. 1,6,5` - **`2500`** arrangements
* `?###???????? 3,2,1` - **`506250`** arrangements

After unfolding, adding all of the possible arrangement counts together produces **`525152`**.

Unfold your condition records; **what is the new sum of possible arrangement counts?**
