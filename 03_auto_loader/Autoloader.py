# Databricks notebook source
# MAGIC %md
# MAGIC #AUTOLOADER

# COMMAND ----------

# MAGIC %md
# MAGIC **STREAMING DATAFRAME**

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df=spark.readStream.format('cloudFiles')\
    .option("cloudFiles.format", "parquet")\
    .option("cloudFiles.schemaLocation", "abfss://source@unitycatalogneha.dfs.core.windows.net/autosink/check")\
    .load('abfss://source@unitycatalogneha.dfs.core.windows.net/autosource')
    

# COMMAND ----------

df.writeStream.format('parquet')\
    .option("checkpointLocation", "abfss://source@unitycatalogneha.dfs.core.windows.net/autosink/check")\
    .trigger(processingTime='10 seconds')\
    .start('abfss://source@unitycatalogneha.dfs.core.windows.net/autosink/data')