#include <iostream>
using namespace std;


int main()
{
	int t;
	cin >> t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		int array[n];
		for(int j=0;j<n;j++)
		{
			int lol;
			cin>>lol;
			array[j]=lol;
		}
		for (int j=0;j<n;j++)
		{
			if (array[j]%2==0)
			{
				cout<<1<<"\n";
				cout<<j<<"\n";
				break;
			}
			int count=0;
			if (array[j]%2!=0 && count==1)
			{
				// cou
			}
		}
	}
}