# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero y Anthony Garcia

Entregas de Tópicos espaciales en telemática.

## Documentación Cluster EMR

**Creacion del cluster:**

- Par de claves de EC2

**Creacion del cluster:**

1. Entrar por opciones avanzadas.
2. Selecionamos la version 6.3.1
3. Seleccionamos los siguientes componentes :
    - Hadoop
    - JupyterHub
    - Hive
    - Sqoop
    - Zeppelin
    - Tez
    - JupyterEnterpriseGateway
    - Hue
    - Spark
    - Livy
    - HCatalog
4. Aceptamos la integracion del catalogo de Glue.
5. Ingresamos la configuracion de S3 para asegurar la persistencia de los JupytersHub
6. En los nodos e instancias del Cluster vamos a cambiar las maquinas por defecto y colocamos las maquinas en m4.xlarge  y lo colocamos en Spot
7. Activamos la autoterminacion despues de una hora de no usarse.
8. En security options seleccionamos el par de llaves previamente creadas.
9. Le damos en crear cluster.

**Aclaraciones:**

El cluster se demora entre 20 y 30 minutos en ser creado.