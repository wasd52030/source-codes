public class P1{
    public static void main(String[] args){
        // 1.String�PChar��X���G���P
        //  - String��X���G�GString = 88
        //  - Char��X���G�GChar = X
        // �r��(char)��X�ɷ|�̷өҤ䴩���r��������������X�A�Ӧr��O�ѳ\�h�r���զ����}�C
        String a="88";
        char b=88;
        System.out.println("String = "+a);
        System.out.println("Char = "+b);

        // 2
        //  - String��X���G�Ga = 881
        //  - Char��X���G�Gb = Y
        //  - ��string�Pint�ۥ[�ɷ|�Nint�֨�r��̭�
        //  - ��char�Pint�ۥ[�ɷ|�Nchar����+1�A�����^�r����
        a=a+1;
        b=(char)(b+1);
        System.out.println("a = "+a);
        System.out.println("b = "+b);
    }
}