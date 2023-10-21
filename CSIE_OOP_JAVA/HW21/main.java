import java.io.IOException;
import java.util.Scanner;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);

        System.out.println("�п�J�Ыμƶq: ");
        int number = scan.nextInt();
        house[] houses = new house[number];

        for (int i = 0; i < houses.length; i++) {
            System.out.printf("�аݲ�%d�ɩФl�W��: ", i + 1);
            String n = scan.next();
            System.out.printf("�аݲ�%d�ɩФl����: ", i + 1);
            int r = scan.nextInt();
            houses[i] = new house(n, r);
        }

        int sum = 0;
        double avg = 0;
        for (house house : houses) {
            sum += house.rental;
        }
        avg = (double) sum / houses.length;

        int key = 0;
        do {
            System.out.println("�п�ܤU�C�ﶵ: ");
            System.out.println("(1) �C�X�C�@���ЫΪ��W�٤ί���");
            System.out.println("(2) �C�X���氪�󥭧����ЫΪ��W�٤ί���");
            System.out.println("(3) �C�X����C�󥭧����ЫΪ��W�٤ί���");
            key = scan.nextInt();
            switch (key) {
                case 1:
                    for (int i = 0; i < houses.length; i++) {
                        house house = houses[i];
                        System.out.printf("��%d�ɩФl%s\n", i + 1, house);
                    }
                    break;
                case 2:
                    for (int i = 0; i < houses.length; i++) {
                        house house = houses[i];
                        if ((double) house.rental > avg) {
                            System.out.println(house);
                        }
                    }
                    break;
                case 3:
                    for (int i = 0; i < houses.length; i++) {
                        house house = houses[i];
                        if ((double) house.rental < avg) {
                            System.out.println(house);
                        }
                    }
                    break;
                default:
                    System.out.println("�п�J���Ī����(1,2, ��3)");
                    continue;
            }
        } while (key > 4);
    }
}

class house {
    public String name;
    public int rental;

    public house(String n, int r) {
        name = n;
        rental = r;
    }

    @Override
    public String toString() {
        return String.format("�W��: %s, ����: %d", name,rental);
    }
}