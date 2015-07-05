import random
from generate_code import visualize_code

def generate_code(possibilities = 25, nums = 5):
   code = []
   population = range(possibilities)
   for i in range(nums):
      choice_index = random.randint(0, possibilities - nums - 1)
      code.append(population[choice_index])

      # Replace with unused population element
      population[choice_index] = population[possibilities - i - 1]
   
   code.sort()
   return code

visualize_code(generate_code())
