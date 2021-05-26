class Solution:
    
    visited=[]
    parent=[]
    time=[]
    low=[]
    t=0
    
    result=[]
    
    def dfs(self,graph,n,p):
        
        if self.visited[n] == False: 
            self.parent[n]=p
            self.visited[n]=True
            self.time[n]=self.t
            self.low[n]=self.t
            self.t+=1
            
            for i in graph[n]:
                if self.parent[n] != i :
                    self.dfs(graph,i,n)
                    self.low[n]=min(self.low[n],self.low[i])
        
                    if self.low[i] > self.time[n]:
                        self.result.append([n,i])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        #Complete the function
        graph={}
       
        #Creation of the graph
        for i in connections :
            
                if graph.get(i[0]) == None:
                    graph[i[0]]= [i[1]]

                else:
                    graph[i[0]].append(i[1])

                if graph.get(i[1]) == None:
                    graph[i[1]]= [i[0]]

                else:
                    graph[i[1]].append(i[0])
                    
        m=max(graph.keys())
        
        self.visited = [False]*(m+1)
        self.parent = [-1]*(m+1)
        self.time = [-1]*(m+1)
        self.low = [-1]*(m+1)
        
        self.result=[]
        
        for i in range(m+1):
            if self.visited[i] == False:
                self.dfs(graph,i,-1)
            
        return self.result 