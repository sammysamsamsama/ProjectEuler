/* 
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
 * that the 6th prime is 13.
 * 
 * What is the 10 001st prime number?
 *
 */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	ofstream myfile;
	myfile.open ("result.txt");

	int p; // number we're checking for prime
	int n; // which prime we're on
	vector<int> primes; // to store found primes
	
	// starting with 3, the 2nd prime, until we reach the 10001st prime
	for (p = 3, n = 1; n < 10001; p+=2) {
		// for each of the previous primes
		for (int i = 0; i <= primes.size(); i++) {
			// if we found a new prime
			if (i == primes.size()) {
				primes.push_back(p);
				n++;
				myfile << n << "th prime number: " << p << endl;
				cout << n << "th prime number: " << p << endl;
				break;
			}
			// if p is divisible by a previous prime number
			else if (p % primes[i] == 0) {
				break;
			}
		}
	}
	
	myfile << "The 10001st prime number: " << primes[primes.size()-1] << endl;
	myfile.close();
	
	cout << "The 10001st prime number: " << primes[primes.size()-1] << endl;
	
	return 0;
}

