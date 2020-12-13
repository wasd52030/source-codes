import  java.util.*;
public class Tester
{
    public static void main(String[] args)
    {
        Fruit apple=new Fruit("Apple",10);
        Fruit banana = new Fruit("Banana",12);
        Fruit orange = new Fruit("Orange",15);

        System.out.println("Shopping cart1 information:");
        Cart Cart1=new Cart();

        Cart1.searchItem(apple);
        Cart1.additem(apple,20);
        Cart1.searchItem(apple);

        Cart1.additem(banana,15);
        Cart1.additem(orange,5);
        System.out.println();
        System.out.println(Cart1.getInfo());

        System.out.println("Shopping cart2 information:");
        Cart Cart2=new Cart();
        Cart2.additem(apple,5);
        System.out.println(Cart2.getInfo());

        System.out.println("Product Information:");
        System.out.println(apple.getInfo());
    }
}

class Cart
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

class Fruit
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
