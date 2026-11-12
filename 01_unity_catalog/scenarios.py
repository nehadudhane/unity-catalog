# Databricks notebook source
# MAGIC %sql
# MAGIC show catalogs;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scenario 1
# MAGIC **Managed Catalog**
# MAGIC **Managed Schema**
# MAGIC **Managed Table**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Managed Catalog**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE CATALOG managed_catalog1
# MAGIC MANAGED LOCATION
# MAGIC 'abfss://destination@unitycatalogneha.dfs.core.windows.net/man_cata';

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema managed_catalog1.man_schema1

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists managed_catalog1.man_schema1.man_table1
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog ext_cat
# MAGIC managed location 'abfss://source@unitycatalogneha.dfs.core.windows.net/external_catalog';

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema ext_cat.man_schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists ext_cat.man_schema.man_table2
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta

# COMMAND ----------

# MAGIC %md 
# MAGIC ## external schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema ext_cat.ext_schema
# MAGIC managed location 'abfss://source@unitycatalogneha.dfs.core.windows.net/ext_schema';
# MAGIC     
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists ext_cat.ext_schema.man_table3
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta

# COMMAND ----------

# MAGIC %md
# MAGIC ## external table

# COMMAND ----------

# MAGIC %sql
# MAGIC create table managed_catalog1.man_schema1.ext_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta
# MAGIC location 'abfss://source@unitycatalogneha.dfs.core.windows.net/ext_table/man_table3'

# COMMAND ----------

# MAGIC %md
# MAGIC ## drop managed table

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE managed_catalog1.man_schema1.man_table1;

# COMMAND ----------

# MAGIC %md
# MAGIC ## undrop managed table

# COMMAND ----------

# MAGIC %sql
# MAGIC  undrop table managed_catalog1.man_schema1.man_table1;
# MAGIC     

# COMMAND ----------

# MAGIC %md
# MAGIC ### querying files

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_catalog1.man_schema1.ext_table values
# MAGIC (1, 'Neha'),
# MAGIC (2, 'Dudhane'),
# MAGIC (3, 'Tedx Speaker')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog1.man_schema1.ext_table

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`abfss://source@unitycatalogneha.dfs.core.windows.net/ext_table/man_table3`

# COMMAND ----------

# MAGIC %md
# MAGIC ###Permanent views

# COMMAND ----------

# MAGIC %sql
# MAGIC create view managed_catalog1.man_schema1.view
# MAGIC as
# MAGIC select * from delta.`abfss://source@unitycatalogneha.dfs.core.windows.net/ext_table/man_table3` where id=1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog1.man_schema1.view

# COMMAND ----------

# MAGIC %md
# MAGIC ### temp views
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view temp_view
# MAGIC as
# MAGIC select * from delta.`abfss://source@unitycatalogneha.dfs.core.windows.net/ext_table/man_table3` where id=1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from temp_view

# COMMAND ----------

# MAGIC %md
# MAGIC #Volumes

# COMMAND ----------

# MAGIC %md
# MAGIC **creating a directory for volume**

# COMMAND ----------

dbutils.fs.mkdirs('abfss://source@unitycatalogneha.dfs.core.windows.net/volumes')

# COMMAND ----------

# MAGIC %md
# MAGIC **creating a volume**

# COMMAND ----------

# MAGIC %sql
# MAGIC drop volume managed_catalog1.man_schema1.myvolumeext
# MAGIC --create volume managed_catalog1.man_schema1.myvolumeext

# COMMAND ----------

# MAGIC %sql
# MAGIC create external volume managed_catalog1.man_schema1.extvolume
# MAGIC location 'abfss://source@unitycatalogneha.dfs.core.windows.net/volumes'

# COMMAND ----------

# MAGIC %md
# MAGIC **copy file for volume**

# COMMAND ----------

# MAGIC %md
# MAGIC **copyfile for volume**

# COMMAND ----------

dbutils.fs.cp('abfss://source@unitycatalogneha.dfs.core.windows.net/volumesource/Sales.txt', 'abfss://source@unitycatalogneha.dfs.core.windows.net/volumes/Sales')  

# COMMAND ----------

# MAGIC %md
# MAGIC **querying volume**

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`/Volumes/managed_catalog1/man_schema1/extvolume/Sales`