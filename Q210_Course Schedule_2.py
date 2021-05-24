class Solution:
    
    visited=[]
    color=[]
    iscycle=0
      
    def dfs(self,graph,i,res):
        
        if self.color[i] == True:
            self.iscycle = 1
            return
        
        if self.visited[i] == True:        
            return
        
        self.color[i] = True 
          
        if len(graph[i]) == 0:
            self.visited[i]=True
            self.color[i] = False
            return res.insert(0,i)
        
        for x in graph[i]:
            self.dfs(graph,x,res)
        
        self.visited[i]=True
        res.insert(0,i)  
        self.color[i] = False
    
        return res    
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph={}
        
        self.iscycle = 0
        self.visited =[False] * numCourses
        self.color = [False] * numCourses
        
        starts=[]
        
        #numCourses are the number of vertices
        for i in range(numCourses):
            graph[i]=[]
        
        for i in range(len(prerequisites)):
            if graph.get(prerequisites[i][1]) == None :
                graph[prerequisites[i][1]]=[prerequisites[i][0]]
            else:
                graph[prerequisites[i][1]].append(prerequisites[i][0])
            
                
        #This provides the graph in the form of hashmap
        res=[]
              
        for i in range(numCourses):
            self.dfs(graph,i,res)
                      
        if self.iscycle == 1:
            return []
        else:
            return res