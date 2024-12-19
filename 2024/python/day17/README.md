# Approach
### Data format

Just store a place for 3 registers (`a`, `b`, and `c`) and the program instructions.

### Part 1
> _Once it halts, what do you get if you use commas to join the values it output into a single string?_

"opcode"...

Oh man...PTSD flashbacks to 2019...

Luckily, this one wasn't that...This part is pretty straightforward -- just implement the instructions exactly as described
and run the program. Not even really any "gotchas" on this part.

### Part 2
> _What is the lowest positive initial value for register A that causes the program to output a copy of itself?_

Well that took a turn...and not where I was expecting. It's actually funny, when I got into programming, my dad told me
one of the exercises he always did to learn a new language was to have a program write an exact copy of itself and that
it would teach me everything I need to know about that language...

Anyways, I knew a reverse-engineering problem would be coming at some point. So here we are. At least this program is
only 8 instructions! So I started off by just writing down exactly what the program did in python and this is
what it came down to:
```python
outputs = []
while a != 0:
	b = a % 8
	b = b ^ 1
	c = a // 2**b
	b = b ^ c
	b = b ^ 4
	a = a // 2**3
	outputs.append(b % 8)
return outputs
```

So I actually wrote that code, and re-ran part 1 on it, and sure enough, it works. Alright, so...what now? The first thing
I did was just start a loop of increasing `a` values and output the outputs to see if I noticed a pattern. I immediately saw that
the length of the output array grew exponentially slower. It started with a length of 1 for 7 iterations, length of 2 for 56 iterations,
length of 3 for 448 iterations, etc. So...to the OEIS! Amazingly, I found a sequence that fit perfectly (A055274) and I was able to determine
that the values for my counter would have to be between `30786325577728` and `246290604621824`...so I've narrowed down
my possible values of `a` to one of 240 trillion or so...

...ok...what else?

So looking back at my outputs, I noticed the FINAL digit had a pattern to it, and that repeated at exponentially increasing amounts
as well...this time the OEIS showed me that it was basically powers of 8. This made sense after looking back at my python
implementation, since the last step is to divide by 8 every time! Ok...so now I narrowed down my values to between `175921860444160` and `246290604621824`.

...still about 170 trillion...

Then I decided to output values when the last TWO values of my outputs matched the last TWO of my instructions...and that's when it
hit me. I can work from the back of the instruction array, find the first time the last digit matches the last digit AND I'm the
correct length by increasing by `8**(len(instructions)-1)` -- that by definition will give me the first location that is the
correct length output that ends in the correct value.

Now to find the first location that is the correct length output and ends in the last TWO correct values, I just need to
start adding `8**(len(instructions)-2)`...

Then for the last THREE correct values, it would be increasing by `8**(len(instructions)-3)`...

You start to see the pattern here!?!?! In the end, just start incrementing the counter by decreasing powers of 8 until it
is narrowed in and you're just increasing by 1 (`8**0`). At that point, you will absolutely find the first value that satisfies
the requirement!

So again, this only works on the input (and any input that is doing the same basic operations)...so it doesn't work on the
samples, since those are just to test the program. Considering sometimes the reverse-engineering problems are the most
frustrating, I was pretty happy with those this one went. In the end, to find the value of `a` that works only took running
the program 79 times in my situation with this approach.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |               4 |
