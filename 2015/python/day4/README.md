# Approach
### Data format

I decided to just read the input as one giant string, since I'll just traverse over each character.

### Part 1
> _...find MD5 hashes which, in hexadecimal, start with at least five zeroes._

I didn't really want to spend much time trying to optimize this one...at least not at first, so
I just went with a brute-force method to see if it would work. Basically just start at 1, and loop
through generating hashes with increasing values and check if the resulting hash starts with
5 zeroes. It took less than a second, so I figured it's good enough.

### Part 2
> _Now find one that starts with six zeroes._

I literally just changed the check from a `5` to a `6` on number of zeroes, and ran it. it took about
20 seconds, which is WAY too long normally, but honestly...I don't care. It gives the right answer
and I'm moving on.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             403 |
| **Part Two** |           13833 |
