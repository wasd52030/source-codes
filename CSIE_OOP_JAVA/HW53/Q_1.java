import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q_1 {
	public static void main(String arg[]) throws IOException {
		BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("�п�J�b�|�G");
		double r = Double.parseDouble(buf.readLine());
		// Circle.pi=5;
		Circle c = new Circle(r);
	}
}
class Circle {
	// �bjava���p�ݫŧi�`��(const)�n�ϥ�final�׹�
	final static double pi = 3.14;

	Circle(double r) {
		System.out.println("�ꪺ���n��:" + r*r*pi);
	}
}