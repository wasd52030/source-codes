namespace dllmer;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }


    private async void btns_click(object sender, EventArgs e)
    {

        var btn = (Button)sender;
        btn.Enabled=false;
        for (int i = 0; i <= 100; i++)
        {
            label1.Text = (btn.TabIndex + 1).ToString().dllm() + $"--{i}";
            progressBar1.Value = i;
            await Task.Delay(100);
        }
        btn.Enabled=true;
    }
}
