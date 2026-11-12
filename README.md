# Databricks Unity Catalog, Delta Lake & Auto Loader

A collection of hands-on **Databricks notebook exports** demonstrating Unity Catalog organization, managed and external Delta tables, schemas and storage locations, views, volumes, Delta Lake operations, and streaming ingestion with Auto Loader.

The original notebook contents are preserved unchanged. Files are organized by topic to make the project easy to navigate.

## Technology stack

- **Databricks and Unity Catalog**
- **Databricks SQL and Delta Lake**
- **PySpark and Structured Streaming**
- **Databricks Auto Loader** (`cloudFiles`)
- **Azure Data Lake Storage Gen2** (ABFSS paths)

## Repository structure

```text
unity-catalog/
├── README.md
├── 01_unity_catalog/
│   └── scenarios.py
├── 02_delta_lake/
│   └── delttutorial.py
├── 03_auto_loader/
│   └── Autoloader.py
└── 04_basic_notebooks/
    ├── Notebook 1.py
    └── Notebook 2.py
```

## Notebook guide

| Notebook | What it demonstrates |
| --- | --- |
| [`scenarios.py`](01_unity_catalog/scenarios.py) | Catalog and schema creation; managed/external Delta tables; drop/undrop; views; volumes; querying storage paths |
| [`delttutorial.py`](02_delta_lake/delttutorial.py) | Delta table creation, updates, history, restore, deletion-vector settings, `OPTIMIZE`, deep and shallow cloning |
| [`Autoloader.py`](03_auto_loader/Autoloader.py) | Streaming Parquet ingestion using Databricks Auto Loader, ADLS Gen2 and a checkpoint |
| [`Notebook 1.py`](04_basic_notebooks/Notebook%201.py) | Introductory Hello World example |
| [`Notebook 2.py`](04_basic_notebooks/Notebook%202.py) | Introductory Python print example |

## 1. Unity Catalog scenarios

The `scenarios.py` notebook explores:

- Creating catalogs with specified managed storage locations.
- Creating schemas and managed Delta tables.
- Defining an external table at an explicit ADLS Gen2 location.
- Dropping and undropping a managed table.
- Querying the Delta data at its storage path.
- Creating permanent and temporary views.
- Creating an external volume, copying a file and querying its contents.

## 2. Delta Lake operations

The `delttutorial.py` notebook demonstrates:

- Creating a Delta table using `LOCATION`.
- Inserting and updating records.
- Viewing extended table metadata and history.
- Restoring an earlier table version.
- Configuring deletion-vector behavior.
- Running `OPTIMIZE`.
- Exploring deep and shallow table clones.

## 3. Auto Loader ingestion

The `Autoloader.py` notebook defines a Structured Streaming ingestion flow using `cloudFiles` with Parquet input:

```text
ADLS Gen2 source folder
         |
         v
Databricks Auto Loader (cloudFiles)
         |
         v
Spark streaming DataFrame
         |
         v
ADLS Gen2 Parquet output + checkpoint
```

The notebook specifies a 10-second processing-time trigger and environment-specific ADLS Gen2 paths. The code is included as exported; no new streaming execution was performed during this GitHub portfolio organization.

## Using the notebooks

These `.py` files are **Databricks notebook exports**. They include notebook cell markers such as `# COMMAND ----------` and magic cell prefixes such as `# MAGIC %sql`. Import them into a Databricks workspace to use the cells.

The original notebooks reference catalogs including `managed_catalog1` and `ext_cat`, and storage paths from the original Azure environment. Reproducing the examples requires appropriate Unity Catalog permissions, configured storage access and environment-specific paths.

**Scope:** This is a collection of learning and implementation examples, not a single packaged production application. The notebooks' code and contents were not changed, and runtime behavior has not been independently verified.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
