from scipy.stats import norm
import numpy.random as rnd
from pyspark.sql import SparkSession

if __name__=='__main__':
    
    spark_session = SparkSession.builder.master('local[*]').getOrCreate()
    sc = spark_session.sparkContext
    
    norm_1 = norm(loc=0, scale=1)
    norm_2 = norm(loc=0, scale=1)
    norm_3 = norm(loc=0, scale=1)
    
    uniform_sample = rnd.mtrand.RandomState().rand(1000000)
    
    inverted_quantiles_1 = sc.parallelize(uniform_sample).map(lambda x: norm_1.ppf(x))
    inverted_quantiles_2 = sc.parallelize(uniform_sample).map(lambda x: norm_2.ppf(x))
    inverted_quantiles_3 = sc.parallelize(uniform_sample).map(lambda x: norm_3.ppf(x))

    combined_sample = list(zip(inverted_quantiles_1.collect(), inverted_quantiles_2.collect(), inverted_quantiles_3.collect()))

    aggregated_distribution = sc.parallelize(combined_sample).map(lambda x: sum(x))
    
    print(aggregated_distribution.mean())
    
    spark_session.stop()
    