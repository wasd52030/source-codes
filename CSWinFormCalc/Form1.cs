using System;
using System.Windows.Forms;
using System.Text.RegularExpressions;

namespace cscalc
{
    public partial class Form1 : Form
    {

        public Form1( ) => InitializeComponent( );
        double num1, num2, x;
        string s;
        public void addnum(object sender, EventArgs e)
        {
            Button bt = (Button)sender;
            //關於下面這行程式，請參考TextFile1.txt
            label1.Text = label1.Text == "0" ? label1.Text = bt.Text : label1.Text += bt.Text;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "calculator";
            label1.Text = 0.ToString( );
            num1 = num2 = x = 0; //所有變數的初始化
        }

        private void button12_Click(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            double x = Math.Sqrt(Convert.ToDouble(label1.Text));
            label1.Text = Convert.ToString(x);
        }

        void Arithmetic(object sender, EventArgs e)
        {
            num1 = Convert.ToDouble(label1.Text);
            label1.Text = "";
            switch (((Button)sender).Text)
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
                case "( )^n":
                    s = "^";
                    break;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            num2 = Convert.ToDouble(label1.Text);
            switch (s)
            {
                case "+":
                    label1.Text = Convert.ToString(num1 + num2);
                    break;
                case "-":
                    label1.Text = Convert.ToString(num1 - num2);
                    break;
                case "*":
                    label1.Text = Convert.ToString(num1 * num2);
                    break;
                case "/":
                    label1.Text = Convert.ToString(num1 / num2);
                    break;
                case "^":
                    label1.Text = Convert.ToString(Math.Pow(num1, num2));
                    break;
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //用正則表達式去檢查有沒有小數點
            if (Regex.IsMatch(label1.Text,@".*\..*"))
                label1.Text = label1.Text.Substring(0, label1.Text.Length - 1);
            else
                label1.Text += ".";
            
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //用正則表達式去檢查有沒有負號
            //正則表達式用法請查google
            //@為避免跳脫字元
            if (Regex.IsMatch(label1.Text, @"^-[0-9]{1,}$"))  //沒小數點
                label1.Text = Math.Abs(Convert.ToDouble(label1.Text)).ToString();
            else if (Regex.IsMatch(label1.Text, @"^-[0-9]{1,}\.[0-9]{1,}$")) //有小數點
                label1.Text = Math.Abs(Convert.ToDouble(label1.Text)).ToString();
            else
                label1.Text = "-" + Math.Abs(Convert.ToDouble(label1.Text)).ToString( );
        }

        public double Factorial(double n) => n == 1 ? 1 : n * Factorial(n - 1);  //以遞迴計算階乘值，最大可顯示到170!，超過均顯示無限大

        private void button22_Click(object sender, EventArgs e)
        {
            label1.Text = Factorial(Convert.ToDouble(label1.Text)).ToString();

            if (label1.Text == "∞")
            {
                label1.Text = "0";
                MessageBox.Show("超出可顯示範圍", "Calc", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        void typical_constant(object sender, EventArgs e)
        {
            switch (((Button)sender).Text)
            {
                case "e":
                    label1.Text = Math.E.ToString();
                    break;
                case "π":
                    label1.Text = Math.PI.ToString();
                    break;
            }
        }

        void trangle_fun(object sender, EventArgs e)
        {
            x = 0; //初始化所有變數，確保計算正確

            //確保輸入為數字
            if (Regex.IsMatch(label1.Text, @"^.*°$"))
                x = Convert.ToDouble(label1.Text.Substring(0, label1.Text.Length - 1));
            else
                x = Convert.ToDouble(label1.Text);

            switch (((Button)sender).Text)
            {
                case "sin( )":
                    label1.Text = Math.Sin(x * Math.PI / 180).ToString();
                    break;
                case "cos( )":
                    label1.Text = Math.Cos(x * Math.PI / 180).ToString();
                    break;
                case "tan( )":
                    label1.Text = Math.Tan(x * Math.PI / 180).ToString();
                    break;
                case "arcsin( )":
                    label1.Text = Math.Asin(x) * 180 / 3.14 + "°";
                    break;
                case "arccos( )":
                    label1.Text = Math.Acos(x) * 180 / 3.14 + "°";
                    break;
                case "arctan( )":
                    label1.Text = Math.Atan(x) * 180 / 3.14 + "°";
                    break;
            }
        }
    }
}
