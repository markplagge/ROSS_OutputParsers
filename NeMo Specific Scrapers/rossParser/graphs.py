import csv
import numpy as np
import itertools as itr
import matplotlib.pyplot as plt
import sys, argparse,os
import glob
import re
import plotly.plotly as py
import plotly.graph_objs as go
import math,cmath
import matplotlib
def plot8x():
    plt.cla()
    vals = [74363023,104901179.5,150906010.6,249698356.9,405189089.4]
    vals =  list(map (lambda v: v / 1000000,vals))
    nodes=[16,32,64,128,512]
    n_cores = [8192] * 5
    fix,ax = plt.subplots()
    index = np.arange(5)
    bar_width = .5
    opacity=.7
    rects = ax.bar(index, vals,bar_width,
                    alpha=opacity,
                   color='b',
                   label="8096 Neurosynaptic Cores")

    xfmt = matplotlib.ticker.ScalarFormatter(useMathText=True)

    plt.xlabel("BG/Q Nodes")
    plt.ylabel("Million Events/Second")
    plt.title("Comparison of NEMO strong scaling on IBM BlueGene/Q")
    plt.xticks(index + bar_width, nodes)
    plt.legend(loc=2)
    plt.tight_layout()

    #plt.show()

    plt.savefig("/Users/mplagge/Documents/PADS_2016/result_img/8xScale.png",dpi=1200,format="png")




def plt32():
    py.sign_in('mplagge', '125b8zplco')
    trace1 = go.Bar(
    x = ['16 bg/q nodes','32 bg/q nodes','64 bg/q nodes','128 bg/q nodes','256 bg/q nodes','512 bg/q nodes'],
    y = [33697889,57873993.2,114515211.4,208556951.9,452170796,863188691.1],
    name='32 MPI Ranks Per Node'
    )
    trace2 = go.Bar(
        x=['16 bg/q nodes','32 bg/q nodes',"64 bg/q nodes","128 bg/q nodes","256 bg/q nodes","512 bg/q nodes"],
        y=[44406330.9,76405419.9,144641856.8,255837316.1,542637813,1031309534],
        name="64 MPI Ranks Per Node"

    )
    layout = go.Layout(barmode='group')
    fig = go.Figure(data = [trace1,trace2], layout=layout)
    plot_url=py.plot(fig,filename="gb-d")


#plt32()

n_groups = 6

vals_32 = [33697889.0,57873993.2,114515211.4,208556951.9,452170796.0,863188691.1]
vals_64 = [44406330.9,76405419.9,144641856.8,255837316.1,542637813.0,1031309534.0]


vals_32 = list(map (lambda v: v / 1000000,vals_32))
vals_64 =list( map (lambda v: v / 1000000,vals_64))
ns_cores = [1024,2048,4096,8192,16384,32768]
cats = []
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width=0.35
opacity = 0.7

rects1 = ax.bar(index, vals_32,bar_width,
                 alpha=opacity,
                 color='b',
                 label="32 MPI Ranks per Node")
rects2 = ax.bar(index + bar_width, vals_64,bar_width,
                 alpha=opacity,
                 color='r',
                 label="64 MPI Ranks per Node")

x_ax = [16,32,64,128,256,512]

def autolabel(rects,vals):

    for rect, i in zip(rects, range(6)):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()-.3,
                np.log2(height)+ height,
                '%d\nCores' % int(vals[i]), style='italic',
                rotation='vertical',
                ha='center', va='bottom')

#autolabel(rects1,ns_cores)
autolabel(rects2,ns_cores)
xfmt = matplotlib.ticker.ScalarFormatter(useMathText=True)


#ax.ticklabel_format(axis='y',style='plain')

plt.xlabel("BG/Q Nodes")
plt.ylabel("Event Rate (Million Events/Second)")
plt.title("Comparison of NEMO weak scaling on IBM BlueGene/Q")
plt.xticks(index + bar_width, x_ax)


plt.legend(loc=2)
plt.tight_layout()


plt.savefig("/Users/mplagge/Documents/PADS_2016/result_img/weaksc.png",dpi=1200,format="png")
print("Done")
plot8x()
