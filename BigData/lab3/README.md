$ pyspark
>>> files_rdd = sc.textFile("hdfs:/user/admin/datasets/gutenberg-small/*.txt")
>>> files_rdd = sc.textFile("s3a://bigdata-telematica/telematica/datasets/gutenberg-small/*.txt")
>>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> wc = wc_unsort.sortBy(lambda a: -a[1])
>>> for tupla in wc.take(10):
>>>     print(tupla)
>>> wc.saveAsTextFile("s3a://bigdata-telematica/telematica/wcout1")

%spark.pyspark
files_rdd = sc.textFile("s3a://bigdata-telematica/telematica/datasets/gutenberg-small/*.txt")
wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wc = wc_unsort.sortBy(lambda a: -a[1])
for tupla in wc.take(10):
    print(tupla)
wc.saveAsTextFile("s3a://bigdata-telematica/telematica/wcout1")

/user/admin/datasets/gutenberg-small