# Project-E-commerce-Business-Transaction-and-Crypto-Analysis

## Data Source
Dataset available at:
https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business


# 📊 E-commerce & Cryptocurrency Analysis Project

## 📌 Project Overview

This project analyzes e-commerce transaction data alongside cryptocurrency market data to uncover patterns in customer behavior, pricing dynamics, product performance, and financial volatility.

The analysis is structured around key business questions and is supported by exploratory data analysis, statistical testing, and interactive visualizations built using Streamlit.

---

## 🎯 Objectives

The project aims to:

- Evaluate the relationship between price and quantity sold  
- Understand customer purchasing behavior  
- Identify top-performing products  
- Analyze sales trends over time  
- Compare volatility across cryptocurrency assets  
- Visualize global revenue distribution  

---

## 🧠 Research Questions

1. Does price influence quantity sold?  
2. Do repeat customers spend more?  
3. Which products are most profitable?  
4. How do sales trends evolve over time?  
5. How does cryptocurrency volatility differ across assets?  

---

## 📁 Project Structure

```plaintext
Project-E-commerce-Business-Transaction-and-Crypto-Analysis/
│
├── Data/
│   ├── Raw/
│   └── Cleaned/
│
├── Notebooks/
│   ├── 1_inspection.ipynb
│   ├── 2_cleaning_&_transformation.ipynb
│   ├── 3_eda_and_analytics.ipynb
│   └── API_data_collection_and_cleaning.ipynb
│
├── Presentations/
│   └── Link.md
│
├── app/
│   ├── app.py
│   ├── clean_ecommerce_data.csv.gz
│   ├── crypto_data_API.csv
│   ├── requirements.txt
│
└── README.md
```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

    git clone https://github.com/Dee-M123/Project-E-commerce-Business-Transaction-and-Crypto-Analysis.git
    cd Project-E-commerce-Business-Transaction-and-Crypto-Analysis

### 2. Install Dependencies

    pip install -r app/requirements.txt

### 3. Run the Streamlit App

    streamlit run app/app.py

### 4. Access the App

Open your browser and go to:

    http://localhost:8501

---

## 📊 Methodology

### Data Processing

- Data cleaning and preprocessing performed in notebooks  
- Outliers removed for accurate statistical analysis  
- Aggregations performed for time series and product-level insights  

### Analysis Techniques

- Correlation and regression analysis  
- Customer segmentation  
- Time series aggregation  
- Volatility (standard deviation of returns)  
- Geographic revenue mapping  

---

## 🔍 Key Insights

### 📉 Price vs Quantity Sold

- A statistically significant negative relationship was observed after removing outliers  
- The relationship is weak in strength  

**Conclusion:**  
Price influences demand, but is not a strong standalone predictor of quantity sold.

---

### 👥 Customer Behavior

- Repeat customers spend significantly more than one-time customers  
- Greater variability in spending among repeat customers  
- Presence of high-value customers  

**Conclusion:**  
Repeat customers contribute disproportionately to overall revenue.

---

### 📦 Product Performance

- Revenue is concentrated among a small subset of products  

**Conclusion:**  
Focusing on high-performing products improves overall performance.

---

### 📈 Sales Trends

- Stable revenue in early months  
- Strong upward trend from late summer into autumn  
- Peak observed in November  

**Conclusion:**  
Clear seasonal demand patterns exist.

---

### 🔄 Monthly Revenue Changes

- Fluctuations with both growth and decline periods  

**Conclusion:**  
Sales performance varies over time due to multiple factors.

---

### 💰 Cryptocurrency Volatility

- Ripple (XRP) shows the highest volatility  
- Bitcoin (BTC) shows the lowest volatility  

**Conclusion:**  
Smaller cryptocurrencies are more volatile; established ones are more stable.

---

## 💼 Business Conclusions

- Pricing alone is not sufficient to drive demand  
- Customer retention is critical for revenue growth  
- Focus on top-performing products  
- Plan for seasonal demand increases  
- Consider risk differences in crypto investments  

---

## 🌍 Additional Features

- Global revenue map segmented into:
  - High revenue regions  
  - Medium revenue regions  
  - Low revenue regions  

- Interactive Streamlit dashboard  

---

## 🚀 Tools & Technologies

- Python  
- Pandas  
- Matplotlib / Plotly  
- Streamlit  
- API Integration  

---

## 📌 Notes

- Dataset compressed using `.csv.gz` for deployment  
- Streamlit caching improves performance  

---
