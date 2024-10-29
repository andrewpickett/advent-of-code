# Approach
### Data format

Just read the number from the file -- I kept it as a string for later parsing ability...but doesn't need to.

### Part 1
> _What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?_

Pretty straightforward. I just implemented the algorithm exactly as they described.

### Part 2
> _How many recipes appear on the scoreboard to the left of the score sequence in your puzzle input?_

I am assuming there is a much better approach than just brute forcing for 100,000,000 iterations and checking if
the original input is present in the list...right? Well, I don't know, because I just did that and it came back in about
2 minutes. Not good, definitely not good...but it was very easy and I'm done and moving on.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             831 |
| **Part Two** |          104740 |
