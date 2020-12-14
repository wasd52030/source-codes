import java.util.*;
public class Cart 
{
    List<Fruit> basket=new ArrayList<>();
    List<Integer> subAmount=new ArrayList<>();
    int totalExpense;

    public Cart()
    {
        totalExpense=0;
        subAmount.clear();
        basket.clear();
    }

    public void setTotalExpense(int totalExpense)
    {
        this.totalExpense = totalExpense;
    }

    public void additem(Fruit fruit,int amount)
    {
        basket.add(fruit);
        subAmount.add(amount);
        fruit.updateTotalSales(amount);
    }

    public void searchItem(Fruit fruit)
    {
        if(basket.contains(fruit))
            System.out.println("Your basket has this product.");
        else
            System.out.println("Your basket does not has this product.");
    }

    private void TotalExpense()
    {
        int x=-1;
        for(Fruit i:basket)
        {
            x++;
            if(i.name.equals(i.name))
                totalExpense+=subAmount.get(x)*i.price;
        }
    }

    public String getInfo()
    {
        TotalExpense();
        String TotalPrice="The current expense is:NT$"+Integer.toString(totalExpense)+"\n";
        String TableTitle="Name  Price($NT) Unit"+"\n";
        String Tableindex="";
        int x=-1;
        for(Fruit i:basket)
        {
            x++;
            Tableindex+=i.name+": "+Integer.toString(i.price)+"   *   "+Integer.toString(subAmount.get(x))+"\n";
        }
        String FinalResult=TotalPrice+TableTitle+Tableindex;
        return FinalResult;
    }
}
