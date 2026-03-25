import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# ----------------------
# STYLE
# ----------------------
sns.set_style("whitegrid")
plt.rcParams.update({
    "axes.titlesize": 14,
    "axes.labelsize": 11
})

# ----------------------
# SIDEBAR
# ----------------------
st.sidebar.title("📊 Navigation")

section = st.sidebar.radio(
    "Go to:",
    [
        "Overview",
        "Price vs Quantity",
        "Customer Behavior",
        "Sales Trends",
        "Geography",
        "Crypto Analysis"
    ]
)

st.title("📊 E-Commerce and Crypto Insights Dashboard")

st.markdown("""
### Business Insights at a Glance
Explore how pricing, customer behavior, and geography impact revenue.
""")

st.markdown("---")

# ----------------------
# LOAD DATA
# ----------------------
@st.cache_data
def load_data():
    return pd.read_csv("app.py/clean_ecommerce_data.csv.gz")

@st.cache_data
def load_crypto():
    return pd.read_csv("app.py/crypto_data_API.csv")

df = load_data()
df1 = load_crypto()

# ----------------------
# DATA PREP
# ----------------------

# --- CUSTOMER ---
customer_summary = df.groupby('CustomerNo').agg({
    'TransactionNo': 'nunique',
    'Revenue': 'sum'
}).rename(columns={
    'TransactionNo': 'NumTransactions',
    'Revenue': 'TotalSpend'
})

customer_summary['CustomerType'] = np.where(
    customer_summary['NumTransactions'] > 1,
    'Repeat',
    'One-time'
)

avg_spend = customer_summary.groupby('CustomerType')['TotalSpend'].mean().reset_index()

# --- TIME SERIES ---
monthly_sales = df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

monthly_sales['Date'] = pd.to_datetime(
    monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str)
)

monthly_sales = monthly_sales.sort_values('Date')
monthly_sales['Revenue_diff'] = monthly_sales['Revenue'].diff()

# --- MAP ---
df_map = df[~df['Country'].isin(['Unspecified', 'European Community'])]

country_revenue = (
    df_map.groupby('Country')['Revenue']
    .sum()
    .reset_index()
)
country_revenue['Tier'] = pd.qcut(
    country_revenue['Revenue'],
    q=4,
    labels=['Low', 'Medium', 'High', 'Top']
)

tier_order = ['Low', 'Medium', 'High', 'Top']
country_revenue['Tier'] = pd.Categorical(
    country_revenue['Tier'],
    categories=tier_order,
    ordered=True
)

fig_map = px.choropleth(
    country_revenue,
    locations='Country',
    locationmode='country names',
    color='Tier',
    color_discrete_map={
        'Low': '#D6EAF8',
        'Medium': '#5DADE2',
        'High': '#F5B041',
        'Top': '#E74C3C'
    },
    title='Revenue Distribution by Country'
)
# --- CRYPTO ---
df1['date'] = pd.to_datetime(df1['date'])
df1 = df1.sort_values(['coin', 'date'])

df1['returns'] = df1.groupby('coin')['price'].pct_change()

volatility = df1.groupby('coin')['returns'].std().reset_index()
avg_price = df1.groupby('coin')['price'].mean().reset_index()
merged = avg_price.merge(volatility, on='coin')

avg_volatility = volatility['returns'].mean()
most_volatile = volatility.sort_values('returns', ascending=False).iloc[0]['coin']

# ----------------------
# OVERVIEW
# ----------------------
if section == "Overview":

    st.subheader("Business Insights at a Glance")

    st.markdown("### 🛍️ E-Commerce")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
    col2.metric("Total Customers", df['CustomerNo'].nunique())
    col3.metric("Avg Order Value", f"${df['Revenue'].mean():.2f}")

    st.markdown("---")

    st.markdown("### 🪙 Crypto Market")
    col4, col5, col6 = st.columns(3)

    col4.metric("Tracked Coins", df1['coin'].nunique())
    col5.metric("Avg Volatility", f"{avg_volatility:.4f}")
    col6.metric("Most Volatile", most_volatile.capitalize())

# ----------------------
# PRICE VS QUANTITY
# ----------------------
elif section == "Price vs Quantity":

    st.header("💰 Price vs Quantity Sold")
    st.info("Price has a statistically significant but weak impact on demand.")

    q_high = df['Quantity'].quantile(0.99)
    df_filtered = df[df['Quantity'] <= q_high]

    fig, ax = plt.subplots(figsize=(6,4))

    sns.regplot(
        data=df_filtered.sample(3000),
        x='Price',
        y='Quantity',
        scatter_kws={'alpha':0.2, 's':10},
        line_kws={'color':'red'},
        ax=ax
    )

    ax.set_title("Weak Negative Relationship")
    sns.despine()

    st.pyplot(fig)

# ----------------------
# CUSTOMER BEHAVIOR
# ----------------------
elif section == "Customer Behavior":

    st.header("👥 Customer Spending Behavior")
    st.success("Repeat customers contribute significantly more revenue.")

    col1, col2 = st.columns(2)

    col1.metric("One-time Avg Spend", f"${avg_spend.iloc[0,1]:,.0f}")
    col2.metric("Repeat Avg Spend", f"${avg_spend.iloc[1,1]:,.0f}")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.barplot(
        data=avg_spend,
        x='CustomerType',
        y='TotalSpend',
        palette=['#4C78A8', '#F58518'],
        ax=ax
    )

    sns.despine()
    st.pyplot(fig)

# ----------------------
# SALES TRENDS
# ----------------------
elif section == "Sales Trends":

    st.header("📈 Sales Over Time")
    st.info("Sales increase toward year-end, indicating seasonality.")

    # --- LINE + AREA ---
    fig1, ax1 = plt.subplots(figsize=(8,4))

    ax1.fill_between(monthly_sales['Date'], monthly_sales['Revenue'], alpha=0.2)
    ax1.plot(monthly_sales['Date'], monthly_sales['Revenue'], marker='o')

    ax1.set_title('Monthly Revenue Trend')
    ax1.tick_params(axis='x', rotation=45)

    st.pyplot(fig1)

    # --- DIFF BAR ---
    fig2, ax2 = plt.subplots(figsize=(8,4))

    # Format dates nicely
    monthly_sales['Month_str'] = monthly_sales['Date'].dt.strftime('%b')

    # Better colors + thicker bars
    colors = ['#2ECC71' if x > 0 else '#E74C3C' for x in monthly_sales['Revenue_diff']]

    ax2.bar(monthly_sales['Month_str'], monthly_sales['Revenue_diff'], color=colors, width=0.6)
    ax2.axhline(0, color='black', linestyle='--', linewidth=1)

    ax2.set_title('Month-to-Month Revenue Change', weight='bold')
    ax2.set_ylabel('Revenue Change')
    # Clean look
    ax2.grid(axis='y', linestyle='--', alpha=0.4)
    sns.despine()

    st.pyplot(fig2)

# ----------------------
# GEOGRAPHY
# ----------------------
elif section == "Geography":

    st.header("🌍 Revenue by Country")
    st.plotly_chart(fig_map, use_container_width=True)

# ----------------------
# CRYPTO
# ----------------------
elif section == "Crypto Analysis":

    st.header("🪙 Cryptocurrency Volatility")
    st.warning("Lower-priced assets tend to show higher volatility.")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(6,4))
        sns.barplot(data=volatility, x='coin', y='returns', ax=ax1)
        ax1.set_title("Volatility Comparison")
        sns.despine()
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(6,4))
        sns.scatterplot(data=merged, x='price', y='returns', hue='coin', s=100, ax=ax2)
        ax2.set_xscale('log')
        ax2.set_title("Price vs Volatility")
        sns.despine()
        st.pyplot(fig2)
