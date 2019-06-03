/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package backtracking;

import java.util.HashSet;



public class Node 
{
	private String name;//name of the node
	private int index;  //position of the 
        private HashSet<Edge>edges; //connections or edges to another node
        private boolean visited;

        
        public HashSet<Edge> getEdges()
	{
		return edges;
	}
        public void visit()
        {
            visited = true;
        }
        public boolean isVisted()
        {
            return visited;
        }
        public void unvisit()
        {
            visited = false;
        }

	public Node(String name)
	{
		this.name = name;
		index = -1;
                visited = false;
                edges = new HashSet<Edge>();
	}
	public int getIndex()
        {
            return index;
        }
        public void setIndex(int index)
        {
            this.index = index;
        }

        @Override
	public String toString()
	{
		return name;
	}
        
        public int name()
        {
            return Integer.valueOf(name);
        }
	
	
	
}
