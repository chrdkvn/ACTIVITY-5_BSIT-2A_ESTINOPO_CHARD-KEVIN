from array_structures import ArrayStack, ArrayQueue
from linked_structures import LinkedStack, LinkedQueue

def is_balanced(expression):
    """6a: Use a stack to check whether a string of parentheses is balanced."""
    stack = LinkedStack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

def simulate_print_queue():
    """6b: Simulate a print queue."""
    q = LinkedQueue()
    print("\n--- Print Queue Simulation ---")
    q.enqueue({"id": "Job1", "pages": 5})
    q.enqueue({"id": "Job2", "pages": 12})
    q.enqueue({"id": "Job3", "pages": 1})
    
    order = 1
    while not q.is_empty():
        job = q.dequeue()
        print(f"Wait Order {order}: Printed {job['id']} ({job['pages']} pages)")
        order += 1

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Test ArrayStack")
        print("2. Test LinkedQueue")
        print("3. Check Balanced Parentheses")
        print("4. Simulate Print Queue")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            stack = ArrayStack(3)
            try:
                stack.push(10)
                stack.push(20)
                stack.push(30)
                print(f"Peek top: {stack.peek()}")
                stack.push(40) # Triggers overflow
            except Exception as e:
                print(f"Error caught: {e}")
                
        elif choice == '2':
            q = LinkedQueue()
            try:
                q.enqueue("A")
                print(f"Dequeued: {q.dequeue()}")
                q.dequeue() # Triggers underflow
            except Exception as e:
                print(f"Error caught: {e}")
                
        elif choice == '3':
            expr = input("Enter parentheses string to check: ")
            print(f"Is balanced? {is_balanced(expr)}")
            
        elif choice == '4':
            simulate_print_queue()
            
        elif choice == '5':
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()