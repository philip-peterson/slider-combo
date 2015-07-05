What is this?
=============

It's an algorithm that produces a sequence of distinct random numbers in some range with an even\* distribution (with guaranteed termination and an upper bound on runtime).

This is useful for coming up with "combination codes" for slider-input systems, such as the firemarble dome in the video game Riven.

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

How to run
==========

Simply type

```
python generate_code.py
```

It will spit out a visualization of the code it generated.
