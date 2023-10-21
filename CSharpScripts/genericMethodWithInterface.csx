int[] Iarr = new int[] { 5, 100, -3 };
double[] Darr = new double[] { 10.2365, 182.542, 100.325 };
char[] Carr = new char[] { 'a', 's', 't' };
long[] Larr = new long[] { 1_000_000, 100_000_000, 50_000_000 };

Iarr.findMAxAndMin();
Darr.findMAxAndMin();
Carr.findMAxAndMin();
Larr.findMAxAndMin();

public static class Extensions
{
    public static void findMAxAndMin<T>(this T[] arr) where T : IComparable
    {
        T max = arr[0], min = arr[0];
        foreach (var item in arr)
        {
            if (item.CompareTo(max) > 0)
            {
                max = item;
            }

            if (item.CompareTo(min) < 0)
            {
                min = item;
            }
        }

        Console.WriteLine($"陣列中的最大值為: {max}");
        Console.WriteLine($"陣列中的最小值為: {min}");
    }
}