/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tf;

/**
 *
 * @author Bagel
 */
import java.util.*;

public class ticketsToFans {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner scan = new Scanner(System.in);
        
        int sizeOfWorld = Integer.parseInt(scan.nextLine());
        int numberOfEvents = Integer.parseInt(scan.nextLine());
        int currentNumEvent = 0;
        
        int[] eventCoords = new int[2*numberOfEvents];
        int[][] pricesPerEvent = new int[2*numberOfEvents][2*numberOfEvents];
        while(numberOfEvents > 0){
            String eventLine = scan.nextLine();
            String[] split = eventLine.split(" ");
            int ticketNum = Integer.valueOf(split[0]);//ticket number 
            for(int i = 1;i<=2;i++)
            {
                eventCoords[2*currentNumEvent+i] = Integer.valueOf(split[i]);
            }
            int k = 0;
            for(int i = 3;i<split.length;i++)
            {
                pricesPerEvent[currentNumEvent][k++] = Integer.valueOf(split[i]);
                //parse the prices into a 2d array 
            }
       
            currentNumEvent++;
            // TODO: you will need to parse and store the events 
            numberOfEvents--;
        }
        
        int numberOfBuyers = Integer.parseInt(scan.nextLine());
        int[]buyerCoords = new int[2*numberOfBuyers];
        int currentBuyer = 0;
        while(numberOfBuyers > 0){
            String buyerLine = scan.nextLine();
            // TODO: you will need to parse and store the buyers 
            String[]split = buyerLine.split(" ");
            buyerCoords[2*currentBuyer] = Integer.valueOf(split[0]);
            buyerCoords[2*currentBuyer+1] = Integer.valueOf(split[1]);

            currentBuyer++;
            numberOfBuyers--;
        }
        for(int i = 0;i<currentBuyer;i++)
        {
            int eventNum = 0;
            int distance = 1000;
            for(int k = 0;k<currentNumEvent;k++)
            {
                int currentDistance = calculateManhattanDistance(buyerCoords[2*i],eventCoords[2*k],
                        buyerCoords[2*i+1],eventCoords[2*k+1]);
                if(currentDistance <distance)
                {
                    distance = currentDistance;
                    eventNum = k;
                }
                
         
                
            }
            for(int j = 0;j<pricesPerEvent.length;j++)
            {
                if(j==0) break;
                
            }
            
            
        }
        // The solution to the first sample above would be to output the following to console:
        // (Obviously, your solution will need to figure out the output and not just hard code it)
        System.out.println("2 50");
    }    
    
    // The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
    public static int calculateManhattanDistance(int x1, int y1, int x2, int y2)    {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
}