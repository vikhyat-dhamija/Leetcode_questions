class Solution:
    
    #This is to form the connected component for starting the bread first traversal to find the shortest distance to
    #reach the destination
    
    dist=0
    m=0
    n=0
    
    cc=[]
    
    def dfs(self,r,c,grid):
        
        if r >= self.m or r < 0 or c >= self.n or c < 0:
            return
        
        if grid[r][c] == 0:
            return
        
        if grid[r][c] == 1 :
            
            self.cc.append( r * self.n + c)
            grid[r][c] = 2  
            self.dfs(r,c+1,grid)
            self.dfs(r,c-1,grid)
            self.dfs(r-1,c,grid)
            self.dfs(r+1,c,grid)
            
          
    def bfs(self,cc,grid):
        
        ncc=[]
        flag=0
        
        for i in cc:
            
            r= int (i /self.n)
            c=i % self.n
            
            if r+1 <= self.m -1:
                if grid[r+1][c] == 0:
                    grid[r+1][c] = 2
                    ncc.append((r+1) * self.n + c)
                    
                elif grid[r+1][c] == 1:
                    flag=1
                    break
                
            if r-1 >= 0 :
                if grid[r-1][c] == 0:
                    grid[r-1][c] = 2
                    ncc.append((r-1) * self.n + c)
                    
                elif grid[r-1][c] == 1:
                    flag=1
                    break
                
            if c+1 <= self.n-1 :
                if grid[r][c+1] == 0:
                    grid[r][c+1] = 2
                    ncc.append((r) * self.n + c+1 )
                    
                elif grid[r][c+1] == 1:
                    flag=1
                    break
                  
            if c-1 >= 0:
                if grid[r][c-1] == 0:
                    grid[r][c-1] = 2
                    ncc.append((r) * self.n + c-1)
                    
                elif grid[r][c-1] == 1:
                    flag=1
                    break
        
        if flag == 0 :  
            self.dist+=1
            self.bfs(ncc,grid)
        
        
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        self.cc=[]
        
        self.m = len(grid)
        self.n = len(grid[0])
        flag=0
            
        for i in range(self.m): 
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(i,j,grid)
                    flag=1
                    break
            if flag ==1 :
                break
                    
        self.bfs(self.cc , grid) 
        
        return self.dist