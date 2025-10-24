class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, Cannot deque!")
            return None
        else:
            removed = self.queue.pop()
            print(f"{removed} dequeued")
            return removed

    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            print(f"Front element is: {self.queue[0]}")
            return self.queue[0]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents: " , self.queue)

if __name__ == '__main__':

    q = Queue()

    while True:
        print()
        print("\n--- Queue Operations Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Is empty")
        print("6. exit")

        choice = input("Enter your choice: ")

        if choice == 1:
            item = input(" Enter the value to enqueue: ")
            q.enqueue()
        
        elif choice == 2:
            q.dequeue

        elif choice == 3:
            q.peek()
