# Approach
### Data format

I read in the packages into a list (since they're in order, I didn't need to maintain the indexes listed).
I then read the regions into a list. I also took the packages and calculated their "density" based on how many `#`
there are in each package.

After actually solving part 1, I realized I never even used the packages themselves ,so I removed them from my data.

### Part 1
> __

Alright...well...I don't know how I should feel about this one. I honestly just started writing something I could
use to get a sanity check. Basically I wrote something that just checks which ones could POTENTIALLY fit based on the
width of each of the packages. I had a couple different use cases where I could immediately rule some out based on
the sizes given, immediately say that some should work, and then get some that I just don't know yet and that I would have
to figure out these as edge cases.

So I ran it on the example given, and it came back as all being "unknown"...

...Well that isn't very helpful, now is it. Just to sanity check myself, I decided I would run it against the input and
see what I got.

When I did that, I had 0 `UNKNOWN` values, and the rest were either `NOT POSSIBLE` or `ABSOLUTELY`...I obviously thought
my rough checker was seriously flawed, since the example input and the actual input were given 100% opposite results, but
I decided to try putting my `ABSOLUTELY` value in to see if it was correct (since according to my tester, everything was
either absolutely in or absolutely not).

It was somehow correct...

I mean...WHAT?!?!?

I cleaned up the unused code (all my other categories, since I only cared about
`ABSOLUTELY`), and just returned it as a counter. So, now I need to go back and figure out a more "general" solution
that also works with the example (or any input for that matter)...
But that will have to wait for another day.

"I'm tired, boss. Dog tired."

### Part 2
> __

Thank you, Eric! He kept the tradition that if you've done every puzzle up to this point, you get this star for free...
you just have to click the link. Did that and got the star. Wow...what a year!

# Results

|              |     Exec. Time (ms) - Python 3.13 | Exec. Time (ms) - PyPy 3.11 |
|--------------|----------------------------------:|----------------------------:|
| **Get Data** |                             0.383 |                       0.416 |
| **Part One** |                             4.339 |                       1.362 |
| **Part Two** |                             0.001 |                       0.002 |
| **TOTAL**    |                           *4.723* |                     *1.780* |
