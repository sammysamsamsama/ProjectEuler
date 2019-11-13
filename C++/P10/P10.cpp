/* 
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * 
 * Find the sum of all the primes below two million.
 *
 */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	
	int p; // number we're checking for prime
	vector<int> primes; // to store found primes
	primes.push_back(2);
	unsigned long sum = 2;
	
	// check for primes starting with starting with 3 until 2,000,000
	for (p = 3; p < 2000000; p+=2) {
		// for each of the previous primes under sqrt(p)
		for (int i = 0; i <= primes.size(); i++) {
			// if we found a new prime
			if (i == primes.size()) {
				primes.push_back(p);
				cout << sum << " + " << p << " = " << sum + p << endl;
				sum += p;
				break;
			}
			// if p is divisible by a previous prime number
			else if (p % primes[i] == 0) {
				break;
			}
		}
	}
	
	cout << "Sum of primes below 2M: " << sum << endl;
	
	return 0;
}

