public class hw51{
    public static void main(String[] args){
        int var=111;
        System.out.println("�ܼ� var ���Ȭ�"+ var);

        // �bint���ϥΤp�Ʒ|�o�ͥH�U�sĶ���~
        // incompatible types: possible lossy conversion from double to int
        // �ݱj�নint�~��sĶ�q�L�A���L�p�Ƴ�����������
        // var=(int)333.3;
        var =333.3;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 

        var=5;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 

        // �bint���ϥΤp�Ʒ|�o�ͥH�U�sĶ���~
        // incompatible types: possible lossy conversion from double to int
        // �B���浲�G�u�|�d�U��Ƴ����A�p�Ƴ�����������
        // �ݱj�নint�~��sĶ�q�L�A���L�p�Ƴ�����������
        // var=(int)7.654321;
        var=7.654321;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 
    }
}