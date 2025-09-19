import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, s=20)


    # Create first line of best fit
    inclinacao_todos, intercepto_todos, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create line from first year in data to 2050
    anos_estendidos = range(df['Year'].min(), 2051)
    linha_todos = [inclinacao_todos * ano + intercepto_todos for ano in anos_estendidos]
    plt.plot(anos_estendidos, linha_todos, 'r-', label='Linha de tendência (todos os dados)')


    # Create second line of best fit
    # Filter data from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    inclinacao_2000, intercepto_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Create line from 2000 to 2050
    anos_2000_estendidos = range(2000, 2051)
    linha_2000 = [inclinacao_2000 * ano + intercepto_2000 for ano in anos_2000_estendidos]
    plt.plot(anos_2000_estendidos, linha_2000, 'g-', label='Linha de tendência (dados de 2000+)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()