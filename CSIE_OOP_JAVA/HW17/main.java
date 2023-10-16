import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

        int total = -1;
        do {
            System.out.print("�п�J��l�����B(�j�󵥩�100000): ");
            total = Integer.parseInt(buf.readLine());
            if (total < 100000) {
                System.out.println("��l�����B���o�p��0�A�Э��s��J");
            }
        } while (total < 100000);

        // �i�ʪѼ�
        int stock = total / 100;
        // �h�٪��B
        float back = total % 100;
        System.out.printf("�h��%.1f��\n",back);

        double interest = stock * 1.5, totalInterest = 0;
        for (int i = 1; i <= 120; i++) {
            int annulStock = 25 * (stock / 1000);
            System.out.printf("��%d�Ӥ�A����%d��(%d�i)�A�t��: %.1f���A�t��: %d��\n", i, stock, stock / 1000, interest, annulStock);       
            if (stock >= 1000) {
                stock += annulStock;
                interest = stock * 1.5;
                totalInterest += interest;
            }
        }
        System.out.printf("10�~��������`�ѼƬ�%d�ѡA�t���`�B��%.1f��\n", stock, totalInterest);
        System.out.printf("�`����:%.1f��\n", 100 * stock + totalInterest);
    }
}