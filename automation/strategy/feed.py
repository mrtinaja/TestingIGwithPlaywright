import random
import time
from automation.mouse.move import Move
from automation.mouse.click import Click
from automation.mouse.scroll import Scroll
from playwright.sync_api import Page  # pyright: ignore[reportMissingImports]


class Feed:
    def __init__(self, page: Page):
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
                # mover el mouse al centro del elemento
                Move(self.page).to(
                    box["x"] + box["width"] / 2,
                    box["y"] + box["height"] / 2,
                    steps=20,
                )

                # si está muy abajo del viewport, scrolleo un poco antes
                if box["y"] > 600:
                    Scroll(self.page).down(amount=int(box["y"] - 300))
                    time.sleep(random.uniform(0.2, 0.5))

            # click usando tu wrapper
            Click(self.page).at(element)
            print("📸 Foto clickeada")
            time.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            print(f"⚠️ No se pudo clickear la foto: {e}")

    # -----------------------------
    # Dar like a una foto / post
    # -----------------------------
    def like_photo(self):
        """
        Intenta darle like al post visible.
        Usa el nombre/label 'Me gusta' (aria-label) del icono de corazón.
        No depende de clases ni XPaths frágiles.
        """
        try:
            # 1) Buscar por label accesible (aria-label="Me gusta")
            heart_locator = self.page.get_by_label("Me gusta")

            if heart_locator.count() == 0:
                # 2) Fallback: buscar por CSS directo sobre el SVG
                heart_locator = self.page.locator(
                    "svg[aria-label='Me gusta'], svg[aria-label='Like']"
                )

            if heart_locator.count() == 0:
                print("⚠️ No se encontró el botón/corazón 'Me gusta'.")
                return

            heart = heart_locator.first

            if not heart.is_visible():
                print("⚠️ El corazón 'Me gusta' no está visible.")
                return

            # Evitar relike: si el aria-label indica que ya está likeado
            aria = heart.get_attribute("aria-label") or ""
            if "Ya no" in aria or "Unlike" in aria:
                print("💡 El post ya estaba likeado.")
                return

            box = heart.bounding_box()
            if box:
                # mover al corazón y clickear con tu wrapper
                Move(self.page).to(
                    box["x"] + box["width"] / 2,
                    box["y"] + box["height"] / 2,
                    steps=15,
                )
                Click(self.page).at(heart)
            else:
                # fallback simple
                heart.click()

            print("❤️ Foto likeada")
            time.sleep(random.uniform(0.5, 1.2))

        except Exception as e:
            print(f"⚠️ Error al dar like: {e}")

    # -----------------------------
    # Click en foto aleatoria del feed
    # -----------------------------
    def click_random_photo(self):
        """
        Clickea una foto aleatoria del feed y le da like.
        Primero busca <article> img, luego intenta likear el post.
        """
        try:
            photo_selector = "article img"
            photos = self.page.query_selector_all(photo_selector)
            if not photos:
                print("⚠️ No se encontraron fotos.")
                return

            photo = random.choice(photos)
            self.click_element(photo)

            # Dar like usando el label "Me gusta"
            self.like_photo()

            time.sleep(random.uniform(1, 3))
        except Exception as e:
            print(f"⚠️ Error al procesar foto aleatoria: {e}")

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
