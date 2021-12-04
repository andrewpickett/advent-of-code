# Approach
### Part 1
> _What will your final score be if you choose that board?_

The first challenge with a puzzle like this is just parsing the input data into some sort of data model that makes sense.
Obviously I wanted to separate the called numbers from the boards themselves, so getting the data became a mutli-step
process:
1. Parse all of the lines of the file
2. Read the first line into a list of numbers
3. Go through the rest of the input and build boards, knowing that whenever there was a blank line, it was the end of a board.

Now, instead of building multi-dimensional arrays (which I hate working with), I decided to represent the boards as just
a single array. Given that, the next challenge is figuring out when a board has won. I decided to just brute force the
check and check the different elements in the single array that would represent a row or column.

Once those are in place, it was just a matter of reading each number from the called number list and marking them down on each
board (by replacing the value with an 'x'). After each time a board is marked, check if it's in a winning state. If it is, then just multiply that last number
by the sum of the squares left on the board.

I ran into some silly mistakes I made while doing it, so it took a bit longer to debug than I wanted, but the overall solution
was pretty simple.

### Part 2
> _Once it wins, what would its final score be?_

So with this one, I was able to use almost everything exactly the same as the first part, but instead of stopping when I
found a winning board, I just kept going until there were no boards left. At that point, I just looked at the last one that
"won" and performed the same calculation to determine the score.

This one did cause me a little bit of a headache, because I was manipulating the list of boards in place (removing them when
they "won")...but what that ended up doing was removing them from the list while I was iterating over them, which means the
index was then off. So, I got the answer wrong at first and had to spend about 15 minutes debugging where the issue was to
figure that out. Once I did, I had to keep track of which boards were going to be removed and then remove them separately
after all the boards were marked. I also struggled with equality checking of the boards, so the code that I used is not
pretty, but it gets the job done.

After that, I got the right answer and went to bed...

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |  41503 |        2 |               2 |              00:25:55 | 2039 |
| **Part Two** |   3178 |        2 |               6 |              00:33:14 | 4313 |

# Original puzzle

### --- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
```
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7
```
After the first five numbers are drawn (`7`, `4`, `9`, `5`, and `11`), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):
```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```
After the next six numbers are drawn (`17`, `23`, `2`, `0`, `14`, and `21`), there are still no winners:
```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```
Finally, `24` is drawn:
```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: `14 21 17 24 4`).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is `188`. Then, multiply that sum by the number that was just called when the board won, `24`, to get the final score, `188 * 24 = 4512`.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

### --- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after `13` is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to `148` for a final score of `148 * 13 = 1924`.

Figure out which board will win last. Once it wins, what would its final score be?
