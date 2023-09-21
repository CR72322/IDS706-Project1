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

if __name__ == "__main__":
    data = load_data("data/data.csv")
    
    # Descriptive statistics for "Cost of a healthy diet"
    print(descriptive_statistics(data, "Cost of a healthy diet"))
    
    # Visualizing the trend for a few countries as an example
    countries_to_visualize = ["United States", "United Kingdom", "China"]
    for country in countries_to_visualize:
        plot_cost_trend(data, country)
