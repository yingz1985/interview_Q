/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package backtracking;

/**
 *
 * @author Bagel
 */
class Edge
{
    private Node A;//The starting node
    private Node B;//The connected node

    public Edge(Node A,Node B)
    {
	this.A = A;
	this.B = B;
        
    }
    public int getBandWidth()
    {
        if(A.getIndex()<0 || B.getIndex()<0) return Integer.MIN_VALUE;
        return Math.abs(A.getIndex()-B.getIndex());
    }
    public Node getB()
    {
        return B;
    }
}
