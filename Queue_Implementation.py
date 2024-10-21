# You will be using a list of fixed length (no more than 10 to create the queue data structure)
# The queue has two functions; pop() and push(), but also we will add other functions later.
# make sure you have the list and a variable called tail_ pointer and head_pointer   as global and initialised
# Create a linear queue first, then change it to circular.
# Make sure you know the conditions that makes the queue empty or full
# ======================================================================================================================

# -----------------------Declaring global variables and lists -----------------
queue = [""]*5
tail = 0
head = 0

# --------------                        validation               -----------------------
def IsEmpty():
    global tail, head, queue
    if head == tail:
        return True
    else:
        return False



def IsFull():
    global tail, head, queue
    if head == 0 and tail == len(queue) - 1:
        return True
    else:
        if head == tail + 1:
            return True
        else:
            return False


# ----------------------------------------POP() function ---------------------------------------------------------------
def pop():
    global head, queue
    if IsEmpty():
        print("Queue is empty")
        print(queue)
        print()
    else:
        e = queue[head]
        queue[head] = ""
        head += 1
        if head == 5:
            head = 0
        print(queue)
        print()
        return e


# ----------------------------------------PUSH() function  -------------------------------------------------------------

def push(element):
    global tail, queue
    if IsFull():
        print("Queue is full")
    else:
        queue[tail] = element
        tail += 1
        if tail == 5:
            tail = 0
    print(queue)
    print()

# ---------------------------------------MAIN PROGRAM ------------------------------------------------------------------

# you will need to write code so that you do not terminate the program after one element.

# Set a Boolean variable to true,  say continue ==True

# Repeat the following until user says no to continue

# Ask user if they want to push, or pop and to enter a value

# if they push, they must provide you with the value they want to push to the queue

# if they push, ask the user to enter a value, store this value in a variable called value for example.

# call either push(value) or pop() according to user needs.

# ask user if he/she wants to continue


# -------------------------------------TESTING IDEAS -------------------------------------------------------------------
# test the above first by pushing different value, until the queue get full, and try to push  a value after the queue is
# full; you should get an error message.
# test the above by pop() all the element  so that you will; get an empty queue.  Try to pop from empty queue, you
# should get a message preventing you from doing so.

# ------------------------------ --------Extension..... Extension.....Extension..... -----------------------------------


# change the linear queue to circular: hint you need to check the conditions that makes the queue full or empty first.

# add another function to check if the queue is full, empty, or in use  - call the function def status().
# This function will return either FULL, EMPTY, or INUSE.

# call the function to display the status of the queue.


