# Approach
### Data format

Read each line in as a tuple of (direction, amount). I then stored that in a dict along with the dial starting point.

#### Time Complexity

We have to read every line in the file, there's no real way around that. So this portion is going to be $\Theta(n)$.

### Part 1
> _What's the actual password to open the door?_

Nice and easy, as I would expect for Day 1, part 1. Just keep a pointer to the current position on the lock dial (starting at `50`)
and run through the list of instructions. After every turn, just modulo 100 and then check if the pointer is sitting on
`0`. Every time it is, increment a counter and return the final count at the end.

UPDATE: I updated the code to be a bit cleaner by storing a dict of the current position and counter and just updating the values
directly in there. This helped clean up the code by removing multi-return functions and just kept it so that both parts
can just use the same function to run through the steps.

#### Time Complexity

Because of the nature of the input and problem statement, we have to go over every row from the input in order to
determine the points at which it will stop at `0`. Therefore, this portion is $\Theta(n)$.

### Part 2
> _Using password method 0x434C49434B, what is the password to open the door?_

Yeah...this shows just how tired I am and how much I need to warm up. I ended up getting the wrong answer 4 times, which meant
I had to wait 5 minutes before submitting my final answer. All of these were silly mistakes because I was trying to be
"clever" and concise with my code, so I would just miss random cases. I also didn't bother reading the puzzle or the
input carefully, so I didn't notice that there were large jumps at first (like turning `1000` in a single step). So...
between all of that, it took much longer than it should have...but overall it wasn't difficult.

Basically, we do the same thing as in part one, but before actually changing the pointer, we check if we ever crossed the `0` line.
If we did, and we didn't START on `0` (since it would have already been counted from the last turn), we increment the
counter by `1`. Once we actually do the turn, we check HOW MUCH we turned it. If the turn was
more than a full turn of the dial (`100`), we check how many full turns it was and add that to the counter as well.

#### Time Complexity

Once again, we have to loop over the full input in order to figure out whenever it crosses the `0` line. This portion is
also $\Theta(n)$.

# Results

|              | Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|----------------------------:|
| **Get Data** |                         2.151 |                       1.475 |
| **Part One** |                         2.454 |                       0.605 |
| **Part Two** |                         4.096 |                       0.819 |
| **TOTAL**    |                     **8.701** |                   **2.899** |

** *Ran each part 20,000 times and averaged the run times to get final execution time*

#### Time Complexity

All parts of the puzzle need to read through every line of the input, so they should all run at approximately the same
speed. The total runtime for this day would be $\Theta(3n)$

#### Possible Improvements

Instead of reading the input data 3 separate times, I could just as easily have run through it once and stored
each of the results as it processed. This would have resulted in the entire puzzle running in $\Theta(n)$.

In testing this approach, the entire program ran in an average of **1.634 ms** compared to the above **2.899 ms** (over the course of
20,000 executions), which certainly shows an improvement in the ballpark of what we would expect to see.
