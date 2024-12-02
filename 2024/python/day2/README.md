# Approach
### Data format

Exactly the same as part one...read each line in as a list of integers so we have a list of lists of integers to parse through.


### Part 1
> _How many reports are safe?_

This one was pretty easy -- except for the DDoS issues the site was having. I was getting 500 and timeout errors for the
first 3 minutes...

Once I got my input, it was really just run through each list in my input and check 3 things:
1. Is the list ascending?
2. Is the list decending?
3. Is the difference between each element 1, 2, or 3

Now, I got a LITTLE hung up and made a mistake early on by misreading the requirements and I thought it was `1 <= x < 3`...
so that took a couple minutes to debug.

I decided to check the ascending/decending lists by just sorting the list and comparing to the original...then reversing
and comparing to the original. If either are true, then it's valid for those 2 checks. The next part was just doing
a for loop through the list and checking the difference.

I then got timeouts when trying to submit my answer as well...so that added another couple minutes. Not a great time due to
those things, but overall, it was fine.

### Part 2
> _How many reports are now safe?_

Yeah...definitely knew there were a few edge cases here to account for...but luckily with how I was checking the
criteria in part 1, it made this pretty simple. All I had to do was check unsafe records and remove each element
from the list one at a time and recheck. If it is EVER found safe by removing any single element, then the whole thing
is safe. So it really didn't change my algorithm much.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |               8 |
