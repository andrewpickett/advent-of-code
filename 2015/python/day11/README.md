# Approach
### Part 1
> _Given Santa's current password (your puzzle input), what should his next password be?_

This one is very similar to day 5. I took the naive approach and just actually incremented the alphabetic characters one
at a time. I then ran the new password through the rules checks to see if it's valid.
Obviously this brute force approach by itself won't be enough, so the biggest/easiest time save is the second rule:

_Passwords may not contain the letters `i`, `o`, or `l`, as these letters can be mistaken for other characters and are therefore confusing._

It's very easy to check if a string has any of those characters. If it does, we can skip all passwords until the next letter.
As an example, if we have the password `ghdizxbbcd`, we can see it has a forbidden letter (`i`). So we we can do is simply increment that letter
(to `j`) and make all following letters back to `a` for a resulting next password of `ghdjaaaaaa`. That can save massive amounts
of checks along the program.

There are obvious other shortcuts we can make with the other rules, but after making just that one change it is enough
for it to finish in just a couple seconds. So I left it there.

### Part 2
> _What's the next one?_

Just take the result from the first part and run it through the code again...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            2242 |
| **Part Two** |            5816 |

# Original puzzle
### --- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by **incrementing** his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: `xx`, `xy`, `xz`, `ya`, `yb`, and so on. Increase the rightmost letter one step; if it was `z`, it wraps around to `a`, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

* Passwords must include one increasing straight of at least three letters, like `abc`, `bcd`, `cde`, and so on, up to `xyz`. They cannot skip letters; `abd` doesn't count.
* Passwords may not contain the letters `i`, `o`, or `l`, as these letters can be mistaken for other characters and are therefore confusing.
* Passwords must contain at least two different, non-overlapping pairs of letters, like `aa`, `bb`, or `zz`.

For example:

* `hijklmmn` meets the first requirement (because it contains the straight `hij`) but fails the second requirement (because it contains `i` and `l`).
* `abbceffg` meets the third requirement (because it repeats `bb` and `ff`) but fails the first requirement.
* `abbcegjk` fails the third requirement, because it only has one double letter (`bb`).
* The next password after `abcdefgh` is `abcdffaa`.
* The next password after `ghijklmn` is `ghjaabcc`, because you eventually skip all the passwords that start with `ghi...`, since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

### --- Part Two ---
Santa's password expired again. What's the next one?
