import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("�п�ж��H��: ");
        String People = buf.readLine();
        int people = Integer.parseInt(People);

        System.out.print("�п�ж��۵M���u�j��: ");
        String Lux = buf.readLine();
        int lux = Integer.parseInt(Lux);

        String quality1 = "", quality2 = "", action = "";
        if (lux > 700) {
            quality1 = "��";
            quality2 = "����";
        } else if (lux > 300 && lux <= 700) {
            quality1 = "���q";
            quality2 = "����";
        } else if (lux < 300) {
            quality1 = "����";
            quality2 = "����";
        }

        if (people > 0 && quality2.equals("����")) {
            action = "�����ө�";
        } else if (people > 0 && quality2.equals("����")) {
            action = "���}�ө�";
        } else if (people < 0 && quality2.equals("����")) {
            action = "�����ө�";
        } else if (people < 0 && quality2.equals("����")) {
            action = "���}�ө�";
        }

        System.out.println("[�ж�]");
        System.out.printf("�H��:%d�H\n", people);
        System.out.printf("���u�j��: %dLux(%s)\n", lux,quality1);
        System.out.printf("���u�~��: %s\n", quality2);
        System.out.printf("�ʧ@: %s\n", action);
    }
}