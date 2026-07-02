# 🍽️ Zomato Data Cleaning using Python & Pandas

A data preprocessing project that cleans the Zomato restaurant dataset using **Python**, **Pandas**, and **NumPy**. The cleaned dataset is exported as a new CSV file, making it suitable for data analysis, visualization, and machine learning applications.

---

## 📌 Project Overview

Raw datasets often contain unnecessary columns, inconsistent data types, and missing or improperly formatted values. This project demonstrates a complete data cleaning workflow on the Zomato restaurant dataset.

The notebook performs:

- Removing irrelevant columns
- Cleaning restaurant ratings
- Handling missing values
- Converting data types
- Exporting a cleaned dataset

The final output is a clean and structured dataset ready for further analysis.

---

## 📂 Project Structure

```text
.
├── Zomato_Data_Cleaning.ipynb
├── zomato.csv
├── zomato_cleaned.csv
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Jupyter Notebook

---

## 📋 Data Cleaning Steps

### 1. Import Required Libraries

```python
import pandas as pd
import numpy as np
```

### 2. Load Dataset

```python
df = pd.read_csv("zomato.csv")
```

### 3. Remove Unnecessary Columns

Removes columns such as:
- url
- address
- reviews_list
- phone

### 4. Clean Restaurant Ratings

Converts values like:

| Original | Converted |
|----------|-----------|
| 4.2/5 | 4.2 |
| NEW | NaN |
| - | NaN |

into numeric values for analysis.

### 5. Convert Data Types

Converts categorical columns to consistent string datatypes.

### 6. Inspect Dataset

```python
df.info()
```

### 7. Export Cleaned Dataset

```python
df.to_csv("zomato_cleaned.csv", index=False)
```

---

## 📊 Dataset

The dataset contains restaurant information including:

- Restaurant Name
- Location
- Rating
- Online Ordering
- Table Booking
- Cuisine
- Restaurant Type
- Votes
- Approximate Cost

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/zomato-data-cleaning.git
cd zomato-data-cleaning
pip install pandas numpy
```

Open `Zomato_Data_Cleaning.ipynb` in Jupyter Notebook or Google Colab.

---

## 📈 Future Improvements

- Handle missing values
- Remove duplicates
- Perform EDA
- Create visualizations
- Build ML models

---

## 🎯 Learning Outcomes

- Data Cleaning
- Data Preprocessing
- Pandas
- Real-world Dataset Handling

---

## 🤝 Contributing

Contributions are welcome through pull requests.

---

## 📜 License

This project is intended for educational purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
