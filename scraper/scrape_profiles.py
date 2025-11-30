# scraper/scraper.py
from playwright.sync_api import sync_playwright
import time

def scrape_target(username):
    with sync_playwright() as p:

        browser = p.chromium.launch(
            channel="chrome",   # 💥 USAR CHROME SIEMPRE
            headless=False
        )

        # Reusar la sesión guardada
        context = browser.new_context(storage_state="session.json")

        page = context.new_page()
        page.goto(f"https://www.instagram.com/{username}/")

        time.sleep(5)

        print(f"📌 Página cargada: {page.url}")

        # Ejemplo: obtener el nombre del usuario
        try:
            name = page.locator("header h2").inner_text()
            print(f"Nombre del perfil: {name}")
        except:
            print("No se pudo obtener el nombre del perfil")

        browser.close()
