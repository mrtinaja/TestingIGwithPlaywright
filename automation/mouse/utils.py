# automation/mouse/utils.py
def update_cursor(page, x, y):
    """
    Actualiza la posición del cursor virtual en la página de manera segura.
    """
    try:
        page.evaluate("""(pos) => {
            if (window.updateBotCursor) {
                window.updateBotCursor(pos.x, pos.y);
            }
        }""", {"x": x, "y": y})
    except Exception:
        # No imprimimos el error para no llenar la consola
        pass
