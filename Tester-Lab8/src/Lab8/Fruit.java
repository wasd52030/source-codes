package src.Lab8;

public class Fruit 
{
	private String name;
	private int price,totalsales;
	private int[]sale;

	public Fruit(String name,int price) 
	{
		sale=new int[3];
		totalsales=0;
		this.name=name;
		this.price=price;
	}

	public String getname() 
	{
		return this.name;
	}

	public int getprice() 
	{
		return this.price;
	}

	public int gettotalsales() 
	{
		return totalsales;
	}
	
	public int updatetotalsales(int amount) 
	{
		for(int i:sale) 
		{
			if(sale[i]==0) 
			{
				sale[i]=amount;
				totalsales+=amount;
			}
		}
		return totalsales;
	}
	public String getinfo() 
	{
		String r="";
		String name="Fruit name:  "+this.name;
		String price="Fruit price: "+this.price;
		String idv="indiv sales:";
		String t=String.format("Total sales: ",totalsales);
		for(int i:sale) 
		{
			idv+=i;		
		}
		r+=name+price+idv+t;
		return r;
	}
}
	
	
	

