import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

        int total = -1;
        do {
            System.out.print("�п�J�U�ڪ��B(�j�󵥩�0): ");
            total = Integer.parseInt(buf.readLine());
            if (total < 0) {
                System.out.println("�U�ڪ��B���o�p��0�A�Э��s��J");
            }
        } while (total < 0);

        int year = -1;
        do {
            System.out.print("�п�J�U�ڦ~��(�ܤ�1�~): ");
            year = Integer.parseInt(buf.readLine());
            if (total < 0) {
                System.out.println("�U�ڦ~�Ƥ��o�p��1�~");
            }
        } while (year < 1);

        int x = total / year;
        for (int i = 1; i <= year; i++) {
            double finalMoney = x + (total * (1.5 / 100));
            System.out.printf("%d�~����ٴڥ��[�Q%.2f��(������%d���B�Q����%.2f��)\n", i, finalMoney, x, total* (1.5/100));        
            total -= x;
        }
    }
}