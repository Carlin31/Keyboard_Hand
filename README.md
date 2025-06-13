# Keyboard_Hand
Teclado controlado por dedo y ojos

Teclado Virtual Sin Contacto
Proyecto en Python que permite escribir sin tocar ninguna superficie: apuntas a una tecla con tu dedo frente a la cámara y confirmas la pulsación con un parpadeo.

Tecnologías
Python 3.11+

OpenCV

MediaPipe (Hands & FaceMesh)

NumPy

Instalación
Clona el repositorio.

Crea y activa un entorno virtual (python3 -m venv venv + source venv/bin/activate o venv\Scripts\activate).

Instala dependencias: pip install -r requirements.txt.

Ejecuta: python main.py.

Uso
Enfoca la cámara.

Mueve el dedo índice sobre la tecla deseada (se resaltará).

Parpadea para “clic”.

El texto aparece en pantalla y se guarda en output.txt.

Pulsa q para salir.

Estructura
config.py: parámetros globales (resolución, umbrales, tamaños).

hand_detector.py: localiza la punta del dedo.

eye_blink_detector.py: detecta parpadeos (EAR).

keyboard_layout.py: define el layout y regiones de teclas.

drawing.py: dibuja y resalta teclas, muestra texto.

text_manager.py: gestiona buffer y guarda en output.txt.

main.py: orquesta captura, detecciones y lógica de UI.

Limitaciones
Requiere buena iluminación y cámara decente.

No guarda historiales más allá de output.txt.

Umbrales pueden necesitar calibración manual.

Mejoras futuras
Persistencia avanzada (bases de datos, integración con apps).

Calibración automática de umbrales.

Reconocimiento de gestos adicionales.

Optimización para dispositivos de bajos recursos.

Perfiles de accesibilidad (alto contraste, voz).
