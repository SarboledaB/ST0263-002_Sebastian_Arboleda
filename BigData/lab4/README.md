# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero y Anthony Garcia

Entregas de Tópicos espaciales en telemática.

## Documentación

**HIVE y SparkSQL, GESTIÓN DE DATOS VIA SQL:**

**URI:**

- Athena: s3://bigdata-telematica/telematica/datasets/athena/
- datasets: s3://bigdata-telematica/telematica/datasets/

**1.1. Hue :**
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-1-1.png)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-1-2.png)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-1-3.png)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-1-4.png)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-1-5.png)

**1.2. AWS EMR Zeppelin :**
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-2-1.PNG)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-2-2.PNG)
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-2-3.PNG)


**1.4. AWS Athena:**

-SELECT "nombre departamento",count(*) as "counter" FROM "AwsDataCatalog"."default"."covid" GROUP BY "nombre departamento" ORDER BY "counter" DESC LIMIT 10;
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-3-1.PNG)

-SELECT "nombre municipio",count(*) as "counter" FROM "AwsDataCatalog"."default"."covid" GROUP BY "nombre municipio" ORDER BY "counter" DESC LIMIT 10;

![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-3-2.PNG)

-SELECT "fecha reporte web",count(*) as "counter" FROM "AwsDataCatalog"."default"."covid" GROUP BY "fecha reporte web" ORDER BY "counter" DESC LIMIT 10;
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-3-3.PNG)

-SELECT "unidad de medida de edad", edad, count(*) as "counter" FROM "AwsDataCatalog"."default"."covid" GROUP BY "unidad de medida de edad", edad;
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-3-4.PNG)

-SELECT "nombre departamento","unidad de medida de edad", edad, count(*) as "counter" FROM "AwsDataCatalog"."default"."covid" GROUP BY "nombre departamento","unidad de medida de edad", edad ORDER BY "nombre departamento" ASC;
![alt text](https://bigdata-telematica.s3.amazonaws.com/imagenes-labs/lab4-3-5.PNG)
