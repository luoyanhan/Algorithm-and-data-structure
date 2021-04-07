from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem1 = Semaphore(1)
        self.sem2 = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.sem1.acquire()
            printFoo()
            self.sem2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.sem2.acquire()
            printBar()
            self.sem1.release()