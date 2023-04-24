from multiprocessing import Process
from Counter import Counter

def test_mp(counter):
    num_processes = 10
    processes = [Process(target=create_children, args=(counter,)) for i in range(num_processes)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
        p.terminate()


def create_children(counter):
    num_children_per_process = 30
    processes = [Process(target=send_request, args=(counter,)) for i in range(num_children_per_process)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
        p.terminate()

def send_request(counter):
    counter.increment()


def main():
    counter = Counter()
    test_mp(counter)

    print("Number of requests sent: " + str(counter.value()))

if __name__ == '__main__':
    main()
