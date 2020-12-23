#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
using namespace std;


void split(const std::string& s, std::vector<std::string>& sv, const char delim = ' ')
{
	sv.clear();
	std::istringstream iss(s);
	std::string temp;

	while (std::getline(iss, temp, delim))
	{
		sv.emplace_back(std::move(temp));
	}
	return;
}

struct Date
{
	string year = "";
	string month = "";
	string Eng_month[12] = { "January","February","March","April","May","June","July","August","September","October","November","December" };
	string digits[10] = { "零","一","二","三","四","五","六","七","八","九" };
	int date=0;
	int month_date_flag=0;

	int getminYr(string in)
	{
		return atoi(year.c_str()) - 1911;
	}
	string getfin_yr(int i)
	{
		string out = "民國" + to_string(atoi(year.c_str()) - 1911) + "年";
		return out;
	}
	string getEngmou(string in)
	{
		return Eng_month[atoi(month.c_str()) - 1];
	}
	string getchidate(int in)
	{
		int dd = in / 10;
		int d = in % 10;
		string out = "";
		if (dd == 0)
		{
			out += digits[d] + "日";
		}
		else if (dd != 0)
		{
			if (dd == 1 && d == 0)
			{
				out += "十日";
			}
			else if (dd == 1)
			{
				out += "十" + digits[d] + "日";
			}
			else
			{
				out += digits[dd] + "十"+ digits[d] + "日";
			}
		}
		return out;
	}
	int get_month_date_flag(int m, int d)
	{
		return pow(m,2) + d;
	}
};

vector<Date> dd;

void a()  //選單1
{
	string k;
	Date d;
	vector<string> data;
	cin >> k;
	split(k, data, '/'); 
	d.year = data[0];
	d.month = data[1];
	d.date = atoi(data[2].c_str());
	d.month_date_flag = d.get_month_date_flag(atoi(d.month.c_str()), d.date);
	dd.push_back(d);
}

bool rankflag(const Date& a, const Date& b)
{
	if (atoi(a.year.c_str()) == (atoi(b.year.c_str())))
	{
		return a.month_date_flag < b.month_date_flag;
	}
	else
	{
		return atoi(a.year.c_str()) < (atoi(b.year.c_str()));
	}
}

void b() //選單2
{
	sort(dd.begin(), dd.end(), rankflag);
	for (auto d : dd)
	{
		cout<<d.getfin_yr(d.getminYr(d.year)) + d.getEngmou(d.month) + d.getchidate(d.date)<<"\n";
	}
}

int main()
{	
	int r;
	regex reg("^[1-3]{1}$");
	while (true)
	{
		cout << "1->input\n2->output\n3->exit\n";
		cin >> r;
		if (regex_match(to_string(r), reg))
		{
			if (r == 3)
			{
				break;
			}
			else if (r == 1)
			{
				a();
			}
			else if (r == 2)
			{
				b();
			}
		}
		else
		{
			cout << "Error,pls restart this program\n";
			break;
		}
	}
	//system("pause");
}