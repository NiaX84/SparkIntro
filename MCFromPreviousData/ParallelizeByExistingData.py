from scipy.stats import norm
from pyspark.sql import SparkSession
import numpy as np
from random import choice
import string


def prepare_simulation(seed, n_iterations, original_data_sequence):
    random_state = np.random.RandomState(seed)
    simulation_matrix = random_state.choice(original_data_sequence, size=n_iterations)
    return simulation_matrix
        

if __name__ == '__main__':
    spark_session = SparkSession.builder.master('local[*]').getOrCreate()
    sc = spark_session.sparkContext

    norm_1 = norm(loc=0, scale=1)
    sample = np.sort(norm_1.rvs(100000))
    
    n_trials = 1000
    n_simulations = 10000
    
    seeds = [int.from_bytes(bytearray(''.join(choice(string.ascii_lowercase) for _ in range(4)), encoding='utf-8'), 'big') for _ in range(n_trials)]
    
    simulation_matrix = sc.parallelize(seeds).map(lambda x: prepare_simulation(x, n_simulations, sample))
    combined_simulation = simulation_matrix.collect()
    
    spark_session.stop()
    
    print(combined_simulation[0])
    