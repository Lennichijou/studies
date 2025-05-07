#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <windows.h>
#include <filesystem>

using namespace std;

int main(int argc, char* argv[]) {
	char code[2048];
	string filename;
	
	if (argc == 1) {
		cout << "Error: no name entered.";
	}
	else if (!(filesystem::exists(argv[1]))) {
		cout << "Error: file does not exist" << endl;
	}
	else {
		filename = argv[1];
		ifstream myfile(filename); int i = 0, length = 0;
		while (!myfile.eof())
		{
			myfile.get(code[i]);
			i++;
			length++;
		}
		myfile.close();
		length -= 1;
		char memory[10]{};
		int ip = 0;
		char temp;
		//char code[] = "@++++++++++++++++++>@+++++++++++++>@+++++++++++>@+++++++++++++++>@++++++++++++++++++++>^----------------------------%<<<<++++++>@+++>@+++++>@+++++++++++>@+++++++++++++++++++++>^----------------------------%<<<<<<@+++++++++++++++>@+++++++++++>@+++++++++++++++++++>@+++++++++++++++++>@+++++++++++++++>^---------------------------%";
		for (int i = 0; i < length; i++) {
			switch (code[i]) {
			case '+':
				memory[ip]++;
				break;
			case '>':
				if (ip < 9) {
					ip++;
					break;
				}
				else {
					cout << endl << "Error: memory overload." << endl;
					break;
				}
			case '<':
				if (ip > 0) {
					ip--;
					break;
				}
				else {
					cout << endl << "Error: memory is out of range." << endl;
					break;
				}
			case '@':
				memory[ip] = 125;
				break;
			case '^':
				memory[ip] = 60;
				break;
			case '-':
				memory[ip]--;
				break;
			case '%':
				for (int j = 0; j < ip + 1; j++) {
					cout << memory[j];
				}
				break;
			case '=':
				if (ip + 1 > 9) {
					cout << endl << "Error: memory overload." << endl;
					break;
				}
				else {
					temp = memory[ip];
					ip++;
					memory[ip] = temp;
					break;
				}
			default:
				cout << endl << "Error: unknown symbol " << code[i] << "." << endl;
				break;
				break;
			}
		}
		//}
		//else {
		//	cout << "Error: no name entered correctly." << endl;
		//}
	}
}