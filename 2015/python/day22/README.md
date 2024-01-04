# Approach
### Data format

I just read the input into a map to represent the boss's stats and return it. It looks something like this:
```
{"hp": 1234, "mp": 0, "atk": 4321, "def": 0, "spells": []}
```

### Part 1
> _What is the least amount of mana you can spend and still win the fight?_

Ick. It was fun, but I just kept stumbling over implementation. I first started trying to create classes for all of the stuff,
which I still think is the "best" way to do it. However, the amount of copying and recursion on objects was giving me a
headache. So I ended up just passing the values into the recursive method over and over and just keep track of the minimum
whenever we win a game. Return the minimum at the end.

Takes WAY too long to run, and I'm not really happy with this one. One of these days I may rewrite it in a more
object oriented fashion, but for now it gave the right answer, so oh well...

### Part 2
> _What is the least amount of mana you can spend and still win the fight?_

I just added a new flag for if we are in hard mode. If so, subtract 1 from the HP amount on each player's turn and
end if they've lost.

I'm completely amazed at how much faster this one ran!

# Results

|              | Exec. Time (ms) |
|--------------|----------------:|
| **Part One** |           76508 |
| **Part Two** |            4439 |
