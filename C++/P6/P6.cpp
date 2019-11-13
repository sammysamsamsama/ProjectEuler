/* 
 * The sum of the squares of the first ten natural numbers is,
 * 
 * 1^2 + 2^2 + ... + 10^2 = 385
 * 
 * The square of the sum of the first ten natural numbers is,
 * 
 * (1 + 2 + ... + 10)^2 = 55^2 = 3025
 * 
 * Hence the difference between the sum of the squares of the first ten 
 * natural numbers and the square of the sum is 3025 − 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the first one 
 * hundred natural numbers and the square of the sum.
 *
 */

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream myfile;
	myfile.open ("result.txt");

	int difference;
	int sum_of_squares;
	int square_of_sum;
	int sum = 0;
	
	for (int i = 1; i <= 100; i++) {
		sum += i;
		sum_of_squares += i * i;
	}
	square_of_sum = sum * sum;
	
	difference = square_of_sum - sum_of_squares;
	
	cout << "Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: " << difference << endl;
	
	myfile << "Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: " << difference << endl;
	myfile.close();
	
	return 0;
}

