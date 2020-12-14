import java.util.*;
public class Fruit 
{
    String name;
    int price;
    int totalSales;
    List<Integer> sale=new ArrayList<>();

    public Fruit(String name,int price)
    {
        this.name=name;
        this.price=price;
        totalSales=0;
    }

    public String getName()
    {
        return name;
    }

    public int getPrice()
    {
        return price;
    }

    public int getTotalSales()
    {
        return totalSales;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public void setPrice(int price)
    {
        this.price = price;
    }

    public void updateTotalSales(int amount)
    {
        sale.add(amount);
        totalSales+=amount;
    }

    public String getInfo()
    {
        String name="Fruit Name: "+this.name+"\n";
        String Price="Fruit Price: "+Integer.toString(this.price)+"\n";
        String indiv="Indiv Sales: ";
        String Total="Total Sales: "+Integer.toString(totalSales)+"\n";
        Collections.sort(sale);
        for(int i:sale)
        {
            indiv+=Integer.toString(i)+", ";
        }
        indiv+="\n";
        String FinalResult=name+Price+indiv+Total;
        return FinalResult;
    }
}
