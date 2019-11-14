/* 
 * The following iterative sequence is defined for the set of positive 
 * integers:
 * 
 * n → n/2 (n is even)
 * n → 3n + 1 (n is odd)
 * 
 * Using the rule above and starting with 13, we generate the following 
 * sequence:
 * 
 * 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 * 
 * It can be seen that this sequence (starting at 13 and finishing at 1) 
 * contains 10 terms. Although it has not been proved yet (Collatz 
 * Problem), it is thought that all starting numbers finish at 1.
 * 
 * Which starting number, under one million, produces the longest chain?
 * 
 * NOTE: Once the chain starts the terms are allowed to go above one 
 * million.
 *
 */

#include <iostream>
using namespace std;

int main() {
	int num_with_longest_chain = 1;
	int longest_chain_length = 1;
	
	for (int i = 1; i < 1000000; i++) {
		int chain_length = 1;
		long n = i;
		
		while (n != 1) {
			/* if n is even proceed 1 step
			 * if n is odd proceed 2 steps
			 * this is because 3 * n + 1 will always be even so there must be
			 * a next step. The sequence often ends like this:
			 * 
			 * 16 → 8 → 4 → 2 → 1
			 */
			if (n % 2 == 0) {
				n /= 2;
				chain_length++;
			} else {
				n = (3 * n + 1) / 2;
				chain_length += 2;
			}
		}
		
		if (chain_length > longest_chain_length) {
			longest_chain_length = chain_length;
			num_with_longest_chain = i;
			cout << "New longest chain: " << i << ", " << chain_length << " terms" << endl;
		}
		
	}
	
	cout << "Number under 1M with longest chain: " << num_with_longest_chain;
	cout << "\nChain length: " << longest_chain_length << " terms" << endl;
	
	return 0;
}

