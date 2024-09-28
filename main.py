import pandas as pd
import streamlit as st
from datetime import datetime

# Streamlit App
def main():
    st.title("Stock Price Analysis")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Check for required columns
        if 'Date' in df.columns and 'Close' in df.columns:
            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'])

            # Filter data from the last date of 2019 to the latest date
            start_date = datetime(2019, 12, 31)
            end_date = df['Date'].max()
            filtered_df = df[(df['Date'] > start_date) & (df['Date'] <= end_date)]

            # Set 'Date' as index
            filtered_df.set_index('Date', inplace=True)

            # Resample data to 3-month frequency and get the last close price
            resampled_3m = filtered_df['Close'].resample('3M').last()
            changes_3m = resampled_3m.diff().dropna()
            changes_3m_df = pd.DataFrame({
                'Date': resampled_3m.index[1:],  
                'Close Price': resampled_3m.values[1:],  
                'Absolute Change': changes_3m.values  
            })

            # Calculate average growth for 3 months
            avg_growth_3m = changes_3m.mean()

            # Resample data to 6-month frequency and get the last close price
            resampled_6m = filtered_df['Close'].resample('6M').last()
            changes_6m = resampled_6m.diff().dropna()
            changes_6m_df = pd.DataFrame({
                'Date': resampled_6m.index[1:],  
                'Close Price': resampled_6m.values[1:],  
                'Absolute Change': changes_6m.values  
            })

            # Calculate average growth for 6 months
            avg_growth_6m = changes_6m.mean()

            # Calculate the last closing price for each year
            yearly_data = filtered_df.resample('Y')['Close'].last()
            changes_yearly = yearly_data.diff().dropna()
            changes_yearly_df = pd.DataFrame({
                'Date': yearly_data.index[1:],  
                'Close Price': yearly_data.values[1:],  
                'Absolute Change': changes_yearly.values  
            })

            # Calculate average growth for yearly
            avg_growth_yearly = changes_yearly.mean()

            # Display the results
            st.subheader("Stock Price Change Every 3 Months")
            st.write(changes_3m_df)
            st.write(f"Average Growth (3 Months): {avg_growth_3m:.2f}")

            st.subheader("Stock Price Change Every 6 Months")
            st.write(changes_6m_df)
            st.write(f"Average Growth (6 Months): {avg_growth_6m:.2f}")

            st.subheader("Stock Price Change Yearly (Last Closing Price Each Year)")
            st.write(changes_yearly_df)
            st.write(f"Average Growth (Yearly): {avg_growth_yearly:.2f}")

        else:
            st.error("The CSV file must contain 'Date' and 'Close' columns.")

if __name__ == "__main__":
    main()
