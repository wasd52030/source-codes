#include <iostream>

int search(int *arr, int key, int left, int right)
{
    int m = left + (right - left) / 2;

    if (left > right)
        return 0;

    if (arr[m] < key)
        return search(arr, key, m + 1, right);

    if (arr[m] > key)
        return search(arr, key, left, m - 1);

    if (arr[m] == key)
        return m + 1;
}

int main(int argc, char const *argv[])
{
    int n, k;
    while (scanf("%d %d", &n, &k) != EOF)
    {
        int data[110000];
        int key[110000];
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &data[i]);
        }

        for (int i = 0; i < k; i++)
        {
            scanf("%d", &key[i]);
        }

        for (int i = 0; i < k; i++)
        {
            printf("%d\n", search(data, key[i], 0, n));
        }
    }
    return 0;
}