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


## Download links
download spark at:
https://spark.apache.org/downloads.html

download 'winutils.exe' at:
https://github.com/steveloughran/winutils/blob/master/hadoop-2.6.0/bin/winutils.exe

download 'java DK' at:
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
