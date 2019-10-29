from variables_and_constants import initial_binary_population
from itertools import accumulate
from functions import calculate_fitness_array_from_binary_data, calculate_probability_array, calculate_new_population

generation = {}

generation['population'] = initial_binary_population

# Genetic Algorithm Performance for 1000 generations
for i in range(1000):
    fitness_sum, generation['fitness_array'] = calculate_fitness_array_from_binary_data(generation['population'])
    generation['probability_array'] = calculate_probability_array(generation['fitness_array'])
    generation['cumulative_array'] = list(accumulate(generation['probability_array']))
    calculate_new_population(generation)
    print('Generation', i, 'has a fitness of', fitness_sum)
