# Approach
### Part 1
> _Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?_

So my approach with this first part was just to code it exactly like the example shows: Basically just have an array,
and append new fish with a value of "8" every time a fish hits "0". Iterating through every element of the list
for every day.

It worked, it was fine...everything was fine...

### Part 2
> _How many lanternfish would there be after 256 days?_

Oh boy...So, I obviously knew the above approach wasn't going to work, because it would be billions or trillions of
entries. For fun, I kicked it off while I rewrote my approach, just in case it somehow did finish faster than I thought.

Alright, so, at this point it's about 12:30am, so my critical thinking was starting to fade...
My first thought was to try a 100% math-based approach to figuring out the total number. I tried a number of approaches for this,
but basically it was given the starting number and the number of days to check ahead, you can easily figure out how many
immediate children any fish would have over that many days. After that, you need to take EACH of those children and calculate
how many children IT would have, etc...Sounded quite recursive. So that's the approach I started going.

After a couple fumbles with maths, I got what seemed to be a working solution, so I kicked it off...Not surprisingly, it
just kept going (because after thinking about it, it's really NOT saving anything, because I'm still iterating over
every single "entry", just not in an actual array).

Alright, so we're at about 1:00am now, and I decided to scrap that approach and try going with an array-based method where
I would trim off "completed" fish. Basically I figured I would iterate over the days, and every time a fish hit "0", calculate how
many more fish it would create in its future, and then remove it from the list completely...but add its children. Keep doing that
and in theory it should all work itself out.

Well, what I didn't plan on was a thunderstorm waking my kids and dog up at 1:15am...which means I spent the next 30 minutes
trying to get everyone settled down.

Now it's 1:45am, I'm really tired, everything I try was giving me completely wrong answers, and I couldn't seem to make heads or
tails out of anything I debugged. I was just falling further and further down a rabbit hole..

So finally at around 2:15am, I decided to go bed and look at it fresh in the morning.

Well, sure enough, I woke up, re-read the problem, and immediately saw the solution in my head: just keep track of the number
of fish for a given "fertility" number. So I only need to keep an array of size 9 which just holds "counts". At the end
just sum up the total counts and that's the answer.

So after all that, 10 minutes of coding later, I had the solution...awesome...

# Results

|              |        Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) |  Rank |
|--------------|--------------:|---------:|----------------:|----------------------:|------:|
| **Part One** |        386536 |        1 |               0 |              00:06:32 |  1313 |
| **Part Two** | 1732821262171 |        3 |               0 |             ~02:00:00 | 30337 |

# Original puzzle

--- Day 6: Lanternfish ---
The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every `7` days.

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have `2` days left until it creates another lanternfish, while another might have `4`. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

So, suppose you have a lanternfish with an internal timer value of `3`:

* After one day, its internal timer would become `2`.
* After another day, its internal timer would become `1`.
* After another day, its internal timer would become `0`.
* After another day, its internal timer would reset to `6`, and it would create a new lanternfish with an internal timer of `8`.
* After another day, the first lanternfish would have an internal timer of `5`, and the second lanternfish would have an internal timer of `7`.

* A lanternfish that creates a new fish resets its timer to `6`, not `7` (because `0` is included as a valid timer value). The new lanternfish starts with an internal timer of `8` and does not start counting down until the next day.

Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:
```
3,4,3,1,2
```
This list means that the first fish has an internal timer of `3`, the second fish has an internal timer of `4`, and so on until the fifth fish, which has an internal timer of `2`. Simulating these fish over several days would proceed as follows:
```
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```
Each day, a `0` becomes a `6` and adds a new `8` to the end of the list, while each other number decreases by `1` if it was present at the start of the day.

In this example, after `18` days, there are a total of `26` fish. After 80 days, there would be a total of `5934`.

Find a way to simulate lanternfish. How many lanternfish would there be after `80` days?

Your puzzle answer was 386536.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After `256` days in the example above, there would be a total of `26984457539` lanternfish!

How many lanternfish would there be after `256` days?
