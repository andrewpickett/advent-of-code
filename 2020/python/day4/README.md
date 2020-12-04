# Approach
### Part 1
> _Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?_

Wow...my brain was not functioning when I solved this...at all. I kept making silly mistake after silly mistake.
The puzzle itself is extremely straighforward: read the data in, where each passport is separated by a blank line,
and make sure they have all of the specific fields in it. Return the number that have all 7 required fields.

* First, I somehow called my validating function over and over with the same passport entry...which was clearly wrong and cost me a guess...
* Then I fat-fingered the fields to be checking...so there went another.
* Then I realized I read the requirements incorrectly...so there went another.
* I don't even know what happened with the next one, but somehow I got the answer wrong a 4th time...

That meant that I now had to wait 5 minutes before guessing again. I finally got it right, but I somehow messed up 2 lines of code 4 times in 10 minutes.

GO ME!

### Part 2
> _Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?_

So...again...my brain was completely fogged up when I started this. This part just required adding another layer
of validation on each of the passports, and making sure specific fields had specific validations.

Not too bad...except I kept getting the wrong answer, again!

* First, I again messed up calling the validations, and somehow ended up with an answer that had MORE valid entries than part 1...
  which considering part 1 is one of the validations, is impressive...
* I quickly fixed that and got an answer that I swore was correct. It wasn't.
* I checked my code over and over and over and over and couldn't see the problem. So brain-fogged-me tried submitting
  the same answer two more times. Shockingly, it didn't work.
* Went to bed and the next day, still didn't see the problem...was about to give up...

...and then I saw it. This was probably the first time I've ever been bitten by not using an anchor character
in my regular expressions. My validation for PID was this:

`\d{9}`

...and apparently I had one entry in my input that was completely valid, except it had a 10 digit PID. So I had to
make sure to tighten all my regular expressions with anchors, and after changing my PID validation to be this:

`^\d{9}$`

All was happy in the world.


# Results

|    | Answer     | Attempts  | Exec. Time (ms) | Solve Time (HH:mm:ss) | Rank |
| ------ |-----------:| ---------:| -------------------:| ----:| ----:|
| **Part One**  | 170  | 5  | <1  | 00:15:38  | 2978  |
| **Part Two**  | 103  | 4  | 1  | ~00:45:00  | 27320  |
