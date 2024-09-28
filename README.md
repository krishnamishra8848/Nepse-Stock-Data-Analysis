# Stock Price Analysis Web App

This is a Streamlit web application that allows users to analyze stock price data. Users can upload a CSV file containing stock prices, and the app will compute and display changes in stock prices over different time frames: every 3 months, every 6 months, and yearly.

## Features

- **Upload CSV**: Users can upload stock price data in CSV format.
- **Date and Close Price Analysis**: The app checks for the presence of 'Date' and 'Close' columns in the uploaded CSV file.
- **Change Calculations**:
  - Changes every 3 months.
  - Changes every 6 months.
  - Yearly price changes based on the last closing price of each year.
- **Average Growth Calculation**: The app calculates and displays the average growth for each time frame.

## Requirements

- Python 3.x
- Streamlit
- Pandas

## Usage

1. Navigate to the web app by opening the following link: [Stock Price Analysis Web App](https://nepse-stock-data-analysis.onrender.com/)
2. Upload your CSV file containing stock price data with 'Date' and 'Close' columns.
3. View the analysis results displayed in the tables.

