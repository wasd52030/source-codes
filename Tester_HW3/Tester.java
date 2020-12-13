public class Tester 
{
    public static void main(String[] args) 
    {
        Student s1=new Student(109356001, "Peter", "MIS");
        Grading g1=new Grading(60);
        s1.addGrade(100);
        s1.addGrade(70);
        s1.addGrade(50);
        s1.addGrade(67);
        s1.addGrade(98);
        s1.addGrade(90);
        System.out.println("------info()");
        System.out.print(s1.info());
        System.out.println("summarizeGrade(...)");
        System.out.print(g1.summarizeGrade(s1));
    }
}
