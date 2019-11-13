/* 
 * A palindromic number reads the same both ways. The largest palindrome 
 * made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * 
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 */

#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ofstream myfile;
	myfile.open ("result.txt");

	int largest_palindrome = 0;

	for (int i = 100; i < 1000; i++) {
		for (int j = i; j < 1000; j++) {
			int product = i * j;
			string str_product = to_string(product);
			reverse(str_product.begin(), str_product.end());
			if (stoi(str_product) == product && product > largest_palindrome) {
				largest_palindrome = product;
				cout << i << " * " << j << " = " << largest_palindrome << endl;
				myfile << i << " * " << j << " = " << largest_palindrome << endl;
			}
		}
	}
	
	
	cout << "Largest palindrome from two 3-digit numbers: " << largest_palindrome << endl;
	
	myfile << "Largest palindrome from two 3-digit numbers: " << largest_palindrome << endl;
	myfile.close();
	
	return 0;
}

