import java.io.IOException;

public class main {
    public static void main(String[] args) throws IOException {
        int target = 10000000;
        int investmentAmount = 100000;
        double investmentResult = 0;

        do {
            System.out.printf("��J%d��\n", investmentAmount);

            // �i�ʪѼ�
            int stock = investmentAmount / 100;
            double interest = 0, totalInterest = 0;
            for (int i = 1; i <= 120; i++) {
                int annulStock = 25 * (stock / 1000);
                if (stock >= 1000) {
                    interest = stock * 1.5;
                    stock += annulStock;
                    totalInterest += interest;
                }
            }
            investmentResult = 100 * stock + totalInterest;
            System.out.printf("10�~��������`�ѼƬ�%d�ѡA�t���`�B��%.1f��\n", stock, totalInterest);
            System.out.printf("�`����:%.1f��\n\n", investmentResult);
            
            if (investmentResult < target) {
                investmentAmount++;
            }
        } while (investmentResult < target);
        System.out.printf("��l�����B�ܤֻݭn%d���A�̦~���`�겣�~�|�W�L1000�U��\n", investmentAmount);
    }
}