// �Ҫ�class�ɯ������ܼ�b���B��P����

public class main {
    public static void main(String[] args) {
        // �а� a ����X���G�O�_�P�p�������X���G�@��?���P���ܡA�иԭz��]�C
        // �p������G�Pjava���浲�G���P
        // ��]��java�b�i�氣�k�ɦp�G���ƬOint���ܵ��G�|�Q���int�A�p�Ƴ����q�q����
        double a = 100 / 71 * 47 + 18 - 7 - 51 * 87 / 5 + 41 * 2 / 75 + 100;
        System.out.println("1.a");
        System.out.println("calculator result: -709.109483568075");
        System.out.println("java result: " + a + "\n");

        // �а� b c �ȬO�_���P?�����ܡA�иԭz��]�C
        // b c���G���P
        // ��]���~�@�ˡAjava�b�i�氣�k�ɦp�G���ƬOint���ܵ��G�|�Q���int�A�p�Ƴ����q�q����
        float b = 100 / 47 * 47;
        System.out.println("1.b");
        System.out.println("calculator result: 100");
        System.out.println("java result: " + b);

        // ��ƹw�]��int�A�B�I�w�]��double
        // �ɭP�U�����{���|�X�{�U�����sĶ���~
        // Type mismatch: cannot convert from double to float
        // float c = 100 / 47.0 * 47.0;
        // System.out.println("1.c");
        // System.out.println("calculator result: 100");
        // System.out.println("java result: " + c + "\n");
    }
}