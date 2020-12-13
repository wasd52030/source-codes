public class Grading 
{
	private int passMark;

	public Grading(int passMark) 
	{
		this.passMark=passMark;
	}

	public void setPassMark(int passMark) {}
		
	public int getPassMark( ) 
	{
		return passMark;
	}
		
	public String toLetterGrade(int score) 
	{
		if (score<=100&&score>=80) {return "A";}
		else if (score<=79&&score>=70) {return "B";}
		else if (score<=69&&score>=60) {return "C";}
		else if (score<=59&&score>=50) {return "D";}
		else if (score<=49&&score>=1) {return "E";}
		else if (score==0) {return "X";}
		else {return "";}
	}

	public double calculateAvg(int[] grades) 
	{
		int sum=0;
		for(int grade:grades) 
		{
			sum=sum+grade;
		}
		double avg=sum/grades.length;
		return avg;
	}

	public String summarizeGrade(Student s1) 
	{
		int pass=0;int fail=0;
		for(int grade:s1.grades) 
		{
			if(grade>=passMark) 
			{
				pass++;
			}
			else
			{
				fail++;
			}
		}
		String average="Avg. Score:"+String.valueOf(calculateAvg(s1.grades))+"\n";
		String pass1="Pass: "+pass+",";
		String fail1="failed: "+fail+"\n";
		String result=average+pass1+fail1+"\n";
		return result;
	}
}
