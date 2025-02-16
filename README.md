# ❤️ Heart Disease Prediction Dataset

Welcome to the **Heart Disease Prediction Dataset** repository! This dataset contains medical attributes that can help in predicting the presence of heart disease. It is useful for researchers, data scientists, and healthcare professionals working on cardiovascular disease prediction models.

---

## 📂 Dataset Overview

- **Filename**: `heart.csv`
- **Format**: CSV (Comma-Separated Values)
- **Size**: Contains multiple records of patient data
- **Purpose**: Used for machine learning models to predict heart disease

---

## 📊 Features & Column Descriptions

| Column Name      | Description                                  |
|-----------------|----------------------------------------------|
| `age`           | Age of the patient                          |
| `sex`           | Gender (1 = Male, 0 = Female)              |
| `cp`            | Chest Pain Type (Categorical: 0-3)         |
| `trestbps`      | Resting Blood Pressure (mm Hg)             |
| `chol`          | Serum Cholesterol (mg/dL)                  |
| `fbs`           | Fasting Blood Sugar (> 120 mg/dL, 1 = True, 0 = False) |
| `restecg`       | Resting Electrocardiographic Results (0-2) |
| `thalach`       | Maximum Heart Rate Achieved                |
| `exang`         | Exercise-Induced Angina (1 = Yes, 0 = No)  |
| `oldpeak`       | ST Depression Induced by Exercise          |
| `slope`         | Slope of Peak Exercise ST Segment (0-2)    |
| `ca`            | Number of Major Vessels (0-3)              |
| `thal`          | Thalassemia (0-3)                          |
| `target`        | Presence of Heart Disease (1 = Yes, 0 = No) |

---

## 🛠️ Usage Instructions

1. **Load the dataset in Python**:
   ```python
   import pandas as pd
   df = pd.read_csv("heart.csv")
   print(df.head())
   ```

2. **Perform Exploratory Data Analysis (EDA)**:
   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt
   
   sns.pairplot(df, hue='target')
   plt.show()
   ```

3. **Train a Machine Learning Model**:
   ```python
   from sklearn.model_selection import train_test_split
   from sklearn.ensemble import RandomForestClassifier
   from sklearn.metrics import accuracy_score
   
   X = df.drop('target', axis=1)
   y = df['target']
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   model = RandomForestClassifier()
   model.fit(X_train, y_train)
   predictions = model.predict(X_test)
   
   print("Accuracy:", accuracy_score(y_test, predictions))
   ```

---

## 🎯 Applications

- Heart Disease Prediction Models 🏥
- Medical Research & Data Analysis 🔬
- Machine Learning & AI Development 🤖
- Academic Projects & Tutorials 📚

---

## 📜 License

This dataset is free to use for research and educational purposes. However, always cite the source if using it in publications.

---

## 👥 Contributors

- **Surya K** (surya.tvm.apm@gmail.com)
- Open to Contributions! 🚀

For any questions or contributions, feel free to open an issue or submit a pull request. Enjoy analyzing! 🎉

