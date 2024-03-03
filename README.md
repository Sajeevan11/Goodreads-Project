
# GoodReads EDA & Feature Engineering Project

This project delves into Exploratory Data Analysis (EDA) and feature engineering using a cleaned GoodReads dataset. The notebook showcases various techniques to analyze the data and prepare it for modeling.

## Setup

Ensure the following Python libraries are installed to run this notebook:

- NumPy
- Pandas
- Matplotlib
- Seaborn

Install these packages using pip if you haven't already:

```bash
pip install numpy pandas matplotlib seaborn
```

## Suppressing Warnings

Warnings from different packages are suppressed to maintain the readability of the notebook.

## Pandas Display Settings

The display settings for Pandas are adjusted to ensure all data is visible when displayed, and floating-point numbers are formatted for better readability.

## Dataset

The dataset, `books_cleaned.csv`, is a version of the GoodReads books dataset that has been previously cleaned. It is loaded into a Pandas DataFrame at the beginning of the notebook:

```python
df = pd.read_csv("path/to/your/books_cleaned.csv")
```

Replace `"path/to/your/books_cleaned.csv"` with the actual path to the cleaned dataset on your machine.

## EDA and Feature Engineering Process

The notebook explores the dataset through visualizations and statistical analyses to understand the data's characteristics, distribution, and relationships between features. It also covers the creation and transformation of features to better suit predictive modeling.

The process includes:

- Visualizing distributions and relationships between variables
- Analyzing trends and patterns in the data
- Creating new features based on the existing data
- Transforming features to improve model performance

Each step is explained and demonstrated using Python libraries tailored for data analysis and visualization.
