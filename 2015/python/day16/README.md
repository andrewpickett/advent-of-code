# Approach
### Data format

This one was kind of fun to parse. I knew I wanted to end up with an array of objects repesenting each "sue" in the input file.
Something that looks like this:
```
[
	{"goldfish": 9, "cars": 0, "samoyeds": 9},
	{"perfumes": 5, "trees": 8, "goldfish": 8},
	...
]
```

So looking at the input file, each line has this format:
```
Sue {line_num}: {key}: {value}, {key}: {value}, ..., {key}: {value}
```

So I spent some time coming up with a crazy list comprehension to parse out the values into objects. Basically I can simply
ignore the first 2 tokens after splitting on spaces (since I don't care about the `Sue {number}` part). Everything after
that is just a key followed by value... so I build the map from that using slices and maths to get the correct
indexes, etc...in the end, it's a pretty nifty little one liner to conver the input into the format I wanted!

### Part 1
> _What is the number of the Sue that got you the gift?_

I hardcoded the ticker values so that I can reference them. Just iterate over the array of Sues and check that the values that are present for a given sue match those values in the
ticker. I did a logical "AND" on the keys lists for the ticker and each sue to only have to compare the keys that are
needed. If all of the values for those given keys match, then we found our Sue.

### Part 2
> _What is the number of the real Aunt Sue?_

This is pretty much the same as part one, but since there is an extra check of "<" and ">" for specific keys, I expanded
the list comprehension I wrote in part one to be more explicit and allow me to interject the comparisons for specific keys.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |               0 |
