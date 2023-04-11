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
        this.ClientSize = new System.Drawing.Size(400, 300);
        this.Text = "正在前往KNN的路上";

        this.rootLayout = new TableLayoutPanel();
        this.rootLayout.Anchor = AnchorStyles.None;
        this.rootLayout.AutoSize = true;
        this.rootLayout.Location = new Point(5, 5);
        this.Controls.Add(this.rootLayout);

        this.btn1 = new Button();
        this.btn1.AutoSize = true;
        this.btn1.Text = "親切問候";
        this.btn1.Anchor = AnchorStyles.None;
        this.btn1.Click += btn1_click;
        this.rootLayout.Controls.Add(this.btn1,1,1);

        this.label1=new Label();
        this.label1.AutoSize=true;
        this.label1.Size=new Size(50,20);
        this.label1.Anchor=AnchorStyles.None;
        this.label1.Text="o4o555";
        this.rootLayout.Controls.Add(this.label1,1,2);

        this.progressBar1=new ProgressBar();
        this.progressBar1.Size=new Size(250,20);
        this.progressBar1.Anchor=AnchorStyles.None;
        this.rootLayout.Controls.Add(this.progressBar1,2,2);
    }

    #endregion

    private TableLayoutPanel rootLayout;
    private Button btn1;
    private Label label1;
    private ProgressBar progressBar1;
}
