# Data Quality Validation Framework

## Overview

This project is a Python-based Data Quality Validation Framework that validates healthcare claims data before it is loaded into downstream systems. It performs common data quality checks such as null validation, duplicate detection, invalid date detection, and negative amount validation while generating reports and logs.

---

## Project Architecture

```
CSV File
    │
    ▼
Extract Data
    │
    ▼
Data Validation
    │
    ├── Null Check
    ├── Duplicate Check
    ├── Invalid Date Check
    └── Negative Amount Check
    │
    ▼
Quality Report
    │
    ▼
Logging
```

---

## Project Structure

```
DE-Project-04-Data-Quality-Validation-Framework
│
├── Data
│   └── claims.csv
│
├── Output
│   ├── Quality_Report.txt
│   └── dq.log
│
├── SRC
│   ├── extract.py
│   ├── validate.py
│   ├── report.py
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

- Read healthcare claims data from CSV
- Detect missing values
- Identify duplicate records
- Validate date fields
- Detect negative claim amounts
- Generate a Data Quality Report
- Generate application logs
- Calculate Data Quality Score
- PASS / FAIL validation status

---

## Technologies Used

- Python
- Pandas
- Logging
- CSV
- File Handling

---

## Validation Rules

| Validation | Description |
|------------|-------------|
| Null Check | Detect missing values |
| Duplicate Check | Detect duplicate records |
| Invalid Date Check | Validate date format |
| Negative Amount Check | Detect negative claim amounts |

---

## Sample Output

```
Quality Report Generated Successfully

Total Records : 10

Null Values : 2

Duplicate Rows : 1

Invalid Dates : 2

Negative Claim Amounts : 2

DQ Score : 82.5

Status : FAIL
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/VenomPavan/DE-Project-04-Data-Quality-Validation-Framework.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
cd SRC
python main.py
```

---

## Future Improvements

- HTML Data Quality Report
- Email Notifications
- Database Integration
- Great Expectations Integration
- Apache Airflow Scheduling

---

## Author

**Pavan Teja**