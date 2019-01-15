from datetime import timedelta, date


def first_days_of_seasons(database):
    """Funkcja zwraca średnie temperatury dla pierwszego dnia wiosny, lata, jesieni i zimy
    :param database: object of DatabaseReader class
    :return: temperatures: dictionary in format {'dd/mm': mean_temperature}
    """
    dates = ["21/03", "22/06", "23/09", "22/12"]
    temperatures = {}
    for next_date in dates:
        temperatures[next_date] = count_mean_temperature(next_date, database)
    return temperatures


def weather_forecast(database):
    """Funkcja zwraca prognozę pogody dla dwóch kolejnych dni, korzystając z metody klimatycznej
    :param database: object of DatabaseReader class
    :return: dictionary in format {'dd/mm': mean_temperature}
    """
    tomorrow_date = date.today() + timedelta(days=1)
    tomorrow = translate_date(tomorrow_date)
    day_after_tomorrow_date = tomorrow_date + timedelta(days=1)
    day_after_tomorrow = translate_date(day_after_tomorrow_date)
    return {'tomorrow': count_mean_temperature(tomorrow, database), 'day after tomorrow': count_mean_temperature(day_after_tomorrow, database)}


def count_mean_temperature(given_date, database):
    """
    :param given_date: date in string format - 'dd/mm'
    :param database: object of DatabaseReader class
    :return: mean_temperature
    """
    temperatures = [float(temp) for temp in database.get_temperatures(given_date).values()]
    mean_temperature = sum(temperatures)/len(temperatures)
    return mean_temperature


def translate_date(given_date):
    """
    :param given_date: date in datetime format - datetime.date(yyyy, mm, dd)
    :return: day_month: date in string format - 'dd/mm'
    """
    month = given_date.month
    day = given_date.day
    if month < 9:
        month_str = '0' + str(month)
    else:
        month_str = str(month)
    if day < 9:
        day_str = '0' + str(day)
    else:
        day_str = str(day)
    day_month = day_str + '/' + month_str
    return day_month

