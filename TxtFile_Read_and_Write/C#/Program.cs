using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;


namespace ConsoleApp1
{
    class Program
    {
        public static bool IsInteger(double f)  //判斷一個浮點數輸入值是否為整數(小數不列入奇偶判斷)
        {
            return Math.Ceiling(f) == Math.Floor(f);
        }

        static void Main(string[] args)
        {
            FileInfo f1 = new FileInfo("input.txt");  //位於專案資料夾的bin\Debug\netcoreapp3.1
            StreamReader a = f1.OpenText();

            FileInfo f2 = new FileInfo("output.txt");
            StreamWriter b = f2.CreateText();
            List<double> g = new List<double>();
            double sum = 0, odd = 0, even = 0;

            while (a.Peek() > 0)
                g.Add(Convert.ToDouble(a.ReadLine()));

            g.Sort();

            b.Write("輸入資料經排序後 : ");

            for (int i = 0; i < g.Count; i++)
            {
                sum += g[i];  //求總和

                if(IsInteger(g[i])==true) //判斷奇偶，需去除小數
                {
                    if (g[i] % 2 == 0)
                        even++;
                    else
                        odd++;
                }

                b.Write("{0} ", g[i]); //輸出排序過後的資料到指定文件
            }

            double max = g.Max();
            double min = g.Min();
            var avg = g.Average();

            b.Write("\n");
            b.Write("最大值 : {0}\n最小值 : {1}\n平均值 : {2}\n偶數有{3}個\n奇數有{4}個", max,min,avg,even,odd);
            b.Flush();
            
            a.Close();
            b.Close();

            Console.WriteLine("資料分析完畢");
            Console.ReadLine();
        }
    }
}
