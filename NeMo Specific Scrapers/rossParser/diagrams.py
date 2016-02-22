import networkx as nx
import numpy as np

from collections import OrderedDict
class OrderedNodeGraph(nx.DiGraph):
    node_dict_factory=OrderedDict

def main():
    import matplotlib
    axonN = 2
    """ 5x5
    0	5	6	7	8	9
    1	10	11	12	13	14
    2	15	16	17	18	19
    3	20	21	22	23	24
    4	25	26	27	28	29
        30	31	32	33	34
    """
    ##PARMS
    synapseN = np.power(axonN,2)
    neuronN = axonN
    nodeN = axonN + synapseN + neuronN

    axons = []
    neurons = []
    synapses = []
    for i in range(nodeN):
        if i < axonN:
            axons.append(i)
        elif i < (synapseN + axonN):
            synapses.append(i)
        else:
            neurons.append(i)


    print(synapses)
    print(axons)
    axpaths = []
    npaths = []


    G = OrderedNodeGraph()
    for a in axons:
        i = 0
        aName = "A " + str(a)
        pth = [aName]

        for s in synapses[a*axonN:axonN + (a * axonN)]:
            synName = "S " + str(s)
            print(str(a) + "->" + str(s))
            pth.append(synName)
            npaths.append((synName,str("N " + str(neurons[i]))))
            i += 1
        axpaths.append(pth)
    print(axpaths)
    print( npaths)
    for path in axpaths:
        G.add_path(path)
    for path in npaths:
        G.add_path(path)


    r = nx.grid_graph([1,5])

    nx.spring_layout(G)
    nx.spectral_layout(G)
    nx.draw(G)
    nx.draw_networkx(r)

    nx.write_graphml(G,'./out.gml')
    nx.write_dot(G,'./out.dot')

#input("WAIT")
def outF():
    ins = [	'S_{1,1}',	'S_{1,2}',	'S_{1,3}',	'S_{1,4}',	'S_{1,N}',
	'S_{2,1}',	'S_{2,2}',	'S_{2,3}',	'S_{2,4}',	'S_{2,N}',
	'S_{3,1}',	'S_{3,2}',	'S_{3,3}',	'S_{3,4}',	'S_{3,N}',
    'S_{4,1}',	'S_{4,2}',	'S_{4,3}',	'S_{4,4}',	'S_{4,N}',
	'S_{N,1}',	'S_{N,2}',	'S_{N,3}',	'S_{N,4}',	'S_{N,N}',
	]
    axs = ['AX_{1}',
    'AX_{2}',
    'AX_{3}',
    'AX_{4}',
    'AX_{5}']
    ns = ['N_{1}',	'N_{2}',	'N_{3}',	'N_{4}',	'N_{N}']
    apath = []
    i = 0
    for axon in axs:
        i = 0


    bnet = []



if __name__ == '__main__':
    main()

