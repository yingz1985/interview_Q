def criticalConnection(numOfWarehouses, numOfRoads, roads):
    if numOfWarehouses==0 or numOfRoads ==0:
        return []
    matrix = [[0]*numOfWarehouses for _ in range(numOfWarehouses)]
    #initialize the graph
    for i in range(numOfRoads):
        start = roads[i][0]-1
        end = roads[i][1]-1
        matrix[start][end]=1 
        matrix[end][start]=1 
    out = []
    for i in range(numOfRoads):
        count = 1
        start=roads[i][0]-1
        end=roads[i][1]-1
        matrix[start][end]=0
        matrix[end][start]=0
        start=numOfWarehouses//2
        visited = [False]*numOfWarehouses
        queue= []
        queue.append(start)
        visited[start] = True
        #if breadth first search doesn't find all the warehouses
        while queue:
            start = queue.pop(0)
            for i in matrix[start]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i] = True
                    count+=1
        
        if count<numOfWarehouses:
            out.append([start+1,end+1])
        matrix[start][end]=1
        matrix[end][start]=1 
        
        
    return out
