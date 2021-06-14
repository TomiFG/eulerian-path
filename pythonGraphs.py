class graph:

    """
    Just a simple graph object
    
    V : list of the graph's vertices
    E : list of lists representing the graph's edges 

    get_adj(v) : takes the name of a vertex as an argument and returns a list of adjacent vertices
    rem_edge(e) : takes a list of two vertices and if there's a matching edge it removes it from the graph
    """

    def __init__(self, V=[], E=[]):
        self.V = V.copy()
        self.E = E.copy()
   
    def get_edges(self):
        return self.E

    def get_vertices(self):
        return self.V

    def get_adj(self, v):        
        self.adjList = [([a] + [v for [x, v] in self.E if x==a] + [v for [v, x] in self.E if x==a]) for a in self.V] 
        for l in self.adjList:
            if l[0] == v:
                return l[1:]
        return []

    def rem_edge(self, e):
        a, b = e
        if [a,b] in self.E:
            self.E.remove([a,b])
        elif [b,a] in self.E:
            self.E.remove([b,a])
    

def r_max(L, v_ini):
    
    """ Takes a graph L and and a vertex v and returns a maximal trial starting at v """  
    
    M = graph(L.get_vertices(), L.get_edges())

    sub_walk = [v_ini]    
    p0 = v_ini

    while len(M.get_adj(p0)) > 0:
        p1 = M.get_adj(p0)[0] 
        sub_walk.append(p1)
        M.rem_edge([p0, p1])
        p0=p1

    return sub_walk 


def euler_walk(L, v_ini):
    
    """ Takes a graph L and a vertex v and returns an eulerian walk given some assumptions """

    temp_walk = r_max(L, v_ini)
    free = graph(L.get_vertices(), L.get_edges())

    for i in range(len(temp_walk)-1):
        free.rem_edge([temp_walk[i], temp_walk[i+1]])
    
    while len(u_list := [x for x in temp_walk if len(free.get_adj(x))>0 ]):
        pos = temp_walk.index(u_list[0]) 
        second_walk = euler_walk(free, u_list[0])  
      
        temp_walk = temp_walk[:pos] + second_walk + temp_walk[pos+1:]
        
        for i in range(len(temp_walk)-1):
            free.rem_edge([temp_walk[i], temp_walk[i+1]])

    return temp_walk
