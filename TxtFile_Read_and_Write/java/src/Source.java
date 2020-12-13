package src;

import java.io.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;

public class Source 
{
    public static Boolean Isinteger(double n)
    {
        return Math.ceil(n)==Math.floor(n);
    }
    public static void main(String[] args) 
    {
        try 
        {
            FileReader f1=new FileReader("./src/in.txt");
            BufferedReader readf1=new BufferedReader(f1);

            FileWriter f2=new FileWriter("./src/out.txt");
            

            List<Double> Data=new ArrayList<>();
            double sum=0,odd=0,even=0;

            while (readf1.ready())
                Data.add(Double.parseDouble(readf1.readLine()));

            Collections.sort(Data);

            f2.write("輸入資料經排序後 : ");
            f2.write(Data.toString());

            for (int i = 0; i < Data.size(); i++) 
            {
                sum+=Data.get(i);
                if (Isinteger(Data.get(i))==true) 
                {
                    if(Data.get(i)%2==0)
                        even++;
                    else
                        odd++;
                }
            }
            
            double max=Collections.max(Data);
            double min=Collections.min(Data);
            double avg=sum/Data.size();

            f2.write("\n");
            f2.write("最大值 : "+max+"\n"+"最小值 : "+min+"\n"+"平均值 : "+avg+"\n"+"奇數有"+odd+"個\n"+"偶數有"+even+"個\n");
            f2.flush();
			
            f1.close();
            f2.close();

            System.out.println("資料分析完畢");
        } 
        catch (Exception e) 
        {
            e.printStackTrace();
        }
    }
}