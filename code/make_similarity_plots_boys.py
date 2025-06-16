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
  
  if "rural" in name:
    plot_title = "Rural boys height similarity"
  elif "urban" in name:
    plot_title = "Urban boys height similarity"
  elif "conv" in name:
    plot_title = "Boys convergence model"
  elif "div" in name:
    plot_title = "Boys divergence model"
  elif "behave_nn" in name:
    plot_title = "Boys nearest neighbours model"
  elif "punctuacted_9" in name:
    plot_title = "Boys punctuated (original) at age 9 model"
  elif "punctuacted_10" in name:
    plot_title = "Boys punctuated (original) at age 10 model"
  elif "punctuacted_11" in name:
    plot_title = "Boys punctuated (original) at age 11 model"
  elif "punctuacted_12" in name:
    plot_title = "Boys punctuated (original) at age 12 model"
  elif "punctuated_nn_9" in name:
    plot_title = "Boys punctuated (revised) at age 9 model"
  elif "punctuated_nn_10" in name:
    plot_title = "Boys punctuated (revised) at age 10 model"
  elif "punctuated_nn_11" in name:
    plot_title = "Boys punctuated (revised) at age 11 model"
  elif "punctuated_nn_12" in name:
    plot_title = "Boys punctuated (revised) at age 12 model"
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

  heatmap.set_xlabel('Oldest', loc = 'right')
  heatmap.set_ylabel('Youngest', loc = 'top')

  c_bar = heatmap.collections[0].colorbar
  c_bar.set_ticks([df.min().min(), df.max().max()])
  c_bar.set_ticklabels(['Low', 'High'])
  
  plt.title(plot_title)
  plt.savefig(filepath, format="jpeg")

  plt.close

  plt.savefig(filepath, format="jpeg")

  plt.close


path = "/Users/scrockford/Library/CloudStorage/OneDrive-FondazioneIstitutoItalianoTecnologia/punctuated_similarity_test/results/boys/*.csv"

plotpath = "/Users/scrockford/Library/CloudStorage/OneDrive-FondazioneIstitutoItalianoTecnologia/punctuated_similarity_test/plots/boys"

for fname in glob.glob(path):

  data2plot = pd.read_csv(fname)
  plotname = os.path.basename(fname)
  plotname = plotname.replace(".csv", "")

  plt.clf()
  plot_heatmaps(data2plot, plotname, plotpath)

