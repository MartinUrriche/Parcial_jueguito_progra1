# 🌻 No es Plantas vs Zombies  
🎮 Juego estilo **Arkanoid / Breakout** inspirado en Plants vs Zombies  
🧠 Desarrollado con **Python + Pygame**

Creadores: Martin Urriche, Malena Fernandez, Maia Portilla, Florencia Roumieu

---

## 📌 Descripción del Juego

**No es Plantas vs Zombies** es un juego estilo *Arkanoid*, donde el jugador controla un **girasol** que rebota un **proyectil (sol)** para destruir **zombies** organizados en forma de grilla.

Cada zombie puede tener:
- 1, 2 o 3 vidas  
- Cambia de imagen según el daño recibido  
- Suma puntos al ser derrotado  

El jugador gana cuando elimina todos los zombies y pierde cuando se queda sin vidas.

---

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| ⬅ Flecha izquierda | Mover girasol a la izquierda |
| ➡ Flecha derecha | Mover girasol a la derecha |
| 🖱 Click izquierdo | Lanzar la pelota |
| ⌫ Backspace | Pausar el juego |
| ↵ Enter | Confirmar nombre en el scoreboard |

---

## ❤️ Sistema de Vidas

- El jugador comienza con **3 corazones**.  
- Si la pelota cae al suelo:
  - Se pierde una vida  
  - La pelota se reinicia sobre el girasol  
- Si las vidas llegan a **0**:
  - Se muestra la pantalla de **Derrota**  
  - Luego se regresa al menú inicial  

---

## 🧟 Enemigos (Zombies)

Los zombies pueden tener:

| Nivel | Imagen | Vidas |
|--------|--------|--------|
| Nivel 1 | Zombie base | 1 |
| Nivel 2 | Zombie con cono → zombie base | 2 |
| Nivel 3 | Zombie caracubo → casco roto → zombie base | 3 |

Cada impacto:
- Reduce una vida  
- Cambia la imagen  
- Suma **10 puntos**

---

## 🏆 Sistema de Puntaje (Scoreboard)

- Al ganar el jugador ingresa su **nombre (AKA)**.  
- El puntaje se guarda en un archivo:

```text
scoreboard.json
