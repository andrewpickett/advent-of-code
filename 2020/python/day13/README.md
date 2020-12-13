# Approach

### Part 1
> _What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?_

This part was fairly self-explanatory. Take the first number from the input and start an index there.
From here you could take 1 of 2 approaches:

1. For each bus number in the input start at the input, and increment one minute at a time until
the time is evenly divisible by the bus number. Once you have the times for all of the busses, find the
minimum
2. Directly count the next time (after the input) each bus will run and then return the minimum from that.
You can do that pretty easily by just taking an integer division and adding 1 and then re-multiplying.

I went with approach #2, as it had only one for loop and seemed to be faster to implement.

### Part 2
> _What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?_

So this one was definitely a head-scratcher. I had to read the puzzle multiple times to understand what
it was asking. The direct brute force approach is pretty simple to write:

```python
t = 0
while True:
	valid = True
	for i, x in enumerate(busses):
		if (t + i) % x != 0:
			valid = False
		   break
	if valid:
		return t
	t += 1
```
Just start at `time=0`, loop over every bus/index and check if the maths works out:

`(time + bus_index) % bus_number == 0`

If it works for every bus in the list, then you have your answer. Simple!

But...the issue is when it says the answer for this puzzle would certainly be over
100,000,000,000,000. A hundred trillion is a large number...even for a computer just doing a basic
calculation that many times. So clearly brute force is out for this.

At this point, I just started jotting notes down to see if I could determine a pattern or correlation
between the numbers and the answers for all of the given examples. They looked something like this:
```
GIVEN: 7,13,x,x,59,x,31,19
ANSWER: 1068788

t = 7a
t = 13b - 1
t = 59c - 4
t = 31d - 6
t = 19e - 7

OR

t		= 7a
t+1 		= 13b
t+4		= 59c
t+6		= 31d
t+7		= 19e

LCM???
3162341
```

and on and on. Lots of rewriting the same data over and over again. I did the first optimization that jumped
out at me, which was changing my interval from `1` to the bus at the first index in the list...because
whatever the answer was, it would have to be evenly divisible by that number. In my input, that bus
number was `13`...

Well, that brings my number of iterations down to still many trillions of iterations, so...that wasn't going
to be enough.

I decided to start my loop at 100,000,000,000,000 since it said it would be higher than that...but that
was just a stab in the dark and wasn't going to gain me anything.

It was pretty clear that the approach for iterating would HAVE to be exponential, not linear in order to
find the answer. I just wasn't seeing how. I also had a nagging thought I had seen math problems/theorems
like this before, but I could for the life of me remember what they were.

So I went to bed.

While laying in bed almost asleep, all my thoughts and notes came together and clicked. So I got out of bed
and tried to implement what I was thinking:

I was on the right track with thinking the answer would have to be a multiple of the bus at the first index...
well, then given that, just find the time when the first TWO busses requirements are met. At this point,
I know the answer will have to be a multiple of THAT index. Which means my interval can change to the current
interval multiplied by the current time interval...because that would make sure I'm only hitting numbers
that work for both of the first two busses. Now move on to the third, and keep going with that until you
try all of the busses and in the end the interval is in the millions...and that will chew through
a trillion pretty quickly.

In fact, I was shocked when I ran it, got an answer of over 500 trillion in under 1ms!!

For what it's worth, the next day I remembered where I had seen this sort of problem before:
The Chinese Remainder Theorem.

I re-looked it up, and it ABSOLUTELY would have been another option to solve this. I feel like the code
would not have been as intuitive or easy to understand. So...I think you could definitely use that
approach if you want...now that you have the name of this sort of problem, I'm sure coding it wouldn't be
too much work.

# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 2305  | 1  | 0  | 00:11:05  | 2088  |
| **Part Two**  | 552612234243498  | 1  | 0  | 01:25:22  | 2592  |


# Original Puzzle

### --- Day 13: Shuttle Search ---
Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book
another ship, you discover that no ships embark from that port to your vacation island. You'll need to
get from the port to the nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus
has an ID number that also indicates how often the bus leaves for the airport.

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed
reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After
that, each bus travels to the airport, then various other locations, and finally returns to the sea port
to repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID `5` departs from the sea
port at timestamps `0`, `5`, `10`, `15`, and so on. The bus with ID `11` departs at `0`, `11`, `22`,
`33`, and so on. If you are there when the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest
timestamp you could depart on a bus. The second line lists the bus IDs that are in service according
to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport.
(There will be exactly one such bus.)

For example, suppose you have the following notes:
```
939
7,13,x,x,59,x,31,19
```
Here, the earliest timestamp you could depart is `939`, and the bus IDs in service are `7`, `13`, `59`,
`31`, and `19`. Near timestamp `939`, these bus IDs depart at the times marked D:
```
time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .
```
The earliest bus you could take is bus ID `59`. It doesn't depart until timestamp `944`, so you would
need to wait `944 - 939 = 5` minutes before it departs. Multiplying the bus ID by the number of
minutes you'd need to wait gives `295`.

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes
you'll need to wait for that bus?

### --- Part Two ---
The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp
such that the first bus ID departs at that time and each subsequent listed bus ID departs at that
subsequent minute. (The first line in your input is no longer relevant.)

For example, suppose you have the same list of bus IDs as above:
```
7,13,x,x,59,x,31,19
```
An `x` in the schedule means there are no constraints on what bus IDs must depart at that time.

This means you are looking for the earliest timestamp (called `t`) such that:

* Bus ID `7` departs at timestamp `t`.
* Bus ID `13` departs one minute after timestamp `t`.
* There are no requirements or restrictions on departures at two or three minutes after timestamp `t`.
* Bus ID `59` departs four minutes after timestamp `t`.
* There are no requirements or restrictions on departures at five minutes after timestamp `t`.
* Bus ID `31` departs six minutes after timestamp `t`.
* Bus ID `19` departs seven minutes after timestamp `t`.

The only bus departures that matter are the listed bus IDs at their specific offsets from `t`.
Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example,
in the list above, because bus ID `19` must depart seven minutes after the timestamp at which bus ID `7`
departs, bus ID `7` will always also be departing with bus ID `19` at seven minutes after timestamp `t`.

In this example, the earliest timestamp at which this occurs is `1068781`:
```
time     bus 7   bus 13  bus 59  bus 31  bus 19
1068773    .       .       .       .       .
1068774    D       .       .       .       .
1068775    .       .       .       .       .
1068776    .       .       .       .       .
1068777    .       .       .       .       .
1068778    .       .       .       .       .
1068779    .       .       .       .       .
1068780    .       .       .       .       .
1068781    D       .       .       .       .
1068782    .       D       .       .       .
1068783    .       .       .       .       .
1068784    .       .       .       .       .
1068785    .       .       D       .       .
1068786    .       .       .       .       .
1068787    .       .       .       D       .
1068788    D       .       .       .       D
1068789    .       .       .       .       .
1068790    .       .       .       .       .
1068791    .       .       .       .       .
1068792    .       .       .       .       .
1068793    .       .       .       .       .
1068794    .       .       .       .       .
1068795    D       D       .       .       .
1068796    .       .       .       .       .
1068797    .       .       .       .       .
```
In the above example, bus ID `7` departs at timestamp `1068788` (seven minutes after `t`). This
is fine; the only requirement on that minute is that bus ID `19` departs then, and it does.

Here are some other examples:

* The earliest timestamp that matches the list `17,x,13,19` is `3417`.
* `67,7,59,61` first occurs at timestamp `754018`.
* `67,x,7,59,61` first occurs at timestamp `779210`.
* `67,7,x,59,61` first occurs at timestamp `1261476`.
* `1789,37,47,1889` first occurs at timestamp `1202161486`.

However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than
`100000000000000`!

What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their
positions in the list?
