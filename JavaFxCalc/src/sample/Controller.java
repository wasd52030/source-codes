package sample;

import javafx.event.*;
import javafx.scene.control.*;
import javafx.fxml.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable
{
    @FXML
    public Label Lbl1;

    public String out="";
    public double num1, num2, x;
    public String s="";

    @FXML
    public void btn1_click(ActionEvent event)
    {
        Button sender=(Button)event.getSource();

        if(Lbl1.getText().equals("0"))
            out=sender.getText();
        else
            out+=sender.getText();
        Lbl1.setText(out);
    }

    @FXML
    public void btnc_click(ActionEvent event)
    {
        var_default();
    }

    @FXML
    public void btnDot_click(ActionEvent event)
    {
        out=Lbl1.getText();
        if(!(Lbl1.getText().matches(".*\\..*")))
            out+=".";
        Lbl1.setText(out);
    }

    private String IntegerString(String in)
    {
        String out="";
        if(in.matches("[0-9]{1,}\\.0"))
            out=in.substring(0,in.length()-2);
        else
            out=in;
        return out;
    }

    @FXML
    public void btnpn_click(ActionEvent event)
    {
        out=Lbl1.getText();

        if(Lbl1.getText().matches("^[0-9]{1,}"))
            out="-"+Math.abs(Integer.parseInt(Lbl1.getText()));
        else if(Lbl1.getText().matches("^-[0-9]{1,}$"))
            out=Integer.toString(Math.abs(Integer.parseInt(Lbl1.getText())));
        else if(Lbl1.getText().matches("^-[0-9]{1,}\\.[0-9]{1,}$"))
            out=Double.toString(Math.abs(Double.parseDouble(Lbl1.getText())));
        else
            out="-"+Math.abs(Double.parseDouble(Lbl1.getText()));

        Lbl1.setText(out);
    }

    @FXML
    public void btnSqrt_click(ActionEvent event)
    {
        out=Lbl1.getText();
        double x=Math.sqrt(Double.parseDouble(Lbl1.getText()));
        out=Double.toString(x);

        Lbl1.setText(IntegerString(out));
    }

    @FXML
    public void Arithmetic(ActionEvent event)
    {
        Button sender=(Button)event.getSource();
        num1=Double.parseDouble(Lbl1.getText());
        out="";
        Lbl1.setText(out);
        switch (sender.getText())
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
                s = "÷";
                break;
            case "x^y":
                s="^";
                break;
        }
    }

    public void btnequal_click(ActionEvent event)
    {
        num2=Double.parseDouble(Lbl1.getText());
        switch (s)
        {
            case "+":
                Lbl1.setText(IntegerString(Double.toString(num1+num2)));
                break;
            case "-":
                Lbl1.setText(IntegerString(Double.toString(num1-num2)));
                break;
            case "*":
                Lbl1.setText(IntegerString(Double.toString(num1*num2)));
                break;
            case "÷":
                Lbl1.setText(IntegerString(Double.toString(num1/num2)));
                break;
            case "^":
                Lbl1.setText(IntegerString(Double.toString(Math.pow(num1,num2))));
        }
    }

    private double Factorial(double n)
    {
        return n == 1 ? 1 : n * Factorial(n - 1);
    }

    private void MessageBox_of_NumberTooBig()
    {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("calc");
        alert.setHeaderText(null);
        alert.setContentText("超出可顯示範圍");
        alert.showAndWait();
    }

    @FXML
    public void btnFactorial_click(ActionEvent event)
    {
        out=IntegerString(Double.toString(Factorial(Double.parseDouble(Lbl1.getText()))));
        if(out.equals("Infinity"))
        {
            MessageBox_of_NumberTooBig();
            out="0";
        }
        Lbl1.setText(out);
    }

    @FXML
    public void btnE_click(ActionEvent event)
    {
        Lbl1.setText(Double.toString(Math.E));
    }

    @FXML
    public void btnPI_click(ActionEvent event)
    {
        Lbl1.setText(Double.toString(Math.PI));
    }

    @FXML
    public void trangle_fun(ActionEvent event)
    {
        Button sender=(Button)event.getSource();

        x = 0;
        if(Lbl1.getText().matches("^.*°$"))
            x=Double.parseDouble(Lbl1.getText().substring(0,Lbl1.getText().length()-1));
        else
            x=Double.parseDouble(Lbl1.getText());

        switch (sender.getText())
        {
            case "sin( )":
                Lbl1.setText(Double.toString(Math.sin(x*Math.PI/180)));
                break;
            case "cos( )":
                Lbl1.setText(Double.toString(Math.cos(x*Math.PI/180)));
                break;
            case "tan( )":
                Lbl1.setText(Double.toString(Math.tan(x*Math.PI/180)));
                break;
            case "arcsin( )":
                Lbl1.setText(Double.toString(Math.asin(x)*180/3.14)+"°");
                break;
            case "arccos( )":
                Lbl1.setText(Double.toString(Math.acos(x)*180/3.14)+"°");
                break;
            case "arctan( )":
                Lbl1.setText(Double.toString(Math.atan(x)*180/3.14)+"°");
                break;
        }
    }

    private void var_default()
    {
        Lbl1.setText("0");
        num1 = num2 = x = 0;
    }

    @Override
    public void initialize(URL url, ResourceBundle rb)
    {
        var_default();
    }
}
