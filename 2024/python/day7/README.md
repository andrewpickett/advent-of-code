# Approach
### Data format

Really just need to read the input file as a map of the total to the list of operands.

I later added a few other pieces so that I can help the performance of part 2 (namely, we don't need to re-process
the ones that we found were valid in the first part).

### Part 1
> _What is their total calibration result?_

Well, I started 40 minutes late because I had a game night with friends and didn't get home until 12:30. So, my overall
score/ranking isn't great on this one, but I was able to solve it pretty quickly.

I decided to try brute forcing this by just looping over each item in the list and checking every combination of `+` and `*`
for each operand to see if it matches the target value. The way I decided to do this was to create an encoding string of
`1`s and `0`s representing the order of operators to try. So the first thing I needed to do was create a binary string
to represent each of the operators. I did that by doing a loop from `0` to `2^n` where `n` is one less than the length of the list of
operands. I then convert that integer to a binary string representation.

Now that I have the operator code, I just try each one until I find one that matches -- or doesn't. If it does match,
I save it off so that I don't have to re-process it in the next part and add that value to our running sum.

I'm sure there are more efficient ways to do this, but I was really tired at this point and I'm fine with it.

### Part 2
> _What is their total calibration result?_

Alright, I mean...let's just update my loop to go from `0` to `3^n`! So I just create a ternary-based string of the values
now to represent the new operator and run it the same way.

I did run into a complete misunderstanding of the requirements in that I for some reason assumed `||` would take priority
over the other operators, and that all concatenations should be done first before the rest. I don't know why I thought this,
since he explicitly says to just do things in order...but I ended up wasting probably 15 minutes writing up a pre-processor
to do the concatenations first and then debug why it wasn't getting the correct answer.

Once I realized it really was the exact same solution as part 1, but with just one more possible operator, I just let it fly.

It started taking forever...I was getting worried and started looking into better ways to do this...and then it finished.
It took about 90 seconds...which I'm not happy with, but it's done. I needed sleep.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            1306 |
| **Part Two** |           92433 |
