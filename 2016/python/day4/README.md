# Approach
### Part 1
> _What is the sum of the sector IDs of the real rooms?_

A lot of parsing and string manipulation. That's what this one ended up being. So I parsed the input data into the individual parts
so that I could then manipulate them individually. Once I had the name portion extracted out, it was a matter of creating a
map counting the occurences of all characters in the string, sorting that map by count, building a string based off of that,
and taking just the first 5 characters of it. This gives me the ACTUAL checksum of each room. Since I already extracted out
each piece of the input, I can just compare it with what was there to see if they match. Once they do, just add up the sector
ID.

It was pretty straightforward, but took a lot of tinkering to get all of the map building/parsing working right.

### Part 2
> _What is the sector ID of the room where North Pole objects are stored?_

This one was worded very strangely and I'm still not completely sure I did it how they expected me to. The first step was
to decrypt, which was pretty simple -- just shift the letters using an alphabet string and modulo operators...but then I just
had a list of all of the decrypted names and wasn't sure exactly what to be looking for. I tried "north pole" and nothing came
up, so then I tried looking for "stor". That gave me a list of about half a dozen room names -- one of which was "north pole object storage".

Clearly this was the one they wanted, so I just put that string as my name search, ran the program again, and returned the
sector id for it.

Felt hacky, but I couldn't think of what else they wanted.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** | 245102 |        1 |              22 |                   N/A |  N/A |
| **Part Two** |    324 |        1 |              13 |                   N/A |  N/A |


# Original puzzle
### --- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

* `aaaaa-bbb-z-y-x-123[abxyz]` is a real room because the most common letters are `a` (5), `b` (3), and then a tie between `x`, `y`, and `z`, which are listed alphabetically.
* `a-b-c-d-e-f-g-h-987[abcde]` is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
* `not-a-real-room-404[oarel]` is a real room.
* `totally-real-room-200[decoy]` is not.

Of the real rooms from the list above, the sum of their sector IDs is `1514`.

### --- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. `A` becomes `B`, `B` becomes `C`, `Z` becomes `A`, and so on. Dashes become spaces.

For example, the real name for `qzmt-zixmtkozy-ivhz-343` is `very encrypted name`.
