#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
#include <ctime>
using namespace std;
void a(); void b(); void c(); void menu();

void split(const string& str, vector<string>& word, const string& key)
{
	int start = str.find_first_not_of(key);
	int end = 0;
	while (start != string::npos)
	{
		end = str.find_first_of(key, start + 1);
		if (end == string::npos)
			end = str.length();
		word.push_back(str.substr(start, end - start));
		start = str.find_first_not_of(key, end + 1);
	}
}

struct Student
{
	int id = 0;
	string name;
	int chi, eng, math,avg;
	int getid() //隨機產生Student id
	{
		srand(time(NULL));
		return rand() % 101;
	}
	int getchi(string x)
	{
		return atoi(x.c_str());
	}
	int geteng(string x)
	{
		return atoi(x.c_str());
	}
	int getmath(string x)
	{
		return atoi(x.c_str());
	}
	double getavg(int c, int e, int m)
	{
		return (c + e + m) / 3;
	}
};

vector<Student> stu_data;
void a()
{
	Student s;
	string k="";
	getline(cin, k);
	vector<string> in_data;
	split(k, in_data, " ");
	s.id = s.getid();
	s.name = in_data[0];
	s.chi = s.getchi(in_data[1].c_str());
	s.eng = s.geteng(in_data[2].c_str());
	s.math = s.getmath(in_data[3].c_str());
	s.avg = s.getavg(s.chi, s.eng, s.math);
	stu_data.push_back(s);
	cout << "\n";
	menu();
}

void rm_stu(vector<Student> & Students, int di)
{
	Students.erase(remove_if(Students.begin(), Students.end(), [&](const Student& Student) {return Student.id == di;}),Students.end());
}

void b()
{
	int id;
	cout << "輸入要刪除的學生ID -> ";
	cin >> id;
	rm_stu(stu_data, id);
	menu();
}

bool rankchi(const Student& a,const Student& b)
{
	return a.chi > b.chi;
}
bool rankeng(const Student& a, const Student& b)
{
	return a.eng > b.eng;
}
bool rankmath(const Student& a, const Student& b)
{
	return a.math > b.math;
}
bool rankavg(const Student& a, const Student& b)
{
	return a.avg > b.avg;
}

void c()
{
	int k;
	cout << "請選擇降序基準:\n1-chi\n2->eng\n3->math\n4->avg\n";
	cin >> k;
	switch (k)
	{
		case 1:
			sort(stu_data.begin(), stu_data.end(), rankchi);
			break;
		case 2:
			sort(stu_data.begin(), stu_data.end(), rankeng);
			break;
		case 3:
			sort(stu_data.begin(), stu_data.end(), rankmath);
			break;
		case 4:
			sort(stu_data.begin(), stu_data.end(), rankavg);
			break;
		default:
			break;
	}
	for (auto x:stu_data)
	{
		cout << x.id<<" " << x.name << " " << x.chi << " " << x.eng << " " << x.math<< " " << x.avg <<"\n";
	}
	cout<<"\n";
	menu();
}


void menu()
{
	string r;
	regex reg("^[1-4]{1}$");
	cout << "1->新增資料，格式==> name ch eng math(以空格分開)\n2->輸入指定id去刪除資料\n3->顯示資料(可選擇要由ch or eng or math or avg做基準、降序排序)\n4->離開\n";
	cin >> r;
	cin.ignore();
	if (regex_match(r, reg))
	{
		int flag = atoi(r.c_str());
		switch (flag)
		{
			case 1:
				a();
				break;
			case 2:
				b();
				break;
			case 3:
				c();
				break;
			case 4:
				cout << "Exit...\n";
				system("pause");
				exit(0);  //把整個程式結束
				break;
			default:
				break;
		}
	}
	else
	{
		cout << "輸入有誤，請重新輸入\n\n";
		menu(); //如果輸入的不是 1、2、3時，遞迴呼叫menu函式去讓使用者輸入
	}
}

int main()
{
	menu();
	return 0;
}