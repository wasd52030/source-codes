#include <iostream>
#include <string>
using namespace std;

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