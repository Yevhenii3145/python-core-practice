from collections import deque


def main():
    queue = deque(maxlen=10)
    queue_other = deque(maxlen=10)
    for i in range(20):
        queue.append(i)
        queue_other.appendleft(i)
    print(queue)
    print(queue_other)
    queue_start = queue.popleft()
    queue_end = queue.pop()
    print(f"queue_start {queue_start} queue_end {queue_end}")
    queue_other_start = queue_other.popleft()
    queue_other_end = queue_other.pop()
    print(f"queue_other_start {queue_other_start} queue_other_end {queue_other_end}")

def main_2():
    user_inputs = deque(maxlen=10)
    while True:
        user_input = input(">>> ")
        user_inputs.append(user_input)
        if user_input == "q":
            break
    print("Good buy!")
    print(f"User steps: {user_inputs}")


if __name__=="__main__":
    main()
    main_2()
