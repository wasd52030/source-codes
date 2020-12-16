import java.io.*;
import java.util.*;

public class slove1 
{
    public static void main(String[] args) throws FileNotFoundException
    {
        Scanner f1=new Scanner(new File("./input.txt"));
        List<Integer> data=new ArrayList<>();
        int[] calc=new int[3];

        while (f1.hasNextInt()) 
        {
            data.add(f1.nextInt());
        }
        f1.close();

        //當counter超過data List而觸發catch時
        //最後三個數字會被略過，於是在觸發catch時設一flag==1
        //當最後一行輸出完畢時，立即用break跳出迴圈
        int endflag=0;

        int datacounter=0;
        int calccounter=0;
        int isTri=0; 
        int NotTri=0;
        while (datacounter<=data.size())
        {
            try 
            {
                try 
                {
                    calc[calccounter]=data.get(datacounter);
                    calccounter++;
                } 
                catch (ArrayIndexOutOfBoundsException e) 
                {
                    String out="";
                    //a=calc[0] b=calc[1] c=calc[2]
                    int a=0,b=0,c=0;

                    for(int x=0;x<=calc.length;x++)
                    {
                        switch (x) 
                        {
                            case 0:
                                a=calc[x];
                                break;
                            case 1:
                                b=calc[x];
                                break;
                            case 2:
                                c=calc[x];
                                break;
                            default:
                                break;
                        }
                    }

                    for(int x:calc)
                    {
                        out+=x+" ";
                    }
                        
                    if(a+b>c&&b+c>a&&c+a>b)
                    {
                        out+="是三角形";
                        isTri++;
                    }
                    else
                    {
                        out+="不是三角形";
                        NotTri++;
                    }
                        
                    System.out.print(out+"\n");

                    calccounter=0;//初始化陣列計數器
                    
                    //當calccounter超過calc陣列而觸發catch時
                    //data.get(counter)的值會被略過，在這裡減一以方便下一輪讀取
                    if(datacounter<data.size())
                        datacounter--;

                    if(endflag==1)
                        break;
                }
                datacounter++;
            } 
            catch (IndexOutOfBoundsException e) 
            {
                datacounter-=3;
                endflag=1;
            }
        }
        System.out.printf("\nTrue: %d\nFalse: %d\n", isTri,NotTri);
    }    
}