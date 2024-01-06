# Approach
### Data format

I parse each line into an array of words, sector, and checksum and store each of those in a list. This way
I know that the second to last element in the array is going to be my sector, the last element is the checksum,
and everything beforehand are the individual words. This makes the parsing much easier later on.

### Part 1
> _What is the sum of the sector IDs of the real rooms?_

Once I had the name portion extracted out, it was a matter of creating a
map counting the occurences of all characters in the string, sorting that map by count, building a string based off of that,
and taking just the first 5 characters of it. This gives me the ACTUAL checksum of each room. Since I already extracted out
each piece of the input, I can just compare it with what was there to see if they match. Once they do, just add up the sector
ID.

It was pretty straightforward, but took a lot of tinkering to get all of the map building/parsing working right.

### Part 2
> _What is the sector ID of the room where North Pole objects are stored?_

This one was worded very strangely and I'm still not completely sure I did it how they expected me to. The first step was
to decrypt, which was pretty simple -- just shift the letters using an alphabet string and modulo operators...but then I just
had a list of all of the decrypted names and wasn't sure exactly what to be looking for. I tried looking for a number of
different words, and found that one of them had the string "northpole" (in fact, it said "northpole object storage"...so it
was pretty obvious once you saw it).

Clearly this was the one they wanted, so I just put that string as my name search, ran the program again, and returned the
sector id for it.

Felt hacky, but I couldn't think of what else they wanted. I'm not sure how to make this completely programmatic without
manually analyzing the data or knowing that "northpole" is what you need...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              19 |
| **Part Two** |               2 |
