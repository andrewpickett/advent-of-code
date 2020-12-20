# Approach
### Part 1
> _Find the two entries that sum to 2020; what do you get if you multiply them together?_

Just like all of the previous years, this first puzzle was extremely basic.
There was no reason to get really clever or tricky on the first pass,
so I just brute forced the solution:
iterate through each pair of numbers and check their sum.

The biggest hiccup today was the site was clearly not ready for the on-rush of fast
submissions this year. I finished part 1 in about 30 seconds, but received 504 and 503
errors every time I submitted for about 6 minutes.

After about 6 minutes, my answer finally submitted and I moved to part 2.

### Part 2
> _...what is the product of the three entries that sum to 2020?_

Part 2 was just another straightforward extension on part one.
Once again, I decided to just brute force it with 3 loops.
I got the answer in about a minute and successfully finished Day 1!

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 197451     | 1  | <1  | 00:00:42  | 43   |
| **Part Two**  | 138233720  | 1  | 94  | 00:01:14  | 340  |

# Original puzzle
### --- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little
picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them,
but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:
```
1721
979
366
299
675
1456
```
In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces
`1721 * 299 = 514579`, so the correct answer is `514579`.

Of course, your expense report is much larger. Find the two entries that sum to `2020`; what do you get if you
multiply them together?

### --- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left
over from a past vacation. They offer you a second one if you can find three numbers in your expense report
that meet the same criteria.

Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`.
Multiplying them together produces the answer, `241861950`.

In your expense report, what is the product of the three entries that sum to `2020`?
