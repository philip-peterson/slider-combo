import random

def select(i, n, excepts):
   """Selects the i'th number (zero-indexed) in the range 0...(n-1) that
   does not equal any number in 'excepts'.
   
   e.g. if excepts = [2,] then select(3, 5, excepts) would select the
   3rd number of the list [0, 1, 3, 4] which would be 4.

   Note: may return None if such a number does not exist.
   """

   counter = 0
   for j in range(n):
      if j in excepts:
         continue
      if counter == i:
         return j
      counter += 1

def generate_code(possibilities = 25, nums = 5):
   assert nums <= possibilities
   assert nums > 0

   code = [-1 for i in range(nums)]

   for i in range(nums):
      dice_roll = random.randint(0, possibilities - i - 1)
      entry = select(dice_roll, possibilities, code)
      code[i] = entry

   code.sort()

   return code

def visualize_code(code, possibilities = 25):
   slots = ['_' for i in range(possibilities)]
   for i in code:
      slots[i] = 'X'
   print ''.join(slots)

visualize_code(generate_code())
