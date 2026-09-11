# 📊 Task 1: Data Immersion & Wrangling

## 📌 Overview
This repository contains the completion of **Task 1: Data Immersion & Wrangling** for the Data Analytics Internship at **ApexPlanet Software Pvt. Ltd.**.

The primary goal of this task is to perform an end-to-end data cleaning, quality assessment, and feature engineering process on the **E-Commerce Online Retail Dataset** to prepare an analysis-ready dataset.

---

## 🛠️ Data Quality Assessment & Identification
During the initial exploration of the raw dataset (`online_retail.csv` with 541,909 records), the following key data issues were identified:
1. **Missing Values:** 135,080 missing values in `CustomerID` and 1,454 in `Description`.
2. **Duplicate Records:** 5,268 exact duplicate transaction lines.
3. **Anomalies / Cancelled Orders:** Negative values in `Quantity` and `UnitPrice` representing returns, adjustments, or cancellations (Invoices starting with 'C').

---

## 🧹 Data Cleaning & Transformation Steps
To fix these issues, a Python automation script (`data_cleaning.py`) using **Pandas** was developed:
* **Duplicate Removal:** Removed 5,268 exact duplicate rows.
* **Missing Value Handling:** Dropped records with null `CustomerID` values as customer tracking is vital for downstream analysis.
* **Filter Out Negative/Invalid Values:** Filtered the dataset to retain only positive `Quantity` (> 0) and `UnitPrice` (> 0).
* **Data Type Conversions:** 
  * Converted `CustomerID` from float to string (integer representation without decimal).
  * Standardized `InvoiceDate` to proper Datetime format.
* **Feature Engineering:**
  * **`TotalAmount`**: Created a calculated column (`Quantity * UnitPrice`) to capture transaction revenue.
  * **`InvoiceYearMonth`**: Extracted period (`YYYY-MM`) for monthly trend analysis.
  * **`DayOfWeek`**: Derived weekday name for weekly pattern detection.
  * **`Hour`**: Extracted the hour of transaction for daily peak-time analysis.

---

## 📈 Summary Statistics
* **Raw Records:** 541,909
* **Cleaned Records:** 392,692
* **Removed Records:** 149,217 (Missing IDs, Duplicates, and Cancellations/Adjustments)

---
