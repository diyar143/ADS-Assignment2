# ADS-Assignment2 Banking System
Student: Diyar Kabyken
Group: IT-2503

Project Description
This project implements a Banking System simulation using logical and physical data structures in Python. 

Data Structures Used:
- List (Dynamic Array)**: Used to store `accounts`. In Python, lists act as dynamic arrays, allowing efficient access.
- List as Stack (LIFO)**: Used `append()` and `pop()` for `transaction_history`. 
-collections.deque (FIFO Queue)**: Used for `bill_queue` and `account_requests`. Deque is preferred for queues in Python because it provides O(1) performance for adding and removing elements from both ends.
- Predefined List: Used to satisfy Task 6 (Fixed initial storage).

How to Run:
1. Ensure Python 3.x is installed.
2. Run the script: `python main.py`
3. Follow the on-screen menu instructions.

Summary:
The project demonstrates how different logical structures (Stacks and Queues) can be implemented using Python's built-in types. The main challenge was integrating the Admin processing queue with the main account storage, which was solved using the `deque` library.

Screenshots:
<img width="384" height="219" alt="image" src="https://github.com/user-attachments/assets/09ff5d9e-4f9e-406f-901a-9371feebce0a" />
<img width="366" height="336" alt="image" src="https://github.com/user-attachments/assets/1891b96f-72d9-4e23-ba35-a2cc042b50b5" />
<img width="364" height="357" alt="image" src="https://github.com/user-attachments/assets/24a22eb0-6da5-4c95-b924-29211e79cb69" />
