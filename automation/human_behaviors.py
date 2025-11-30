# automation/human_behaviors.py
import time
import random
import math
from automation.mouse.move import Move
from automation.mouse.click import Click
from automation.mouse.scroll import Scroll
from ig_scraper.automation.strategy.strategy import view_stories_and_scroll

# -----------------------------
# Movimiento hacia un selector
# -----------------------------
def move_to_selector(page, selector, steps=50):
    """Mueve el cursor suavemente hacia el centro del selector."""
    element = page.query_selector(selector)
    if not element:
        print(f"⚠️ No se encontró selector: {selector}")
        return False

    box = element.bounding_box()
    if not box:
        print(f"⚠️ Bounding box vacío: {selector}")
        return False

    target_x = box["x"] + box["width"] / 2
    target_y = box["y"] + box["height"] / 2

    Move(page).to(target_x, target_y, steps=steps, delay_min=0.02, delay_max=0.05)
    return True

# -----------------------------
# Click humano
# -----------------------------
def human_click(page, selector):
    """Mueve el cursor al selector y hace click de manera humana."""
    if move_to_selector(page, selector):
        time.sleep(random.uniform(0.1, 0.4))
        Click(page).at(selector)
        time.sleep(random.uniform(0.3, 1.0))
        return True
    return False

# -----------------------------
# Escribir texto como humano
# -----------------------------
def human_type(page, selector, text):
    """Mueve el cursor al input, hace click y escribe el texto como humano."""
    if move_to_selector(page, selector):
        time.sleep(random.uniform(0.1, 0.3))
        Click(page).at(selector)
        for char in text:
            page.keyboard.type(char)
            time.sleep(random.uniform(0.08, 0.25))
        time.sleep(random.uniform(0.3, 0.8))
        return True
    return False

# -----------------------------
# Scroll humano aleatorio
# -----------------------------
def human_scroll(page, min_amount=300, max_amount=1200):
    """Hace scroll hacia abajo de manera humana."""
    amount = random.randint(min_amount, max_amount)
    Scroll(page).down(amount=amount)
    time.sleep(random.uniform(0.3, 1.0))

# -----------------------------
# Movimiento circular opcional
# -----------------------------
def circular_move(page, center_x=600, center_y=400, radius=90, loops=1):
    """Mueve el cursor en un círculo pequeño para simular exploración visual."""
    steps = 50
    for _ in range(loops):
        for i in range(steps):
            angle = (2 * math.pi / steps) * i
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            Move(page).to(x, y, steps=1, delay_min=0.01, delay_max=0.03)
            time.sleep(0.015)

# -----------------------------
# Visitar un perfil humano
# -----------------------------
def visit_profile(page, username):
    """Busca un perfil y hace click en el resultado como un humano."""
    search_input = "input[placeholder='Search']"
    result_selector = "div[role='dialog'] a.x1i10hfl"

    print(f"🔎 Buscando perfil: {username}")

    if not human_type(page, search_input, username):
        return False

    time.sleep(random.uniform(1.0, 1.8))

    if not human_click(page, result_selector):
        return False

    time.sleep(random.uniform(4.0, 8.0))
    return True

# -----------------------------
# Agencia: decide qué hacer
# -----------------------------
def act_humanly(page):
    """Decide de manera humana qué acción ejecutar."""
    roll = random.random()

    if roll < 0.3:
        human_scroll(page)
    elif roll < 0.6:
        selectors = ["button", "a", "div[role='button']"]
        sel = random.choice(selectors)
        human_click(page, sel)
    elif roll < 0.9:
        inputs = ["input[type='text']", "input[placeholder='Search']"]
        sel = random.choice(inputs)
        human_type(page, sel, random.choice(["hola", "test", "cristiano"]))
    else:
        # ✅ Llamada a la estrategia para ver historias y luego scroll
       view_stories_and_scroll(page)

