#include <iostream>
#include <string>



class user_c { 
private:
	std::string firstname;
	std::string lastname;
	int ID;
public:
	void setfirstname(std::string firstname);
	void setlastname(std::string lastname);
	void searchcourse();
	void printschedule();
	void setID(int ID);
	void printAll(){
		std::cout << "First Name: " << firstname << " Last name: " << lastname << " ID: " << ID << endl;
	}
};


class student_c : user_c{
private:

public:
	void addcourse();
	void dropcourse();
};

class instructor_c : user_c{
private:

public:
	void printRoster();
	}
};

class admin_c : user_c{
private:

public:
	void createcourse();
	void removecourse();
	void adduser();
	void removeuser();
	void forceStudentinRoster();
	void forceStudentOutRoster();
	void printRoster();
	}
};

int main() {

	int number = 0;
	int studentNum = 0;
	int instructorNum = 0;
	int adminNum = 0;
	
	do {
		// Menu to ask if the person wants to continue or which function to do.
		std::cout << "1: Student\n 2: Instructor\n 3: Admin\n 0: Exit\n";
		std::cin >> number;

		switch (number) {
		case 1: {//student
			do
			{
				std::cout << "You have selected Student, select an action: " << std::endl;
				std::cout << "1: Search Courses\n" << "2: Print Schedule\n" << "3: Add Course\n" << "4: Drop Course\n";
				std::cin >> studentNum;
				if (studentNum == 1){
					//Search courses
				}
				else if (studentNum == 2){
					//Print schedule
				}
				else if (studentNum == 3){
					//Add course
				}
				else  if (studentNum == 4){
					//Drop course
				}
				else if (studentNum > 4){
					std::cout << "Incorrect Value, try again" << std::endl;
				}
			}while (studentNum != 0);			
			break;
		}
		case 2: {
			do
			{
				std::cout << "You have selected Instructor, select an action: " << std::endl;
				std::cout << "1: Search Courses\n" << "2: Print Schedule\n" << "3: Print Roster\n";
				std::cin >> instructorNum;
				if (instructorNum == 1){
					//Search courses
				}
				else if (instructorNum == 2){
					//Print schedule
				}
				else if (instructorNum == 3){
					//Print roster
				}
				else if (studentNum > 4){
					std::cout << "Incorrect Value, try again" << std::endl;
				}
			}while (instructorNum != 0);
		}
		case 3: {
			do
			{
				std::cout << "You have selected Admin, select an action: " << std::endl;
				std::cout << "1: Search Courses\n" << "2: Print Schedule\n" << "3: Create Course\n" << "4: Remove Course\n" << "5: Force Student into Roster\n" << "6: Force Student out of Roster\n"; 
				std::cin >> adminNum;

				if (adminNum == 1){
					//Search courses
				}
				else if (adminNum == 2){
					//Print schedule
				}
				else if (adminNum == 3){
					//Create course
				}
				else if (adminNum == 4){
					//Remove course
				}
				else if (adminNum == 5){
					//Force into Roster
				}
				else if (adminNum == 6){
					//Force out of Roster		
				}
				else if (studentNum > 6){
					std::cout << "Incorrect Value, try again" << std::endl;
				}
			}while (adminNum != 0);
			break;
		}
		default:{
			std::cout << "Incorrect Value, try again" << std::endl;
		}
		break;
		}

	} while (number != 0);

	return 0;
}
