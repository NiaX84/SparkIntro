from scipy.stats import norm
from pyspark.sql import SparkSession
import numpy as np

if __name__ == '__main__':
    # spark_session = SparkSession.builder.master('local[*]').getOrCreate()
    # sc = spark_session.sparkContext

    norm_1 = norm(loc=0, scale=1)
    sample = np.sort(norm_1.rvs(10000))
    
    n_trials = 100
    n_simulations = 1000
    shuffle_matrix = np.empty((100,1000), dtype=int)
    mc_sample = np.empty((100,1000))
    for i in range(n_trials):
        shuffle_matrix[i, :] = np.random.randint(0, 10000, size=1000, dtype=int)
        mc_sample[i, :] = sample[shuffle_matrix[i, :]]
    
    # spark_session.stop()