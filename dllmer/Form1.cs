namespace dllmer;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private async void btns_click(object sender, EventArgs e)
    {

        for (int i = 0; i <= 100; i++)
        {
            label1.Text = (((Button)sender).TabIndex + 1).ToString().dllm() + $"--{i}";
            progressBar1.Value = i;
            await Task.Delay(100);
        }
    }
}
