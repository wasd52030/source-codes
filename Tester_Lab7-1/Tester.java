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
