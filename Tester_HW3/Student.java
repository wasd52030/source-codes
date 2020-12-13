public class Student 
{
	int studentID;
	String name;
	String department;
	int grade;
	int[] grades=new int[5];
	int gradesIndex=-1;
	
  
	public Student(int studentID,String name,String department)
	{
    	this.studentID=studentID;
    	this.name=name;
		this.department=department;	
    }
	public void setStudentID(int student) {}
	
	public void setName(String name) {}
	
	public void setDepartment(String department) {}  
	  
	public int getStudentID()
	{
		return studentID;
	}

	public String getName() 
	{
		return name;
	}

	public String getDepartment() 
	{
		return department;
	}

	public int[] getGrades() 
	{
		return grades;
	}


	public void addGrade(int grade) 
	{
		try 
		{
			gradesIndex++;
			grades[gradesIndex]=grade;
		} 
		catch (ArrayIndexOutOfBoundsException e) 
		{
			System.out.printf("Array index out of bounds.\n");
		}
	}
	
	public String info() 
	{
		String out="";
		out+="Student ID: "+studentID+"\n";
		out+="   Name:"+name+"\n";
		out+="Department:"+department+"\n";
		out+="  Grades: ";
		for(int i:grades)
		{
			out+=i+" ";
		}
		out+="\n";
		return out;
	}
}
