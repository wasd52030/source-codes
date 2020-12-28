#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
using namespace std;
void a(); void b(); void menu();

/*
  string::find_first_of(const string& str,size_t pos=0)
  -> 從pos(default->0)開始，尋找第一個和str相符的字串所在的位置，找不到則返回string::npos
*/
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

struct Date
{
	string year = "";
	string month = "";
	string Eng_month[12] = { "January","February","March","April","May","June","July","August","September","October","November","December" };
	string digits[10] = { "零","一","二","三","四","五","六","七","八","九" };
	int date=0;
	int md_flag=0;

	string GetKmtYear(string in)
	{
		string out = "";
		int i = atoi(in.c_str()) - 1911;
		if (i<0)
		{
			out = "民國前" + to_string(abs(i)) + "年";
		}
		else if(i==0)
		{
			out = "民國元年";
		}
		else
		{
			out = "民國" + to_string(i) + "年";
		}
		return out;
	}

	string GetEnMonth(string in)
	{
		return Eng_month[atoi(month.c_str()) - 1];
	}

	string GetCnDate(int in)
	{
		int m = in / 10;
		int d = in % 10;
		string out = "";
		if (m == 0)
		{
			out += digits[d] + "日";
		}
		else if (m != 0)
		{
			if (m == 1 && d == 0)
			{
				out += "十日";
			}
			else if(m != 1 && d == 0)
			{
				out += digits[m]+"十日";
			}
			else if (m == 1)
			{
				out += "十" + digits[d] + "日";
			}
			else
			{
				out += digits[m] + "十"+ digits[d] + "日";
			}
		}
		return out;
	}
	
	int get_md_flag(int m, int d)
	{
		return pow(m,2) + d; //set flag as m^2+d
	}
};

bool rankflag(const Date& a, const Date& b)
{
	if (atoi(a.year.c_str()) == (atoi(b.year.c_str())))
	{
		return a.md_flag < b.md_flag;
	}
	else
	{
		return atoi(a.year.c_str()) < (atoi(b.year.c_str()));
	}
}

void menu()
{
	string r;
	regex reg("^[1-3]{1}$");
	cout << "1->input\n2->output\n3->exit\n";
	cin >> r;
	if (regex_match(r, reg))
	{
		if (r == "3")
		{
			cout << "Exit...\n";
			system("pause");
			exit(0);  //把整個程式結束
		}
		else if (r == "1")
		{
			a();
		}
		else if (r == "2")
		{
			b();
		}
	}
	else
	{
		cout << "輸入有誤，請重新輸入\n\n";
		menu(); //如果輸入的不是 1、2、3時，遞迴呼叫menu函式去讓使用者輸入
	}
}


vector<Date> operation;
void a()  //選單1
{
	string x;
	regex input_check("^(([1-9]{1})|([1-9]{1}[0-9]{1,}))\/(([0]{1}[1-9]{1})|([1]{1}[0-2]{1}))\/(([0]{1}[1-9]{1})|([1-2]{1}[0-9]{1})|([3]{1}[0-1]{1}))$");
	Date d;
	vector<string> split_contianer;
	while (true)
	{
		cin >> x;
		if (regex_match(x, input_check))
		{
			split(x, split_contianer, "/");
			d.year = split_contianer[0];
			d.month = split_contianer[1];
			d.date = atoi(split_contianer[2].c_str());
			d.md_flag = d.get_md_flag(atoi(d.month.c_str()), d.date);
			operation.push_back(d);
			cout << "\n";
			break;
		}
		else
		{
			cout << "輸入有誤，請重新輸入\n";
		}
	}
	menu();
	
}

void b() //選單2
{
	sort(operation.begin(), operation.end(), rankflag);
	for (auto d : operation)
	{
		cout<< d.GetKmtYear(d.year) + d.GetEnMonth(d.month) + d.GetCnDate(d.date)<<"\n";
	}
	cout << "\n";
	menu();
}

int main()
{	
	menu();
	return 0;
}