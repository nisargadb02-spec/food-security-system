import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="India Food Security Dashboard",
    layout="wide"
)

# -----------------------------
# Title + Intro
# -----------------------------
st.title("🍽️ India Food Security Analysis System")

st.write("""
This dashboard analyzes hunger and poverty trends in India using real-world dataset insights.
It helps visualize long-term changes in undernourishment and poverty levels.
""")

# -----------------------------
# Load data safely
# -----------------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "hunger_india.csv")

df = pd.read_csv(file_path)

# -----------------------------
# Show dataset
# -----------------------------
st.subheader("📊 Dataset Preview")
st.dataframe(df)

# -----------------------------
# Key Insights
# -----------------------------
st.subheader("🔍 Key Insights")

st.markdown("""
- 📉 Undernourished population shows gradual decline over time  
- 📉 Poverty rate is also decreasing slowly  
- 🔗 Strong correlation between poverty and hunger  
- ⚠️ Rural areas still face higher food insecurity  
""")

# -----------------------------
# Hunger Trend Graph
# -----------------------------
st.subheader("📉 Hunger Trend in India")

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Undernourished_Million"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("Millions")
ax.set_title("Undernourished Population Trend")
ax.grid(True)

st.pyplot(fig)

# -----------------------------
# Poverty Trend Graph
# -----------------------------
st.subheader("📉 Poverty Trend in India")

fig2, ax2 = plt.subplots()
ax2.plot(df["Year"], df["Poverty_Rate"], marker="o", color="orange")
ax2.set_xlabel("Year")
ax2.set_ylabel("Percentage")
ax2.set_title("Poverty Rate Trend")
ax2.grid(True)

st.pyplot(fig2)

# -----------------------------
# Correlation Analysis
# -----------------------------
st.subheader("📊 Data Correlation")

st.write(df.corr(numeric_only=True))

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.write("Built with ❤️ using Streamlit | Food Security Analysis Project")