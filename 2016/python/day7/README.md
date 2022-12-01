# Approach
### Part 1
> _How many IPs in your puzzle input support TLS?_

The idea here was to do the initial parse of the data into hypernets and supernets all before doing any processing.
I found it a little tricky, and so the best I could do was to just parse the inputs into an array, including the brackets.
Then I could just iterate over the array, and if I saw a `[`, I knew I was now in a hypernet, and if I saw a `]` I was back
in a supernet. I could then just start going through and check each input for letter patterns of `abba` in both hypernets and supernets.
If I saw any in any supernet, I tentatively marked them as "valid", but then if I ever saw any in a hypernet, I could immediately
mark it as "invalid" and quick processing right there. If I finished all of the data in a given input, and it was marked "valid",
then I just incremented a counter. Not too bad, but I did forgot to set the "is_valid" flag back to false when it found an invalid...so I
failed my first attempt and had to debug.

### Part 2
> _How many IPs in your puzzle input support SSL?_

Basically the same idea, but this time, I would iterate over the supernets first, find any parts of the data that matched the `aba`
pattern. Whenever I found one, I then lopped over ALL hypernets in the input to find if there were any `bab`. If I found one,
I could count it valid and stop processing.

I did keep putting the break statements in the wrong for-loop, which caused me to get the answer wrong twice. But other than that,
it went quickly.

# Results

|              | Answer | Attempts | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
|--------------|-------:|---------:|----------------:|----------------------:|-----:|
| **Part One** |    118 |        2 |              23 |                   N/A |  N/A |
| **Part Two** |    260 |        3 |              17 |                   N/A |  N/A |


# Original puzzle
### --- Day 7: Internet Protocol Version 7 ---
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as `xyyx` or `abba`. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

* `abba[mnop]qrst` supports TLS (`abba` outside square brackets).
* `abcd[bddb]xyyx` does not support TLS (`bddb` is within square brackets, even though xyyx is outside square brackets).
* `aaaa[qwer]tyui` does not support TLS (`aaaa` is invalid; the interior characters must be different).
* `ioxxoj[asdfgh]zxcvbn` supports TLS (`oxxo` is outside square brackets, even though it's within a larger string).


### --- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as `xyx` or `aba`. A corresponding BAB is the same characters but in reversed positions: `yxy` and `bab`, respectively.

For example:

* `aba[bab]xyz` supports SSL (`aba` outside square brackets with corresponding `bab` within square brackets).
* `xyx[xyx]xyx` does not support SSL (`xyx`, but no corresponding `yxy`).
* `aaa[kek]eke` supports SSL (`eke` in supernet with corresponding kek in hypernet; the `aaa` sequence is not related, because the interior character must be different).
* `zazbz[bzb]cdb` supports SSL (`zaz` has no corresponding `aza`, but `zbz` has a corresponding `bzb`, even though `zaz` and `zbz` overlap).
