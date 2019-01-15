from typing import List, Any

import matplotlib.pyplot as plt
import database_helpers

#TODO: get real data from file

def get_historical_temperature_data_for_date(day, database):
    temperatures = [temp for temp in database.get_temperatures(day).values()]
    return temperatures

def plot_first_days_of_seasons_trend(database):
    '''Tworzy wykresy teperatur w pierwsze dni pór roku: wiosna, laito, jesień i zima'''

    x = []
    for year in range(1961, 2017): x.append(year);
    y = []

    '''y1 = [2, 4, 3, 4, 1, 8, 2, 5, 3, 0]
    y2 = [20, 14, 13, 14, 10, 8, 20, 15, 13, 10]
    y3 = [-2, -4, -3, -4, -1, -8, -2, -5, -3, 0]
    y4 = [2, 14, 13, 4, 11, 18, 12, 5, 3, 10]'''

    figure, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True)

    fig1 = axs[0, 0]
    fig2 = axs[0, 1]
    fig3 = axs[1, 0]
    fig4 = axs[1, 1]

    for ax in axs.flatten():
        ax.set_xlabel('Rok', fontsize=10)
        ax.set_ylabel('Temperatura [C]', fontsize=10)

    '''align axes:'''
    figure.align_xlabels(axs[:, :])
    figure.align_ylabels(axs[:, :])

    dates = ["21/03", "22/06", "23/09", "22/12"]

    for date in dates:
        temperatures = [float(temp) for temp in database.get_temperatures(date).values()]
        y.append(temperatures)



    fig1.set_title('Temperatura w dniu ' + dates[0], fontsize=12)
    fig1.plot(x,y[0], 'limegreen')

    fig2.set_title('Temperatura w dniu ' + dates[1], fontsize=12)
    fig2.plot(x,y[1],'gold')

    fig3.set_title('Temperatura w dniu ' + dates[2], fontsize=12)
    fig3.plot(x,y[2], 'darkred')

    fig4.set_title('Temperatura w dniu ' + dates[3], fontsize=12)
    fig4.plot(x,y[3], 'darkblue')

    plt.show()

def plot_weatherforcast():
    '''Tworzy wykres przewidywanych teperatur na kolejne dwa dni'''

    '''Dummy data'''
    # Zakres od dzisiejszej daty + 2 dni do przodu
    days = ["14/01", "15/01", "16/01"]
    temperatures = [2, -1, 0]

    plt.plot(days, temperatures, ':')
    plt.title('Prognoza na najblższe dni')
    plt.xlabel('Dzień')
    plt.ylabel('Temperatura [C]')
    plt.show()
