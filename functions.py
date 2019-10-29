import math
import random
from variables_and_constants import constant1, constant2, Pc, Pm


def calculate_fitness_value(x, y):
    """
    Calculate the fitness value
    """
    return 21.5 + x * math.sin(4 * math.pi * x) + y * math.sin(20 * math.pi * y)


def calculate_fitness_array_from_binary_data(binary_vector):
    """
    Calculate the fitness array from a binary vector
    Every binary datum has 33 bits (first 18 to x1 and the other 15 to x2)
    """
    final_vector = []

    for value in binary_vector:
        value1 = -3 + int(value[0:18], 2) * constant1
        value2 = 4.1 + int(value[18:33], 2) * constant2
        final_vector.append(calculate_fitness_value(value1, value2))

    return final_vector


def calculate_probability_array(fitness_vector):
    """
    Calculate the probability to select every chromosome from a fitness vector
    """
    total_fitness = sum(fitness_vector)

    return [fitness_value / total_fitness for fitness_value in fitness_vector]


def generate_random_numbers():
    """
    Generate random numbers
    """

    return [random.uniform(0, 1) for i in range(20)]


def adapt_selected_chromosomes_array(chromosomes, random_sequence):
    """
    The selected chromosomes array can be odd so it has to choose if we'll have to add o remove one element to the array
    """

    if len(chromosomes) % 2 == 1:
        choice = random.randrange(0, 2, 1)
        if choice:
            chromosomes.append(list(filter(lambda x: x > Pc, random_sequence))[0])
        else:
            chromosomes.pop()


def calculate_new_population(generation):
    """
    Calculate a random array in order to select the new generation of chromosomes
    """

    random_numbers_sequence = generate_random_numbers()

    new_population = []
    for random_number in random_numbers_sequence:
        # Find the index to select new chromosome
        index = 0
        while random_number > generation['cumulative_array'][index]:
            index += 1
        new_population.append(generation['population'][index])
    generation['population'] = new_population

    # Select operation
    crossover_random_numbers_sequence = generate_random_numbers()
    selected_chromosomes = list(filter(lambda x: x < Pc, crossover_random_numbers_sequence))
    adapt_selected_chromosomes_array(selected_chromosomes, crossover_random_numbers_sequence)

    # Crossover Operation
    # for i in range(0, len(selected_chromosomes), 2):

    amigo = selected_chromosomes

    return True
