# interview
To run the code , simply use , I do not install any external library. I am using python 3.9
python3 question_1.py
python3 question_2.py

# question 1 output 
wheels=4
doors=4
seats=7
maxSpeed=120
120
120
120
120
120
120
120
120
120
120

wheels=4
doors=4
seats=2
maxSpeed=200
200
200
200
200
200
200
200
200
200
200

# question 2 output 
120
200
120
200
120
200
120
200
120
200
120
200
120
200
120
200
120
200
120
200

# question 3 
1. Why is the output in 2 and 1 different ?
-We spawn only one process and the code run in sequential in question 1. In question 2, we call the methods in seperate threads and they run simultaneously.
2. How can we make sure that the question 2 will produce the order just like question 1?
-We can use join() method that is provided method by threading library of python. This will wait for the thread to finish before it starts a new thread.

# question 4 
-We have to set the timing right like what i did in model class.