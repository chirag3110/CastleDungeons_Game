import java.util.ArrayList; 
import java.util.Arrays; 
import java.util.List; 
import java.util.*;
 class Diametre_tree { 

	static int x; 
	static int maxCount; 
	static List<Integer> adj[]; 
	
	
	static void dfsUtil(int node, int count, 
						boolean visited[], 
					List<Integer> adj[]) 
	{ 
		visited[node] = true; 
		count++; 
		
		List<Integer> l = adj[node]; 
		for(Integer i: l) 
		{ 
			if(!visited[i]){ 
				if (count >= maxCount) { 
					maxCount = count; 
					x = i; 
				} 
				dfsUtil(i, count, visited, adj); 
			} 
		} 
	} 
	
	
	static void dfs(int node, int n, List<Integer> 
									adj[]) 
	{ 
		boolean[] visited = new boolean[n + 1]; 
		int count = 0; 
	
		Arrays.fill(visited, false); 
	
		dfsUtil(node, count + 1, visited, adj); 
		
	} 
	
	
	static int diameter(List<Integer> adj[], int n) 
	{ 
		maxCount = Integer.MIN_VALUE; 
	
		
		dfs(1, n, adj); 
	
		dfs(x, n, adj); 
	
		return maxCount; 
	} 
	
	public static void main(String args[]) 
	{ 
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
	
		
		adj = new List[n + 1]; 
		for(int i = 0; i < n+1 ; i++) 
			adj[i] = new ArrayList<Integer>(); 
	
		
		for(int i=0;i<n-1;i++){
			int a=s.nextInt();
			int b=s.nextInt();
			adj[a].add(b);
			adj[b].add(a);
		}
		
		System.out.println( diameter(adj, n)-1); 
	} 
} 
