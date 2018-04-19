class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        visited = [ [0 for x in range(len(image[0]))] for y in range(len(image))] 

        self.dfs(image,sr,sc,image[sr][sc],newColor,visited)
        return image
        
        
    def dfs(self,image,x,y,oldColor,newColor,visited):
        
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or visited[x][y]:
            return
        if image[x][y] != oldColor:
            return
        
        image[x][y] = newColor
        visited[x][y] = 1
        self.dfs(image,x+1,y,oldColor,newColor,visited)
        self.dfs(image,x,y+1,oldColor,newColor,visited)
        self.dfs(image,x-1,y,oldColor,newColor,visited)
        self.dfs(image,x,y-1,oldColor,newColor,visited)
        visited[x][y] = 0
