"""
@author: Michał Wąsik
"""
from Graph import Graph_Transformation
from read_Graph import read_Graph

class GraphData:
   
    def __init__(self,G): #Done
        V, E = G.find_nodes_and_edges()
        supportlist=[]
        for i in range(len(V)):
            supportvar=1
            return1 = ''
            return2 = ''
            while(V[i][supportvar].isdigit()):
                return1 = return1 + V[i][supportvar]
                supportvar += 1
            return2 = V[i][len(V[i])-2]
            supportlist.append([return1,return2])
        self.V = supportlist
        supportlist=[]
        for i in range(len(E)):
            supportvar = 1
            return1 = ''
            return2 = ''
            while(E[i][supportvar].isdigit()):
                return1 = return1 + E[i][supportvar]
                supportvar += 1
            supportvar += 4
            while(supportvar < len(E[i]) and E[i][supportvar].isdigit()):
                return2 = return2 + E[i][supportvar]
                supportvar += 1
            supportlist.append([return1,return2])
        self.E = supportlist
        
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
                    if(node[0] == E[i][0]):
                        for j in range(len(V)):
                            if E[i][1] == V[j][0] and visited[j] != True:
                                visited[j] =  True
                                supportQue.append(V[j])
                    elif(node[0] == E[i][1]):
                        for j in range(len(V)):
                            if E[i][0] == V[j][0] and visited[j] != True:
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
        if(len(self.V) == 0):
            return None
        return round(2*len(self.E)/len(self.V),2)

    def average_ABCD_nodes_degree(self): #Done
        #średni stopień wierzchołka a b c d
        E = self.E 
        V = self.V 
        supportlist = []
        supportlist2 = []
        returnvar = 0
        #szukam wszystkich etykiet wierzcholkow a b c d
        for i in range(len(V)):
            if V[i][1] == 'a' or V[i][1] == 'b' or V[i][1] == 'c' or V[i][1] == 'd' :
                supportlist.append(V[i][0])
        
        #szukam wszystkich etykiet wierzcholkow polaczonych ze soba 
        for i in range(len(E)):
            supportlist2.append(E[i][0])
            supportlist2.append(E[i][1])

        #zliczam wszystkie krawędzie połaczone z wierzcholkiem a,b c lub d
        for i in range(len(supportlist)):
            for j in range(len(supportlist2)):
                if(supportlist[i] == supportlist2[j]):
                    returnvar += 1
        
        #dziele te polacznia przez liczbe wierzcholkow a,b,c,d
        if(len(supportlist) == 0):
            return None
        return round(returnvar/len(supportlist),2)

    def average_of_nodes_in_components(self): #Done
        #liczba wierzchołków przez ilośc spójnych składowych
        if(self.number_of_components() == 0):
            return None
        return round(len(self.V)/self.number_of_components(),2)
    
    def get_data(self): #Done
        data = [self.number_of_nodes(),self.number_of_edges(),
                self.number_of_components(),self.average_of_nodes_degree(),
                self.average_ABCD_nodes_degree(),self.average_of_nodes_in_components()]
        return data
    
    


