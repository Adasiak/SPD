#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	fstream file;
	file.open("JACK3.DAT");
	if(file.good())
	{
		int quantity;
		file >> quantity;
		quantity=quantity+1;
		int *r=new int[quantity];
		int *p=new int[quantity];
		p[0]=0;
		r[0]=0;
		for(int i=0; i<quantity; i++)
		{
			file >> r[i];
			file >> p[i];
		}
		file.close();
		//for (int i=0; i<quantity; i++)
		//	cout << "r " << r[i] << " p " << p[i] << endl;

		for (int i=0; i<quantity; i++)
		{
			for(int j=1; j<quantity; j++)
			{
				if(r[j-1]>r[j])
				{
					swap(r[j-1], r[j]);
					swap(p[j-1], p[j]);
				}
			}
		}


		int *C=new int[quantity];
		C[0]=0;
		for (int i=1; i<quantity; i++)			
			C[i]=max(r[i], C[i-1])+p[i];

		for (int i=1; i<quantity; i++)
			cout << C[i] << " ";
		cout << endl;
		cout << "Cmax " << C[quantity-1] << endl;

		delete [] C;
		delete [] r;
		delete [] p;
	}
}