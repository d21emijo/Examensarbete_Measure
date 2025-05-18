import matplotlib
matplotlib.use('Agg')  # Använd icke-GUI-backend
import matplotlib.pyplot as plt
import pandas as pd

IMG_PATH = "bilder/"
measure_mode = "TTI " # "plt"/"TTI "
measure_label = {
    "plt": "Page Load Time",
    "TTI ": "Time to Interactive "
}

scenarios = [
#pilot
  #  ("WarmLoad, All Cached",
  #   pd.read_csv("CSVfiler/pilotcsv/react_pilot_warm.csv"),
  #   pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_warm.csv")),

 #   ("Offline Mode, All Cached",
 #    pd.read_csv("CSVfiler/pilotcsv/react_pilot_offline.csv"),
#     pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_offline.csv")),

#    ("ColdLoad, No Cache",
#     pd.read_csv("CSVfiler/pilotcsv/react_pilot_cold.csv"),
#     pd.read_csv("CSVfiler/pilotcsv/Vue_pilot_cold.csv")),

    ("WarmLoad, All Cached",
     pd.read_csv("CSVfiler/React_Warm_load_0.csv"),
     pd.read_csv("CSVfiler/Vue_warm_load.csv")),

    ("Offline Mode, All Cached",
     pd.read_csv("CSVfiler/React_Offline_load_0cache.csv"),
     pd.read_csv("CSVfiler/Vue_offline_load.csv")),
    ("ColdLoad, No Cache",
     pd.read_csv("CSVfiler/React_cold_load.csv"),
     pd.read_csv("CSVfiler/Vue_cold_load.csv")),

]

#61dbfb react blå
#42b883
reactColorTTI = color ="#61dbfb"
reactColorPLT = color ="blue"
vueColorTTI = color = "#42b883"
vueColorPLT = color = "green"
N = 250
x = range(1, N + 1)

for label, r_df, v_df in scenarios:
    plt.figure(figsize=(12, 6))

    plt.plot( r_df[measure_mode].iloc[:N], label="React " + measure_mode.upper(), color="#61dbfb")
    plt.plot( v_df[measure_mode].iloc[:N], label="Vue " + measure_mode.upper(), color="#42b883")
    plt.ylim(ymin=0,ymax=4500)
    plt.xlabel("Testnummer")
    plt.ylabel(f"{measure_label.get(measure_mode)} i ms")
    plt.title(f" {measure_label[measure_mode]} – {label}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"{IMG_PATH} ny {measure_mode}_{label.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()



