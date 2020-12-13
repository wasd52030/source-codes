import java.util.*;

public class z036 
{
    public static void main(String[] args) 
    {
        Scanner s1=new Scanner(System.in);
        String in=s1.nextLine();
        List<Character> inChr=new ArrayList<>();
        List<Integer> numcnt=new ArrayList<>();

        for(char k:in.toCharArray())
            inChr.add(k);

        for(int i=0;i<10;i++)
            numcnt.add(0);

        for(char k:inChr)
        {
            switch (k) 
            {
                case '0':
                    numcnt.set(0,numcnt.get(0)+1);
                    break;
                case '1':
                    numcnt.set(1,numcnt.get(1)+1);
                    break;
                case '2':
                    numcnt.set(2,numcnt.get(2)+1);
                    break;
                case '3':
                    numcnt.set(3,numcnt.get(3)+1);
                    break;
                case '4':
                    numcnt.set(4,numcnt.get(4)+1);
                    break;
                case '5':
                    numcnt.set(5,numcnt.get(5)+1);
                    break;
                case '6':
                    numcnt.set(6,numcnt.get(6)+1);
                    break;
                case '7':
                    numcnt.set(7,numcnt.get(7)+1);
                    break;
                case '8':
                    numcnt.set(8,numcnt.get(8)+1);
                    break;
                case '9':
                    numcnt.set(9,numcnt.get(9)+1);
                    break;
                default:
                    break;
            }
        }
        
        for(int i=0;i<10;i++)
            System.out.println(Integer.toString(i)+" : "+Integer.toString(numcnt.get(i)));

        System.out.println();
        System.out.println(numcnt.indexOf(Collections.max(numcnt)) + " : " + Collections.max(numcnt));
        s1.close();
    }    
}