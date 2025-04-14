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

    ("test",
     pd.read_csv("CSVfiler/oldcsv/ReactWarmLoad.csv"),
     pd.read_csv("CSVfiler/oldcsv/VueWarmLoad.csv")
     )

]

#61dbfb react blå
#42b883
reactColorTTI = color ="#61dbfb"
reactColorPLT = color ="blue"
vueColorTTI = color = "#42b883"
vueColorPLT = color = "green"
N = 200
x = range(1, N + 1)

for label, r_df, v_df in scenarios:
    plt.figure(figsize=(12, 6))

    plt.plot(x, r_df[measure_mode].iloc[:N], label="React " + measure_mode.upper(), color="#61dbfb")
    plt.plot(x, v_df[measure_mode].iloc[:N], label="Vue " + measure_mode.upper(), color="#42b883")
    plt.ylim(ymin=0)
    plt.xlabel("Testnummer")
    plt.ylabel(f"{measure_label.get(measure_mode)} i ms")
    plt.title(f"{measure_label[measure_mode]} – {label}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"{IMG_PATH} nyattiLine_{measure_mode}_{label.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()



