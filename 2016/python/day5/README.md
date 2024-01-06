# Approach
### Data format

Just read the whole contents of the input to a string.

### Part 1
> _Given the actual Door ID, what is the password?_

This one is pretty much a **_RE-HASH_** of 2015 Day 4. Really nothing hard here...just follow exactly
what the puzzle asks.

I got the answer wrong at first, because I forgot to strip the input, so it had a new line on it that got included with the hashing.
Once I removed that it worked just fine.

### Part 2
> _Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation_

Again, very simple, but just brute forced. This one took a bit longer to run, but it worked without really changing anything with my code.
I could probably clean it up a bit, but I'm fine with it.

It's unfortunate this one just takes forever to run, and I don't think there's really any way to optimize it...

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |           12129 |
| **Part Two** |           41195 |
