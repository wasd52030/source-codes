import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q_2 {
	public static void main(String[] args) throws IOException {
		BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
		String c;
		do {
			System.out.print("�z���m�W : ");
			String name = buf.readLine();
			System.out.print("�z���ʧO : ");
			String gender = buf.readLine();
			Student student = new Student(name, gender);
			System.out.print("�а��٦��U�@��ܡH(��Jy�~��) : ");
			c = buf.readLine();
		} while (c.equals("y"));
	}
}

class Student {
	// �R�A�ܼ�(static variable)�������쪫�󲣥ʹN�i�H�ߧY�s��
	// �i���@��class�@�Ϊ������ܼ�
	static int m_num = 0, f_num = 0;
	private String name, gender;

	Student(String name, String gender) {
		this.gender = name;
		if (gender.equals("�k")) {
			this.gender = "�k";
			m_num++;
			System.out.println(name + "���͡A�z�O���ղ�" + m_num + "��k��");
		} else if (gender.equals("�k")) {
			this.gender = "�k";
			f_num++;
			System.out.println(name + "�p�j�A�z�O���ղ�" + f_num + "��k��");
		} else
			System.out.println("���ըå��ۦ��ʧO�� " + gender + " ���ǥ�");
	}
}