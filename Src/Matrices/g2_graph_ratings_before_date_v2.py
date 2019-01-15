import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

# Plot

def nb_ratings_before_date(filepath_rating, nrows):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=nrows)
    df_rating = df_rating.rename(columns={"date_rating":"date"})
    df_rating = df_rating.loc[:, ['rating_id', 'date']]
    df_rating = df_rating.groupby(['date']).count()
    df_rating = df_rating.sort_values(by='date', ascending=True)
    df_cum = np.cumsum(df_rating)
    df_cum = df_cum.reset_index()
    df_cum['date'] = pd.to_datetime(df_cum['date'])
    
    fig, ax = plt.subplots()
    ax.plot(df_cum.date, df_cum.rating_id)
    years = mdates.YearLocator()  
    months = mdates.MonthLocator()  
    yearsFmt = mdates.DateFormatter('%Y')
    datemin = datetime.date(df_cum.date.min().year, 1, 1)
    datemax = datetime.date(df_cum.date.max().year + 1, 1, 1)
    ax.set_xlim(datemin, datemax)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    plt.title("Nombre de notes cumulées par date")
    plt.xlabel('Date')
    plt.ylabel('Nombre de notes cumulées')
    plt.show()



#cumule = nb_ratings_before_date("C:/Projet/Data/ratings_V3.csv", nrows=1e3)
#cumule

# Bar

def nb_ratings_years(filepath_rating, nrows):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=nrows)
    df_rating = df_rating.rename(columns={"date_rating":"date"})
    df_rating = df_rating.loc[:, ['rating_id', 'date']]
    df_rating = df_rating.groupby(['date']).count()
    df_rating = df_rating.sort_values(by='date', ascending=True)
    df_rating = df_rating.reset_index()
    df_rating['date'] = pd.to_datetime(df_rating['date'])
    per = df_rating.date.dt.to_period("Y")
    g = df_rating.groupby(per)
    df_rating = g.sum()
    df_rating = df_rating.reset_index()
    
    plt.bar(df_rating['date'].apply(lambda x : str(x)), df_rating['rating_id'])
    plt.title("Nombre de notes par année")
    plt.xlabel('Année')
    plt.ylabel('Nombre de notes')
    plt.show()

#histo = nb_ratings_years("C:/Projet/Data/ratings_V3.csv", nrows=1e2)
#histo









