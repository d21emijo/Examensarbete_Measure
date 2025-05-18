import scipy.stats as stats

import numpy as np

import statsmodels.stats.multicomp as multi

import pandas as pd

scenarios = [

    # pilot
    ("WarmLoad, All Cached",
     pd.read_csv("CSVfiler/pilotcsv/react_pilot_warm.csv"),
     pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_warm.csv")),

    ("Offline Mode, All Cached",
     pd.read_csv("CSVfiler/pilotcsv/react_pilot_offline.csv"),
     pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_offline.csv")),

    ("ColdLoad, No Cache",
     pd.read_csv("CSVfiler/pilotcsv/react_pilot_cold.csv"),
     pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_cold.csv")),

    #        ("WarmLoad, All Cached",
    #         pd.read_csv("CSVfiler/React_Warm_load_0.csv"),
    #         pd.read_csv("CSVfiler/Vue_warm_load.csv")),

    #        ("Offline Mode, All Cached",
    #         pd.read_csv("CSVfiler/React_Offline_load_0cache.csv"),
    #         pd.read_csv("CSVfiler/Vue_offline_load.csv")),
    #        ("ColdLoad, No Cache",
    #         pd.read_csv("CSVfiler/React_cold_load.csv"),
    #         pd.read_csv("CSVfiler/Vue_cold_load.csv")),


]

def anova(*data):  # * indicates, 0, 1 , 2 .. arguments
    if len(data) == 2:
        statistic, pvalue = stats.f_oneway(data[0], data[1])

    elif len(data) == 3:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2])
    elif len(data) == 4:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2], data[3])
    print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))
    if pvalue < 0.05:
        return True
    else:
        return False

labels = []
vue = []
react = []


def exampleAnova():

    for label, r_df, v_df in scenarios:
        labels.append(label)
        react.append(r_df)
        vue.append(v_df)
        print(label)
        print(v_df.mean(),'\n',"Vye")
        print(r_df.mean(), '\n',"react")
    # Run Anova on data groups
        if (anova(r_df['plt'], v_df['plt'])):
            print(f"The plt means are different")
        else:
            print("No differences in means")

        if (anova(r_df['TTI '], v_df['TTI '])):
            print(f"The tti means are different \n")
        else:
            print("No differences in means")

exampleAnova()