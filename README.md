# 💳 Credit Card Fraud Detection  

## 📌 Project Overview  
This project focuses on detecting **fraudulent credit card transactions** using Machine Learning techniques.  
Credit card fraud is a major concern in the financial industry due to its rarity and high financial risk.  
The dataset is highly **imbalanced** (fraud cases represent only 0.17% of all transactions), making it a challenging **anomaly detection problem**.  

The goal is to build a robust model that can identify fraudulent transactions with high precision and recall while minimizing false positives.  

---

## 📂 Dataset  
- **Source**: [Kaggle – Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
- **Transactions**: 284,807  
- **Fraudulent Cases**: 492  
- **Features**:  
  - PCA-transformed numerical features (V1, V2, …, V28)  
  - `Amount` → Transaction amount  
  - `Class` → Target variable (0 = Legitimate, 1 = Fraud)  

---

## ⚙️ Features of the Project  
- **Data Preprocessing**  
  - Normalization & feature scaling  
  - Handling missing/imbalanced data  
- **Techniques for Imbalanced Data**  
  - SMOTE (Synthetic Minority Oversampling)  
  - Random undersampling  
  - Class weight adjustments  
- **Machine Learning Models**  
  - Logistic Regression  
  - Decision Trees  
  - Random Forest  
  - Gradient Boosting (XGBoost/LightGBM)  
- **Anomaly Detection Models**  
  - Isolation Forest  
  - Local Outlier Factor  
- **Evaluation Metrics**  
  - Precision, Recall, F1-score  
  - Confusion Matrix  
  - ROC-AUC curve & PR curve  

