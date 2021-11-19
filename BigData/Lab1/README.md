# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero y Anthony Garcia

Entregas de Tópicos espaciales en telemática.

## Documentación Cluster ERM - HDFS

1. Copiamos el dataset.
```bash
    user@master$ hdfs dfs -copyFromLocal /datasets/* /user//datasets/
```    
2. Listamos los archivos en nuestro hdfs
```bash
    user@master$ hdfs dfs -ls /user/<username>/datasets
    user@master$ hdfs dfs -ls /user/<username>/datasets/gutenberg-small/
```    
3. Validamos los archivos copiados en HUE :
    