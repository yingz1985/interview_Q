package backtracking;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Permutations {
    // turn on the DEBUG flag to see a bunch of helpful println statements
    // to watch the recursion trace
    private static HashMap<String,Node> graph;
    private static int bandwidth = Integer.MAX_VALUE;
    private static int vertex;
    private static int edge;

    public static void main(String[] args) throws FileNotFoundException {

        System.out.println("Enter file to be processed:");
        String filename = "/Users/Bagel/Documents/CSE373/test_files/";
        Scanner stdin = new Scanner(System.in);
        filename += stdin.nextLine() +".txt";
        File file = new File(filename);
        stdin = new Scanner(file);
        vertex = Integer.valueOf(stdin.nextLine());
        edge = Integer.valueOf(stdin.nextLine());
        //vertex = Integer.valueOf(stdin.nextLine());
        String nextLine;
        graph = new HashMap();
        int[] vertices = new int[vertex];
        
        for(int i = 0;i<vertices.length;i++)
        {
            vertices[i] = -1;

        }
        

        while(stdin.hasNextLine())
        {
            nextLine = stdin.nextLine();
            String[] nodePair = nextLine.split("    ");
            vertices[Integer.valueOf(nodePair[0])-1] = Integer.valueOf(nodePair[0]);
            vertices[Integer.valueOf(nodePair[1])-1] = Integer.valueOf(nodePair[1]);
            Node A = new Node(nodePair[0]);
            Node B = new Node(nodePair[1]);
            
            

            if(!graph.containsKey(nodePair[0]))
            {
                graph.put(nodePair[0],A);
            }
            
            if(!graph.containsKey(nodePair[1]))
            {
                graph.put(nodePair[1],B);
            }   //initialize a list of all vertices
            Edge A1 = new Edge(graph.get(nodePair[0]),graph.get(nodePair[1]));
            Edge B1 = new Edge(graph.get(nodePair[1]),graph.get(nodePair[0]));
            graph.get(nodePair[0]).getEdges().add(A1);  //make graph directed 
            graph.get(nodePair[1]).getEdges().add(B1);
            
        }
        stdin.close();
        
        List<Integer> list = checkComplete(graph.get(vertices[0]+""));
        if(list!=null)
        {
            for(int i = 0;i<list.size();i++ )
           {
               System.out.print(list.get(i)+" ");
           }
           System.out.println("minimum bandwidth:"+(vertex-1));
        }
        else
        {
            
            permute(vertices);
        }
        


    }
    
    public static List<Integer> checkComplete(Node root)//it's complete if every node is connect to every other node 
    {
        List<Integer> list = new ArrayList();
        int size = root.getEdges().size();
        if(size==vertex-1)
        {
            list.add(root.name());
            for(Object child: root.getEdges())
            {
                if(   ((Edge)child).getB().getEdges().size()==vertex-1   )  
                {
                    list.add(((Edge)child).getB().name());
                }
                else
                    return null;
            }
                     
        }
        else
        {
            return null;
        }
        return list;
        
    }
    
public static int findWidth(List<Integer> list,int print)
{
    int width = 0;
    
    for(int i = 0 ; i<list.size();i++)
    {
        Node nodeToInspect = graph.get(list.get(i)+"");
        if(!nodeToInspect.isVisted())
        {
            Object[] j = nodeToInspect.getEdges().toArray();

            for(Object edges: nodeToInspect.getEdges().toArray())
            {

                if(((Edge)edges).getBandWidth()>width)
                    width = ((Edge)edges).getBandWidth();
                if(width>=bandwidth)
                {
                    //clearVisitStatus();
                    return -1;//not better than current bandwidth - disregard
                }
                //if current width is not optimal, return prematurely 
                //find maximum width
            }
            nodeToInspect.visit();
        
        }
    }

    return width;
}
public static void clearVisitStatus()
{
        for(Object s:graph.values())
    {
        ((Node)s).unvisit();
        //unvisit all the nodes
    }
}
    
public static List<List<Integer>> permute(int[] nums) 
{
    List<List<Integer>> list = new ArrayList<>();

   
   backtrack(list, new ArrayList<>(), nums);
   for(int i = 0;i<list.size();i++ )
   {
       System.out.print(list.get(i)+"\n");
   }
   System.out.println("minimum bandwidth:"+bandwidth);
   return list;
}


public static void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums)//
{  

   if(tempList.size() == nums.length)
   {

       int possibleMin = findWidth(tempList,0);
       clearVisitStatus();
       
       //System.out.printf("currentMin \n"+possibleMin);
       if(bandwidth>possibleMin && possibleMin!=-1)
       {
           bandwidth = possibleMin;
           list.clear();
           list.add(new ArrayList<>(tempList));
           

       }
       if(bandwidth==1)
           return;
       //bandwidth can't get better than 1 

         

   } else{
      for(int i = 0; i < nums.length; i++){ 
         if(tempList.contains(nums[i])) continue; 
            // element already exists, skip
         if(!tempList.isEmpty())
            if(nums[i]<tempList.get(0) && i==(vertex-1)) 
                break;
         
         int add = check(tempList.size()+1,graph.get(nums[i]+""));
         
         if(add==1)
         {

             tempList.add(nums[i]);
             graph.get(nums[i]+"").setIndex(tempList.size());


         }
         else
         { //if current placement -> greater bandwidth
             //-> disregard all permutations that are like this

             break;//don't consider 
         }
             
         
            backtrack(list, tempList, nums);
            int n = tempList.remove(tempList.size() - 1);
            graph.get(n+"").setIndex(-1);
            

      }
   }
} 

public static int check(int currentIndex, Node node)
{
    //check if the current index will result in a longer distance
            int edge = 0;
            for(Object edges:node.getEdges())
            {
                Node b = ((Edge)edges).getB();
                if(b.getIndex()<currentIndex && b.getIndex()!=-1)
                {//b has already been placed 

                    int newBand = Math.abs(b.getIndex()-currentIndex);

                    if(bandwidth<=newBand)
                    {

                        //if there's already a better placement for this  value
                        return 0; //creates an even greater bandwidth
                    }


                }
                else
                {
                    if(currentIndex+(edge++)>=bandwidth)
                    {
                        return 0;
                    }
                }
        }

        
        return 1;
    
}

}