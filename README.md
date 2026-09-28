# Student Performance Analyzer

A beginner-friendly data analysis project built using **Python, NumPy, and Pandas** to analyze student academic performance.

## Project Overview

The Student Performance Analyzer processes student marks and generates useful insights such as total marks, average marks, grades, rankings, subject performance, and overall class statistics.

This project was created to practice and strengthen fundamental **NumPy and Pandas** concepts through a practical data analysis application.

## Features

* Load student data from a CSV file
* Display dataset shape and column information
* Calculate total marks
* Calculate average marks
* Assign grades based on average marks
* Determine Pass/Fail status
* Categorize student performance
* Find the highest-performing student
* Find the lowest-performing student
* Display the Top 5 students
* Calculate subject-wise averages
* Identify the best and worst-performing subjects
* Display grade distribution
* Display Pass/Fail distribution
* Identify students needing improvement
* Analyze subject performance by grade
* Count students failing each subject
* Rank students based on average marks
* Generate an overall class performance summary

## Technologies Used

* **Python**
* **NumPy**
* **Pandas**

## Dataset

The project uses a CSV file named:

```text
new_data.csv
```

The dataset contains student information and marks for:

* Math
* Python
* DBMS
* English

The project also calculates additional columns such as:

* `Total2`
* `Average`
* `Grade`
* `Result`
* `Category`
* `Rank`

> `Total2` is intentionally calculated separately because the original CSV already contains a `Total` column. It was added for practicing Pandas calculations.

## Concepts Practiced

### NumPy

* `np.where()`
* `np.select()`

### Pandas

* `pd.read_csv()`
* `DataFrame.shape`
* `DataFrame.columns`
* `DataFrame.head()`
* Column selection
* Boolean filtering
* `sum()`
* `mean()`
* `max()`
* `min()`
* `idxmax()`
* `idxmin()`
* `sort_values()`
* `value_counts()`
* `groupby()`
* `rank()`
* `.loc[]`

## Project Workflow

```text
CSV Dataset
     ↓
Load Data
     ↓
Inspect Dataset
     ↓
Calculate Total & Average
     ↓
Assign Grades
     ↓
Determine Pass/Fail
     ↓
Categorize Performance
     ↓
Rank Students
     ↓
Analyze Subjects
     ↓
Generate Performance Summary
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/harshakr7/student_performance_analyser.git
```

### 2. Navigate to the project directory

```bash
cd student_performance_analyser
```

### 3. Install required libraries

```bash
pip install numpy pandas
```

### 4. Run the program

```bash
python main.py
```

## Example Analysis

The program provides information such as:

```text
Top Student
Lowest Performing Student
Top 5 Students
Subject Averages
Grade Distribution
Result Distribution
Students Needing Improvement
Subject Failure Count
Class Average
Highest Average
Lowest Average
Pass Percentage
```

## Learning Outcome

Through this project, I practiced how to:

* Work with CSV datasets
* Manipulate DataFrames
* Perform numerical calculations using NumPy and Pandas
* Filter and sort data
* Group data and perform aggregations
* Extract useful information from datasets
* Build a complete beginner-level data analysis workflow

## Future Improvements

Possible future improvements include:

* Add data visualization using Matplotlib
* Create charts for subject-wise performance
* Add interactive dashboards
* Handle missing values automatically
* Add more student performance metrics

## Author

**Harsha**

B.Tech Computer Science Engineering Student

---

⭐ This project was built as part of my journey toward strengthening my **Python, NumPy, Pandas, and Data Analytics** skills.
