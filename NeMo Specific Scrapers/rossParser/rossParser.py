import csv
import numpy as np
import itertools as itr
import matplotlib.pyplot as plt
import sys, argparse,os
import glob
import re
import plotly.plotly as py
import plotly.graph_objs as go


### Standard CMD Line Arg Parser / Main Entry Point


     


def loadNemoStats(filename="ross.csv",ehdrs="second_row_hdrs.csv",runhdrs="first_row_hdrs.csv"):
    endStats = []
    rawStats = []
    headers = []

    fullstats = {}


    with open(filename, newline='') as cvsfile:
        with open(ehdrs) as end_headers:
            with open(runhdrs) as first_headers:

                eheaders = csv.reader(end_headers,delimiter=",")
                oheaders = csv.reader(first_headers,delimiter=',')
                reader = csv.reader(cvsfile, delimiter=",")
                myRow = 0;
                for e_hdr in oheaders:
                    for elem in e_hdr:
                        headers.append(elem)          
                for e_hdr in eheaders:
                    for elem in e_hdr:
                        headers.append(elem) 
                
               # print (headers)
                
                myRow = 0
                oddRows = []
                evenRows = []
                values = []
                for line in reader:
                    
                    if (myRow % 2 == 0):
                        evenRows.append(line)
                    else:
                        oddRows.append(line)
                    myRow +=1
                for even, odd in zip(evenRows,oddRows):
                    values.append(even + odd)

                statsCSV = dict(zip(headers,values))
                print("\n\n\n*****************************************\n\n\n")
                #print(statsCSV)
                
    return headers,values
                                    
def combine(logdats, csvdats):
    pass

def createOut(filename,data):
    assert (isinstance(data,dict))
    headers = data.keys()
    values = data.values()


def parseLogs(path = os.curdir):
    logFiles = glob.glob(path+"*.log")
    print("Log files are " + str(logFiles))
    times = []
    effs = []
    evt_s = []
    names = []
    nodes = []
    ranks = []
    ranks_node = []
    prb = []
    srb = []
    res = {}
    res["ns_cores"] = []


    for file in logFiles:
        with open(file,"r") as f:
            filetxt = str(f.readlines())
            eff = re.search("Efficiency\s*(\d\d\D\d\d)",filetxt)

            eventsSecond = re.search("events.sec.\s*(\d*\D\d*)",filetxt)


            time = re.search("(\d+\D\d+)\ssec",filetxt)

            times.append(float(time.groups()[0]))
            evt_s.append(eventsSecond.groups()[0])
            #effs.append(eff.groups()[0])
            names.append(file)

            ranks.append(re.search("to be (\d+)",filetxt).groups()[0])
            nsc = re.search("cores=(\d+)",filetxt).groups()[0]
            res["ns_cores"].append(re.search("cores=(\d+)",filetxt).groups()[0])

            x = str(file)
            eff = re.search("N(\d+)",x)
            ranks_node.append( int(re.search("to be (\d+)",filetxt).groups()[0]) / int(eff.groups()[0]))
            print(ranks_node)

            #rollback data
            prb.append(int(re.search("Primary Roll Backs\s*(\d+)",filetxt).groups()[0]))
            srb.append(int(re.search("Secondary Roll Backs\s*(\d+)",filetxt).groups()[0]))




        x = str(file)
        eff = re.search("N(\d+)",x)
        print(eff.group())
        nodes.append(eff.groups()[0])



    res["names"] = names
    res["times"] = times
    #res["effs"] = effs
    res["evts_second"] = evt_s
    res["nodes"] = nodes
    res["ranks"] = ranks
    res["ranks_per_node"] = ranks_node
    res["primary_rollbacks"] = prb
    res["secondary_rollbacks"] = srb
    return res







    #with open(filename, newline='') as cvsfile:
    #    with open(ehdrs) as end_headers:
    #        eheaders = csv.reader(end_headers,delimiter=",")
    #        reader = csv.reader(cvsfile, delimiter=",")
    #        for rowl,hdrl in zip(reader,eheaders):
    #            if (myRow % 2 == 0):
                
    #                #print(",".join(row))
    #                print("Shoud be even row")
    #                for col,hdr in zip(rowl,hdrl):
    #                    endStats.append((hdr,col))
    #                    print(str(hdr) + "->" + str( col))
    #            else:
    #                #print(",".join(row))
    #                print("Should be odd row")
    #            myRow += 1

    

parser = argparse.ArgumentParser(description="Parse and Graph Nemo Ross Results")





parser.add_argument('-g', help='graph results', action='store_true')
parser.add_argument('-Svc', help='specify save file name',default="saved_stats.csv")
parser.add_argument('-p', help="specify log file reading dir", default="/Users/mplagge/Google Drive/RPI Work/tn_work/post-fix runs/runs/8k_runs/")
parser.add_argument('-rc', help='ross csv file', default="ross.csv")
parser.add_argument('-log', help="read only log files", default=False, action='store_true')

args = parser.parse_args()

if not args.log:
    #load ross.csv file and headers
    print("loading from ross CSV file at " + args.rc)
    heads, values = loadNemoStats(args.rc)
    output = heads + values
    #print (output)
    runtimeIDX = heads.index("Total Time")
    runtimes = []
    effI = heads.index("Efficiency")
    effs = []
    evtrate = []
    evtrI = heads.index("Event Rate")
    ## Runtime Params for categories
    num_nodes = []
    num_nodesI = heads.index("Total Processors")
    num_ranks = []
    num_ranksI = heads.index("Total Nodes")
    ns_cores = []




    for row in values:
        runtimes.append (row[runtimeIDX])
        effs.append(row[effI])
        evtrate.append(row[evtrI])
        num_nodes.append(row[num_nodesI])
        num_ranks.append(row[num_ranksI])

    big = [list(i) for i in zip(num_nodes,runtimes)]

    big = np.array(big)
    space = 0.3

    conditions = np.unique(big[:,0])
    categories = np.unique(big[:,0])

    n = len(categories)
    width = (1 - space) / (len(conditions))

    for i,cond in enumerate(conditions):


        vals = big[big[:,0] == cond][:,1].astype(np.float)
        pos = [j - (1-space) / 2. + i * width for j in range(1,len(categories) + 1)]
    #    ax.bar(vals)


    outt = list(big)
    outt = []
    for i in big:
        outt.append([i[0],i[1]])




        #np.savetxt(out,outt,delimiter=',')


logdata = parseLogs(args.p)

print(logdata)

hds = logdata.keys()
vls = list(logdata.values())

#save to disk
with open(args.Svc,"w") as f:
    w = csv.writer(f)
    w.writerow(hds)
    data = np.array(vls).transpose()
    w.writerows(data)


##Plotting

x1 = logdata["ranks_per_node"]
y1 = logdata["times"]

traces = []

rpns = {}
# for rpn,times,evts,cores in zip(x1,y1,logdata["evts_second"],logdata["ns_cores"]):
#     evts = float(evts)
#     cores = int(cores)
#     print(str(rpn) + "->" + str(times))
#     if str(rpn) not in rpns.keys():
#         rpns[str(rpn)] = []
#     rpns[str(rpn)].append([rpn,times,evts,cores])
#
# trace1 = go.Bar(
#     x=rpns["32.0"][0][2],
#     y=rpns["32.0"][0][1],
#     name="32 ranks per node")
# layout = go.Laoyout(barmode='group')
# fig = go.Figure(data=trace1,layput=layout)

print(rpns)





