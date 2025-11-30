// CREA UN CURSOR VISIBLE PARA EL BOT
(() => {
    if (window._botCursorActive) return;
    window._botCursorActive = true;

    const cursor = document.createElement("div");

    Object.assign(cursor.style, {
        width: "110px",
        height: "110px",
        background: "rgba(255, 0, 0, 0.9)", // rojo para destacar
        
        borderRadius: "50%",
        position: "fixed",
        top: "0px",
        left: "0px",
        transform: "translate(-50%, -50%)",
        pointerEvents: "none",
        zIndex: "9999999",
        transition: "transform 0.05s linear"
    
    
    });

    document.body.appendChild(cursor);

    window.updateBotCursor = (x, y) => {
        cursor.style.transform = `translate(${x}px, ${y}px)`;
        cursor.style.border = "2px solid black";

    };
})();
