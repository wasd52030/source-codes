namespace dllmer;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private async void btn1_click(object sender, EventArgs e)
    {
        Console.WriteLine(label1.Size);
        for (int i = 0; i <= 100; i++)
        {
            label1.Text = i.ToString().dllm();
            progressBar1.Value = i;
            await Task.Delay(100);
        }
        Console.WriteLine(label1.Size);
    }
}
