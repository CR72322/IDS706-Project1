import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def descriptive_statistics(data, column_name):
    return data[column_name].describe()

def plot_cost_trend(data, country):
    country_data = data[data["Entity"] == country]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data["Year"], country_data["Cost of a healthy diet"])
    plt.title(f'Trend of Cost of a Healthy Diet for {country}')
    plt.xlabel('Year')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.show()

def plot_top_10_countries(data, year):
    year_data = data[data["Year"] == year]
    top_10 = year_data.nlargest(10, "Cost of a healthy diet")

    # Define a list of colors
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'pink', 'cyan', 'gray']
    
    plt.figure(figsize=(12, 8))
    plt.barh(top_10["Entity"], top_10["Cost of a healthy diet"], color=colors)
    plt.xlabel('Cost of a Healthy Diet')
    plt.title(f'Top 10 Countries with Highest Cost of a Healthy Diet in {year}')
    plt.gca().invert_yaxis()  # This will make the country with the highest cost appear at the top
    plt.show()

if __name__ == "__main__":
    data = load_data("data/data.csv")
    
    # Descriptive statistics for "Cost of a healthy diet"
    print(descriptive_statistics(data, "Cost of a healthy diet"))
    
    # Visualizing the trend for a few countries as an example
    countries_to_visualize = ["United States", "United Kingdom", "China"]
    for country in countries_to_visualize:
        plot_cost_trend(data, country)
    
    # Plotting the top 10 countries for the year 2021
    plot_top_10_countries(data, 2021)
