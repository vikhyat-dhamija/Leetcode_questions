class Solution:
    m=0
    n=0
    visited=[]
    colored=[]
    
    def dfs(self,grid,r,c,color,key):
        
        #condition to check that whether r and c are within bound
        if r < 0 or c < 0 or r >= self.m or c >= self.n:
            return
        
        if grid[r][c] == key and self.visited[r][c] != True:
            #condition of checking whether it belongs to the last,first column or row
            if r-1 < 0 or c-1 < 0 or r+1 >= self.m or c+1 >= self.n :
                self.colored.append(r*self.n + c)
                self.visited[r][c]=True  
            elif grid[r-1][c] != key or grid[r+1][c] != key or grid[r][c-1] != key or grid[r][c+1] != key:
                self.colored.append(r*self.n + c)
                self.visited[r][c]=True
            
            self.visited[r][c]=True
            
            self.dfs(grid,r-1,c,color,key)
            self.dfs(grid,r+1,c,color,key)
            self.dfs(grid,r,c-1,color,key)
            self.dfs(grid,r,c+1,color,key)
        
        
           
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        self.visited=[]
        self.colored=[]
        
        self.m=len(grid)
        self.n=len(grid[0])
        self.visited =  [[False for i in range(self.n)] for j in range(self.m)]
        
        self.dfs(grid,r0,c0,color,grid[r0][c0])
        
        for x in self.colored :
            r=int(x/self.n)
            c=x%self.n
            grid[r][c]=color
            
        return grid