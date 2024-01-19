from garden import Garden
from person import Person

def main():
    shared_garden = Garden()

    alice = Person("Alice", shared_garden)
    bob = Person("Bob", shared_garden)

    alice.start()
    bob.start()

    alice.join()
    bob.join()

if __name__ == "__main__":
    main()
