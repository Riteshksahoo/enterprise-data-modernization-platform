# Enterprise Data Modernization Platform

## Project Overview

This project demonstrates an end-to-end modern data engineering workflow using Snowflake, Snowpark, Python, JSON, and BI tools.

The platform ingests structured and semi-structured data, performs transformations using Snowflake ELT patterns, and prepares curated datasets for analytics and reporting.

---

## Architecture

Raw Data Sources

* Superstore Dataset (Excel)
* Marketing Events (JSON)

↓

Python Data Processing

* Dataset Generation
* CSV Creation
* JSON Creation

↓

Snowflake Ingestion

* Internal Stage
* File Formats
* COPY INTO

↓

Raw Layer

* SALES_RAW
* CUSTOMERS_RAW
* PRODUCTS_RAW
* INVENTORY_RAW
* STORE_EVENTS_RAW

↓

Transformation Layer

* SALES_CURATED
* EVENT_PRODUCTS_CURATED

↓

Automation

* Stored Procedures
* Streams
* Tasks

↓

Analytics Layer (Upcoming)

* Snowpark Transformations
* KPI Tables
* Business Metrics

↓

Visualization

* Power BI
* Streamlit

---

## Technologies Used

* Python
* Pandas
* Snowflake
* Snowpark
* SQL
* JSON
* Git
* GitHub
* Power BI
* Streamlit

---

## Project Structure

enterprise-data-modernization-platform/

├── data/
│   ├── raw/
│   ├── processed/
│   └── json/
│
├── scripts/
│   └── dataset_generator.py
│
├── sql/
│   ├── ingestion/
│   ├── procedures/
│   ├── streams/
│   ├── tasks/
│   └── json/
│
├── snowpark/
├── streamlit/
├── powerbi/
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Features Implemented

### Structured Data Pipeline

* Loaded CSV files into Snowflake
* Created Internal Stages
* Created File Formats
* Used COPY INTO for ingestion
* Built RAW data layer
* Created curated business tables

### Snowflake Automation

* Stored Procedures
* Streams
* Tasks
* Automated data refresh workflow

### Semi-Structured Data Processing

* Loaded JSON into VARIANT columns
* Queried JSON attributes
* Used LATERAL FLATTEN
* Converted nested arrays into relational tables

---

## Sample Datasets

### CSV Files

* sales.csv
* customers.csv
* products.csv
* inventory.csv

### JSON File

* store_events.json

Contains promotional campaign information and product discounts.

---

## Snowflake Concepts Demonstrated

* Database & Schema Design
* Internal Stages
* File Formats
* COPY INTO
* Stored Procedures
* Streams
* Tasks
* VARIANT Data Type
* LATERAL FLATTEN
* ELT Architecture

---

## Current Status

Completed:

* Data Generation
* Snowflake Ingestion
* ELT Pipeline
* JSON Processing
* Stream & Task Automation

In Progress:

* Snowpark
* Analytics Layer
* Streamlit Dashboard
* Power BI Dashboard

---

## Author

Ritesh Sahoo

GitHub:

