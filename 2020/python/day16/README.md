# Approach

Ugly. There is nothing pretty about anything I did here. The first, and probably ugliest, part was just parsing the
input. Unlike most puzzle inputs, this one is not well-formed. There are really 3 distinct sections that need
to be handled seperately:
* Validators - the fields and their allowed values
* My Ticket
* Everyone Else's Tickets

I just read in the full data file once at the beginning into a list as I typically do in these puzzles, and then
I have different methods to extract each of those sections into their appropriate data structures.

### Part 1
> _What is your ticket scanning error rate?_

Alright, well, the core part of this problem was just figuring out a data model that works. In reading through
the whole thing, for this first part, you really only need to keep track of values that don't match any validators.

So, the main approach here is (after parsing out the input), just loop over each of the "others tickets" values
and run them against every validator. If it is valid by any ONE, then you can stop and move to the next value to test.
If it fails all of the validators, then add it to a list. Then just return the sum of that list.

The main question here is "how do you write the validation logic for these based on the input"?

I decided to simply create an array of `0`s that is `n` length, where `n` is the highest number in the ranges given. Then
parse out the ranges, and put a `1` in that index. So after parsing the input, I have a dictionary of all allowed
values for each of the labels. Something like this:
```
{
  "class": [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
  "row":   [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  "seat"   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
}
```
To make things easier for myself, I then do a logical "OR" across them all to create one consolidated array of
all possible values. So the above would turn into this:
```
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
```
Now, when I want to look up a value from someone's ticket. I just check the index in my array to see if it's `1`.

If it is a `0`, then it is not valid in any of the validators/ranges...so we'll add all of these together to get the
answer.

### Part 2
> _What do you get if you multiply those six values together?_

So for this second part, we now needed to keep track of fields across tickets based on common indices. The way
I approached this one is I create an array that's the size of a ticket. Each element in this array is a list of
possible values for that ticket index. It gets initialized to all possible values (taken from my data validator
map keys above). So it initially looks something like this:
```
[
  ['class', 'row', 'seat'],
  ['class', 'row', 'seat'],
  ['class', 'row', 'seat']
]
```
Now, I loop over every ticket, and run every validator against each entry. If I get a validation error, then I know
that field is not valid for that index. So I then remove that field from my list of possible fields at that index.
So if I have ANY ticket that the 2nd number fails the "seat" validation, I remove "seat" from index 1 in the list above,
and so it looks like this:
```
[
  ['class', 'row', 'seat'],
  ['class', 'row'],
  ['class', 'row', 'seat']
]
```
Now, I keep doing this until I've run through every ticket value. It leaves me with a list of "POSSIBLE" values
for each index...and hopefully some of them only have one possibility. I now just find all of the places where
there is only one, and remove that value from all other possibilities, and keep doing that until all entries
only have 1 possible value. So if I have this at the end of validating all ticket values:
```
[
  ['class', 'row'],
  ['row'],
  ['class', 'row', 'seat']
]
```
I can see that `row` MUST be index 1...so I can remove it from the others. That leaves `class` being index 0, and so
I remove it from all of the others. Finally, `seat` is index 2, and now all of them only have one possible value.

From here, it's just a matter of finding the indices of any that start with "departure" and grab that index from
my own ticket to multiply together.

Whew. It's so ugly...so many for-loops...so many steps...but it works, and it works pretty fast.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 24110  | 1  | 4  | 00:25:16  | 2843  |
| **Part Two**  | 6766503490793  | 1  | 24  | ~02:00:00  | 11866  |

# Original Puzzle

### --- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming
up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You
should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you
figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for
the same train service (via the airport security cameras) together into a single document you can reference
(your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of
values for each field. For example, a rule like `class: 1-3 or 5-7` means that one of the fields in every ticket
is named class and can be any value in the ranges `1-3` or `5-7` (inclusive, such that 3 and 5 are both valid in
this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket
in the order they appear; every ticket has the same format. For example, consider this ticket:
```
.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
```
Here, `?` represents text in a language you don't understand. This ticket might be represented as
`101,102,103,104,301,302,303,401,402,403`; of course, the actual train tickets you're looking at are much more
complicated. In any case, you've extracted just the numbers in such a way that the first number is always the
same specific field, the second number is always a different specific field, and so on - you just don't know what
each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't
valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:
```
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
```
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by
considering only whether tickets contain values that are not valid for any field. In this example, the values on
the first nearby ticket are all valid for at least one field. This is not true of the other three nearby
tickets: the values `4`, `55`, and `12` are are not valid for any field. Adding together all of the invalid
values produces your ticket scanning error rate: `4 + 55 + 12 = 71`.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

### --- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining
valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is
consistent between all tickets: if seat is the third field, it is the third field on every ticket, including
your ticket.

For example, suppose you have the following notes:
```
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
```
Based on the nearby tickets in the above example, the first position must be row, the second position must be
class, and the third position must be seat; you can conclude that in your ticket, `class` is `12`, `row` is `11`,
and `seat` is `13`.

Once you work out which field is which, look for the six fields on your ticket that start with the word
departure. What do you get if you multiply those six values together?
