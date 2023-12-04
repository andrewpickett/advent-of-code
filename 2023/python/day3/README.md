# Approach
### Part 1
> _What is the sum of all of the part numbers in the engine schematic?_

Ok, so I'm really ticked at myself for this one. I created a Grid class a few years ago, that really comes in handy with
any puzzles that require knowing about neighbors for points in a grid. I decided to start using that and it worked
perfectly. I had the data parsed and all of the points mapped with their neighbors within 1 minute of the puzzle starting.

I wrote some quick code, got an answer and it was wrong. I looked through everything and found a defect, which I fixed and
was SURE my new answer would be correct -- nope...wrong again.

I spent the next 40 minutes trying to figure out what my problem was, and just could not figure it out...

...yeah...so...it turns out I just can't read and I was adding all the numbers that WEREN'T valid/connected to a special
symbol. Instead of using the numbers that were invalid..

So I just changed which numbers I used and I got the right number immediately.

I should have had this one solved in 5 minutes, but I just didn't read carefully. So ticked at myself.

Long story short, I iterate over every point. If it's a number, I start building the current number as I read through them.
While I'm reading each digit, I check if any neighbors are special characters. If so, I know the whole number will be valid.
Once I get to the end of a row or any non-digit, I know I'm done with building the current number and I can check if it was valid
at any point.

At the end, I have a list of all numbers that were valid, and I can just sum them up.

### Part 2
> _What is the sum of all of the gear ratios in your engine schematic?_

This one wasn't really any harder than the first, since I already had the framework and everything. I just changed what
it meant to be "adjacent" to something valid and instead of a simple boolean tracker, I kept track of all of the numbers
adjacent to the gears. At the end, just sum up which ones had exactly 2 numbers attached to it. Pretty much the same
logic as part 1, so I could probably extract things out a bit more, but I don't want to right now...

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        3 |              46 |              00:48:04 | 5524 |
| **Part Two** |        1 |              36 |              00:58:55 | 4245 |


# Original puzzle
### --- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can **add up all the part numbers** in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently **any number adjacent to a symbol**, even diagonally, is a "part number" and should be included in your sum. (Periods (`.`) do not count as a symbol.)

Here is an example engine schematic:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, two numbers are **not** part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so **is** a part number; their sum is `4361`.

Of course, the actual engine schematic is much larger. **What is the sum of all of the part numbers in the engine schematic?**

### --- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A **gear** is any `*` symbol that is adjacent to **exactly two part numbers**. Its **gear ratio** is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, there are **two** gears. The first is in the top left; it has part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is in the lower right; its gear ratio is `451490`. (The `*` adjacent to `617` is **not** a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces `467835`.

**What is the sum of all of the gear ratios in your engine schematic?**
