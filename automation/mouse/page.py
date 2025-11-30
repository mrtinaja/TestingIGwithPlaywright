from automation.mouse.move import Move
from automation.mouse.scroll import Scroll
from automation.mouse.click import Click
import random
import time

class Page:
    def __init__(self, page):
        """
        Wrapper sobre Playwright page que sincroniza movimiento real y cursor visual.
        """
        self.page = page
        self.move = Move(page)
        self.scroll = Scroll(page)
        self.click = Click(page)
        self.last_x = 300
        self.last_y = 300

    # -----------------------------
    # Mover cursor suavemente
    # -----------------------------
    def move_to(self, x, y, steps=50, delay_min=0.02, delay_max=0.05):
        self.move.to(x, y, steps=steps, delay_min=delay_min, delay_max=delay_max)
        self.last_x = x
        self.last_y = y

    # -----------------------------
    # Scroll humano aleatorio
    # -----------------------------
    def scroll_down(self, min_amount=300, max_amount=1200):
        amount = random.randint(min_amount, max_amount)
        self.scroll.down(amount=amount)
        time.sleep(random.uniform(0.3, 1.0))

    # -----------------------------
    # Click en un selector CSS
    # -----------------------------
    def click_at(self, selector):
        """Click en un selector CSS"""
        self.click.at(selector)

    # -----------------------------
    # Click en un ElementHandle
    # -----------------------------
    def click_element_handle(self, element):
        """Mueve el cursor a la posición del ElementHandle y hace click"""
        try:
            box = element.bounding_box()
            if box:
                # Si está fuera de la pantalla, scrollea
                if box["y"] > 600:
                    self.scroll.down(amount=int(box["y"] - 300))
                    time.sleep(random.uniform(0.2, 0.5))

                # Mueve cursor y hace click
                self.move_to(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=20)
            self.click_at(element)  # Click usando ElementHandle
        except Exception as e:
            print(f"⚠️ No se pudo clickear ElementHandle: {e}")

    # -----------------------------
    # Mover cursor a posición aleatoria en pantalla
    # -----------------------------
    def move_random(self, x_min=100, x_max=900, y_min=80, y_max=800):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        self.move_to(x, y)
        return x, y
