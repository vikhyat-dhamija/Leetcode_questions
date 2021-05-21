class Solution:
    
    count=0    
    m=0        
    n=0
    
    
    def dfs(self,grid,r,c):
        
        if r >= self.m or r < 0 or c >= self.n or c < 0 :
            return
            
        if grid[r][c] == "2" or  grid[r][c] == "0" :
            return
        
        grid[r][c]="2" ;
        
        self.dfs(grid,r+1,c);
        
        self.dfs(grid,r-1,c);
        
        self.dfs(grid,r,c+1);
        
        self.dfs(grid,r,c-1);
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #Traversing the 2 d array
        self.m=len(grid);
        self.n=len(grid[0]);
        
        for j in range(self.m):
            for i in range(self.n):
                if grid[j][i] == "1" :
                    self.dfs(grid,j,i)
                    self.count+=1                    
        
        return self.count