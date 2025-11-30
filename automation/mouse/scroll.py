import time
import random

class Scroll:
    def __init__(self, page):
        self.page = page

    def down(self, amount=None):
        if amount is None:
            amount = random.randint(300, 900)
        self.page.mouse.wheel(0, amount)
        time.sleep(random.uniform(0.5, 1.2))
