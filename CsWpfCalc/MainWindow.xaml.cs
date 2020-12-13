using System;
using System.Windows;
using System.Windows.Controls;
using System.Text.RegularExpressions;
namespace WpfApp1
{
    /// <summary>
    /// MainWindow.xaml 的互動邏輯
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow() => InitializeComponent();
        double num1, num2, ctrl_trangle, x;
        string s;

        private void addnum(object sender, RoutedEventArgs e)
        {
            Button bt = (Button)sender;
            label1.Content = label1.Content.ToString() == "0" ? label1.Content = bt.Content : label1.Content += bt.Content.ToString();
        }

        private void btnClean_Click(object sender, RoutedEventArgs e)
        {
            calc_initial(sender, e);
        }

        private void calc_initial(object sender, RoutedEventArgs e)
        {
            label1.Content = 0.ToString();
            num1 = num2 = ctrl_trangle = x = 0; //所有變數的初始化
        }

        private void Arithmetic(object sender, RoutedEventArgs e)
        {
            num1 = Convert.ToDouble(label1.Content);
            label1.Content = "";
            switch (((Button)sender).Content.ToString())
            {
                case "+":
                    s = "+";
                    break;
                case "-":
                    s = "-";
                    break;
                case "*":
                    s = "*";
                    break;
                case "÷":
                    s = "/";
                    break;
                case "x^y":
                    s = "^";
                    break;
            }
        }

        private void btnEqual_Click(object sender, RoutedEventArgs e)
        {
            num2 = Convert.ToDouble(label1.Content);
            switch (s)
            {
                case "+":
                    label1.Content = Convert.ToString(num1 + num2);
                    break;
                case "-":
                    label1.Content = Convert.ToString(num1 - num2);
                    break;
                case "*":
                    label1.Content = Convert.ToString(num1 * num2);
                    break;
                case "/":
                    label1.Content = Convert.ToString(num1 / num2);
                    break;
                case "^":
                    label1.Content = Convert.ToString(Math.Pow(num1, num2));
                    break;
            }
        }

        private void btnpn_Click(object sender, RoutedEventArgs e)
        {
            if (Regex.IsMatch(label1.Content.ToString(), @"^-[0-9]{1,}$"))  //沒小數點
                label1.Content = Math.Abs(Convert.ToDouble(label1.Content)).ToString();
            else if (Regex.IsMatch(label1.Content.ToString(), @"^-[0-9]{1,}\.[0-9]{1,}$")) //有小數點
                label1.Content = Math.Abs(Convert.ToDouble(label1.Content)).ToString();
            else
                label1.Content = "-" + Math.Abs(Convert.ToDouble(label1.Content)).ToString();
        }

        private void btnE_Click(object sender, RoutedEventArgs e)
        {
            label1.Content = Math.E.ToString();
        }

        private void btnPI_Click(object sender, RoutedEventArgs e)
        {
            label1.Content = Math.PI.ToString();
        }

        private void btnSqrt_Click(object sender, RoutedEventArgs e)
        {
            double x = Math.Sqrt(Convert.ToDouble(label1.Content));
            label1.Content = Convert.ToString(x);
        }

        private void btndot_Click(object sender, RoutedEventArgs e)
        {
            //用正則表達式去檢查有沒有小數點
            if (!(Regex.IsMatch(label1.Content.ToString(), @".*\..*")))
                label1.Content += ".";

        }

        public double Factorial(double n) => n == 1 ? 1 : n * Factorial(n - 1);
        private void btnFactorial1_Click(object sender, RoutedEventArgs e)
        {
            label1.Content = Factorial(Convert.ToDouble(label1.Content)).ToString();

            if (label1.Content.ToString() == "∞")
            {
                label1.Content = "0";
                MessageBox.Show("超出可顯示範圍", "Calc",MessageBoxButton.OK,MessageBoxImage.Warning);
            }
        }

        private void trangle_fun(object sender, RoutedEventArgs e)
        {
            x = ctrl_trangle = 0; //初始化所有變數，確保計算正確

            //確保輸入為數字
            if (Regex.IsMatch(label1.Content.ToString(), @"^.*°$"))
                x = Convert.ToDouble(label1.Content.ToString().Substring(0, label1.Content.ToString().Length - 1));
            else
                x = Convert.ToDouble(label1.Content);

            switch (((Button)sender).Content)
            {
                case "sin( )":
                    ctrl_trangle = 1;
                    break;
                case "cos( )":
                    ctrl_trangle = 2;
                    break;
                case "tan( )":
                    ctrl_trangle = 3;
                    break;
                case "arcsin( )":
                    ctrl_trangle = 4;
                    break;
                case "arccos( )":
                    ctrl_trangle = 5;
                    break;
                case "arctan( )":
                    ctrl_trangle = 6;
                    break;
            }

            switch (ctrl_trangle)
            {
                case 1:
                    label1.Content = Math.Sin(x * Math.PI / 180).ToString();
                    break;
                case 2:
                    label1.Content = Math.Cos(x * Math.PI / 180).ToString();
                    break;
                case 3:
                    label1.Content = Math.Tan(x * Math.PI / 180).ToString();
                    break;
                case 4:
                    label1.Content = Math.Asin(x) * 180 / 3.14 + "°";
                    break;
                case 5:
                    label1.Content = Math.Acos(x) * 180 / 3.14 + "°";
                    break;
                case 6:
                    label1.Content = Math.Atan(x) * 180 / 3.14 + "°";
                    break;
            }
        }

    }
}
