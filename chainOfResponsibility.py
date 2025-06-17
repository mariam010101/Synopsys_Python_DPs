class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            self.next_handler.handle(request)


class Level1Support(Handler):
    def handle(self, request):
        if request == "easy":
            print("Level 1 Support: I handled it.")
        else:
            super().handle(request)


class Level2Support(Handler):
    def handle(self, request):
        if request == "medium":
            print("Level 2 Support: I handled it.")
        else:
            super().handle(request)


class Level3Support(Handler):
    def handle(self, request):
        if request == "hard":
            print("Level 3 Support: I handled it.")
        else:
            print("Level 3 Support: Sorry, we can't handle this.")


level3 = Level3Support()
level2 = Level2Support(level3)
level1 = Level1Support(level2)

level1.handle("easy")    # Level 1 handles it
level1.handle("medium")  # Passed to Level 2
level1.handle("hard")    # Passed to Level 3
level1.handle("unknown") # Rejected at the end
