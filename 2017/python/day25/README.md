# Approach
### Data format

I read the input file into an object which contains the different states and their `0` and `1` configurations. This
allowed me to just jump around and load the next state and its associated behavior really simply. The resulting
map looked something like:
```
{
	"A": {
		"0": {
			"w": #write value,
			"m": #move value (-1 or 1),
			"s": #state to jump to value
		},
		"1": {
			"w": #write value,
			"m": #move value (-1 or 1),
			"s": #state to jump to value
		}
	}
	...
}
```

I then stored that in a map along with the initial state and the number of times to run.

### Part 1
> _What is the diagnostic checksum it produces once it's working again?_

Nothing fancy. Use the map I created above and just actually run through it the number of times it said. I knew it
would take a little while, but 12 million is doable, so I gave it a shot. Took about 10 seconds, but finished...so...
Since it was the last puzzle, I was happy and just accepted it.

### Part 2
> __

Click the button, and we're done. Merry Christmas!!!!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |            9131 |
| **Part Two** |                 |
