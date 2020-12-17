#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Student
{
	int id = 0;
	int grade_hw = 0;
	int midexam = 0;
	int finalexam = 0;
	int Finalgrade = 0;

	int getfinal(int x, int y, int z)
	{
		return  x * 0.2 + y * 0.4 + z * 0.4;
	}
};

bool rankgrade(const Student& a, const Student& b)
{
	return a.Finalgrade > b.Finalgrade;
}

int main()
{
	int k;
	cout << "pls enter the num of student: ";
	cin >> k;
	vector<Student> data;
	for (int i = 0; i < k; i++)
	{
		Student input;
		cout << "pls enter " << i + 1 << "-th students's student id number: ";
		cin >> input.id;
		cout << "pls enter his hw grade: ";
		cin >> input.grade_hw;
		cout << "pls enter his mid exam grade: ";
		cin >> input.midexam;
		cout << "pls enter his final exam grade: ";
		cin >> input.finalexam;
		input.Finalgrade = input.getfinal(input.grade_hw, input.midexam, input.finalexam);
		data.push_back(input);
	}
	sort(data.begin(), data.end(), rankgrade);
	cout << "student ID number     Final Grade"<<"\n";
	for (const auto& k : data)
	{
		cout << k.id << "            " << k.Finalgrade<<"\n";
	}
	system("pause");
    return 0;
}