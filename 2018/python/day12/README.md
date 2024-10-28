# Approach
### Data format

Just read the data into a map with the first line as the "initial" input and then each following line into a map of
rules.

### Part 1
> _After 20 generations, what is the sum of the numbers of all pots which contain a plant?_

I started writing this one actually morphon the string itself every generation (just like the example). I iterated over the
string, and if the string from `[i-1:i+3]` was in my rules map, I replaced the character with the value in the map. Otherwise,
I just left it alone. I had to pad the string on both sides in order to handle the edge cases. It worked well for the
sample input, but for some reason I was off by a little bit on my actual input. I tried multiple times and it just
wasn't working.

Eventually I realized I don't actually need to manipulate the string itself, but instead just needed to know the
indices of where the `#`s are. So instead I started just keeping a dictionary of the indices where the `#`s are.

In order to accomplish this, I have to re-build the 5 character string to check the pattern match, but that is really
pretty quick because the string doesn't get very long.

This also has the added benefit of simply returning the sum of the keys in the dictionary, as that will give the sum of
the indices!

### Part 2
> _After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?_

Obviously running this 50 billion times isn't actually feasible. Obviously there must be some trick or way of
shortcutting it. For something like this, I assumed there would be a pattern that would be repeated. So what I did
was just wrote some code to check the difference of the one generation to the next to see if I could find any place
where there was some loop or pattern of how many pots get added/subtracted each time. I was very pleasantly surprised
to find that after 100 generations, it just ALWAYS added `51` pots. Talk about a short loop!

So, that means the total at the end of 50 billion would just be
`(50000000000 - 100) * 51 + {number of pots present at generation 99}`
So I just keep track of the first 100, keep the 99th, run the above simple calculation, and voilà. There's my number!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               2 |
| **Part Two** |              15 |
