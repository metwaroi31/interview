# interview
To run the code , simply use , I do not install any external library. I am using python 3.9 <br />
python3 question_1.py <br />
python3 question_2.py <br />

# question 1 output 
wheels=4    <br />
doors=4     <br />
seats=7     <br />
maxSpeed=120<br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />
120         <br />

wheels=4    <br />
doors=4     <br />
seats=2     <br />
maxSpeed=200<br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />
200         <br />

# question 2 output 
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />
120         <br />
200         <br />

# question 3 
1. Why is the output in 2 and 1 different ?
-We spawn only one process and the code run in sequential in question 1. In question 2, we call the methods in seperate threads and they run simultaneously.
2. How can we make sure that the question 2 will produce the order just like question 1?
-We can use join() method that is provided method by threading library of python. This will wait for the thread to finish before it starts a new thread.

# question 4 
-We have to set the timing right like what i did in model class.