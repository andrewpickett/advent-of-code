# Approach
### Part 1
> _What is the highest seat ID on a boarding pass?_

Today's puzzle was quick. They gave away the secret to it when the mentioned it was "binary" seating.

Once you think in binary terms, you quickly realize that in the first portion of the ticket,
'F' equates to '0' and 'B' equates to '1' in a binary string. Simply replace the values and convert
the resulting binary string to a number you are have the row. Do the same thing with the last portion
of the ticket ('L'=='0' and 'R'=='1') to get the column.

Then simply do the maths on your row/column and you have your answer.


### Part 2
> _What is the ID of your seat?_

Since for this one you need to look at all of the other seats in order to determine your own, I immediately
just thought of initializing an array large enough to fit every possible seat id (128*8)...then go through
and set the value to 1 at the index of every seat. You then just loop through the whole list and find
the first empty seat with both neighboring seats populated.

Nothing fancy, nothing over-complicated.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 911  | 1  | 1  | 00:14:17  | 2282  |
| **Part Two**  | 629  | 1  | 1  | 00:03:30  | 1826  |
