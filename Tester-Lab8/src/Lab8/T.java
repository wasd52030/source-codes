package src.Lab8;

import java.util.*;
import java.io.*;

public class T 
{
	public static void main(String[] args) 
	{
		try
		{	
			FileWriter mywriter=new FileWriter("register_info.txt");
			Scanner reader=new Scanner(new File("sales.txt"));
			Fruit a=new Fruit("Apple",10);
		 	Fruit b=new Fruit("Banana",12);
		 	Fruit o=new Fruit("Orange",15);
		 	Fruit []fruits= {a,b,o};  //用來確認每一筆數字所對應到的項目
		 	register r=new register();
		
		 	try 
		 	{
				reader.nextLine(); //把標示行(第一行)先讀掉，方便下面的數字處理
				int id=0;//行數計數器
				while(reader.hasNextInt())
				{
					//遍歷fruits陣列，調用register class中的calctotalcost函式來計算每一行的總金額
					// 並累加到register class中的totalrevenue變數中以紀錄全部加起來的總金額
					for(Fruit fruit:fruits)
					{
						r.calctotalcost(id, reader.nextInt(), fruit.getprice());					
					}
					id++;
				}
				mywriter.write(r.getinfo());
			}
			finally
			{
				reader.close();
				mywriter.close();
			}
		}
		catch (FileNotFoundException e)
		{ 
			System.out.println("File canot found."); 
		}
		catch (NoSuchElementException e)
		{ 
			System.out.println("File contents are invalid."); 
		}
		catch (IOException e)
		{ 
			System.out.println("File contents are invalid"); 
		}
	}
}
