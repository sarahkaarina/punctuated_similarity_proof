import numpy as np
import pandas as pd
import seaborn as sns
import glob
import os

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def plot_heatmaps(df, name, plotpath):

  cmap = 'mako'
  words = name.split("_")
  
  if "close" in name:
    plot_title = "GDAXI daily closing price similarity"
  elif "open" in name:
    plot_title = "GDAXI daily opening price similarity"
  elif "conv" in name:
    plot_title = "GDAXI convergence model"
  elif "div" in name:
    plot_title = "GDAXI divergence model"
  elif "behave_nn" in name:
    plot_title = "GDAXI nearest neighbours model"
  elif "punctuacted_china" in name:
    plot_title = "GDAXI punctuated (original) at China model"
  elif "punctuacted_who" in name:
    plot_title = "GDAXI punctuated (original) at WHO model"
  elif "punctuacted_usa" in name:
    plot_title = "GDAXI punctuated (original) at USA model"
  elif "punctuated_nn_china" in name:
    plot_title = "GDAXI punctuated (revised) at China model"
  elif "punctuated_nn_who" in name:
    plot_title = "GDAXI punctuated (revised) at WHO model"
  elif "punctuated_nn_usa" in name:
    plot_title = "GDAXI punctuated (revised) at USA model"
  else:
    plot_title = words[0].upper() + " " + words[1].capitalize()
    #plot_title = plot_title.title()


  filename = name + ".jpeg"
  filepath = os.path.join(plotpath, filename)

  heatmap = sns.heatmap(df,
                        cmap = cmap,
                        square=True,
                        cbar=True,
                        xticklabels=False,
                        yticklabels=False,
                        cbar_kws={"shrink":0.5})

  heatmap.set_xlabel('02-September-2020', loc = 'right')
  heatmap.set_ylabel('02-September-2019', loc = 'top')

  c_bar = heatmap.collections[0].colorbar
  c_bar.set_ticks([df.min().min(), df.max().max()])
  c_bar.set_ticklabels(['Low', 'High'])
  
  plt.title(plot_title)
  plt.savefig(filepath, format="jpeg")

  plt.close

  plt.savefig(filepath, format="jpeg")

  plt.close


path = "/Users/scrockford/Library/CloudStorage/OneDrive-FondazioneIstitutoItalianoTecnologia/punctuated_similarity_proof/results/GDAXI/*.csv"

plotpath = "/Users/scrockford/Library/CloudStorage/OneDrive-FondazioneIstitutoItalianoTecnologia/punctuated_similarity_proof/plots/GDAXI"

for fname in glob.glob(path):

  data2plot = pd.read_csv(fname)
  plotname = os.path.basename(fname)
  plotname = plotname.replace(".csv", "")

  plt.clf()
  plot_heatmaps(data2plot, plotname, plotpath)

