# stories.py
import random
import time
from automation.mouse.move import Move
from automation.mouse.click import Click
from automation.mouse.scroll import Scroll

class Stories:
    def __init__(self, page):
        self.page = page

    def click_element(self, element):
        """Intenta hacer click en un ElementHandle con scroll y movimiento humano."""
        try:
            box = element.bounding_box()
            if box:
                # Mueve el cursor
                Move(self.page).to(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=20)
                
                # Si está fuera de la pantalla, scrollea
                if box['y'] > 600:
                    Scroll(self.page).down(amount=int(box['y'] - 300))
                    time.sleep(random.uniform(0.2, 0.5))

            # Click
            Click(self.page).at(element)
            print("✅ Elemento clickeado (story)")
        except Exception as e:
            print(f"⚠️ No se pudo clickear el elemento: {e}")

    def view_stories(self):
        """Busca historias y reproduce una aleatoria."""
        story_selector = "div[role='button'][aria-label*='Story']"
        stories = self.page.query_selector_all(story_selector)
        if not stories:
            print("⚠️ No se encontraron historias.")
            return

        story = random.choice(stories)
        self.click_element(story)
        print("▶️ Viendo historia...")
        time.sleep(random.uniform(3, 6))
        self.page.keyboard.press("Escape")
        print("✖️ Historia cerrada")
        time.sleep(random.uniform(0.5, 1.0))
