import numpy as np
import pandas
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.style.use('ggplot')

path = '/Users/mplagge/Google Drive/RPI Work/tn_work/graphing/csv_stats_processed/'

#Eff Graphs
#with open(path + "8x_eff_stats.csv") as f:

eff8x = pandas.read_csv(path + "8x_eff_stats.csv",
                        skipinitialspace=True)

eff8x.plot(x='Nodes',y='Efficiency')
eff8x.plot(secondary_y=True, x="Nodes", y='Run Time')
print("loaded files.")



plt.show()
