"""
@author: Michał Wąsik
"""


class GraphData:
    
    def __init__(self,V,E):
        self.E = E
        self.V = V

    def number_of_nodes(self): #Done
        #długość listy wierzchołków
        return len(self.V)

    def number_of_edges(self): #Done
        #długość listy krawędzi
        return len(self.E)

    def number_of_components(self): #Done
        def component_check():
            while len(supportQue) != 0:
                node = supportQue.pop(0)
                for i in range(len(E)):
                    if(node[1] == E[i][1]):
                        for j in range(len(V)):
                            if E[i][6] == V[j][1] and visited[j] != True:
                                visited[j] =  True
                                supportQue.append(V[j])
                    elif(node[1] == E[i][6]):
                        for j in range(len(V)):
                            if E[i][1] == V[j][1] and visited[j] != True:
                                visited[j] =  True
                                supportQue.append(V[j])
        E = self.E 
        V = self.V
        visited = [False]*len(V)
        supportQue =[]
        returnvar = 0
        for z in range(len(visited)):
            if(visited[z] == False):
                returnvar += 1
                visited[z] = True
                supportQue.append(V[z])
                component_check()
        return returnvar
        
    def average_of_nodes_degree(self): #Done
        #średni stopień wierzchołka
        return 2*len(self.E)/len(self.V)

    def average_ABCD_nodes_degree(self): #Done
        #średni stopień wierzchołka a b c d
        E = self.E 
        V = self.V 
        supportlist = []
        supportlist2 = []
        returnvar = 0
        #szukam wszystkich etykiet wierzcholkow a b c d
        for i in range(len(V)):
            if V[i][10] == 'a' or V[i][10] == 'b' or V[i][10] == 'c' or V[i][10] == 'd' :
                supportlist.append(V[i][1])
        
        #szukam wszystkich etykiet wierzcholkow polaczonych ze soba 
        for i in range(len(E)):
            supportlist2.append(E[i][1])
            supportlist2.append(E[i][6])

        #zliczam wszystkie krawędzie połaczone z wierzcholkiem a,b c lub d
        for i in range(len(supportlist)):
            for j in range(len(supportlist2)):
                if(supportlist[i] == supportlist2[j]):
                    returnvar += 1
        
        #dziele te polacznia przez liczbe wierzcholkow a,b,c,d
        return returnvar/len(supportlist)

    def average_of_nodes_in_components(self): #Done
        #liczba wierzchołków przez ilośc spójnych składowych
        return len(self.V)/self.number_of_components()
    
    def data_print(self): #Done
        data = [self.number_of_nodes(),self.number_of_edges(),self.number_of_components(),self.average_of_nodes_degree(),self.average_ABCD_nodes_degree(),self.average_of_nodes_in_components()]
        return ('number of nodes: ' + str(data[0]) + '\nnumber of edges: ' + str(data[1]) +
                '\nnumber of components:' + str(data[2]) + '\naverage of nodes degree: ' + str(data[3]) +
                '\naverage of "a,b,c,d" nodes degree: ' + str(data[4]) + '\naverage of nodes in components: ' + str(data[5]))
    

V = ['\t2 [label=c]', '\t3 [label=a]', '\t0 [label=Y]', '\t1 [label=c]', '\t4 [label=a]']
E = ['\t2 -- 1', '\t1 -- 3', '\t3 -- 2']
print(GraphData(V,E).data_print())

