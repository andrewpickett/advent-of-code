# Approach
### Data format

Just read each line into a single array.

### Part 1
> _Given the recording in your puzzle input, what is the error-corrected version of the message being sent?_

I decided to just build a map of character occurrences in each column and then take the max value from that map.
It was pretty simple and once I got passed accidentally using a pointer to the dictionaries in my array, it worked just fine.

### Part 2
> _Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?_

Literally just changed the `max` function to `min` and ran it. Worked right away.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              <1 |
| **Part Two** |              <1 |
