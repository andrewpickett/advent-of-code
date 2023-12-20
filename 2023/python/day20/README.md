# Approach
### Part 1
> _What do you get if you multiply the total number of low pulses sent by the total number of high pulses sent?_

More sleep...I actually planned on working on this when it was released, but I fell asleep around 11:30 and didn't wake up until 5...
so I started working on it around 7:30am or so...

Another fun one involving some parsing and basic maps. The instructions were not the clearest, and the example didn't make
sense at first until you actually coded things correctly (namely that lines `a -high-> b` and `b -high-> c` just end the flow,
because they're flip-flops and when those receive `high`, it's done).

I did run into some issues because I didn't initially do the extra work to find all inputs to the conjunction modules before
starting to process. I figured I'd add them as I ran into them in the input, but that caused incorrect behavior for a while.

After debugging, I figured it out, added that initialization step at the beginning and it worked wonderfully.

The other thing that I didn't realize until I was into part 2 was that I needed to deep-copy the data before processing
so that the first runs didn't impact part 2 runs.

### Part 2
> _what is the fewest number of button presses required to deliver a single low pulse to the module named rx?_

Well, again, you know there's got to be a mathematical approach to this. I spent a while looking for loops and other ways
to identify shorter chunks that could then be combined.

After about 30 minutes of trying different programmatic approaches, I decided to just manually look at the input.

I noticed there was only one module (we'll call it module `A`) that sent signals to my target node `rx`. Module `A` was
a conjunction module, so that means the only way it would send a low signal to `rx` is if all of its inputs send a high
pulse to them at the same time.

So there we go. That's the shortcut. We need to figure out how many button presses it takes to send a high pulse to each of
those modules and then take the LCM of those to calculate the number of presses for ALL of them to have high pulses sent
to them in the same pass.

It took quite a bit of tinkering with my algorithm and figuring out how to keep track of those data points. I kept running
into an issue where I was checking the state after the full button press was completed -- but there were clearly times when
high pulses were sent to those individual modules in the midst of the program running, but by the end they were reset...
which meant that when I was checking the values at the end, they were always reset and I wasn't finding any loops.

So, again, I had to keep track of state a bit through the algorithm and update the state in the middle of a program run
and then check once all of my dependent modules have been hit.

So once I did that and I got my 4 numbers (because I had 4 modules that fed into module `A`), I just returned the LCM and
it was the correct answer! WHEW!

# Results

|              | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|---------:|----------------:|----------------------:|-----:|
| **Part One** |        1 |               1 |              08:23:27 | 9021 |
| **Part Two** |        1 |               3 |              09:54:24 | 6135 |


# Original puzzle
### --- Day 20: Pulse Propagation ---
With your help, the Elves manage to find the right parts and fix all of the machines. Now, they just need to send the command to boot up the machines and get the sand flowing again.

The machines are far apart and wired together with long **cables**. The cables don't connect to the machines directly, but rather to communication **modules** attached to the machines that perform various initialization tasks and also act as communication relays.

Modules communicate using pulses. Each pulse is either a **high pulse** or a **low pulse**. When a module sends a pulse, it sends that type of pulse to each module in its list of **destination modules**.

There are several different types of modules:

**Flip-flop** modules (prefix `%`) are either **on** or **off**; they are initially **off**. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it **flips between on and off**. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

**Conjunction** modules (prefix `&`) **remember** the type of the most recent pulse received from **each** of their connected input modules; they initially default to remembering a **low pulse** for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers **high pulses** for all inputs, it sends a **low pulse**; otherwise, it sends a **high pulse**.

There is a single **broadcast module** (named `broadcaster`). When it receives a pulse, it sends the same pulse to all of its destination modules.

Here at Desert Machine Headquarters, there is a module with a single button on it called, aptly, the **button module**. When you push the button, a single **low pulse** is sent directly to the `broadcaster` module.

After pushing the button, you must wait until all pulses have been delivered and fully handled before pushing it again. Never push the button if modules are still processing pulses.

Pulses are always processed **in the order they are sent**. So, if a pulse is sent to modules `a`, `b`, and `c`, and then module `a` processes its pulse and sends more pulses, the pulses sent to modules `b` and `c` would have to be handled first.

The module configuration (your puzzle input) lists each module. The name of the module is preceded by a symbol identifying its type, if any. The name is then followed by an arrow and a list of its destination modules. For example:
```
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
```
In this module configuration, the broadcaster has three destination modules named `a`, `b`, and `c`. Each of these modules is a flip-flop module (as indicated by the `%` prefix). `a` outputs to `b` which outputs to `c` which outputs to another module named `inv`. `inv` is a conjunction module (as indicated by the `&` prefix) which, because it has only one input, acts like an inverter (it sends the opposite of the pulse type it receives); it outputs to `a`.

By pushing the button once, the following pulses are sent:
```
button -low-> broadcaster
broadcaster -low-> a
broadcaster -low-> b
broadcaster -low-> c
a -high-> b
b -high-> c
c -high-> inv
inv -low-> a
a -low-> b
b -low-> c
c -low-> inv
inv -high-> a
```
After this sequence, the flip-flop modules all end up **off**, so pushing the button again repeats the same sequence.

Here's a more interesting example:
```
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
```
This module configuration includes the `broadcaster`, two flip-flops (named `a` and `b`), a single-input conjunction module (`inv`), a multi-input conjunction module (`con`), and an untyped module named `output` (for testing purposes). The multi-input conjunction module `con` watches the two flip-flop modules and, if they're both on, sends a **low pulse** to the `output` module.

Here's what happens if you push the button once:
```
button -low-> broadcaster
broadcaster -low-> a
a -high-> inv
a -high-> con
inv -low-> b
con -high-> output
b -high-> con
con -low-> output
```
Both flip-flops turn on and a low pulse is sent to `output`! However, now that both flip-flops are on and `con` remembers a high pulse from each of its two inputs, pushing the button a second time does something different:
```
button -low-> broadcaster
broadcaster -low-> a
a -low-> inv
a -low-> con
inv -high-> b
con -high-> output
```
Flip-flop `a` turns off! Now, `con` remembers a low pulse from module `a`, and so it sends only a high pulse to `output`.

Push the button a third time:
```
button -low-> broadcaster
broadcaster -low-> a
a -high-> inv
a -high-> con
inv -low-> b
con -low-> output
b -low-> con
con -high-> output
```
This time, flip-flop `a` turns on, then flip-flop `b` turns off. However, before `b` can turn off, the pulse sent to `con` is handled first, so it **briefly remembers all high pulses** for its inputs and sends a low pulse to `output`. After that, flip-flop `b` turns off, which causes `con` to update its state and send a high pulse to `output`.

Finally, with `a` on and `b` off, push the button `a` fourth time:
```
button -low-> broadcaster
broadcaster -low-> a
a -low-> inv
a -low-> con
inv -high-> b
con -high-> output
```
This completes the cycle: `a` turns off, causing `con` to remember only low pulses and restoring all modules to their original states.

To get the cables warmed up, the Elves have pushed the button `1000` times. How many pulses got sent as a result (including the pulses sent by the button itself)?

In the first example, the same thing happens every time the button is pushed: `8` low pulses and `4` high pulses are sent. So, after pushing the button `1000` times, `8000` low pulses and `4000` high pulses are sent. Multiplying these together gives **`32000000`**.

In the second example, after pushing the button `1000` times, `4250` low pulses and `2750` high pulses are sent. Multiplying these together gives **`11687500`**.

Consult your module configuration; determine the number of low pulses and high pulses that would be sent after pushing the button `1000` times, waiting for all pulses to be fully handled after each push of the button. **What do you get if you multiply the total number of low pulses sent by the total number of high pulses sent?**

### --- Part Two ---
The final machine responsible for moving the sand down to Island Island has a module attached named `rx`. The machine turns on when a **single low pulse** is sent to `rx`.

Reset all modules to their default states. Waiting for all pulses to be fully handled after each button press, **what is the fewest number of button presses required to deliver a single low pulse to the module named rx?**
