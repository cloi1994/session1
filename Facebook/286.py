class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        
        q = []
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0: # gate
                    q.append([i,j])
        
        while q != []:
            x,y = q.pop(0)
            self.addToQueue(x+1,y,rooms,rooms[x][y]+1,q)
            self.addToQueue(x,y+1,rooms,rooms[x][y]+1,q)
            self.addToQueue(x-1,y,rooms,rooms[x][y]+1,q)
            self.addToQueue(x,y-1,rooms,rooms[x][y]+1,q)
        
    def addToQueue(self,x,y,rooms,steps,q):
        
        if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]):
            return
        if rooms[x][y] == -1 or rooms[x][y] != 2147483647:
            return
        rooms[x][y] = steps 
        q.append([x,y])
