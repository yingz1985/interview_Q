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
import java.util.Arrays;
class AppearsK
{
    public static void main(String[]args)
    {
        int[] n = {6,2,3,2,3,6,4,5,6};
        System.out.println(appearsKTimes(9,n,3));
    }
    public static int appearsKTimes(int size, int inputArray[], int k)
    {
        Arrays.sort(inputArray);
        int i=1, count = 1;
        int element = inputArray[0];
        int res = -1;
        while(i < size)
        {
            if(element == inputArray[i])
            {
                count++;
            }
            else
            {
                if(count == k && element>res)
                {
                    res = element;
                }
                element = inputArray[i];
                count = 1;
            }
            i++;
//            System.out.println(count);
        }
        if(count == k && element>res)
        {
            res = element;
        }
        return res;
    }
}