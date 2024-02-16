# Approach
### Data format

I read the input in as a `Grid` to allow me to traverse through it easily. The biggest hiccup I had was that IntelliJ
was stripping trailing whitespace off my input file lines, which made it hard to initialize the grid completely.
Basically I decided to just find how long the longest line was and left justify every line to that length first and then
initialize the `Grid`.

### Part 1
> _What letters will it see (in the order it would see them) if it follows the path?_

Alright, so the first step is find the start...which happens to be the only non ` ` character in the first row. Simple.
Now, I just continually find the neighbors that aren't ` ` characters and use some deductive rules to determine
which neighbor I should travel to. I keep track of the last direction I was going to do this. If I ever run into a `+`
character, I know my direction MUST change. If I run into any letters, I add those to my running list of letters that I've seen
and keep going in the same direction. The hardest part is when I'm on a space that has multiple neighbors, including letters, and
multiple directions. I pretty much just say "keep going the direction you're going!" unless I have a `+`.

Once I have no more possible places to go in my path, I'm done. I decided to keep track of the full path I took as well,
since I was already going to be doing it as part of my check for valid positions to move to.

### Part 2
> _How many steps does the packet need to go?_

Well, since I already was keeping track of the full path, I literally just had to count the number of elements. Simple!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |              35 |
| **Part Two** |              33 |
