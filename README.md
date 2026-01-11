# Student Performance Analysis with Pandas

## Overview
This project is a redo of a previous student performance analysis using pandas. The goal is to practice core pandas skills including data cleaning, feature engineering, aggregation, and grouped statistics. This is my first hands-on project after a break, providing a structured approach to working with real datasets.  

## Dataset
The dataset contains student demographics and exam scores:  

- **gender**  
- **race/ethnicity**  
- **parental level of education**  
- **lunch** (standard or free/reduced)  
- **test preparation course** (completed or none)  
- **math score**  
- **reading score**  
- **writing score**  

## Features Implemented
1. **Structural Audit**
   - Inspect column types, missing values, and score ranges.  

2. **Target Construction**
   - Create `total_score`, `average_score`, and `passed_all` columns.  

3. **Univariate Analysis**
   - Compute mean, median, std, percentiles, and detect outliers.  

4. **Grouped Performance Analysis**
   - Aggregate scores by gender, race/ethnicity, parental education, lunch, and test preparation.  
   - Rank groups and calculate score gaps.  

## Future Work
- Conditional comparisons (test preparation effects)  
- Multidimensional aggregation (pivot tables)  
- Correlation analysis between subjects  
- Ranking top and bottom performers  
- Inequality indicators by demographic variables  

## How to Use
1. Clone the repository:  
  ```bash
  git clone https://github.com/cotenthusiast/students-dataset-pandas.git
  ```

2. Install dependencies
  ```bash
  pip install pandas
  ```

## Learning Goals

- Practice pandas aggregation, grouping, and feature engineering.
- Rebuild a past project with structured code.
- Prepare for more advanced data analysis projects.