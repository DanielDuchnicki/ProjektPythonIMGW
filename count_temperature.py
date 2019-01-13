from datetime import timedelta, date
# TODO dodać import funkcji get_temperatures


def first_days_of_seasons():
    """Funkcja zwraca średnie temperatury dla pierwszego dnia wiosny, lata, jesieni i zimy
    :return: temperatures: dictionary in format {'dd/mm': mean_temperature}
    """
    dates = ["21/03", "22/06", "23/09", "22/12"]
    temperatures = {}
    for next_date in dates:
        temperatures[next_date] = count_mean_temperature(next_date)
    return temperatures


def weather_forecast():
    """Funkcja zwraca prognozę pogody dla dwóch kolejnych dni, korzystając z metody klimatycznej
    :return: dictionary in format {'dd/mm': mean_temperature}
    """
    tomorrow_date = date.today() + timedelta(days=1)
    tomorrow = translate_date(tomorrow_date)
    day_after_tomorrow_date = tomorrow_date + timedelta(days=1)
    day_after_tomorrow = translate_date(day_after_tomorrow_date)
    return {tomorrow: count_mean_temperature(tomorrow), day_after_tomorrow: count_mean_temperature(day_after_tomorrow)}


def count_mean_temperature(given_date):
    """
    :param given_date: date in string format - 'dd/mm'
    :return: mean_temperature
    """
    temperatures = [temp for temp in get_temperatures(given_date).values()]
    mean_temperature = sum(temperatures)/len(temperatures)
    return mean_temperature


def translate_date(given_date):
    """
    :param given_date: date in datetime format - datetime.date(yyyy, mm, dd)
    :return: day_month: date in string format - 'dd/mm'
    """
    day_month = str(given_date.day)+'/'+str(given_date.month)
    return day_month
