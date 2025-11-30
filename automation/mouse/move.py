# automation/mouse/move.py
import time
import random
from automation.mouse.utils import update_cursor
from automation.mouse.scroll import Scroll

class Move:
    last_x = 300
    last_y = 300

    def __init__(self, page):
        self.page = page

    def to(self, x, y, steps=50, delay_min=0.02, delay_max=0.05):
        """
        Mueve el cursor suavemente de la última posición a (x, y)
        y actualiza el cursor virtual usando update_cursor.
        Si el destino está fuera de pantalla, hace scroll para que sea visible.
        """
        viewport_height = self.page.evaluate("() => window.innerHeight")
        viewport_width = self.page.evaluate("() => window.innerWidth")

        # Si Y está fuera del viewport, hace scroll vertical
        if y > viewport_height - 50:
            scroll_amount = int(y - (viewport_height / 2))
            Scroll(self.page).down(scroll_amount)
            time.sleep(random.uniform(0.2, 0.5))
            # Ajusta la coordenada Y para la posición visible
            y = viewport_height / 2

        # Si X está fuera del viewport, se ajusta al máximo visible
        if x > viewport_width - 50:
            x = viewport_width - 50
        elif x < 50:
            x = 50

        start_x = Move.last_x
        start_y = Move.last_y

        for i in range(1, steps + 1):
            t = i / steps
            nx = start_x + (x - start_x) * t
            ny = start_y + (y - start_y) * t

            # Mueve el mouse real
            self.page.mouse.move(nx, ny)

            # Actualiza el cursor virtual
            update_cursor(self.page, nx, ny)

            # Pequeño delay aleatorio para simular movimiento humano
            time.sleep(random.uniform(delay_min, delay_max))

        Move.last_x = x
        Move.last_y = y
