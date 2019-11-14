/* 
 * 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
 * 
 * What is the sum of the digits of the number 2^1000?
 *
 */

#include <iostream>
#include <vector>
using namespace std;

int main() {
	// digits of 2^n, least significant digits at the front
	vector<int> digits = {1};
	int sum = 0;
	
	// keep doubling until we reach 2^n
	for (int i = 1; i < 1000; i++) {
		bool carry = false;
		for (int j = 0; j < digits.size(); j++) {
			int twice = digits[j] * 2;
			// keep the 1s digit
			digits[j] = twice % 10;
			if (carry) {
				digits[j] += 1;
				carry = false;
			}
			// carry the 1
			if (twice >= 10) {
				if (j + 1 == digits.size()) {
					digits.push_back(1);
					break;
				} else {
					carry = true;
				}
			}
		}
		cout << "2^" << i << " = ";
		for (int digit = digits.size() - 1; digit >= 0; digit--) {
			cout << digits[digit];
		}
		cout << endl;
	}
	
	for (int digit = 0; digit < digits.size(); digit++) {
		sum += digits[digit];
	}
	
	cout << "The sum of the digits of the number 2^1000 is " << sum << endl;
	
	return 0;
}

