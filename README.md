What is this?
=============

It's an algorithm that produces a sequence of distinct random integers in some range with an even\* distribution (with guaranteed termination and an upper bound on runtime).

This is useful for coming up with "combination codes" for slider-input systems, such as the firemarble dome in the video game Riven.

![One of the firemarble domes in RIVEN](https://github.com/philip-peterson/slider-combo/raw/master/dome.png)

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
Soon after writing this I realized that R's sample(..., replace = FALSE) function does the same thing. My colleague [Ned Batchelder](https://github.com/nedbat) also pointed out that Python has the `random.sample()` function. Curious, I looked into how random.sample works, and it's rather clever. It's much better in terms of time (O(possibilities)), but slightly worse in terms of space (O(possibilities)). This means my algorithm is the best choice when you are extremely strapped for memory.

You can view my rendition of the approach taken by Python, in `alt_generate_code.py`.

How to run
==========

Simply type

```
python generate_code.py
```

It will spit out a visualization of the code it generated.

Some example outputs
====================

```
XX________X__XX__________
_X__XX________________X_X
____________X___XX_X__X__
__X____X____XX_______X___
_X___X____X___X_________X
XX___X_____X_____X_______
_____X___X___X____X_____X
____XXX___X__X___________
_________X__X___X____X__X
__X____X_X_________X___X_
__________X_X__X_____XX__
_____XX___________X__XX__
XX__X________X_____X_____
____XX______XX____X______
_____XX_____X____X_____X_
____X__X____X___X_X______
_________XX_X_____X_____X
__X______________XX__X_X_
________X__X__X_X_X______
X_X__XX___X______________
______________XX___XX___X
___________X_X___XX_____X
__________XX___X___X____X
_XX________X___X_______X_
__X__X____X_________X__X_
______________X___XX___XX
____X__XX___XX___________
___________X__X_X_X___X__
___X_XX_____________X__X_
_X________X__X__X_______X
__X________X____X__X___X_
___________X___XXX______X
______X_X_________XX__X__
X_X_X__X_____X___________
X_______X_____X____X_X___
_XX______X________X___X__
___X______________X___XXX
_______________XX_X___XX_
X_________X___X___X_X____
X____X_X______X____X_____
____X_______X__X_____X_X_
________X_____XX_X______X
X__________X_XX______X___
___X_________X____X____XX
_________XX___X_____X___X
_X______X__X__X______X___
X____XX_____X_________X__
XX_X__X_______________X__
X____________X__X_X_____X
X_X_____________X___X__X_
X_XX_____X______________X
______X____X___X__X__X___
_____X__X___XX__X________
```
