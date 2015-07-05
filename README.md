What is this?
=============

It's an algorithm that produces a sequence of distinct random integers in some range with an even\* distribution (with guaranteed termination and an upper bound on runtime).

This is useful for coming up with "combination codes" for slider-input systems, such as the firemarble dome in the video game Riven.

![One of the firemarble domes in RIVEN](https://raw.github.com/philip-peterson/slider-combo/master/dome.png)

\* = as much as possible...

Key Feature
====

The key feature here is that the algorithm executes in bounded time (i.e. it definitely halts). A naive solution to the problem (for 25 possibilities and 5 numbers) that does not have this feature might be written as so:

```
import random
while True:
   combo = [random.randint(0,25) for i in range(5)]
   combo.sort()
   if not (combo[0] == combo[1]
      or combo[1] == combo[2]
      or combo[2] == combo[3]
      or combo[3] == combo[4]):
         break
print combo
````

But what if something strange happens with the pseudorandom number generator, for instance, it gets stuck always generating only 0's and 1's? Then, this loop would never terminate.

In my team's specific use-case, our code gets executed when we are starting a new game, so we would like to be certain that the algorithm will halt in finite time. So, that is what this library tries to provide -- an algorithm that accomplishes the same result as the above code but runs in bounded time.

Wait, you're actually worried about a widely-used and well-tested game engine's PRNG failing?
==========

Okay, no, not really... This is really just a thinly-veiled academic diversion. :P

What's the complexity?
======================
Currently it's O(possibilities * nums^2) time. Better than O(infinity)!

Also, the space complexity is O(nums).

Other solutions
===============
Soon after writing this I realized that R's sample(..., replace = FALSE) function does the same thing. My colleague [Ned Batchelder](https://github.com/nedbat) also pointed out that Python has the `random.sample()` function. Curious, I looked into how random.sample works, and it's rather clever. It's much better in terms of time (O(possibilities)), but slightly worse in terms of space (O(possibilities)). This restricts the usefulness of my implementation to refrigerators with less memory than buttons on their slider combination locks. Oh well!

How to run
==========

Simply type

```
python generate_code.py
```

It will spit out a visualization of the code it generated.
