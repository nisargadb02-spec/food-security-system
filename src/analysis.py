import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load dataset safely
# -----------------------------
def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "hunger_india.csv")

    print("Loading dataset from:", file_path)

    df = pd.read_csv(file_path)
    return df


# -----------------------------
# Plot Hunger Trend
# -----------------------------
def plot_hunger(df):
    plt.figure()
    plt.plot(df["Year"], df["Undernourished_Million"], marker="o")
    plt.title("Undernourished Population Trend in India")
    plt.xlabel("Year")
    plt.ylabel("Millions")
    plt.grid()
    plt.show()


# -----------------------------
# Plot Poverty Trend
# -----------------------------
def plot_poverty(df):
    plt.figure()
    plt.plot(df["Year"], df["Poverty_Rate"], marker="o")
    plt.title("Poverty Rate Trend in India")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.grid()
    plt.show()


# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    df = load_data()

    print("\nDATA PREVIEW:")
    print(df.head())

    print("\nBASIC STATS:")
    print(df.describe())

    plot_hunger(df)
    plot_poverty(df)