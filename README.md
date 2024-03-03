
# GoodReads Data Cleaning Project

This project focuses on cleaning and preparing a dataset obtained from GoodReads for further analysis. The notebook demonstrates various data cleaning techniques using Python libraries such as Pandas and NumPy.

## Setup

To run this notebook, ensure you have the following Python libraries installed:

- NumPy
- Pandas

You can install these packages using pip:

```bash
pip install numpy pandas
```

## Suppressing Warnings

During the execution, warnings from different packages are suppressed to keep the notebook cleaner and more readable.

## Pandas Display Settings

The notebook adjusts Pandas display settings to show all rows and columns, ensuring that the entire dataset is visible when printed. It also sets the precision for floating-point numbers to improve readability.

## Dataset

The dataset used in this project is a CSV file containing information about books collected from GoodReads. The path to the dataset is specified when loading it into a Pandas DataFrame:

```python
df = pd.read_csv("path/to/your/books.csv")
```

Replace `"path/to/your/books.csv"` with the actual path to the dataset on your machine.

## Data Cleaning Process

The notebook covers several data cleaning steps, including but not limited to:

- Handling missing values
- Removing duplicates
- Standardizing data formats
- Correcting data types

Each step is thoroughly explained and demonstrated using Pandas functions and methods.
