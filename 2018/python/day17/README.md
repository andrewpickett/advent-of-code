# Approach
### Data format

I started by creating a map with all of the information that would be needed, which included: the minimum `y` value
in the input, the starting point, and then the `Grid` that I create from the input. So I used my `Grid` again, and
then iterated over the input to actually set the values to be accurate.

Once I had that, I solved part 1, but then realized part 2 would just use the exact same output from part 1...so
I instead did the "solve" in the process of getting the data and stored the actual FINAL output to the data object
that I can just pass to my part 1 and part 2 code -- making them really trivial. So I'll describe the actual solve
in the `Part 1` section below...but in the end, I actually do the work in the setup, so I can use it across both
parts.

### Part 1
> _How many tiles can the water reach within the range of y values in your scan?_

So this was fun for a while...and it wasn't too difficult at first. Using my `Grid` class, I was able to instantiate the
input exactly as described. I then started work on the algorithm to actually have the water flow. I basically broke it down
to this:
1. From the start point, fall until I hit a "solid" (`#`).
2. From there, check if the row I'm on will overflow either left or right
   1. If it will NOT overflow, simply fill that row from the left `#` to the right `#` with `~` and then move up a row and repeat this step.
   2. If it will overflow, fill that row with `|` from the place it overflows to the opposite wall. Return the position of the overflow
3. Now, repeat the last 2 steps using the last overflow position and it SHOULD just flow down and down and down...

Right?

Well, the first use case that broke this logic was if it overflows on BOTH sides. Well now I had to make sure I ran the
algorithm for ALL places where water is falling. So, that means maintaining a stack of overflow points. Now I just need to
keep iterating through the algorithm until there are no more points that are "falling".

The "end" cases were hitting the bottom of the grid or hitting an already full "bucket". Alright! now it should work!!

...right??

Nope...the big use case that I was missing was if there was a "box" inside of a "bucket". So this use case:
```
.....|....
.#...|..#.
.#..###.#.
.#..#.#.#.
.#..###.#.
.#......#.
.#......#.
.########.
```
When this happened, my overflow logic just got completely destroyed. So I revamped it all, and changed how I detect when it
overflows and just made sure that it would work for this case as well.

Once that use case worked, it all flowed down so nicely. Store the resulting grid (with all of the flows) into my data.

Now just count the number of `~` and `|` and we should be good!

...right??????

Nope...I misread that you shouldn't include any water that's "above" the highest point in your input. So I had to add
one final piece to count how much water was above the highest defined point and subtract that from my final answer.

FINALLY!!

### Part 2
> _How many water tiles are left after the water spring stops producing water and all remaining water not at rest has drained?_

Since I already have the full data built out, it's just counting the number of `~` characters...don't need to worry about
the `|` because they will all just "go away" when the water stops...and don't have to worry about anything "above" the highest
point, since no water would be there anyways...Very simple.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |             118 |
| **Part Two** |             120 |
