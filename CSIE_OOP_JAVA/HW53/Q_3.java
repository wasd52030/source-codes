import java.io.*;

public class Q_3 {
	public static void main(String[] args) throws IOException {
		BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("�п�J�b�|�G");
		double r = Double.parseDouble(buf.readLine());
		System.out.print("�п�J��P�v(PI)�G");
		double pi = Double.parseDouble(buf.readLine());
		Circle c = new Circle(r,pi);
	}
}

class Circle {
	final double pi = 3.14;

	Circle(double r , double pi) {
		
		System.out.println("�ꪺ�b�|��:" + r + "�API = " + pi);
		System.out.println("�ꪺ���n��:" + r*r*pi);
	}
}