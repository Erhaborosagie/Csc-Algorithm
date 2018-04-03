'''
#Python code for dept first search(dfs) and bread first search(bfs)

Initialize: put the start node into OPEN
while OPEN is not empty
    take a node N from OPEN
        if N is a goal node, report success
    put the children of N onto OPEN
Report failure
If OPEN is a stack, this is a depth-first search
If OPEN is a queue, this is a breadth-first search


'''

def dfs(tr,item):
	que=[list(tr.keys())[0]]
	path=[]
	while(que!=[]):
		a=que[0]
		path.append(a)
		if(a==item):
			return path
		que.pop(0)
		if a in tr:
			que = tr[a]+que
	return 'Item not found'

gr={'A':['B','C','D'],
	'B':['E','F'],
	'C':['G','H'],
	'D':['I','J'],
	'G':['N']
	}

def bfs(tr,item):
	que=[list(tr.keys())[0]]
	path=[]
	while(que!=[]):
		a=que[0]
		path.append(a)
		if(a==item):
			return path
		que.pop(0)
		if a in tr:
			que = que+tr[a]
	return 'Item not found'
