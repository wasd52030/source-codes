import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {
    public static void main(String[] args) throws IOException {
        final double AU = 149597871;

        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("�п�J���P��Ӷ����Ѥ���: ");
        String Venus = buf.readLine();

        System.out.print("�п�J���P��Ӷ����Ѥ���: ");
        String Mars = buf.readLine();

        System.out.print("�п�J�����P��Ӷ����Ѥ���: ");
        String Neptune = buf.readLine();

        System.out.printf("���P��Ӷ����Z����: %.2f����\n",Double.parseDouble(Venus) * AU);
        System.out.printf("���P��Ӷ����Z����: %.2f����\n",Double.parseDouble(Mars) * AU);
        System.out.printf("�����P��Ӷ����Z����: %.2f����\n",Double.parseDouble(Neptune) * AU);
    }
}