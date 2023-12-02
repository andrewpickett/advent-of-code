# Approach
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
| **Part One** |             460 |
| **Part Two** |           15907 |

# Original puzzle
### --- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least **five zeroes**. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

For example:
* If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043` starts with five zeroes (`000001dbbfa...`), and it is the lowest such number to do so.
* If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef...`.

### --- Part Two ---
Now find one that starts with **six zeroes**.
