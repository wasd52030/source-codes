using System;
using System.Drawing;
using Microsoft.VisualBasic;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        bool[] segstate = new bool[8];
        int[] segdata = new int[8];
        string k = "0";
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            segstate[0]= !segstate[0];
            if (segstate[0])
            {
                button1.BackColor = Color.Red;
                segdata[0] = 0x01;
            }
            else
            {
                button1.BackColor = SystemColors.ControlLight;
                segdata[0] = 0;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i < segstate.Length; i++)
                segstate[i] = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            segstate[1]= !segstate[1];
            if (segstate[1])
            {
                button2.BackColor = Color.Red;
                segdata[1] = 0x02;
            }
            else
            {
                button2.BackColor = SystemColors.ControlLight;
                segdata[1] = 0;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            segstate[2] = !segstate[2];
            if (segstate[2])
            {
                button3.BackColor = Color.Red;
                segdata[2] = 0x04;
            }
            else
            {
                button3.BackColor = SystemColors.ControlLight;
                segdata[2] = 0;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            segstate[3] = !segstate[3];
            if (segstate[3])
            {
                button4.BackColor = Color.Red;
                segdata[3] = 0x08;
            }
            else
            {
                button4.BackColor = SystemColors.ControlLight;
                segdata[3] = 0;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            segstate[4] = !segstate[4];
            if (segstate[4])
            {
                button5.BackColor = Color.Red;
                segdata[4] = 0x010;
            }
            else
            {
                button5.BackColor = SystemColors.ControlLight;
                segdata[4] = 0;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            segstate[5] = !segstate[5];
            if (segstate[5])
            {
                button6.BackColor = Color.Red;
                segdata[5] = 0x20;
            }
            else
            {
                button6.BackColor = SystemColors.ControlLight;
                segdata[5] = 0;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            segstate[6] = !segstate[6];
            if (segstate[6])
            {
                button7.BackColor = Color.Red;
                segdata[6] = 0x40;
            }
            else
            {
                button7.BackColor = SystemColors.ControlLight;
                segdata[6] = 0;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            segstate[7] = !segstate[7];
            if (segstate[7])
            {
                button8.BackColor = Color.Red;
                segdata[7] = 0x80;
            }
            else
            {
                button8.BackColor = SystemColors.ControlLight;
                segdata[7] = 0;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            int x = 0;
            foreach(var i in segdata)
            {
                x |= i;
            }
            k = "0x" ;
            label1.Text = k+x.ToString("X");
        }
    }
}
