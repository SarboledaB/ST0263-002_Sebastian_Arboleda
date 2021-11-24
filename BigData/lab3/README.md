# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero y Anthony Garcia

Laboratorio 3 Big Data Topicos Especiales de Telemática

# Evidencias en S3

- **Salida de los datos del pundo 3.x:** s3://bigdata-telematica/telematica/lab3-2/df_csv/
# Parte 1

```bash
$ pyspark
>>> files_rdd = sc.textFile("hdfs:/user/admin/datasets/gutenberg-small/*.txt")
>>> files_rdd = sc.textFile("s3a://bigdata-telematica/telematica/datasets/gutenberg-small/*.txt")
>>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> wc = wc_unsort.sortBy(lambda a: -a[1])
>>> for tupla in wc.take(10):
>>>     print(tupla)
>>> wc.saveAsTextFile("s3a://bigdata-telematica/telematica/wcout1")
```

## Datos en HDFS:
 ![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-1-1.PNG)

## Datos en S3:
  ![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-1-2.PNG)


## Uso de pyspark con Jupyterhub:
```bash
%spark.pyspark
files_rdd = sc.textFile("s3a://bigdata-telematica/telematica/datasets/gutenberg-small/*.txt")
wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wc = wc_unsort.sortBy(lambda a: -a[1])
for tupla in wc.take(10):
    print(tupla)
wc.saveAsTextFile("s3a://bigdata-telematica/telematica/wcout1")
``` 
## WordCount PySpark:
  ![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-1-3.PNG)

# Parte 2
## Replicación del notebook Data_processing_using_PySpark.ipynb con los datos respectivos
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-2-1.PNG)

![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-2-2.PNG)

![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-2-3.PNG)

![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-2-4.PNG)

![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab3-2-5.PNG)

# Parte 3
## Jupiter notebook:
[Lab3-2.ipynb](Lab3-2.ipynb)
