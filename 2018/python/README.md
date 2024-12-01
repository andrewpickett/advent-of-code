# Overall Results

Ouch, this one had some HARD problems...and ones where my solution just is NOT good. I still have one (day 15) that I
haven't finished -- I have spent hours working on my solution, and it's "off by one"...I only got the right answer because
in my attempts to debug, I ran someone else's code. I am going to fix mine at some point...but I needed to walk away from
it for a while, because seriously...nothing I do is fixing the off by one, and everything I have SEEMS right (and works
for all input, including additional examples from the community...just not my own input!).

Other than that, I have one or two that just take forever to run, so clearly I need to work on them as well.

So yeah, overall, this year was the hardest yet...

## Timings

I created a utility to run all of the days a given number of times and average the times to get a true average run time.
I made it so I can run just the parsing of the input data, part 1, part 2, or all of them combined so I can see a true
breakdown of how long each part of my total Advent of Code takes.

For the below, I ran each part individually and then everything together. It averages almost 3 seconds per day for part
1 and over 16 seconds for each day on part 2...so...definitely needs some improvements...

|              | Total Exec. Time (ms) |
|--------------|----------------------:|
| **Get Data** |                  6185 |
| **Part One** |               3518067 |
| **Part Two** |               3575905 |
| **TOTAL**    |               7100157 |

## System Details

* Python 3.10.0
* Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz
	* 4 Cores
   * 8 Processors
* 32 GB Available memory (2133 MHz SODIMM)
* SAMSUNG MZCVKV512HAJH-OOOL1 SSD

## Daily Analysis/Breakdown

I rated each day in 4 categories:
1. **Story** - How much I enjoyed reading the puzzle and the story.
2. **Fun** - How much fun I had during the solving stage of the puzzle.
3. **Difficulty** - How difficult I thought the puzzle was. This encompasses both parts.
4. **Overall** - My overall ranking of the puzzle. This takes into account all of the above and just my general feelings on it.

![2018 Daily Rankings](images/daily_rankings.png)
