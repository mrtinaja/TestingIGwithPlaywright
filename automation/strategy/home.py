# home.py
import time
import random
from automation.mouse.move import Move
from automation.mouse.click import Click

class Home:
    def __init__(self, page):
        self.page = page

    def go_home(self):
        """
        Mueve el cursor al botón 'Home', hace click y espera que la página recargue.
        """
        home_selector = "a[aria-label='Home'], a[href='/' ]"  # Ajusta según la versión de IG
        home_button = self.page.query_selector(home_selector)

        if not home_button:
            print("⚠️ No se encontró el botón Home")
            return

        try:
            # Mueve el cursor al centro del botón
            box = home_button.bounding_box()
            if box:
                Move(self.page).to(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=20)
            
            # Click
            Click(self.page).at(home_button)
            print("🏠 Click en Home")
            
            # Espera a que la página recargue
            time.sleep(random.uniform(2.0, 4.0))
        except Exception as e:
            print(f"⚠️ Error al ir a Home: {e}")
