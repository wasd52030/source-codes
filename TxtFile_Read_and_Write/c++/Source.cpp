#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool Isinteger(double n)
{
	double x = ceil(n);
	return x = floor(n);
}

void main()
{
	ifstream f1("in.txt");
	ofstream f2("out.txt");

	string x;
	vector<double> Data;
	double sum = 0, odd = 0, even = 0;

	while (getline(f1,x))
	{
		Data.push_back(atof(x.c_str()));
	}

	sort(Data.begin(), Data.end());

	f2 << "��J��Ƹg�Ƨǫ� : ";

	for (double i = 0; i < Data.size(); i++)
	{
		f2 << Data[i] << " ";
		sum += Data[i];
		if (Isinteger(Data[i]) == true) 
		{
			if (fmod(Data[i],2)==0) //���l�B��l % ���䴩Double
				even++;
			else
				odd++;
		}
	}

	auto max = max_element(Data.begin(),Data.end());
	auto min = min_element(Data.begin(), Data.end());
	double avg = sum / Data.size();

	f2 << "\n";
	f2 << "�̤j�� :" << *max<<"\n";
	f2 << "�̤p�� :" << *min << "\n";
	f2 << "������ :" << avg << "\n";
	f2 << "�_�Ʀ�" << odd << "��" << "\n" << "���Ʀ�" << even << "��";

	f1.close();
	f2.close();

	cout << "��Ƥ��R����\n";

	system("pause");
}