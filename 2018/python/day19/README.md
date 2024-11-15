# Approach
### Data format

Read the instruction pointer value and then the actual instructions into a map along with a placeholder for the
registers. In the end, we have a map that looks like this:
```
{
	"r": [0, 0, 0, 0, 0, 0],
	"program": [
		["seti", 0, 0, 0],
		["gtri", 1, 2, 3],
		...
	],
	"ip": 0
}
```

### Part 1
> _What value is left in register 0 when the background process halts?_

Just run the code in the input file. It took longer than I was hoping, but finished just fine.

### Part 2
> _What value is left in register 0 when this new background process halts?_

Obviously this isn't going to work by just setting register 0 to `1` and running it...but I had to try.

Yeah, didn't work.

So I figured this is going to be another one like in previous years where we have to reverse engineer the input program.
So I put a debugger in to figure out which lines were causing the slowdown. I found that it was looping over one small section
of the program, and after a BUNCH of pseudocode chicken scratch, I was able to figure out that it was essentially
adding a counter to register 0 for every factor of the number that gets stored in register 5.

This was my really-hard to read reverse engineering of the part of the code that was going to loop trillions of times:
```
if r3 * r1 == r5:
	r2 = 1
	r4 += r2	// Skips ONE step (specifically the add 4 1 4...which means it will Run the addr 3 0 0 step next!)
else:
	r2 = 0

// The "addi 4 1 4" step makes it skip step "addr 3 0 0"

r1 += 1
if r1 > r5:
	r2 = 1
	r4 += r2
else:
	r2 = 0

r4 = 2 // Jump back to top.

// r0 += 1 for each time r3 is a factor of r5!!
```

Somehow from that, I figured out what it was doing. ...That's it...that's all we need to do. Instead of actually running the code, we just need it to run far enough
to set a value in register 5, and then find all factors of that number and add them up. Pretty simple...but man was
it confusing to figure out...

After figuring that out, we can just do the same thing for part 1, so make it all run the exact same way.

The reason it goes crazy for part 2 is because setting register 0 to `1` just makes the number in register 5 pretty massive...
and the code is not very efficient for finding factors (something like n^3), meaning it would take a few trillion (or more)
instructions to calculate without shortcutting it.

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |               0 |
| **Part Two** |            1073 |
