import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("�п�a�x���Ѧ~�H�H��: ");
        String Old = buf.readLine();
        int old = Integer.parseInt(Old);

        System.out.print("�п�a�x���C�~�H�H��: ");
        String Young = buf.readLine();
        int young = Integer.parseInt(Young);

        System.out.print("�п�a�x�~���J(��): ");
        String Money = buf.readLine();
        float money = Float.parseFloat(Money);

        // �|�B�ŶZ
        float taxP = 0;
        if (money > 2000000) {
            taxP = 30 / 100f;
        } else if (money > 1500000 && money <= 2000000) {
            taxP = 20 / 100f;
        } else if (money > 1000000 && money <= 1500000) {
            taxP = 15 / 100f;
        } else {
            taxP = 10 / 100f;
        }

        // �K�|���e
        float noTaxGate = money / (young + old);
        if (noTaxGate < 15000) {
            taxP = 0;
        }

        //�ѤH��K
        taxP -= old * (4 / 100f);

        System.out.printf("�a�x�H�Ʋզ�: �Ѧ~�H%d�H�A�C�~�H%d�H�A�`�H��%d�H\n", old, young, old + young);
        System.out.printf("�|�v: %.0f%%\n", (taxP*100));
        System.out.printf("�ұo�|�`�B: %.1f\n", (money * taxP));
    }
}