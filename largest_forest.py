def dfs(r, c):  
    area = 1 
    grid[r][c] = 0 
    paths = [(r-1, c), 
             (r+1, c), 
             (r, c-1),
             (r, c+1)] 

    for row, col in paths:
        if(row >= 0 and row < len(grid) and   
           col < len(grid[0]) and col >= 0 and 
           grid[row][col] == 1):  
            area += dfs(row, col) 
    return area
def largest_forest(grid):        
    max_area = float('-inf')     
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if(grid[r][c]==1):  
                max_area = max(max_area, dfs(r, c)) 
                
    return max_area if max_area!=float('-inf') else -1

r = int(input())
c = r
grid = []
for i in range(c):
    grid.append(input().split())
for j in range(c):
    for k in range(r):
        if grid[j][k]=='T':
            grid[j][k]=1
        else:
            grid[j][k]=0
print(largest_forest(grid))
    
    