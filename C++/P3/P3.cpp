/* 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 *
 */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	long number = 600851475143;
	long p = 3;
	long biggest_prime = 0;
	vector<long> primes;
	
	while (p * p < number) {
		// check if p is prime
		bool prime = true;
		for (int i = 0; i <= primes.size(); i++) {
			// if p is new prime number
			if (i == primes.size()) {
				primes.push_back(p);
				break;
			}
			// if p is divisible by a previous prime number
			if (p % primes[i] == 0) {
				prime = false;
				break;
			}
		}
		
		// if p is prime and a factor of number
		if (prime && number % p == 0) {
			biggest_prime = p;
			cout << "New biggest_prime: " << biggest_prime << endl;
		}
		p += 2;
	}
	
	cout << biggest_prime << endl;
	
	ofstream myfile;
	myfile.open ("result.txt");
	myfile << "Largest prime factor of 600851475143: " << biggest_prime << endl;
	myfile.close();
	
	return 0;
}

