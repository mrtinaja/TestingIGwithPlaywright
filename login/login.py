# login/login.py
import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:

        # Lanzamos Chrome REAL, NO Chromium
        browser = p.chromium.launch(
            channel="chrome",    # 💥 ESTA ES LA CLAVE
            headless=False,
            slow_mo=80
        )

        context = browser.new_context(
            viewport={"width": 1200, "height": 800},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            locale="es-ES",
            timezone_id="America/Argentina/Buenos_Aires"
        )

        page = context.new_page()
        page.goto("https://www.instagram.com/accounts/login/")

        print("\n👉 Inicia sesión MANUALMENTE en Instagram.")
        print("👉 NO cierres la ventana.")
        print("👉 Tienes 60 segundos...\n")
        time.sleep(60)

        print("✅ Guardando sesión en session.json...")
        context.storage_state(path="session.json")

        print("🎉 Listo. Tu sesión está guardada correctamente.")
        browser.close()

if __name__ == "__main__":
    main()
