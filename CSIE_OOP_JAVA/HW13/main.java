import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("�п�J�ǥͪ��m�W: ");
        String name = buf.readLine();

        System.out.print("�п�J�ǥͪ��y��: ");
        int number = Integer.parseInt(buf.readLine());

        if (number < 1) {
            System.out.print("��J��Ʀ��~");
        } else if (number > 60) {
            System.out.printf("%s�P�Ǥ��b3�~A�Z��\n",name);
        } else {
            switch (number % 3) {
                case 0:
                    System.out.printf("%s�P�Ǧb�ĤT��", name);
                    break;
                case 1:
                    System.out.printf("%s�P�Ǧb�Ĥ@��", name);
                    break;
                case 2:
                    System.out.printf("%s�P�Ǧb�ĤG��", name);
                    break;
                default:
                    break;
            }
        }
    }
}