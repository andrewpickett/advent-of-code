# Approach
### Data format

I decided to just read the input as one giant string, since I'll just traverse over each character and use the `.count()`
function

#### Time Complexity

Reading the contents of a single line file is $\Theta(n)$ where $n$ is the length of the file.

### Part 1
> _To what floor do the instructions take Santa?_

Since `(` is `+1` floor and `)` is `-1` floor, just subtract the number of `)` from the number of `(` in the input
and it will give you the resulting floor.

#### Time Complexity

I am just running a `.count()` on the input string twice. As a result, the time complexity is $\Theta(2n)$ where $n$ is
the length of the string.

### Part 2
> _What is the position of the character that causes Santa to first enter the basement?_

Just iterate through the input and add/subtract based on each character. Once you have a value of `-1`, return the
index you're on plus one (because of 0-based indexing).

#### Time Complexity

This part needs to traverse over all of the input in its worst case, so it would be $O(n)$. In theory, this part should be faster
than part 1, since it doesn't necessarily need to iterate over the entire list. However, there is more logic checking in it,
so it does run a little bit slower.

# Results

|              | Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|------------------------------:|----------------------------:|
| **Get Data** |                         0.052 |                       0.050 |
| **Part One** |                         0.068 |                       0.013 |
| **Part Two** |                         0.350 |                       0.034 |
| **TOTAL**    |                     **0.470** |                   **0.097** |

** *Ran each part 20,000 times and averaged the run times to get final execution time*

#### Time Complexity

The entire time complexity for all parts together is $O(4n)$ where $n$ is the length of the input.

#### Possible Improvements

Theoretically, I could just iterate over the list once, and keep track of both parts of the puzzle. This would allow me to
only have to traverse over it twice (once to read the data from the file, once to keep track of the floor). For more
complicated inputs (with multiple characters to keep track of), using the `collections.Counter` utility would likely
give a faster performance as well. However, for only 2 characters, the approach I have done seems to be faster.
