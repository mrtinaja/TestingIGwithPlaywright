# bot.py
import random
import time
from playwright.sync_api import sync_playwright

from automation.mouse.utils import update_cursor
from automation.mouse.move import Move
from automation.strategy.strategy import Strategy

# -----------------------------
# JS para cursor visible
# -----------------------------
BOT_CURSOR_JS = """
(() => {
    if (window._botCursorActive) return;
    window._botCursorActive = true;

    const cursor = document.createElement("div");
    Object.assign(cursor.style, {
        width: "20px",
        height: "20px",
        background: "rgba(255, 0, 0, 1)",
        borderRadius: "50%",
        position: "fixed",
        top: "50px",
        left: "50px",
        transform: "translate(-50%, -50%)",
        pointerEvents: "none",
        zIndex: "9999999",
        transition: "transform 0.05s linear",
        border: "2px solid white"
    });
    document.body.appendChild(cursor);

    window.updateBotCursor = (x, y) => {
        cursor.style.transform = `translate(${x}px, ${y}px)`;
    };
})();
"""

def inject_cursor_js(page):
    """Inyecta el cursor en la página de manera segura"""
    page.evaluate(BOT_CURSOR_JS)


# -----------------------------
# Movimiento aleatorio suave
# -----------------------------
def move_random(page, last_pos):
    """Mueve el cursor a una posición aleatoria suavemente"""
    new_x = random.randint(100, 900)
    new_y = random.randint(80, 800)
    Move(page).to(new_x, new_y, steps=random.randint(20, 50), delay_min=0.02, delay_max=0.05)
    return (new_x, new_y)


# -----------------------------
# Función principal
# -----------------------------
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="chrome_profile",
            headless=False,
            channel="chrome"
        )
        page = browser.new_page()

        # Abrir Instagram
        page.goto("https://www.instagram.com/")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(1)

        # Inyectar cursor visible
        inject_cursor_js(page)
        print("🟢 Cursor activado y bot iniciado...")

        # Inicializa posición del cursor
        last_pos = (random.randint(100, 900), random.randint(80, 800))
        update_cursor(page, *last_pos)

        # Inicializa Strategy (Feed activo por defecto)
        strategy = Strategy(page)

        # -----------------------------
        # Loop principal
        # -----------------------------
        while True:
            # Ejecuta el módulo activo definido en Strategy
            strategy.run()

            # Movimiento humano aleatorio
            last_pos = move_random(page, last_pos)

            # Pausa humana
            time.sleep(random.uniform(0.5, 2.0))


if __name__ == "__main__":
    main()
