import random
import time
loged_in = False

def register():
    name = input("Enter your Name. ")
    psw = input("Set a password. ")
    age = int(input("Enter your age. "))
    city = input("Enter your City. ")
    contact_number = int(input("Enter your contact number. "))
    c_n= str(contact_number)
    en_no = input("Enter your college enrollement number. ")
    
    if age < 8:
        print("Grow up kid and play this game.")
    else:
        print("User Registration successfully completed.")
        
    while len(c_n)<10 or len(c_n) > 10:
        print("Invalid contact number. Please enter a valid contact number.")
        c_n = int(input("Enter your contact number."))
    
    user_name = (random.sample(name,2) + random.sample(psw,2))
    username1 = ''.join(user_name)
    print(f"Your Generated username is '{username1}'. You can use it for login purposes.")
    
    c = input("Proceed for login. (Y/N) ").upper()
    while c != "Y" and c != "N":
        print("Invalid answer.")
        c = input("Proceed for login. (Y/N) ").upper()

    if c == "Y":
        login(username1,psw,name)
    elif c == "N":
        print("Exiting........")

    
def login(username1,psw,name):
    global loged_in

    i = 3 # creating this so that the user is left with only 3 chances for login successfully.
    while i > 0:
        username = input("Enter a valid username.")
        password = input("Enter your passwrord.")
        
        if username == username1 and password == psw:
            print(f"Login successfull. Welcome {name}.")
            loged_in = True
            break
        else:
           i -= 1
           print("'Login failed. Please check your username or password and try again.")
           loged_in = False
        
        if i == 0:
            print("Login blocked.")
    
# Function to ask 5 random questions from the user
def ask_py_questions():
    
    questions_and_options_py = (
        ("Who developed Python Programming Language?", ["Wick Van Rossum", "Rasmus Lerdorf", "Guido van rossom", "Niene stom"]),
        ("Which type of Programming does Python support?", ["Object oriented programming", "Structured programming", "Functional programming", "All of the above"]),
        ("Is Python case sensitive when dealing with identifiers?", ["no", "yes", "machine dependent", "none of these"]),
        ("Which of the following is the correct extension of the Python file?", [".python",".pl",".py",".p"]),
        ("Is Python code compiled or interpreted?", ["Python code is both compiled and interpreted."," Python code is neither compiled nor interpreted.","Python code is only compiled.","Python code is only interpreted."]),
        (" All keywords in Python are in _________", ["capitalize", "Lower case", "Upper case", "none of these"]),
        (" Which keyword is used for function in Python language?", ["function", "def", "fun", "define"]),
        ("Which of the following character is used to give single-line comments in Python?", ["//", "#", "!", "/*"]),
        ("Which of the following is used to define a block of code in Python language?", ["identation", "key", "brackets", "All of these"]),
        ("Python supports the creation of anonymous functions at runtime, using a construct called __________", ["pi", "anonymous", "lambda", "none of these"]),
        ("Which of the following functions can help us to find the version of python that we are currently working on?", ["sys.version(1)", "sys.version(0)", "sys.version()", "sys.version"]),
        ("What does pip stand for python?", ["pip install python", "pip install package", "preferred installer program", "all of these"]),
        (" Which of the following functions is a built-in function in python?", ["factorial()", "print()", "seed()", "sqrt()"]),
        ("Which of the following is not a core data type in Python programming?", ["tuples", "lists", "class", "dictionary"]),
        ("What arithmetic operators cannot be used with strings in Python?", ["*", "-", "+", "all of these"]))
    
    correct_answers_py = (
        "Guido van rossom",
        "All of the above",
        "yes",
        ".py",
        "Python code is both compiled and interpreted.",
        "none of these",
        "def",
        "#",
        "identation",
        "lambda",
        "sys.version",
        "preferred installer program",
        "print()",
        "class",
        "-" )   
     
    score = 0
    your_guess = []
    correct_guess = []

    random_choice = random.sample(range(15), 5)

    for i in random_choice:
        question, options = questions_and_options_py[i]
        
        print("----------------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = int(input("Please enter the correct option number: "))
        your_guess.append(user_answer)

        correct_option = options.index(correct_answers_py[i]) + 1
        correct_guess.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_py[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_py[i]}\n")
    print("Your score is: ", ((score*100)/5), "%")
    print(f"Your guesses are: {your_guess}")
    print(f"The correct answers are: {correct_guess}")

def ask_dbms_questions():
    questions_and_options_dbms = (
    ("What is the primary purpose of a Database Management System (DBMS)?", ["Store data", "Manage data", "Analyze data", "Retrieve data"]),
    ("Which of the following is a type of DBMS?", ["Relational DBMS", "File System", "Spreadsheet", "XML"]),
    ("Which SQL command is used to retrieve data from a database?", ["SELECT", "INSERT", "UPDATE", "DELETE"]),
    ("What does ACID stand for in database transactions?", ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Integrity, Durability", "Atomicity, Control, Integrity, Durability", "Access, Consistency, Isolation, Distribution"]),
    ("What is a primary key in a database?", ["A unique identifier for each record", "A non-unique identifier", "A foreign key", "A composite key"]),
    ("Which of the following is a NoSQL database?", ["MongoDB", "MySQL", "Oracle", "PostgreSQL"]),
    ("In normalization, what is the purpose of removing redundancy?", ["To minimize duplicate data", "To increase query performance", "To ensure data security", "To improve data storage"]),
    ("What is a foreign key?", ["A key that refers to the primary key in another table", "A key that identifies a record in the same table", "A non-unique key", "A unique key for each record"]),
    ("Which SQL clause is used to filter records?", ["WHERE", "GROUP BY", "ORDER BY", "JOIN"]),
    ("What is an index in a database?", ["A data structure to improve search speed", "A primary key", "A record identifier", "A method to enforce relationships"]),
    ("What type of relationship is defined by the term 'many-to-many'?", ["Multiple records in both tables are related", "One record in one table relates to many in another", "Each table can only have one related record", "Many records relate to one record in another table"]),
    ("What is a view in a database?", ["A virtual table based on a query", "A physical table", "A stored procedure", "A primary key"]),
    ("What does SQL stand for?", ["Structured Query Language", "Sequential Query Language", "Simple Query Language", "Standard Query Language"]),
    ("Which of the following commands is used to modify an existing record in a database?", ["UPDATE", "INSERT", "ALTER", "DELETE"]),
    ("What is the role of a database administrator (DBA)?", ["Manage and maintain the database", "Develop applications", "Create data models", "Analyze data"]))

    correct_answers_dbms = (
    "Manage data",  
    "Relational DBMS",  
    "SELECT",  
    "Atomicity, Consistency, Isolation, Durability",  
    "A unique identifier for each record",  
    "MongoDB",  
    "To minimize duplicate data",  
    "A key that refers to the primary key in another table",
    "WHERE",  
    "A data structure to improve search speed",  
    "Multiple records in both tables are related",  
    "A virtual table based on a query",  
    "Structured Query Language",  
    "UPDATE",  
    "Manage and maintain the database"  )

    score = 0
    guesses = []
    correct_guesses = []

    random_indices = random.sample(range(15), 5)

    for i in random_indices:
        question, options = questions_and_options_dbms[i]
        
        print("--------------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = input("Please enter the correct option number: ")
        guesses.append(user_answer)

        correct_option = options.index(correct_answers_dbms[i]) + 1
        correct_guesses.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_dbms[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_dbms[i]}\n")
    print("Your score is: ", ((score*100)/5), "%")
    print(f"Your guesses are: {guesses}")
    print(f"The correct answers are: {correct_guesses} ")

def ask_dsa_questions():

    questions_and_options_dsa = (
    ("Which data structure uses LIFO (Last In, First Out) principle?", ["Stack", "Queue", "Linked List", "Tree"]),
    ("Which of the following is an example of a dynamic data structure?", ["Array", "Linked List", "Hash Table", "Queue"]),
    ("What is the time complexity of binary search on a sorted array?", ["O(n)", "O(log n)", "O(n^2)", "O(1)"]),
    ("Which algorithm is used to find the shortest path in a graph?", ["Dijkstra's Algorithm", "Kruskal's Algorithm", "Merge Sort", "Quick Sort"]),
    ("What is the space complexity of a breadth-first search (BFS) algorithm?", ["O(b^d)", "O(d)", "O(1)", "O(n)"]),
    ("Which data structure is used to implement recursion?", ["Stack", "Queue", "Graph", "Tree"]),
    ("What is the worst-case time complexity of quicksort?", ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"]),
    ("Which data structure is ideal for implementing a priority queue?", ["Heap", "Stack", "Queue", "Tree"]),
    ("Which algorithm is used for sorting in O(n log n) time complexity?", ["Merge Sort", "Selection Sort", "Bubble Sort", "Insertion Sort"]),
    ("What is the best data structure for representing hierarchical relationships?", ["Tree", "Graph", "Array", "Linked List"]),
    ("Which traversal technique visits the root node first, then left subtree, and finally right subtree?", ["Preorder", "Inorder", "Postorder", "Level-order"]),
    ("Which of the following is a self-balancing binary search tree?", ["AVL Tree", "Binary Search Tree", "Heap", "Trie"]),
    ("What is the purpose of a hash function in a hash table?", ["Map keys to indexes", "Sort data", "Balance a tree", "Traverse a list"]),
    ("What is the time complexity of inserting a node in a binary search tree (BST) in the worst case?", ["O(n)", "O(log n)", "O(n^2)", "O(1)"]),
    ("Which algorithm uses divide and conquer technique?", ["Merge Sort", "Bubble Sort", "Linear Search", "DFS"]))

    correct_answers_dsa = (
    "Stack",  
    "Linked List",  
    "O(log n)",  
    "Dijkstra's Algorithm",  
    "O(b^d)", 
    "Stack", 
    "O(n^2)",  
    "Heap",  
    "Merge Sort",  
    "Tree",  
    "Preorder",  
    "AVL Tree",  
    "Map keys to indexes", 
    "O(n)",  
    "Merge Sort" )

    score = 0
    your_guesses = []
    correct_guesses = []

    random_indices = random.sample(range(15), 5)

    for i in random_indices:
        question, options = questions_and_options_dsa[i]
        
        print("---------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = input("Please enter the correct option number: ")
        your_guesses.append(user_answer)

        correct_option = options.index(correct_answers_dsa[i]) + 1
        correct_guesses.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_dsa[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_dsa[i]}\n")
    print("Your score is: ", ((score*100)/5), "%")
    print(f"Your guesses are {your_guesses}")
    print(f"The correct answers are: {correct_guesses}")

print("Hey! Welcome to the ""QUIZ GAME"". For Playing this game, first you need to register and login,,, then play game.")
a = input('''If you want to [' REGISTER '] then type "YES" and If no then type "NO")   ''').upper()
time.sleep(1)

# asking if the ans is yes proceed and repeat till the user gives a correct ans. 
while True:
    if a == "YES":
        register()
        break
    elif a == "NO":
        print("Exiting........")
        break
    else:
        print("Wrong input. Try again.")

time.sleep(2)
#this is a loop to continuosly ask the user to play more or quit the game.
while loged_in == True:
    print("Select the domain in which you need to play the quiz")
    input_user = input('''1. Python.
2.Database Management System.
3.Data structure and Algorithms.
Press the number(1,2 etc.)
''')

    if input_user == "1":
        ask_py_questions()
    elif input_user == "2":
        ask_dbms_questions()
    elif input_user == "3":
        ask_dsa_questions()
    else:
        print("Thanks for playing with us. Exiting........")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing!")
        break
