import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    print(df.head())

    # Create scatter plot
    fig, ax=plt.subplots(figsize=(10,6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

   

    # Create first line of best fit
    result=linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_full=pd.Series(range(df["Year"].min(),2051))
    y_full=result.intercept + result.slope * x_full
    ax.plot(x_full, y_full, "r")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    result_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = result_recent.intercept + result_recent.slope * x_recent
    ax.plot(x_recent, y_recent, 'green')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")       
    ax.set_title("Rise in Sea Level")       
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()