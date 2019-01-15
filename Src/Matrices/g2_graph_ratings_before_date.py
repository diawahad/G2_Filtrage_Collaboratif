import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

# Graph courbe

def nb_ratings_before_date(filepath_rating, nrows):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=nrows)
    df_rating = df_rating.rename(columns={"date_rating":"date"})
    df_rating = df_rating.loc[:, ['rating_id', 'date']]
    df_rating = df_rating.groupby(['date']).count()
    df_rating = df_rating.sort_values(by='date', ascending=True)
    df_cum = np.cumsum(df_rating)
    df_cum = df_cum.reset_index()
    df_cum['date'] = pd.to_datetime(df_cum['date'])
    return df_cum

fig, ax = plt.subplots()
ax.plot(cumule.date, cumule.rating_id)
years = mdates.YearLocator()  
months = mdates.MonthLocator()  
yearsFmt = mdates.DateFormatter('%Y')
#datemin = datetime.date(cumule.date.min().year, 7, 1)
#datemax = datetime.date(cumule.date.max().year, 11, 1)
datemin = datetime.date(cumule.date.min().year, 1, 1)
datemax = datetime.date(cumule.date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
plt.title("Nombre de notes cumulées par date")
plt.xlabel('Date')
plt.ylabel('Nombre de notes cumulées')
plt.show()

# Graph histogramme

def nb_ratings_years(filepath_rating, nrows, time):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=nrows)
    df_rating = df_rating.rename(columns={"date_rating":"date"})
    df_rating = df_rating.loc[:, ['rating_id', 'date']]
    df_rating = df_rating.groupby(['date']).count()
    df_rating = df_rating.sort_values(by='date', ascending=True)
    df_rating = df_rating.reset_index()
    df_rating['date'] = pd.to_datetime(df_rating['date'])
    per = df_rating.date.dt.to_period(time)
    g = df_rating.groupby(per)
    df_rating = g.sum()
    df_rating = df_rating.reset_index()
    return df_rating

plt.bar(histo['date'].apply(lambda x : str(x)) ,histo['rating_id'])
plt.show()

