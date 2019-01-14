import matplotlib.pyplot as plt
import database_helpers

#TODO: get real data from file

'''Dummy data'''
x = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
y1 = [2, 4, 3, 4, 1, 8, 2, 5, 3, 0]
y2 = [20, 14, 13, 14, 10, 8, 20, 15, 13, 10]
y3 = [-2, -4, -3, -4, -1, -8, -2, -5, -3, 0]
y4 = [2, 14, 13, 4, 11, 18, 12, 5, 3, 10]

def plot_first_days_of_seasons_trend():
    '''Tworzy wykresy teperatur w pierwsze dni pór roku: wiosna, lato, jesień i zima'''

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

    fig1.set_title('Temperatura w dniu ' + dates[0], fontsize=12)
    fig1.plot(x,y1, 'limegreen')

    fig2.set_title('Temperatura w dniu ' + dates[1], fontsize=12)
    fig2.plot(x,y2,'gold')

    fig3.set_title('Temperatura w dniu ' + dates[2], fontsize=12)
    fig3.plot(x,y3, 'darkred')

    fig4.set_title('Temperatura w dniu ' + dates[3], fontsize=12)
    fig4.plot(x,y4, 'darkblue')

    plt.show()

plot_first_days_of_seasons_trend()