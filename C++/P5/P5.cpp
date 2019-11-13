/* 
 * 2520 is the smallest number that can be divided by each of the numbers 
 * from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of 
 * the numbers from 1 to 20?
 *
 */

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream myfile;
	myfile.open ("result.txt");

	int smallest = -1;

	for (int i = 20; true; i++) {
		bool divisible = true;
		for (int j = 1; j <= 20; j++) {
			if (i % j != 0) {
				divisible = false;
				break;
			}
		}
		if (divisible) {
			smallest = i;
			break;
		}
	}
	
	cout << "Smallest positive number that is evenly divisible by all of  * the numbers from 1 to 20: " << smallest << endl;
	
	myfile << "Smallest positive number that is evenly divisible by all of  * the numbers from 1 to 20: " << smallest << endl;
	myfile.close();
	
	return 0;
}

