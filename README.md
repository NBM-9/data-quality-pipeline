# Data Quality Pipeline (End-to-End Data Engineering Project)

## 📌 Project Overview
This project demonstrates an end-to-end data engineering pipeline that extracts data from a REST API, performs data quality checks, transforms the data using Python, and loads it into a SQLite database for analytics.

The goal is to simulate a real-world data engineering workflow focusing on data validation and reliability.

---

## 🏗️ Architecture
API → Data Extraction → Data Quality Checks → Data Cleaning → Database Storage

---

## ⚙️ Tech Stack
- Python
- Pandas
- Requests
- SQLite
- REST API

---

## 🔄 Workflow Steps

### 1. Data Extraction
- Fetched user data from a public REST API:
  https://jsonplaceholder.typicode.com/users

### 2. Data Transformation
- Converted JSON data into structured tabular format using Pandas

### 3. Data Quality Checks
- Checked for missing values
- Identified duplicate records
- Validated data structure

### 4. Data Cleaning
- Removed duplicate records
- Ensured clean dataset for storage

### 5. Data Storage
- Stored cleaned data into SQLite database (`users.db`)

---

## 📊 Key Features
- End-to-end ETL pipeline
- Automated data quality validation
- Structured data transformation
- Database integration using SQLite

---

## 🚀 How to Run

```bash
pip install pandas requests
python pipeline.py
