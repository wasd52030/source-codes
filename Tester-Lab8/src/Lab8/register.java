package src.Lab8;

import java.util.*;

public class register 
{
	private int totalrevenue;
	private ArrayList<Integer>bills; //這個arraylist的每一個元素代表每一行的總金額

	public register() 
	{
		totalrevenue=0;
		bills=new ArrayList<Integer>();
	}

	public int gettotalrevenue() 
	{
		return this.totalrevenue;
	}
	
	public ArrayList<Integer> getbill(int id)
	{
		return bills;
	}

	public void calctotalcost(int id,int num,int price) 
	{
		//當這一行第一次計算時，由於bills Arraylist中對應的索引並沒有東西，所以會拋出IndexOutOfBoundsException異常
		//用try catch確實掌握到異常後，將這一行的第一筆交易金額計算後加入bills Arraylist中
		//往後那一行有新的交易紀錄要計入那一行的總交易金額時，只要使用bills.set(id,bills.get(id)+num*price)就可以把那一行的總交易金額統計完成
		//最後，把每一次算完的交易金額累加到totalrevenue變數中以紀錄全部的交易金額
		try 
		{
			bills.set(id,bills.get(id)+num*price);
		}
		catch(IndexOutOfBoundsException e)
		{
			bills.add(num*price);
		}
		finally
		{
			this.calctotalRevenue(num*price);
		}
	}	

	public void calctotalRevenue(int cost) 
	{
		totalrevenue+=cost;
	}
	
	public String getinfo() 
	{
		String out="My register info:\nBill\n";
		for(int i:bills) 
		{
			out+=String.format("%d\n", i);
		}
		out+=String.format("Total Revenue:%d",totalrevenue);
		return out;
	}
}
