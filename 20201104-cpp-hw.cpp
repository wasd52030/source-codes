#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a0=0,a10=0,a20=0,a30=0,a40=0,a50=0,a60=0,a70=0,a80=0,a90=0;
    int c=0;
    vector<int> data;

    while(true)
    {
        cin>>c;
        if(c<0||c>100)
            break;
        else
            data.push_back(c);
    }

    for(int k:data)
        cout<<k<<" ";

    cout<<"\n";

    for(int i=0;i<data.size();i++)
    {
        switch(data[i])
        {
            case 0 ... 9:
            case 10:
                a0++;
                break;
            case 11 ... 19:
            case 20:
                a10++;
                break;
            case 21 ... 29:
            case 30:
                a20++;
                break;
            case 31 ... 39:
            case 40:
                a30++;
                break;
            case 41 ... 49:
            case 50:
                a40++;
                break;
            case 51 ... 59:
            case 60:
                a50++;
                break;
            case 61 ... 69:
            case 70:
                a60++;
                break;
            case 71 ... 79:
            case 80:
                a70++;
                break;
            case 81 ... 89:
            case 90:
                a80++;
                break;
            case 91 ... 99:
            case 100:
                a90++;
                break;
            default:
                break;
        }
    }

    sort(data.begin(),data.end());

    //求中位數
    int mid=0;
    if(data.size()==0)
        mid=0;
    else
    {
        sort(data.begin(),data.end());
        if(data.size()%2==0)
            mid=data[data.size()/2-1]+data[data.size()/2];
        else
            mid=data[data.size()/2];
    }


    cout<<"0-10有"<<a0<<"個"<<"\n";
    cout<<"10-20有"<<a10<<"個"<<"\n";
    cout<<"20-30有"<<a20<<"個"<<"\n";
    cout<<"30-40有"<<a30<<"個"<<"\n";
    cout<<"40-50有"<<a40<<"個"<<"\n";
    cout<<"50-60有"<<a50<<"個"<<"\n";
    cout<<"60-70有"<<a60<<"個"<<"\n";
    cout<<"70-80有"<<a70<<"個"<<"\n";
    cout<<"80-90有"<<a80<<"個"<<"\n";
    cout<<"90-100有"<<a90<<"個"<<"\n";
    cout<<"mid="<<mid<<"\n";


    switch(mid)
    {
        case 0 ... 9:
        case 10:
            cout<<"中位數在0-10之間"<<"\n";
            break;
        case 11 ... 19:
        case 20:
            cout<<"中位數在10-20之間"<<"\n";
            break;
        case 21 ... 29:
        case 30:
            cout<<"中位數在20-30之間"<<"\n";
            break;
        case 31 ... 39:
        case 40:
            cout<<"中位數在30-40之間"<<"\n";
            break;
        case 41 ... 49:
        case 50:
            cout<<"中位數在40-50之間"<<"\n";
            break;
        case 51 ... 59:
        case 60:
            cout<<"中位數在50-60之間"<<"\n";
            break;
        case 61 ... 69:
        case 70:
            cout<<"中位數在60-70之間"<<"\n";
            break;
        case 71 ... 79:
        case 80:
            cout<<"中位數在70-80之間"<<"\n";
            break;
        case 81 ... 89:
        case 90:
            cout<<"中位數在80-90之間"<<"\n";
            break;
        case 91 ... 99:
        case 100:
            cout<<"中位數在90-100之間"<<"\n";
            break;
        default:
            break;
    }

    system("pause");
}
