from collections import deque

def bfs(maze,start,end):
	queue = deque()
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]
	queue.appendleft((start[0], start[1], 0, None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(queue) != 0:
		coord = queue.pop()
		#print(coord[0], coord[1], coord[2])
		visited[coord[0]][coord[1]] = True
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
			#return coord[2]
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == "1" or visited[nr][nc]):
				continue
			queue.appendleft((nr,nc,coord[2]+dir[2], coord))
	return 0,visited #no solution

def dfs(maze,start,end):
	queue = deque()
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]
	queue.append((start[0], start[1], 0, None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(queue) != 0:
		coord = queue.pop()
		visited[coord[0]][coord[1]] = True
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == "1" or visited[nr][nc]):
				continue
			queue.append((nr,nc,coord[2]+dir[2], coord))
	return 0,visited #no solution
	
def calculate_gn(current, start):
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4
	if current[0] > start[0]:#down
		if current[1] > start[1]:#right
			return abs(current[0]-start[0])+(abs(current[1]-start[1])*3)
		else:#left
			return abs(current[0]-start[0])+(abs(current[1]-start[1])*4)
	else:#up
		if current[1] > start[1]:#right
			return (abs(current[0]-start[0])*2)+(abs(current[1]-start[1])*3)
		else:#left
			return (abs(current[0]-start[0])*2)+(abs(current[1]-start[1])*4)
		
def ucs(maze,start,end):
	fringe = []
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]
	fringe.append((start[0], start[1], 0, 0,None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(fringe) != 0:
		coord = fringe[0]
		k = coord[3]
		#getting minimun g(n)
		for fr in fringe:
			if k > fr[3]:
				coord = fr
				k = fr[3]
		fringe.remove(coord)
		visited[coord[0]][coord[1]] = True
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == "1" or visited[nr][nc]):
				continue
			gn = calculate_gn((nr,nc), start)
			fringe.append((nr,nc,coord[2]+dir[2], gn, coord))
	return 0,visited #no solution
	
def calculate_hn(current, end):
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4
	if end[0] > current[0]:#down
		if end[1] > current[1]:#right
			return abs(end[0]-current[0])+(abs(end[1]-current[1])*3)
		else:#left
			return abs(end[0]-current[0])+(abs(end[1]-current[1])*4)
	else:#up
		if end[1] > current[1]:#right
			return (abs(end[0]-current[0])*2)+(abs(end[1]-current[1])*3)
		else:#left
			return (abs(end[0]-current[0])*2)+(abs(end[1]-current[1])*4)
		
def greedy(maze,start,end):
	fringe = []
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]
	fringe.append((start[0], start[1], 0, 0,None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(fringe) != 0:
		coord = fringe[0]
		k = coord[3]
		#getting minimun g(n)
		for fr in fringe:
			if k > fr[3]:
				coord = fr
				k = fr[3]
		fringe.remove(coord)
		visited[coord[0]][coord[1]] = True
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == "1" or visited[nr][nc]):
				continue
			hn = calculate_hn((nr,nc), end)
			fringe.append((nr,nc,coord[2]+dir[2], hn, coord))
	return 0,visited #no solution
	
def a_star(maze,start,end):
	fringe = []
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]
	fringe.append((start[0], start[1], 0, 0,None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(fringe) != 0:
		coord = fringe[0]
		k = coord[3]
		#getting minimun g(n)
		for fr in fringe:
			if k > fr[3]:
				coord = fr
				k = fr[3]
		fringe.remove(coord)
		visited[coord[0]][coord[1]] = True
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == "1" or visited[nr][nc]):
				continue
			fn = calculate_gn((nr,nc), start) + calculate_hn((nr,nc), end)
			fringe.append((nr,nc,coord[2]+dir[2], fn, coord))
	return 0,visited #no solution
	
def main():
	#bfs
	print("\n\n")
	a, visited = bfs(maze, start, end)
	if a== 0:
		print("no solution")
		return;
	print("USING BFS")
	for i in range (r):
		for j in range (c):
			if visited[i][j] == True:
				if start[0] == i and start[1] == j:
					print("S", end=" ")
				elif end[0] == i and end[1] == j:
					print("E", end=" ")
				else:
					print("x",end=" ")
			else:
				print("_",end=" ")
		print()
	print("path cost:", a[2])
	while(a[3]):
		print((a[0],a[1]), end="<=")
		a = a[3]
	print((start))

	print("\n\n")
	#dfs
	a, visited = dfs(maze, start, end)
	print("USING DFS")
	for i in range (r):
		for j in range (c):
			if visited[i][j] == True:
				if start[0] == i and start[1] == j:
					print("S", end=" ")
				elif end[0] == i and end[1] == j:
					print("E", end=" ")
				else:
					print("x",end=" ")
			else:
				print("_",end=" ")
		print()
		
	print("path cost:", a[2])
	while(a[3]):
		print((a[0],a[1]), end="<=")
		a = a[3]
	print((start))

	print("\n\n")
	#ucs
	a,visited = ucs(maze, start, end)
	print("USING UCS")
	for i in range (r):
		for j in range (c):
			if visited[i][j] == True:
				if start[0] == i and start[1] == j:
					print("S", end=" ")
				elif end[0] == i and end[1] == j:
					print("E", end=" ")
				else:
					print("x",end=" ")
			else:
				print("_",end=" ")
		print()
		
	print("path cost:", a[2])
	while(a[4]):
		print((a[0],a[1]), end="<=")
		a = a[4]
	print((start))

	print("\n\n")
	#greedy
	a,visited = greedy(maze, start, end)
	print("USING GREEDY")
	for i in range (r):
		for j in range (c):
			if visited[i][j] == True:
				if start[0] == i and start[1] == j:
					print("S", end=" ")
				elif end[0] == i and end[1] == j:
					print("E", end=" ")
				else:
					print("x",end=" ")
			else:
				print("_",end=" ")
		print()
		
	print("path cost:", a[2])
	while(a[4]):
		print((a[0],a[1]), end="<=")
		a = a[4]
	print((start))

	print("\n\n")
	#A*
	a,visited = a_star(maze, start, end)
	print("USING A STAR(A*)")
	for i in range (r):
		for j in range (c):
			if visited[i][j] == True:
				if start[0] == i and start[1] == j:
					print("S", end=" ")
				elif end[0] == i and end[1] == j:
					print("E", end=" ")
				else:
					print("x",end=" ")
			else:
				print("_",end=" ")
		print()
		
	print("path cost:", a[2])
	while(a[4]):
		print((a[0],a[1]), end="<=")
		a = a[4]
	print((start))

if __name__ == "__main__":
	fp = open("data.txt", "r");
	maze = [[num for num in line.split(' ')] for line in fp]
	r = len(maze)
	c = len(maze[0])
	print("Maze is:")
	for i in range (r):
		for j in range (c):
			if maze[i][j] == "1":#block
					print("B", end=" ")
			else:
				print("_", end=" ")
		print()

	#start = (0,0);end = (7,0)
	#start=(0,0);end = (8,0)#no solution
	#start = (4,4);end = (7,2)
	start = (5,2);end = (7,4)
	#start = (7,0);end = (0,0)
	#start = (1,3);end = (2,2)#no solution
	
	if maze[start[0]][start[1]] == '1' or maze[end[0]][end[1]] == '1':
		print("No solution")
		exit()
	main()
