public class hw52{
    public static void main(String[] args){
        // �bJava�{�����A�p�G�b�B�I�ƫ��A���ŧi��ƪ��ܷ|�ɤ@�Ӥp�Ʀ쬰0�A�i�H�z�LSystem.out.printf��ƥH���x��c�y���榡�Ӿ�z
        float var=111;
        System.out.println("�ܼ� var ���Ȭ�"+ var);
        System.out.printf("�ܼ� var ���Ȭ�%.0f\n", var);

        // �bJava�{�����A�y�B�I�ƼƦr�z�A�w�]���A�Odouble
        // double���float�@�˷|�X�{error
        // incompatible types: possible lossy conversion from double to float
        // �ݱj�নfloat�~��sĶ�q�L
        // var =(float)333.3;
        // float�Pdouble�t���b��float�i�H�O�Ҧb�p���I��6��O��T���A��double�i�H��O�Ҥp���I��15��
        var =333.3;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 

        var=5;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 
        System.out.printf("�ܼ� var ���Ȭ�%.0f\n", var);

        // �bJava�{�����A�y�B�I�ƼƦr�z�A�w�]���A�Odouble
        // double���float�@�˷|�X�{error
        // incompatible types: possible lossy conversion from double to float
        // �ݱj�নfloat�~��sĶ�q�L
        // var=(float)7.654321;
        // float�Pdouble�t���b��float�i�H�O�Ҧb�p���I��6��O��T���A��double�i�H��O�Ҥp���I��15��
        var=7.654321;
        System.out.println("�ܼ� var ���Ȭ�"+ var); 
    }
}