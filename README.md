# SparkIntro
a playground for SPARK setup and basic usage
prerequisites: Python (anaconda), java (1.8), jupyter-notebook

HADOOP_HOME=<some_directory>\Hadoop

PYSPARK_DRIVER_PYTHON=ipython

PYSPARK_DRIVER_PYTHON_OPTS=notebook

SPARK_HOME=<some_directory>\spark-2.3.1-bin-hadoop2.7

JAVA_HOME=<location_of_java_dk>

PATH=%PATH%;%SPARK_HOME%/bin;%HADOOP_HOME%/bin

%HADOOP_HOME%/bin contains 'winutils.exe' file on windows

## Making pyspark work with your IDE:

set the following environment variable:

PYTHONPATH=%SPARK_HOME%\python;%SPARK_HOME%\python\lib\py4j-<version>-src.zip

## Download links
download spark at:
https://spark.apache.org/downloads.html

**Note**: do not use spark 2.4.0. With this version you get an error when calling an action on RDD

download 'winutils.exe' at:
https://github.com/steveloughran/winutils/blob/master/hadoop-2.6.0/bin/winutils.exe

download 'java DK' at:
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

# Parallelism in spark

http://www.openkb.info/2018/06/how-to-control-parallelism-of-spark-job.html
http://www.openkb.info/2015/06/resource-allocation-configurations-for.html
https://www.learningjournal.guru/article/apache-spark/apache-spark-parallel-processing/
https://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/
https://dzone.com/articles/apache-spark-performance-tuning-degree-of-parallel
https://umbertogriffo.gitbooks.io/apache-spark-best-practices-and-tuning/content/sparksqlshufflepartitions_draft.html
https://spark.apache.org/docs/latest/configuration.html
