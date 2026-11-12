# Databricks notebook source
# MAGIC %md
# MAGIC #  DELTA TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE table managed_catalog1.man_schema1.deltatbl
# MAGIC (
# MAGIC     id int,
# MAGIC     name STRING,
# MAGIC     city string
# MAGIC )
# MAGIC using delta
# MAGIC LOCATION 'abfss://deltalake@unitycatalogneha.dfs.core.windows.net/deltatbl'

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table managed_catalog1.man_schema1.deltatbl set tblproperties('delta.enableDeletionVectors'=false);

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_catalog1.man_schema1.deltatbl values 
# MAGIC (1,'aa','mumbai'),
# MAGIC (2,'bb','delhi'),
# MAGIC (3,'cc','london')

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended managed_catalog1.man_schema1.deltatbl

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog1.man_schema1.deltatbl

# COMMAND ----------

# MAGIC %md
# MAGIC **update**
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC update managed_catalog1.man_schema1.deltatbl
# MAGIC set city ='paris' where id=2

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history managed_catalog1.man_schema1.deltatbl

# COMMAND ----------

# MAGIC %md
# MAGIC **time travel**
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC restore managed_catalog1.man_schema1.deltatbl to version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog1.man_schema1.deltatbl

# COMMAND ----------

# MAGIC %md
# MAGIC **DELETION VECTOR**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE table managed_catalog1.man_schema1.deltatb2
# MAGIC (
# MAGIC     id int,
# MAGIC     name STRING,
# MAGIC     city string
# MAGIC )
# MAGIC using delta
# MAGIC LOCATION 'abfss://deltalake@unitycatalogneha.dfs.core.windows.net/deltatb2'

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_catalog1.man_schema1.deltatb2 values 
# MAGIC (1,'aa','mumbai'),
# MAGIC (2,'bb','delhi'),
# MAGIC (3,'cc','london')

# COMMAND ----------

# MAGIC %sql
# MAGIC update managed_catalog1.man_schema1.deltatb2
# MAGIC set city ='Seattle' where id=2

# COMMAND ----------

# MAGIC %md
# MAGIC # OPTIMIZATION

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE managed_catalog1.man_schema1.deltatb2 

# COMMAND ----------

# MAGIC %md
# MAGIC **DEEP CLONE AND SHALLOW TABLE**

# COMMAND ----------

# MAGIC %sql
# MAGIC create table managed_catalog1.man_schema1.deepclonetb1
# MAGIC deep clone managed_catalog1.man_schema1.deltatbl

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog1.man_schema1.deepclonetb1

# COMMAND ----------

# MAGIC %sql
# MAGIC create table managed_catalog1.man_schema1.shallowtb1
# MAGIC shallow clone managed_catalog1.man_schema1.man_table1

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended managed_catalog1.man_schema1.man_table1

# COMMAND ----------

