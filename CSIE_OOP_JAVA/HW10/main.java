import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("�п�J�J�����H�H��: ");
        String adult = buf.readLine();

        System.out.print("�п�J�J���ൣ�H��: ");
        String children = buf.readLine();

        if (Integer.parseInt(adult) < 1) {
            System.out.println("�p�ĤJ���ݭn�j�H���P��");
        } else if (Integer.parseInt(children) < 1) {
            System.out.printf("�����J���H��: %d�Ӥj�H\n", Integer.parseInt(adult));
            System.out.printf("�����`���B: %d��\n", Integer.parseInt(adult)*589);      
        } else {
            System.out.printf("�����J���H��: %d�Ӥj�H\t%d�Ӥp��\n", Integer.parseInt(adult), Integer.parseInt(children));
            System.out.printf("�a�x����u�f�����`���B: %.0f��\n", (Integer.parseInt(adult) * 589 + Integer.parseInt(children) * 369) * 0.8);
        }
    }
}