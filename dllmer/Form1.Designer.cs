namespace dllmer;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.components = new System.ComponentModel.Container();
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.AutoSize=true;
        this.Text = "正在前往KNN的路上";

        this.rootLayout = new TableLayoutPanel();
        this.rootLayout.Location=new Point(5,30);
        this.rootLayout.AutoSize = true;

        this.Controls.Add(this.rootLayout);

        this.btns = new Button[100];
        int temp = 1;
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                this.btns[i] = new Button();
                this.btns[i].Size=new Size(115,50);
                // this.btns[i].AutoSize = true;
                this.btns[i].Text = $"親切問候{temp}";
                this.btns[i].Anchor = AnchorStyles.None;
                this.btns[i].Click += btns_click;
                this.rootLayout.Controls.Add(this.btns[i], j, i + 1);
                temp++;
            }
        }

        this.label1 = new Label();
        this.label1.AutoSize = true;
        this.label1.Size = new Size(50, 5);
        this.label1.Anchor = AnchorStyles.None;
        this.label1.Text = "o4o555";
        this.label1.Location=new Point(10,5);
        this.Controls.Add(this.label1);

        this.progressBar1 = new ProgressBar();
        this.progressBar1.Size = new Size(250, 20);
        this.progressBar1.Anchor = AnchorStyles.None;
        this.progressBar1.Location=new Point(135,5);
        this.Controls.Add(this.progressBar1);
    }

    #endregion

    private TableLayoutPanel rootLayout;
    private Button[] btns;
    private Label label1;
    private ProgressBar progressBar1;
}
