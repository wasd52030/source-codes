import java.io.*;

public class slove2 
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader f1=new BufferedReader(new FileReader("./input.txt"));
        int istri=0,notri=0;
        while (f1.ready()) 
        {
            String instr=f1.readLine();
            String[] numstr=instr.split(" "); //以空格做基準分割字串
            int[] nums=new int[numstr.length];

            for(int i=0;i<numstr.length;i++)
            {
                nums[i]=Integer.parseInt(numstr[i]);
            }

            System.out.print(instr+" ");

            if(nums[0]+nums[1]>nums[2] && nums[1]+nums[2]>nums[0] && nums[2]+nums[0]>nums[1])
            {
                System.out.println("是三角形");
                istri++;
            }
            else
            {
                System.out.println("不是三角形");
                notri++;
            }
        }
        System.out.printf("\nTrue: %d\nFalse: %d\n", istri,notri);
        f1.close();
    }
}
