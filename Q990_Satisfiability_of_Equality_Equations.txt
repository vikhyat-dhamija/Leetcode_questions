class Solution:
    
    parent=[]
    size=[]
    
    def root(self,x):
        r=x     
        while r != self.parent[r]:
            r = self.parent[r]            
        return r
            
    def union(self,ch1,ch2):
        
        x= ord(ch1)-ord('a')
        y= ord(ch2)-ord('a')
        
        x_=self.root(x)
        y_=self.root(y)
        
        if self.size[x_] > self.size[y_]:
             self.parent[y_]=self.parent[x_]
        elif self.size[x_] < self.size[y_]:
            self.parent[x_]= self.parent[y_]
        else:
            self.parent[x_]= self.parent[y_]
            self.size[y_]+=1
        
    def find(self,ch1,ch2):
        
        x= ord(ch1)-ord('a')
        y= ord(ch2)-ord('a')
        
        return self.root(x) == self.root(y)
            
    def equationsPossible(self, equations: List[str]) -> bool:
        
        self.parent=[i for i in range(26)]
        self.size=[1]*26
        res=True
        
        for i in equations:
            if i[1] == '=':
                self.union(i[0],i[3])
                
        for i in equations:
            if i[1] == '!':
                res=res and not (self.find(i[0],i[3]))
                
        return res