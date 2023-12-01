# Approach
### Part 1
> What is the sum of all of the calibration values?

Pretty standard "first" puzzle, in that it's along the lines of "for each line, add up a total...", but this was actually a LITTLE
tougher than most other "day 1" puzzles.

The first way I solved it was with regular expressions and just iterate over every line, replace any/all non-numeric characters with
blanks, leaving a string of just the numbers. Then it's just return 10 times the first character plus the last character.

Sum every line together and you have your answer.

I tried to make it more concise and pythonic...but after a few minutes of trying, I figured it's good enough and I left it.

### Part 2
> What is the sum of all of the calibration values?

Ok...this is day 1...right?!?!?! I mean, on the outset it seemed like this was not much more difficult that part one, but
I just kept running into bugs and defects as I wrote it.

The first trap I ran into, was I just iterated over all the word-numbers and replaced them in the original string with the
number instead. This obviously broke because of cases where the numbers "overlap" like `eightwo` -- my solution was leaving it
as `eigh2` because I was going in order of numbers while I replaced, not in order left to right.

So once I figured that out, I changed it to start left to right and replace any numbers I ran into...I thought for sure it was
working and correct, because I completely misinterpreted the instructions. I assumed something like `eightwone` would be
represented as `8w1` because it should replace the `eight` with `8` and then that just leaves `wone` which would be `w1`...

My solution worked for all the samples, and his description did NOT make it clear that that was the incorrect interpretation.
So I spent 30 minutes just fighting with it, debugging, and trying to figure out what was wrong. Eventually I just decided that
maybe the issue was my interpretation, and it should be that `eightwone` should become `821`...once I made that change
I got the right answer.

I then thought I was being really silly or that lack of sleep was causing me to not think straight, but I then read that a
lot of people had the same issue as me, and it was just a very ambiguously written problem.

I really hope the rest go smoother this year.

# Original puzzle
### --- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all **fifty stars** by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been **amended** by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific **calibration value** that the Elves now need to recover. On each line, the calibration value can be found by combining the **first digit** and the **last digit** (in that order) to form a single **two-digit number**.

For example:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```
In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `142`.

Consider your entire calibration document. What is the sum of all of the calibration values?

### --- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually **spelled out with letters**: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` **also** count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```
In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces `281`.

What is the sum of all of the calibration values?
