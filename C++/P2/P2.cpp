/* 
 * Each new term in the Fibonacci sequence is generated by adding the
 * previous two terms. By starting with 1 and 2, the first 10 terms will be:
 * 
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * 
 * By considering the terms in the Fibonacci sequence whose values do not
 * exceed four million, find the sum of the even-valued terms.
 *
 */

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int sum = 2;
	int nums[] = {1, 2, 3};
	
	// for Fibonacci numbers less than 4 million
	while (nums[2] < 4000000) {
		if (nums[2]%2 == 0) {
			sum += nums[2];
		}
		
		nums[0] = nums[1];
		nums[1] = nums[2];
		nums[2] = nums[0] + nums[1];
	}
	
	cout << sum << endl;
	
	ofstream myfile;
	myfile.open ("result.txt");
	myfile << sum << endl;
	myfile.close();
	
	return 0;
}

