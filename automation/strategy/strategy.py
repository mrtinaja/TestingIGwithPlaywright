# strategy.py
from automation.strategy.stories import Stories
from automation.strategy.feed import Feed
from automation.strategy.home import Home
import time
import random

class Strategy:
    def __init__(self, page):
        """
        Coordinador de módulos de Instagram.
        Solo ejecuta un módulo activo a la vez.
        Por defecto, Feed está activo.
        Stories y Home solo se ejecutan cuando se activan explícitamente.
        """
        self.page = page
        self.stories = Stories(page)
        self.feed = Feed(page)
        self.home = Home(page)

        # Diccionario de módulos activos
        self.active_modules = {
            "stories": False,  # nunca se ejecuta por defecto
            "feed": True,      # módulo por defecto
            "home": False
        }

    # -----------------------------
    # Activar módulo explícitamente
    # -----------------------------
    def activate_module(self, module_name):
        """
        Activa un módulo y desactiva todos los demás.
        Garantiza que nunca haya superposición de acciones.
        """
        for key in self.active_modules:
            self.active_modules[key] = (key == module_name)
        print(f"🔹 Módulo activo: {module_name}")

    # -----------------------------
    # Ejecutar módulo activo
    # -----------------------------
    def run(self):
        """
        Ejecuta solo la acción del módulo activo.
        Por defecto solo Feed se ejecuta.
        Stories y Home solo se ejecutan si se activan explícitamente.
        """
        if self.active_modules.get("feed"):
            self._run_feed()
        elif self.active_modules.get("stories"):
            self._run_stories()
        elif self.active_modules.get("home"):
            self._run_home()
        else:
            print("⚠️ Ningún módulo activo. Use activate_module para activar uno.")

    # -----------------------------
    # Métodos internos de ejecución
    # -----------------------------
    def _run_feed(self):
        try:
            # Solo click y scroll del feed, NO tocar Stories
            self.feed.click_random_photo()
            time.sleep(random.uniform(0.5, 1.5))
            self.feed.human_scroll()
            time.sleep(random.uniform(0.5, 1.0))
        except Exception as e:
            print(f"⚠️ Error en Feed: {e}")

    def _run_stories(self):
        try:
            self.stories.view_stories()
            time.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            print(f"⚠️ Error en Stories: {e}")

    def _run_home(self):
        try:
            self.home.go_home()
            time.sleep(random.uniform(1.0, 2.0))
        except Exception as e:
            print(f"⚠️ Error en Home: {e}")

    # -----------------------------
    # Estrategias predefinidas
    # -----------------------------
    def strategy_feed(self):
        """Ejecuta Feed (módulo por defecto)."""
        self.activate_module("feed")
        self.run()

    def strategy_stories(self):
        """Ejecuta Stories solo si se llama explícitamente."""
        self.activate_module("stories")
        self.run()

    def strategy_home(self):
        """Ejecuta Home solo si se llama explícitamente."""
        self.activate_module("home")
        self.run()
