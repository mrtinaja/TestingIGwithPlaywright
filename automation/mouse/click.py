class Click:
    def __init__(self, page):
        self.page = page

    def at(self, selector_or_handle, timeout=5000):
        """Click en un selector o ElementHandle asegurando que sea visible en pantalla."""
        try:
            if hasattr(selector_or_handle, "hover"):
                # Es un ElementHandle
                selector_or_handle.scroll_into_view_if_needed(timeout=timeout)
                selector_or_handle.hover()
                selector_or_handle.click()
            else:
                # Es un selector string
                self.page.wait_for_selector(selector_or_handle, state="visible", timeout=timeout)
                # Asegura que el selector esté en pantalla
                self.page.eval_on_selector(selector_or_handle, "el => el.scrollIntoView({block: 'center', inline: 'center'})")
                self.page.hover(selector_or_handle)
                self.page.click(selector_or_handle)
        except Exception as e:
            print(f"⚠️ No se pudo clickear {'ElementHandle' if hasattr(selector_or_handle, 'hover') else selector_or_handle}: {e}")
