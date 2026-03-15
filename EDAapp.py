import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Seoul Bike EDA", layout="wide")

@st.cache_data
def load_and_fix_data():
    data = pd.read_csv("SeoulBikeData.csv", encoding='unicode_escape')
    # Fix the broken degree symbols
    data.columns = [col.replace('蚓', '°C') for col in data.columns]
    return data

df = load_and_fix_data()

# 3. Data-Driven Business Questions (The 5 questions you requested)
with st.expander("Business Questions:"):
    st.write("""
    **This analysis covers all 10 numeric variables found in the SeoulBikeData.csv:**
    
    1. **Usage & Timing:** How does the **'Rented Bike Count'** change depending on the **'Hour'** of the day? (Answers: *When are bikes most needed?*)
    2. **Rider Comfort:** How do **'Temperature(°C)'**, **'Humidity(%)'**, and **'Dew point temperature(°C)'** affect the frequency of rentals? (Answers: *What is the ideal weather for a ride?*)
    3. **Weather Obstacles:** At what levels of **'Rainfall(mm)'** and **'Snowfall (cm)'** do we see the distribution of rentals drop to zero? (Answers: *How does the city lose revenue?*)
    4. **Safety & Visibility:** Do low **'Visibility (10m)'** or high **'Wind speed (m/s)'** patterns show a decrease in bike usage? (Answers: *When is it too dangerous or unpleasant to ride?*)
    5. **Energy & Sunlight:** Does the amount of **'Solar Radiation (MJ/m2)'** lead to more people choosing bikes over indoor transport? (Answers: *Does a sunny day guarantee more customers?*)
    """)


st.title("🚲 Seoul Bike Rental Histogram Dashboard")

# --- SIDEBAR: Data Controls ---
st.sidebar.header("Data Controls")

# Variable Selection
numeric_cols = df.select_dtypes("number").columns
selected_var = st.sidebar.selectbox("Choose Variable", numeric_cols)

# Bin Selection
bins = st.sidebar.slider("Number of Bins", 5, 100, 21)

# --- SIDEBAR: THEME & SETTINGS ---
st.sidebar.divider()
st.sidebar.header("Appearance & Themes")

# Color Picker
chart_color = st.sidebar.color_picker("Pick Bar Color", "#3498db")

# Graph Style Selector
graph_style = st.sidebar.selectbox(
    "Select Graph Theme", 
    ["default", "ggplot", "fivethirtyeight", "bmh", "dark_background"]
)

# --- MAIN PAGE OUTPUTS ---
plt.style.use(graph_style)
col1, col2 = st.columns([2, 1])

with col1:
    # Centered title
    st.markdown(f"<h3 style='text-align: center;'>Distribution of {selected_var}</h3>", unsafe_allow_html=True)
    
    fig, ax = plt.subplots()
    
    # Histogram logic
    ax.hist(df[selected_var].dropna(), bins=bins, color=chart_color, edgecolor='white')
    
    # Add Border around the plot
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(2)
        spine.set_edgecolor('black')

    ax.set_xlabel(selected_var)
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Summary Statistics")
    st.write(df[selected_var].describe())

# Optional: Data Preview at the bottom
with st.expander("Click to see raw data (Check Column Names)"):
    st.dataframe(df)