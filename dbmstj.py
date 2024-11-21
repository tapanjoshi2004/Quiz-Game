import random
import time
import mysql.connector
loged_in = False

def register():
    name = input("Enter your name. ")
    psw = input("Set a password. ")
    email = input("Enter your Email address. ")
    clg = input("Enter your College.")
    age = int(input("Enter your age. "))
    if age < 8:
        print("Grow up kid and play this game.")
    else:
        pass
    city = input("Enter your City. ")
    contact_num = int(input("Enter your contact number. "))
    c_n = str(contact_num)
    while True:
        if len(c_n)<10 or len(c_n) > 10:
            print("Invalid contact number. Please provide us with a proper number.")
            contact_num = int(input("Enter your contact number."))
        else:
            break

    wp_num = int(input("Enter your whatsapp number. (if same then press '1' )"))
    if wp_num != 1:
        wp_num = contact_num
    en_no = input("Enter your college enrollement number. ")
    with open ("enrollment.txt", "a") as enr:
        enr.write(en_no + "\n")

    username1 = input("Please create your username.")
    with open ("username.txt", "r") as u:
        user = u.read().splitlines()

    while True:
        if username1 in user:
            print("The username is already taken. Please choose another username.")
            username1 = input("Please create another username: ")
        else:
            break

    with open("username.txt", "a") as u:
        u.write(username1 + "\n")        
    print("Username created successfully! You can use this usernname for future purposes.")

    with open("username and password.txt", "a") as up:
        up.write(username1 +" " + psw + " " + "\n")
    
    with open ("email and password.txt", "a") as e:
        e.write(email + " " + psw + " " + "\n")
    
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

def login_without_register():
        global loged_in

        i = 3  # creating this so that the user is left with only 3 chances for login successfully.
        while i > 0:
            username = input("Enter a valid username: ")
            password = input("Enter your password: ")

            with open("username and password.txt", "r") as u:
                user = u.read().splitlines()
            
            seperate = [line.split() for line in user]
            
            if [username, password] in seperate:
                print("Login successful. Welcome.")
                loged_in = True
                break
            else:
                i -= 1
                print("Login failed. Please check your username or password and try again.")
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
    your_guesses = []
    correct_guesses = []

    random_indices = random.sample(range(15), 5)

    for i in random_indices:
        question, options = questions_and_options_py[i]
        
        print("---------------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = input("Please enter the correct option number: ")
        your_guesses.append(user_answer)

        correct_option = options.index(correct_answers_py[i]) + 1
        correct_guesses.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_py[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_py[i]}\n")
    print("Your score is: ", ((score*100)/5), "%") 
    print(f"Your guesses are: {your_guesses}")
    print(f"The correct answers are: {correct_guesses}")

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

def ask_ai_questions():
    questions_and_options_ai = (
    ("What is the primary goal of Artificial Intelligence?", ["To simulate human intelligence", "To solve mathematical problems", "To replace all human jobs", "To perform repetitive tasks"]),
    ("Which of the following is an application of AI?", ["Self-driving cars", "File Compression", "Packet Switching", "Firewall Security"]),
    ("Which algorithm is commonly used in supervised learning?", ["Decision Trees", "K-means Clustering", "Genetic Algorithms", "Q-Learning"]),
    ("What does 'NLP' stand for in the field of AI?", ["Natural Language Processing", "Network Level Programming", "Node Level Processing", "Neural Language Protocol"]),
    ("Which AI technique is used to enable machines to learn from past experiences?", ["Machine Learning", "Quantum Computing", "Virtual Reality", "Cloud Computing"]),
    ("Which type of learning is associated with labeled data?", ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning"]),
    ("What is a neural network in AI?", ["A model inspired by the human brain", "A sorting algorithm", "A type of database", "A method to generate random numbers"]),
    ("Which technique is used in AI for making decisions by exploring a sequence of actions?", ["Reinforcement Learning", "Supervised Learning", "Unsupervised Learning", "Transfer Learning"]),
    ("Which algorithm is used to find the best possible action in a game-playing AI?", ["Minimax Algorithm", "Backpropagation", "Gradient Descent", "Random Forest"]),
    ("What is the main advantage of deep learning over traditional machine learning models?", ["Automatic feature extraction", "Requires more data", "Slower processing", "Uses less data"]),
    ("Which type of neural network is primarily used for image recognition?", ["Convolutional Neural Network (CNN)", "Recurrent Neural Network (RNN)", "Radial Basis Function Network", "Feedforward Neural Network"]),
    ("What is overfitting in machine learning?", ["Model performs well on training data but poorly on unseen data", "Model underestimates the complexity of data", "Model is too simple to learn the data", "Model performs equally on both training and unseen data"]),
    ("Which search algorithm is used in AI to find the shortest path in a graph?", ["A* Algorithm", "Breadth-First Search", "Depth-First Search", "Linear Search"]),
    ("What is the role of an agent in AI?", ["Perceive its environment and take actions", "Generate random actions", "Store data in databases", "Execute algorithms sequentially"]),
    ("What does 'Turing Test' measure?", ["A machine's ability to exhibit intelligent behavior", "A machine's speed in solving problems", "A machine's ability to perform calculations", "A machine's efficiency in learning"]))

    correct_answers_ai = (
    "To simulate human intelligence",  
    "Self-driving cars",  
    "Decision Trees",  
    "Natural Language Processing",  
    "Machine Learning",  
    "Supervised Learning",  
    "A model inspired by the human brain",  
    "Reinforcement Learning",  
    "Minimax Algorithm",  
    "Automatic feature extraction",  
    "Convolutional Neural Network (CNN)",  
    "Model performs well on training data but poorly on unseen data",  
    "A* Algorithm", 
    "Perceive its environment and take actions", 
    "A machine's ability to exhibit intelligent behavior" )

    score = 0
    your_guesses = []
    correct_guesses = []

    random_indices = random.sample(range(15), 5)

    for i in random_indices:
        question, options = questions_and_options_ai[i]
        
        print("---------------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = input("Please enter the correct option number: ")
        your_guesses.append(user_answer)

        correct_option = options.index(correct_answers_ai[i]) + 1
        correct_guesses.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_ai[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_ai[i]}\n")
    print("Your score is: ", ((score*100)/5), "%") 
    print(f"Your guesses are: {your_guesses}")
    print(f"The correct answers are: {correct_guesses}")

def ask_ml_questions():
    questions_and_options_ml = (
    ("Which of the following is a type of supervised learning algorithm?", ["Linear Regression", "K-means Clustering", "Apriori", "DBSCAN"]),
    ("What is the purpose of a cost function in machine learning?", ["To measure the error between predicted and actual values", "To optimize the performance of the algorithm", "To reduce data size", "To store the data in memory"]),
    ("Which machine learning model is used for classification tasks?", ["Support Vector Machine (SVM)", "K-means", "Linear Regression", "PCA"]),
    ("What is 'overfitting' in machine learning?", ["Model performs well on training data but poorly on unseen data", "Model fits the test data perfectly", "Model has too few features", "Model learns from too little data"]),
    ("Which of the following is an example of unsupervised learning?", ["K-means Clustering", "Decision Tree", "Logistic Regression", "Random Forest"]),
    ("Which machine learning technique is best suited for detecting outliers in a dataset?", ["Isolation Forest", "Logistic Regression", "Naive Bayes", "Linear Regression"]),
    ("What is the purpose of cross-validation in machine learning?", ["To evaluate the performance of a model on unseen data", "To reduce the size of the dataset", "To increase the speed of training", "To normalize the data"]),
    ("Which algorithm is commonly used for dimensionality reduction?", ["Principal Component Analysis (PCA)", "K-nearest Neighbors (KNN)", "Random Forest", "SVM"]),
    ("What is the main difference between supervised and unsupervised learning?", ["Supervised learning uses labeled data, unsupervised learning uses unlabeled data", "Supervised learning uses a cost function, unsupervised learning does not", "Supervised learning is faster", "Unsupervised learning is used for classification"]),
    ("Which of the following is used to avoid overfitting in models?", ["Regularization", "Maximization", "Normalization", "Backpropagation"]),
    ("What is the role of a learning rate in gradient descent?", ["It controls how much to adjust the model in response to an error", "It decides the number of iterations", "It selects the features for the model", "It splits the data into training and testing sets"]),
    ("Which algorithm is used for classification and regression tasks?", ["Random Forest", "K-means", "PCA", "Apriori"]),
    ("What is a confusion matrix in machine learning?", ["A table that shows the performance of a classification model", "A type of optimization technique", "A matrix that stores data", "A way to visualize a decision tree"]),
    ("What is the goal of unsupervised learning?", ["To find hidden patterns or structures in data", "To predict the output for new data", "To minimize the cost function", "To classify data into categories"]),
    ("What is 'bias' in machine learning?", ["The error due to overly simplistic models", "The error due to too complex models", "The error caused by noise in the data", "The tendency to select a specific model"]))

    correct_answers_ml = (
    "Linear Regression",  
    "To measure the error between predicted and actual values",  
    "Support Vector Machine (SVM)", 
    "Model performs well on training data but poorly on unseen data",  
    "K-means Clustering", 
    "Isolation Forest", 
    "To evaluate the performance of a model on unseen data",  
    "Principal Component Analysis (PCA)",  
    "Supervised learning uses labeled data, unsupervised learning uses unlabeled data",  
    "Regularization",  
    "It controls how much to adjust the model in response to an error", 
    "Random Forest", 
    "A table that shows the performance of a classification model",  
    "To find hidden patterns or structures in data",  
    "The error due to overly simplistic models" )

    score = 0

    your_guesses = []
    correct_guesses = []

    random_indices = random.sample(range(15), 5)

    for i in random_indices:
        question, options = questions_and_options_ml[i]
        
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = input("Please enter the correct option number: ")
        your_guesses.append(user_answer)

        correct_option = options.index(correct_answers_ml[i]) + 1
        correct_guesses.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers_ml[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers_ml[i]}\n")
    print("Your score is: ", ((score*100)/5), "%")
    print(f"Your guesses are: {your_guesses}")
    print(f"The correct answers are: {correct_guesses}")

def ask_se_questions():

    questions_and_options = (
        ("Which programming language do you prefer for backend development?", ["Python", "Java", "C#", "Node.js"]),
        ("What is your favorite software development methodology?", ["Agile", "Waterfall", "Scrum", "Kanban"]),
        ("Which version control system do you use?", ["Git", "SVN", "Mercurial", "Perforce"]),
        ("What type of testing is most important to you?", ["Unit testing", "Integration testing", "System testing", "Acceptance testing"]),
        ("Which cloud platform do you prefer?", ["AWS", "Azure", "Google Cloud", "IBM Cloud"]),
        ("What is your preferred database management system?", ["MySQL", "PostgreSQL", "MongoDB", "SQLite"]),
        ("Which development environment do you use the most?", ["VS Code", "IntelliJ IDEA", "PyCharm", "Eclipse"]),
        ("Which software design pattern do you find most useful?", ["Singleton", "Factory", "Observer", "Strategy"]),
        ("Which agile role do you prefer?", ["Scrum Master", "Product Owner", "Developer", "Tester"]),
        ("Which tool do you use for continuous integration?", ["Jenkins", "CircleCI", "TravisCI", "GitLab CI"]),
        ("Which architecture pattern do you prefer for building systems?", ["Monolithic", "Microservices", "Serverless", "Event-driven"]),
        ("What is your preferred method for handling errors in code?", ["Try-catch", "Error codes", "Logging", "Ignoring errors"]),
        ("Which operating system do you prefer for development?", ["Linux", "Windows", "macOS", "Unix"]),
        ("Which tool do you use for project management?", ["Jira", "Trello", "Asana", "Monday.com"]),
        ("Which front-end framework do you like the most?", ["React", "Angular", "Vue.js", "Svelte"]))

    correct_answers = (
        "Python",
        "Agile",
        "Git",
        "Unit testing",
        "AWS",
        "PostgreSQL",
        "VS Code",
        "Factory",
        "Developer",
        "Jenkins",
        "Microservices",
        "Try-catch",
        "Linux",
        "Jira",
        "React")
    
    score = 0
    your_guess = []
    correct_guess = []

    random_choice = random.sample(range(15), 5)

    for i in random_choice:
        question, options = questions_and_options[i]
        
        print("----------------------------------------")
        print(f"Q) {question}")
        print()
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        
        user_answer = int(input("Please enter the correct option number: "))
        your_guess.append(user_answer)

        correct_option = options.index(correct_answers[i]) + 1
        correct_guess.append(correct_option)

        if options[int(user_answer) - 1] == correct_answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answers[i]}\n")
    print("Your score is: ", ((score*100)/5), "%")
    print(f"Your guesses are: {your_guess}")
    print(f"The correct answers are: {correct_guess}")


print("Hey! Welcome to the quizz game. In order to play this game you first need to register then login.")
a = input('''For Login page press(L). If not registered then press (R) to register.
To EXIT press E. ''').upper()
time.sleep(1)

# asking if the ans is yes proceed and repeat till the user gives a correct ans. 
while True:
    if a == "R":
        register()
        break
    elif a == "E":
        print("Exiting........")
        break
    elif a == "L":
        login_without_register()
        break
    else:
        print("Wrong input :) . Try again.")
        a = input('''For Login page press(L). If not registered then press (R) to register.
To EXIT press E. ''').upper()

time.sleep(2)
#this is a loop to continuosly ask the user to play more or quit the game.
while loged_in == True:
    print("Select the domain in which you need to play the quiz")
    input_user = input('''1.Python.
2.Database Management System (DBMS).
3.Data structure and Algorithms (DSA).
4.Artificial intelligence (AI).
5.Machine Learning (ML).
6.Software Engineering (SE).
Press the number(1,2 etc.)
''')

    if input_user == "1":
        ask_py_questions()
    elif input_user == "2":
        ask_dbms_questions()
    elif input_user == "3":
        ask_dsa_questions()
    elif input_user == "4":
        ask_ai_questions()
    elif input_user == "5":
        ask_ml_questions()
    elif input_user == "6":
        ask_se_questions()
    else:
        print("Thanks for playing with us. Exiting........")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing!")
        break