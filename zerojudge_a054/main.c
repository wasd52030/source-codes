#include <stdio.h>

int main()
{
	int k = 0;
	//ROC ID ENG->NUM
	int enn[] = {10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33};
	int lenofenn = sizeof(enn) / sizeof(enn[0]);

	while (scanf("%d", &k) != EOF)
	{
		int cnt = 0, chk = k % 10, q[30]={0}, i = 1; //i=1 -> 最後一位(去掉檢查碼)之加權值

		//將輸入的數字去掉最後一位(檢查碼)
		k /= 10;

		//取得剩下的八位數字(逆序)乘上對應之加權之總和
		while (k > 0)
		{
			cnt += (k % 10) * i;
			i++;
			k /= 10;
		}

		//窮舉所有英文字母
		for (int i = 0; i < lenofenn; i++)
		{
			//加上英文轉數字和其對應之加權
			q[i] += (enn[i] / 10) + (enn[i] % 10 * 9) + cnt;

			//求檢查碼
			int x = 10 - (q[i] % 10);
			x = x == 10 ? 0 : x;

			//如果求得的數字與輸入的最後一位相符，則輸出index對應的字母
			if (x == chk)
				printf("%c",(char)(65 + i));
		}
		printf("\n");
	}
	return 0;
}