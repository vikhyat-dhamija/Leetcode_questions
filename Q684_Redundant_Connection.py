class Solution:
    
    visited=[]
    max_vert=0
    visit_c=0
        
    def restore(self,graph,i):
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    def remove(self,graph,i):
        graph[i[0]].remove(i[1])
        graph[i[1]].remove(i[0])
    
    
    def dfs(self,graph,n):
        
        if self.visited[n] == True :
            return
        
        adj=graph[n]
        self.visited[n] = True
        self.visit_c+=1

        for i in adj:
            self.dfs(graph,i)
        
        
    
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph={}
        v_count=0
        ret=[]
        
        #Creation of the graph
        for i in edges:
            if graph.get(i[0]) == None:
                graph[i[0]]= [i[1]]
                
                v_count+=1
            else:
                graph[i[0]].append(i[1])
            
            if graph.get(i[1]) == None:
                graph[i[1]]= [i[0]]
                v_count+=1
            else:
                graph[i[1]].append(i[0])
                
        self.max_vert=max(graph.keys())
        
        
       
        #Then check by removing one edge and then performing the dfs
        for i in edges[::-1]:
            self.remove(graph,i)
            self.visited=[False] * (self.max_vert+1)
            self.visit_c=0
            self.dfs(graph,1)
            self.restore(graph,i)
            
            #print(self.visit_c,v_count)
            
            if self.visit_c == v_count :
                ret=i
                break
                
        return ret