import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("�п�J�ʪ��w��: ");
        int number = Integer.parseInt(buf.readLine());
        int total = 0;
        char key = 'Y';

        while (key == 'Y') {
            System.out.println("1.�F�o�G7,000 ��/��");
            System.out.println("2.�Ȥl�G499 ��/��");
            System.out.println("3.��l�G759 ��/��");
            System.out.println("4.�����M�G58 ��/��");

            System.out.print("�п�ܭn�R�����~: ");
            char item = buf.readLine().charAt(0);

            System.out.print("�п�ܭn�R���ƶq: ");
            int itemNumber = Integer.parseInt(buf.readLine());

            if (itemNumber < 1) {
                System.out.println("�ƶq���o�p��1�A�Э��s��J");
                continue;
            }

            switch (item) {
                case '1':
                    total += 7000 * itemNumber;
                    break;
                case '2':
                    total += 499 * itemNumber;
                    break;
                case '3':
                    total += 759 * itemNumber;
                    break;
                case '4':
                    total += 58 * itemNumber;
                    break;
                default:
                    System.out.println("�d�L���ӫ~");
                    break;
            }

            System.out.print("�ٻݭn�ʶR���~��?");
            key = buf.readLine().charAt(0);
            System.out.println(key);
        }
        
        System.out.printf("�w��%d��\n", number);
        System.out.printf("�ʪ�%d��\n", total);
        if (total > number) {
            System.out.printf("�W�X�w��%d��\n", total - number);
        } else {
            System.out.printf("�ѤU�w��%d��\n", number - total);
        }
    }
}