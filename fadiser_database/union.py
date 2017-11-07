def find(idx, parents):




def union(idx, new_idx, parents):
	root1 = find(idx, parents)
	root2 = find(new_idx, parents)
	return root1 == root2






def numIslands(self, grid):
    row = len(grid)
    if row == 0:
        return 0
    col = len(grid[0])
     
    #mark = [x[:] for x in [[True]*col]*row]
    mark = [[1 for x in range(col)] for x in range(row)]
     
    res  = 0
     
    q = []
     
    for i in range(0,row):
        for j in range(0, col):
            if grid[i][j] == '1' and mark[i][j] == 1:
                q.append([i,j])
                mark[i][j] = False
                while q:
                    ii = q[0][0]
                    jj = q[0][1]
                    q.pop(0)
                     
                    if ii+1 < len(grid) and grid[ii+1][jj] == '1' and mark[ii+1][jj] == 1:
                        q.append([ii+1, jj])
                        mark[ii+1][jj] = 0
             
                    if jj+1 < len(grid[0]) and grid[ii][jj+1] == '1' and mark[ii][jj+1] == 1:
                        q.append([ii, jj+1])
                        mark[ii][jj+1] = 0
             
                    if ii-1 >= 0 and grid[ii-1][jj] == '1' and mark[ii-1][jj] == 1:
                        q.append([ii-1, jj])
                        mark[ii-1][jj] = 0
             
                    if jj-1 >=0 and grid[ii][jj-1] == '1' and mark[ii][jj-1] == 1:
                        q.append([ii, jj-1])
                        mark[ii][jj-1] = 0

                    if jj-1 >=0 and ii-1>=0 grid[ii-1][jj-1] == '1' and mark[ii-1][jj-1] == 1:
                        q.append([ii-1, jj-1])
                        mark[ii-1][jj-1] = 0

                    if jj+1 < col and ii+1 < row grid[ii+1][jj+1] == '1' and mark[ii+1][jj+1] == 1:
                        q.append([ii+1, jj+1])
                        mark[ii+1][jj+1] = 0


                    if jj+1 < col and ii-1 <= 0 grid[ii-1][jj+1] == '1' and mark[ii-1][jj+1] == 1:
                        q.append([ii-1, jj+1])
                        mark[ii-1][jj+1] = 0

                    if jj-1 >= 0 and ii+1 < row grid[ii+1][jj-1] == '1' and mark[ii+1][jj-1] == 1:
                        q.append([ii+1, jj-1])
                        mark[ii+1][jj-1] = 0

                res += 1       
                     
    return res




def count_islands(image):
	m = len(image)
	n = len(image[0])
	for i in range(len(image)):
		for j in range(len(image[0])):
			idx = m * i + j
			parents[idx] = idx
			if image[i][j][0] != 1.:
				continue
			dirs = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1)]
			# num += 1
			for d in dirs:
				i1, j1 = i + d[0], j + d[1]
				new_idx = m * i1 + j1
				if i1 < 0 or j1 < 0 or i1 >= m or j1 >= n or image[i1][j1][0] != 1.:
					continue
				if not union(idx, new_idx, parents):
					num += 1
