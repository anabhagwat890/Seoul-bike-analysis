# Title : Seoul Bike Rental Analysis (BAN601)

# Project Overview :
This application provides a comprehensive Exploratory Data Analysis (EDA) of the Seoul Bike dataset, specifically investigating how 10 different numeric variables influence rental bike demand.

# Project Structure & Requirements :
As per the project requirements, this application includes:
1. Two Primary Inputs: User-controlled Variable Selection and Histogram Binning slider.
2. One Primary Plot: An interactive distribution chart generated via Matplotlib.
3. One Other Output: A mathematical Summary Statistics table (Mean, Max, Min) to support the business audit.
4. Optional Output: A "Raw Data" expander for source verification and transparency.


#  10-Column Business Audit :
I have designed this app to answer specific business questions for every variable in the SeoulBikeData.csv:

1. Rented Bike Count: What is the average hourly demand, and what is the maximum number of bikes we need to have ready for the public?
2. Hour: Which specific hours are our "Rush Hours" where we see the highest volume of riders?
3. Temperature(°C): Is there a "sweet spot" temperature where people are more likely to rent bikes?
4. Humidity(%): Does high humidity make riding too uncomfortable, leading to a drop in total rentals?
5. Wind speed (m/s): At what wind speed do we see people switching from bikes to other forms of transport for safety?
6. Visibility (10m): Does poor visibility (like fog or smog) significantly impact the number of bikes being used?
7. Dew point temperature(°C): How does the moisture in the air affect general rider comfort and rental trends?
8. Solar Radiation (MJ/m2): Do we see a surge in rentals on very sunny days, or does the heat eventually drive people away?
9. Rainfall(mm): What is the "cutoff point" of rainfall where bike rentals essentially stop for the day?
10. Snowfall (cm): How much does a snowy day impact our daily revenue compared to a clear winter day?

#  Tech Stack & Features :
1. Streamlit & Python: For the interactive web interface.
2. Matplotlib: Dynamic histograms with custom colors and themes (ggplot, dark_mode).
3. Data Handling: Robust management of missing values (NaNs) to ensure summary statistics remain accurate and      histograms render correctly.
4. Real-time Stats: Automatic generation of Summary Statistics for any selected variable.

#  How to Run :
1. Install dependencies: pip install streamlit pandas matplotlib
2. Launch the app: streamlit run app.py
