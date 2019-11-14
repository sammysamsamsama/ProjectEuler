/* 
 * Starting in the top left corner of a 2×2 grid, and only being able to 
 * move to the right and down, there are exactly 6 routes to the bottom 
 * right corner.
 * 
 * How many such routes are there through a 20×20 grid?
 *
 */

#include <iostream>
using namespace std;

int main() {
	
	/* The solution is 40!/(20!^2)
	 * 
	 * Each path can be considered as a series of 0s and 1s.
	 * Each digit is either a left or right turn.
	 * There are n! ways to arrange n numbers.
	 * In order to know the number of recognizably different ways to arrange 
	 * those numbers, you must divide n! by m! for each quantity m of
	 *	different numbers.
	 * 
	 * For example, if there were 39 1s and 1 0, there would be only 40
	 * ways to arrange them because the only significant difference is the 0
	 * and there would be only 40 places to put it.
	 * 
	 * For the set [0, 0, 0, 1, 1], the answer is 5!/(3!*2!) = 10
	 * 1		2		3		4		5		6		7		8		9		10
	 * 00011 00101 00110 01001 01010 01100 10001 10010 10100 11000
	 * 
	 * In this case, there are 20 1s and 20 0s, so 20! * 20! or 20!^2
	 */
	 
	unsigned long answer = 1;
	
	/* Because of C++ big number limitations, I've shortened the calculation.
	 * 40! contains 20!, so we can remove 1*2*3*...*18*19*20 to divide out
	 * the first 20!. The second 20! will be divided out as we go.
	 */
	for (int i = 21; i <= 40; i++) {
		if (answer * i < answer) {
			cout << "OVERFLOW" << endl;
		}
		answer *= i; // calculate 40!/20!
		answer /= i-20; // divide out another 20!
	}

	cout << "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.\n" << endl;

	cout << "There are " << answer;
	cout << " such routes through a 20×20 grid." << endl;
	
	return 0;
}

