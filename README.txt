Instagram Automation Bot
========================
Automatiza acciones humanas en Instagram con movimientos de mouse, scroll, visualización de
historias y navegación en el feed, bajo un sistema de estrategias que evita la ejecución simultánea
de módulos.
Funcionalidades del bot
-----------------------
| Módulo | Acción | Descripción |
|---------|----------------|-----------------------------------------------------------------------------|
| Feed | Scroll + Click | Simula usuario navegando el feed e interactuando con publicaciones. |
| Stories | Ver historias | Abre una historia aleatoria y la cierra tras unos segundos. |
| Home | Navegar a inicio | Lleva al usuario a la pantalla principal de Instagram. |
| Strategy | Coordinación | Garantiza que solo haya un módulo activo a la vez. |
Prevención de solapamientos: El sistema activa y desactiva módulos mediante activate_module(),
garantizando que, por ejemplo, Stories no interrumpa al Feed.
Instalación y configuración
---------------------------
1. Clonar el repositorio:
git clone https://github.com/tu_usuario/instagram-bot.git
cd instagram-bot
2. Crear entorno virtual:
python -m venv venv
Activación:
- Windows: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate
3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar bot:
python main.py
Estrategias predefinidas
------------------------
from automation.strategy.strategy import Strategy
strategy = Strategy(page)
strategy.strategy_feed()
strategy.strategy_stories()
strategy.strategy_home()
Errores conocidos
-----------------
Unsupported token "@role": No puede usarse XPath dentro de un selector CSS. Usar CSS puro
como:
element.query_selector("svg[aria-label='Like']")
Contribución
------------
1. git checkout -b feature/nueva-funcionalidad
2. git commit -m "Agrego scroll inteligente"
3. git push origin feature/nueva-funcionalidad
Licencia
--------
MIT License – Puedes modificar y usar libremente bajo tu responsabilidad.
Contacto
--------
Desarrollo por: Tu nombre / Alias
Instagram Bot Project 2025
IA Assistant Support by ChatGPT