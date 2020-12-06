# Approach
### Part 1
> _For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?_

So I misread the instructions at first, and my first answer was incorrect...but I couldn't figure out why.
I finally realized where I misread and it made this part of the puzzle MUCH easier than what I had
originally. Really just take the input, divide it into groups (split on double new line), and add
every letter to a set. This will remove duplicates and leave you with the unique list of questions
answered within the group...so then just add them all together and you have your answer.

### Part 2
> _For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?_

It's actually really funny...you remember how I said I mis-read the instructions for part one, and so my
first answer was wrong? Yeah...that's because I had actually solved part 2 initially.

After dividing the input into the groups, you just iterate over each member in a group and count the number
of times each letter is used. Then add up the number of times each letter count matches the number of
people in the group (which is the number of lines).

Add all of those up for the whole file and you have your answer.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 6583  | 2  | 1  | 00:11:40  | 4378  |
| **Part Two**  | 3290  | 1  | 4  | 00:07:52  | 3573  |
