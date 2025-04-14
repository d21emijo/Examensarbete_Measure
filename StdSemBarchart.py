import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# vad mäta
error_mode ="sem" #ci = confidence , sem = standard error , std = standardavikelse
measure_mode = "plt" # "plt"/"TTI "
measure_label = {
    "plt": "Page Load Time",
    "TTI ": "Time to Interactive "
}
error_labels = {
    "std": "Standardavikelse",
    "ci": "95% Konfidensintervall",
    "sem": "Standard error"
}

def mean_confidence_interval(data, confidence=0.95):
    a = np.array(data.dropna())  # Ta bort NaN
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return h

# scenarios
scenarios = [
    ("WarmLoad, All Cached",
     pd.read_csv("CSVfiler/ReactWarmLoad_3x50_0Cach.csv"),
     pd.read_csv("CSVfiler/VueWarmLoad_3x50_0Cache.csv")),
    ("WarmLoad, 1 picture Cached",
     pd.read_csv("CSVfiler/ReactWarmLoad_3x50_1cache.csv"),
     pd.read_csv("CSVfiler/VueWarmLoad_3x50_1Cache.csv")),
    ("Offline Mode, All Cached",
     pd.read_csv("CSVfiler/ReactOffline_3x50_0cache.csv"),
     pd.read_csv("CSVfiler/VueOffline_3x50_0Cache.csv")),
    ("ColdLoad, No Cache",
     pd.read_csv("CSVfiler/ReactColdLoad_3x50.csv"),
     pd.read_csv("CSVfiler/VueColdLoad_3x50.csv"))

]

# Initiera listor
labels = []
means_react = []
means_vue = []
errors_react = []
errors_vue = []

for label, r_df, v_df in scenarios:
    labels.append(label)

    means_react.append(r_df[measure_mode].mean())
    means_vue.append(v_df[measure_mode].mean())

    if error_mode == "std":
        errors_react.append(r_df[measure_mode].std())
        errors_vue.append(v_df[measure_mode].std())
    if error_mode == "sem":
        errors_react.append(r_df[measure_mode].sem())
        errors_vue.append(v_df[measure_mode].sem())
    if error_mode == "ci":
        errors_react.append(mean_confidence_interval(r_df[measure_mode]))
        errors_vue.append(mean_confidence_interval(v_df[measure_mode]))

#
x = np.arange(len(labels))  #
width = 0.35
fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width/2, means_react, width, yerr=errors_react, label=f'React {measure_mode}', capsize=5, color='#61dbfb', alpha=0.8)
bars2 = ax.bar(x + width/2, means_vue, width, yerr=errors_vue, label=f'Vue {measure_mode}', capsize=5, color='#42b883', alpha=0.8)

# Layout
ax.set_ylabel(f"{measure_label.get(measure_mode)} i ms")
ax.set_title(f'Genomsnittlig {measure_mode} för olika scenarios (React vs Vue) med \n {error_labels.get(error_mode)}')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(f"{"bilder/"}fffffff {error_labels.get(error_mode)}_React_vs_Vue_{measure_mode}.png")

for label, mean,std in zip(labels, means_react ,errors_react):
    print(f"{label}: \nmean {mean:.2f} ms \n{error_mode} : {std:.2f}")




