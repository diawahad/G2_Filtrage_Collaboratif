#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:08:16 2019

@author: Group 2 !
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# %%

'''
Function subscribers_before_date

Input : - filepath_user : csv user file path

Output : Graph date/number_of_users

The function shows a graph of the number of users over time :
    horizontal axis : date
    vertical axis : number of users
'''


def subscribers_before_date(filepath_user):
    df_user = pd.read_csv(filepath_user, header=0, sep=";")
    df_user = df_user.loc[:, ['user_id', 'date_create']]
    df_user = df_user.groupby(['date_create']).count()
    df_user = np.cumsum(df_user)
    df_user = df_user.reset_index()
    df_user['date_create'] = pd.to_datetime(df_user['date_create'])
    df_user = df_user.rename(columns={"date_create": "date",
                                      "user_id": "user"})
    fig, ax = plt.subplots()
    ax.plot(df_user.date, df_user.user)
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_minor_locator(months)
    plt.title("Number of users over time")
    plt.xlabel("Date")
    plt.ylabel("Number of users")
    plt.show()

# %%


'''
Function subscribers_by_year

Input : - filepath_user : csv user file path

Output : Graph year/number_of_users

The function shows a graph of the number of users subscribing each year :
    horizontal axis : year
    vertical axis : number of users
'''


def subscribers_by_year(filepath_user):
    df_user = pd.read_csv(filepath_user, header=0, sep=";",
                          parse_dates=["date_create"])
    df_user["year_create"] = [data.year for data in df_user.date_create]
    df_user = df_user.loc[:, ['user_id', 'year_create']]
    df_user = df_user.groupby(["year_create"]).count()
    df_user = df_user.reset_index()
    df_user = df_user.rename(columns={"year_create": "year",
                                      "user_id": "user"})

    fig, ax = plt.subplots()
    ax.bar(df_user.year, df_user.user)
    plt.title("Number of users per year")
    plt.xlabel("Year")
    plt.ylabel("Number of users")
    plt.show()
