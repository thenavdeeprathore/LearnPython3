class Human:

    def __init__(self):
        self.name = "Vicky"
        self.head = self.Head()

    def display(self):
        print('Name: ', self.name)
        self.head.talk()
        self.head.brain.think()

    class Head:

        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            print('Head Talking...')

        class Brain:

            def think(self):
                print('Brain Thinking.. ')


h = Human()
h.display()
# Name:  Vicky
# Head Talking...
# Brain Thinking..
