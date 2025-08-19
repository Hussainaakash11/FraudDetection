# Fraud Detection Case Study

This repository contains a **fraud detection analysis** performed on a financial transactions dataset.  
The dataset simulates 30 days of customer transactions, including normal activity and fraudulent behavior, with the objective of building models to detect fraudulent transactions.

---

## 📌 Dataset Description

Each transaction in the dataset is represented with the following fields:

- **step**: Unit of time (1 step = 1 hour, total 744 steps for 30 days).
- **type**: Transaction type (CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER).
- **amount**: Transaction amount in local currency.
- **nameOrig**: Customer who initiated the transaction.
- **oldbalanceOrg**: Initial balance before the transaction.
- **newbalanceOrig**: New balance after the transaction.
- **nameDest**: Recipient of the transaction.
- **oldbalanceDest**: Initial balance of recipient before the transaction (NaN for merchants).
- **newbalanceDest**: New balance of recipient after the transaction (NaN for merchants).
- **isFraud**: `1` if the transaction was fraudulent, `0` otherwise.
- **isFlaggedFraud**: `1` if the transaction was flagged for exceeding 200,000 in a single transfer.

---

## 🎯 Objectives

- Explore and understand the dataset through **EDA** (Exploratory Data Analysis).
- Identify **patterns of fraudulent behavior**.
- Preprocess data for machine learning models.
- Train and evaluate classification models to **predict fraudulent transactions**.
- Derive actionable insights for fraud prevention.

---

## 🔎 Exploratory Data Analysis (EDA)

The notebook includes detailed EDA with markdown explanations and Q&A. Key steps include:

- Distribution of transaction types.
- Fraud vs non-fraud transaction analysis.
- Class imbalance visualization.
- Correlation of features with fraud.

---

## 🤖 Machine Learning Workflow

1. **Preprocessing**
   - Handling missing values.
   - Feature encoding.
   - Scaling numeric values.
   - Train-test split.

2. **Modeling**
   - Logistic Regression
   - Random Forest
   - XGBoost (if available)

3. **Evaluation Metrics**
   - Accuracy
   - Precision, Recall, F1-score
   - Confusion Matrix
   - ROC-AUC Score

---

## 📊 Key Insights

- Fraudulent transactions occur mainly in **CASH-OUT** and **TRANSFER** types.
- Transactions involving **merchants (M\*)** do not have balance details.
- Fraudulent cases are **highly imbalanced** compared to normal transactions.
- Precision and Recall are critical to minimize false alarms and missed frauds.

---

---

## 💡 Example Questions & Answers

**Q: Why do we focus on class imbalance?**  
A: Fraudulent transactions are rare compared to normal transactions. Without addressing imbalance, models will be biased towards predicting "non-fraud".  

**Q: Which transaction types are most associated with fraud?**  
A: Most fraud occurs in **TRANSFER** and **CASH-OUT** transactions, where attackers attempt to move or withdraw money.  

**Q: How can flagged fraud differ from actual fraud?**  
A: Flagged fraud only checks if a transaction exceeds 200,000, but actual fraud may occur with smaller amounts that bypass this rule.

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fraud-detection-case-study.git


## Install Dependencies
pip install -r requirements.txt



