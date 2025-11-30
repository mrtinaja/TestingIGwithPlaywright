# feed.py
import random
import time
from automation.mouse.move import Move
from automation.mouse.click import Click
from automation.mouse.scroll import Scroll

class Feed:
    def __init__(self, page):
        """
        Clase que gestiona las interacciones con el feed de Instagram:
        - Click en fotos
        - Dar like
        - Scroll humano lento, mayormente hacia abajo
        """
        self.page = page

    # -----------------------------
    # Click en un elemento
    # -----------------------------
    def click_element(self, element):
        """Click en un elemento, moviendo cursor y haciendo scroll si es necesario"""
        try:
            box = element.bounding_box()
            if box:
                Move(self.page).to(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=20)
                if box['y'] > 600:
                    Scroll(self.page).down(amount=int(box['y'] - 300))
                    time.sleep(random.uniform(0.2, 0.5))
            Click(self.page).at(element)
            print("📸 Foto clickeada")
            time.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            print(f"⚠️ No se pudo clickear la foto: {e}")

    # -----------------------------
    # Dar like a una foto
    # -----------------------------
    def like_photo(self, photo_element):
        """Intenta darle like a la foto usando XPath relativo y verificando fill"""
        try:
            heart = photo_element.query_selector(
                ".//div[@role='button']/svg[@aria-label='Me gusta' or @aria-label='Like']"
            )
            if heart:
                fill = heart.get_attribute("fill")
                if fill == "currentColor":
                    box = heart.bounding_box()
                    if box:
                        Move(self.page).to(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=15)
                        Click(self.page).at(heart)
                        print("❤️ Foto likeada")
                        time.sleep(random.uniform(0.5, 1.2))
                else:
                    print("ℹ️ Foto ya estaba likeada")
            else:
                print("⚠️ No se encontró el corazón de like en la foto.")
        except Exception as e:
            print(f"⚠️ Error al dar like: {e}")

    # -----------------------------
    # Click en foto aleatoria del feed
    # -----------------------------
    def click_random_photo(self):
        """Clickea una foto aleatoria del feed y le da like"""
        photo_selector = "article img"
        photos = self.page.query_selector_all(photo_selector)
        if not photos:
            print("⚠️ No se encontraron fotos.")
            return

        photo = random.choice(photos)
        self.click_element(photo)
        self.like_photo(photo)
        time.sleep(random.uniform(1, 3))

    # -----------------------------
    # Scroll humano lento alternando down/up
    # -----------------------------
    def human_scroll(self, max_duration=10):
        """
        Scroll lento por el feed:
        - Mayormente hacia abajo
        - Ocasionalmente hacia arriba (10% de las veces)
        - Se detiene cada pocos segundos
        """
        start_time = time.time()
        while time.time() - start_time < max_duration:
            # Decidir dirección: 90% down, 10% up
            direction = "down" if random.random() < 0.9 else "up"
            amount = random.randint(100, 400)

            if direction == "down":
                Scroll(self.page).down(amount=amount)
                print(f"⬇️ Scroll de {amount} píxeles")
            else:
                Scroll(self.page).up(amount=amount)
                print(f"⬆️ Scroll de {amount} píxeles")

            # Pausa aleatoria para simular lectura
            time.sleep(random.uniform(1.0, 2.5))
