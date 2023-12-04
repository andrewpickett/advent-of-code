# Approach
### Part 1
> _How many strings are nice?_

It's really very straightforward to solve this one, because all you have to do is for each string in the input, run it
through a few regular expressions or basic rule checks to ensure it passes all of them. None of the rules are very difficult,
as they can be represented like this in pseudocode:

For a given string s:
* if s.count("[aeiou]") >= 3
* if s[x] == s[x+1] for some index x in the string
* if any of ['ab', 'cd', 'pq', 'xy'] are anywhere in the string

As long as all three of those are true, then it's a valid string. I originally had those all as separate checks and multiple
lines of code, but I was able to represent all of them as one long list comprehension, which was pretty slick!

### Part 2
> _How many strings are nice under these new rules?_

This part is similar to the previous, but we just had to change what the rules meant. So instead of s[x] == s[x+1] for
repeated letters, we have s[x] == s[x+2] for repeated letters one place away. We can represent the other one by iterating
over every letter in the string and getting a count of each pair of letters s[x:x+2]...and if it's more than one, then
it passes as well. Again, it took a little playing around, but I got it all into one comprehension!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              10 |
| **Part Two** |              11 |

# Original puzzle
### --- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A **nice string** is one with all of the following properties:
* It contains at least three vowels (`aeiou` only), like `aei`, `xazegov`, or `aeiouaeiouaeiou`.
* It contains at least one letter that appears twice in a row, like `xx`, `abcdde` (`dd`), or `aabbccdd` (`aa`, `bb`, `cc`, or `dd`).
* It does **not** contain the strings `ab`, `cd`, `pq`, or `xy`, even if they are part of one of the other requirements.

For example:
* `ugknbfddgicrmopn` is nice because it has at least three vowels (`u...i...o...`), a double letter (`...dd...`), and none of the disallowed substrings.
* `aaa` is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
* `jchzalrnumimnmhp` is naughty because it has no double letter.
* `haegwjzuvuyypxyu` is naughty because it contains the string `xy`.
* `dvszwmarrgswjxmb` is naughty because it contains only one vowel.

How many strings are nice?

### --- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:
* It contains a pair of any two letters that appears at least twice in the string without overlapping, like `xyxy` (`xy`) or `aabcdefgaa` (`aa`), but not like `aaa` (`aa`, but it overlaps).
* It contains at least one letter which repeats with exactly one letter between them, like `xyx`, `abcdefeghi` (`efe`), or even `aaa`.

For example:
* `qjhvhtzxzqqjkmpb` is nice because is has a pair that appears twice (`qj`) and a letter that repeats with exactly one letter between them (`zxz`).
* `xxyxx` is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
* `uurcxstgmygtbstg` is naughty because it has a pair (`tg`) but no repeat with a single letter between them.
* `ieodomkazucvgmuy` is naughty because it has a repeating letter with one between (`odo`), but no pair that appears twice.

How many strings are nice under these new rules?
