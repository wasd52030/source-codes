import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.util.Timer;

public class WhackMole
{
    ArrayList<JButton> btns=new ArrayList<JButton>();
    JFrame main=new JFrame();
    GridBagLayout gridBagLayout = new GridBagLayout();
    int nums=(int)(Math.random()*11)+5;
    JLabel[] labels = new JLabel[3];
    int score=0,level=1,cnt=0;
    Timer timer=new Timer();

    WhackMole()
    {
        GameInit();
        SetLevelData();
        timer.schedule(new TimerTask(){
            @Override
            public void run() {
                cnt++;
                labels[1].setText(String.format("%d秒",cnt));
                if (cnt==15)
                {
                    timer.cancel();
                    JOptionPane.showMessageDialog(main, "遊戲結束", "",JOptionPane.WARNING_MESSAGE);
                    for (JButton jButton : btns) jButton.setEnabled(false);
                }
                else if(cnt%5==0)
                {
                    level++;
                    nums=(int)(Math.random()*11)+5;
                    SetLevelData();
                    labels[0].setText(String.format("現在是第%d關，共%d分", level,score));
                    labels[2].setText(String.format("共%d隻地鼠",nums));
                }
            }
        },0,1000);
    }

    void SetLevelData()
    {
        for(var btn : btns) btn.setText("  ");
        for (int i = 0; i < nums; i++)
        {
            int nums=(int)(Math.random()*100);
            btns.get(nums).setText("X");
        }
    }

    void GameInit()
    {
        main.setLayout(gridBagLayout);

        for (int i = 0; i < labels.length; i++)
        {
            var c=new GridBagConstraints();
            c.fill=GridBagConstraints.BOTH;
            c.gridx=0;
            c.gridwidth=10;
            c.gridy=i;
            JLabel a=new JLabel("");
            a.setHorizontalAlignment(SwingConstants.CENTER);
            labels[i]=a;
            main.add(labels[i],c);
        }

        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                JButton btn=new JButton("  ");
                btn.addActionListener(e->{
                    if(btn.getText()=="X")
                    {
                        btn.setText("  ");
                        score++;
                    }
                    labels[0].setText(String.format("現在是第%d關，共%d分", level,score));
                });
                var c=new GridBagConstraints();
                c.fill=GridBagConstraints.BOTH;
                c.gridx=i;
                c.gridy=j+4;
                main.add(btn,c);
                btns.add(btn);
            }
        }
        labels[0].setText(String.format("現在是第%d關，共%d分", level,score));
        labels[1].setText(String.format("%d秒",cnt));
        labels[2].setText(String.format("共%d隻地鼠",nums));
        main.setSize(430,360);
    }

    public static void main(String[] args)
    {
        WhackMole a=new WhackMole();
        a.main.setVisible(true);
    }
}