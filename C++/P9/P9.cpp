/* 
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
 * which,
 * 
 * a^2 + b^2 = c^2
 * 
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 * 
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 *
 */

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int product = -1;
	
	for (int a = 1; a < 1000 && product == -1; a++) {
		for (int b = a; b < 1000 && product == -1; b++) {
			for (int c = b; c < 1000 && product == -1; c++) {
				if (a * a + b * b == c * c) {
					cout << a << ", " << b << ", " << c << endl;
					cout << "\t" << a << "^2 + " << b << "^2 = " << c << "^2" << endl;
					if (a + b + c == 1000) {
						cout << "FOUND: " << a << " + " << b << " + " << c << " = 1000" << endl;
						product = a * b * c;
					}
				}
			}
		}
	}
	
	cout << "abc: " << product << endl;
	
	return 0;
}

