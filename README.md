# Broadcasting-scheme modeling
Places of requests represented as nodes, roads as edges on graph G = (V,E) <br />
Given a network V = {1,…, N} is the set of nodes, E in VxV is the set of links between nodes. 
A node s in V is the source node which will transmit a package to others nodes. 
A node receiving the package can continue transmit this package to adjacent nodes. <br />
t(i,j) and c(i,j) are transmission time and transmission cost when transmitting the package from node i to node j. 
Compute the set of links used for broadcasting the package from the source node to all other nodes such that: <br />
Total transmission time from s to any node cannot exceed a given value L <br />
Total transmission cost is minimal <br />
# Input
Line 1: contains 4 positive integers n,m,s,L (1 <= n, m <= 20, 1 <= L <= 100) <br />
Line i+1 (i = 1, 2, . . ., m): contains 4 integers u,v,t,c in which t and c are respectively the transmision time and the cost associated with the link (u,v) (1 <= t,c <= 100) <br />
# Output
Write the total cost of the solution found or write NO_SOLUTION if no solution exists. <br />

# Example 
Input <br />
7 12 1 6  <br />
1 2 2 10  <br />
1 3 6 4  <br />
1 4 1 5 <br/>
2 3 4 9 <br/>
2 6 5 1 <br/>
2 7 2 3 <br/>
3 4 8 9 <br/>
3 5 6 2 <br/>
3 6 8 7 <br/>
4 5 3 5 <br/>
5 6 1 4 <br/>
6 7 4 5 <br/>

Output <br/>
31 <br/>
<img width="280" height="223" alt="image" src="https://github.com/user-attachments/assets/ca150f23-ec26-4694-b0c1-4324264a7ebf" />

Explanation: the links selected are (1,2), (1,3), (1,4), (2,7), (4,5), (5,6)
