from collections import deque
def print_current(visited,r,c,start,end):
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
	print()

def bfs(maze,start,end):
	queue = deque()
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]
	queue.append((start[0], start[1], 0, None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(queue) != 0:
		coord = queue.popleft()
		#print(coord[0], coord[1], coord[2])
		visited[coord[0]][coord[1]] = True
		print_current(visited,r,c,start,end)
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
			#return coord[2]
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == 1 or visited[nr][nc]):
				continue
			queue.append((nr,nc,coord[2]+dir[2], coord))
	return 0,visited #no solution

def dfs(maze,start,end):
	queue = deque() #stack
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]
	queue.append((start[0], start[1], 0, None))
	visited = [[False]*c for x in range(r)] #2D array
	while len(queue) != 0:
		coord = queue.pop()
		visited[coord[0]][coord[1]] = True
		print_current(visited,r,c,start,end)
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == 1 or visited[nr][nc]):
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
	directions = [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]
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
		print_current(visited,r,c,start,end)
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == 1 or visited[nr][nc]):
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
	directions = [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]
	fringe.append((start[0], start[1], 0, 0,None))
	visited = [[False]*c for x in range(r)] #2D array
	print_current(visited,r,c,start,end)
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
		print_current(visited,r,c,start,end)
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == 1 or visited[nr][nc]):
				continue
			hn = calculate_hn((nr,nc), end)
			fringe.append((nr,nc,coord[2]+dir[2], hn, coord))
	return 0,visited #no solution
	
def a_star(maze,start,end):
	fringe = []
	#Down Up Right Left, for down cost = 1 up cost=2 right cost=3 left cost = 4 
	directions = [[1,0,1],[-1,0,2],[0,1,3],[0,-1,4]]
	fringe.append((start[0], start[1], 0, 0,None))
	visited = [[False]*c for x in range(r)] #2D array
	print_current(visited,r,c,start,end)
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
		print_current(visited,r,c,start,end)
		if(coord[0] == end[0] and coord[1] == end[1]):
			return coord, visited
		for dir in directions:
			nr, nc = coord[0] + dir[0], coord[1] + dir[1]
			if(nr < 0 or nr >= r or nc < 0 or nc >= c or maze[nr][nc] == 1 or visited[nr][nc]):
				continue
			fn = calculate_gn((nr,nc), start) + calculate_hn((nr,nc), end)
			fringe.append((nr,nc,coord[2]+dir[2], fn, coord))
	return 0,visited #no solution
	
def main():
	print("Start coordinates:")
	x = int(input())
	y = int(input())
	start = (x,y)
	print("Goal coordinates:")
	x = int(input())
	y = int(input())
	end = (x,y)
	if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
		print("No solution")
		exit()
	while(input("Do you want to use another search algorithm(y/n):") == "y"):
		print("1.Breadth First search(BFS)")
		print("2.Depth First search(DFS)")
		print("3.Uniform Cost search(UCS)")
		print("4.Best First Search(Greedy)")
		print("5.A*")
		print("Enter choice: ")
		ch = int(input())
		if ch == 1:
			print("USING BFS")
			a, visited = bfs(maze, start, end)
		elif ch == 2:
			a, visited = dfs(maze, start, end)
			print("USING DFS")
		elif ch == 3:
			a,visited = ucs(maze, start, end)
			print("USING UCS")
		elif ch == 4:
			a,visited = greedy(maze, start, end)
			print("USING GREEDY")
		else:
			a,visited = a_star(maze, start, end)
			print("USING A STAR(A*)")
			
		print("\n\n")
		if a== 0:
			print("no solution")
			return;
		print_current(visited,r,c,start,end)
		print("path cost:", a[2])
		if ch == 1 or ch == 2:#if bfs or dfs
			while(a[3]):
				print((a[0],a[1]), end="<=")
				a = a[3]
		else:
			while(a[4]):
				print((a[0],a[1]), end="<=")
				a = a[4]
		print((start))

if __name__ == "__main__":
	maze = [[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 1, 0, 1, 0],[0, 0, 0, 1, 0],[0, 1, 0, 1, 0],[0, 1, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 0, 0]]
	r = len(maze)
	c = len(maze[0])
	print("Maze is:")
	for i in range(r):
		for j in range(c):
			if maze[i][j] == 1:#block
					print("B", end=" ")
			else:
				print("_", end=" ")
		print()
	
	main()
