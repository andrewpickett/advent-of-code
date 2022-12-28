# Approach
### Part 1
> _What number will the monkey named root yell?_

This was a fun puzzle. This first part wasn't really too tricky. It was quite a welcome break from the last few days.

The approach I took for this part was to parse the input into a map where the keys are the names of the monkeys and the values
are either the integer value for it, or an object that has the operation and other values (or names of other monkeys).

Once I have that map, it's just a matter of recursively performing the operations when they are defined until all monkeys have
static values set. At which point, just return `root`'s value.

### Part 2
> _What number do you yell to pass root's equality test?_

OK...so...I started off by just doing what the instructions said: change root to be an equality check. I did this by just taking
the two "other" monkeys referenced by `root` and built the trees from them (instead of from `root` itself).

The next step was to find which of those two trees contained the `humn` monkey. In my case it was the first one. So...now what I decided to do
was build an equation using another recursive function to pretty much just write out the entire equation to calculate that tree.
I made sure to replace `humn`'s value with a variable `x`, and then set that really long equation equal to the value from the
other tree.

I then decided to just print out that equation...and it seemed to work pretty well, but it was really long...like 1500 characters long.

I decided to try plugging it into Wolfram Alpha, just to see if it would work, and sure enough, it told me that it was too long
to calculate.

So...the next thing I did was tried to simplify the equation as much as I could: Basically I evaluated any of the "simple" nested
expressions within the long equation (e.g. `(4*3)` and replace it with just `12`). I do this as much as possible until I'm left with
just a bunch of nested constant values and a single equation with `x` in it.

After I finally got that working, my equation was only about 350 characters long, so I plugged into Wolfram Alpha, and it worked!

I got my answer! I then moved on...I only recently came back to this to actually have my code figure out the value for me.

The approach I took to do that is: since my "simplified" expression is just a bunch of single constants with an operation all the
way down to the single x-based equation, I decided to just work from the outside inwards, one operation at a time, and perform the opposite
operation on the known value on the left. It ESSENTIALLY works like popping operations and values off of a stack, but without actually
using a stack. Once I get down to having no parentheses left, I just evaluate the last equation (which should be my simple x-based one)...and
return the value.

It really was a fun puzzle from the beginning to the end. Still lots of optimizations I could make, but it's pretty good now.

# Results

|              |         Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------------:|---------:|----------------:|----------------------:|-----:|
| **Part One** | 81075092088442 |        1 |               1 |              00:17:59 | 1861 |
| **Part Two** |  3349136384441 |        1 |              14 |              00:50:55 | 2117 |


# Original puzzle
### --- Day 21: Monkey Math ---
The monkeys are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding
their ground and making various monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard
you talking about trying to find the grove; they can show you a shortcut if you answer their riddle.

Each monkey is given a job: either to yell a specific number or to yell the result of a math operation. All of the number-yelling
monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number,
and those two other monkeys might also be waiting on other monkeys.

Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

For example:

```
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
```

Each line contains the name of a monkey, a colon, and then the job of that monkey:

* A lone number means the monkey's job is simply to yell that number.
* A job like `aaaa` + `bbbb` means the monkey waits for monkeys `aaaa` and `bbbb` to yell each of their numbers; the monkey then yells the sum of those two numbers.
* `aaaa` - `bbbb` means the monkey yells aaaa's number minus `bbbb`'s number.
* Job `aaaa` * `bbbb` will yell `aaaa`'s number multiplied by `bbbb`'s number.
* Job `aaaa` / `bbbb` will yell `aaaa`'s number divided by `bbbb`'s number.

So, in the above example, monkey `drzm` has to wait for monkeys `hmdt` and `zczc` to yell their numbers. Fortunately,
both `hmdt` and `zczc` have jobs that involve simply yelling a single number, so they do this immediately: `32` and `2`.
Monkey `drzm` can then yell its number by finding `32` minus `2`: `30`.

Then, monkey `sjmn` has one of its numbers (`30`, from monkey `drzm`), and already has its other number, `5`, from `dbpl`. This
allows it to yell its own number by finding `30` multiplied by `5`: `150`.

This process continues until root yells a number: `152`.

However, your actual situation involves considerably more monkeys.


### --- Part Two ---
Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named `root`; specifically, you got the wrong math operation. The correct operation for
monkey `root` should be `=`, which means that it still listens for two numbers (from the same two monkeys as before), but
now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with `humn`:. It isn't a monkey - it's you. Actually, you got the job wrong,
too: you need to figure out what number you need to yell so that `root`'s equality check passes. (The number that appears after `humn`:
in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test is `301`. (This causes root to get the same number, `150`,
from both of its monkeys.)

