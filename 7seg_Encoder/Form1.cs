using System;
using System.Drawing;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        int[] segdata = new int[8];
        bool[] segstate = new bool[8];
        int x;
        public Form1() => InitializeComponent();

        private void button1_Click(object sender, EventArgs e)
        {
            segstate[0] = !segstate[0];
            button1.BackColor = segstate[0] ? Color.Red : SystemColors.ControlLight;
            segdata[0] = segstate[0] ? 0x01 : 0;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            segstate[1] = !segstate[1];
            button2.BackColor = segstate[1] ? Color.Red : SystemColors.ControlLight;
            segdata[1] = segstate[1] ? 0x02 : 0;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            segstate[2] = !segstate[2];
            button3.BackColor = segstate[2] ? Color.Red : SystemColors.ControlLight;
            segdata[2] = segstate[2] ? 0x04 : 0;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            segstate[3] = !segstate[3];
            button4.BackColor = segstate[3] ? Color.Red : SystemColors.ControlLight;
            segdata[3] = segstate[3] ? 0x08 : 0;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            segstate[4] = !segstate[4];
            button5.BackColor = segstate[4] ? Color.Red : SystemColors.ControlLight;
            segdata[4] = segstate[4] ? 0x10 : 0;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            segstate[5] = !segstate[5];
            button6.BackColor = segstate[5] ? Color.Red : SystemColors.ControlLight;
            segdata[5] = segstate[5] ? 0x20 : 0;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            segstate[6] = !segstate[6];
            button7.BackColor = segstate[6] ? Color.Red : SystemColors.ControlLight;
            segdata[6] = segstate[6] ? 0x40 : 0;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            segstate[7] = !segstate[7];
            button8.BackColor = segstate[7] ? Color.Red : SystemColors.ControlLight;
            segdata[7] = segstate[7] ? 0x80 : 0;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            foreach (var i in segdata)
            {
                x |= i;
            }

            if (x > 15)
                label1.Text = "0x" + x.ToString("X");
            else
                label1.Text = "0x0" + x.ToString("X");

            x = 0;
        }
    }
}
