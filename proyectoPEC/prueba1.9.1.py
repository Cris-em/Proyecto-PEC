import tkinter as tk
from tkinter import messagebox, PhotoImage
import os
import pygame


# === Rutas ===
ruta_actual = os.path.dirname(__file__)
ruta_imagen = os.path.join(ruta_actual, "mascota.png")
ruta_musica = os.path.join(ruta_actual, "rockinstrumental.mp3")

# === Colores y estilos ===
# Gama de azules armoniosa
FONDO = "#48CAE4"  # Azul claro
TEXTO = "#0077B6"  # Azul medio
ENTRADA_BG = "#90E0EF"  # Azul más claro
ENTRADA_FG = "#FFF8DC"  # Blanco roto
FUENTE = ("JetBrains Mono", 12)

# === Splash screen ===
splash = tk.Tk()
splash.title("Cargando...")
splash.geometry("300x150")
splash.configure(bg=FONDO)
tk.Label(splash, text="Cargando recursos...", font=("Arial", 14), fg=TEXTO, bg=FONDO).pack(expand=True)
splash.update()

pygame.mixer.init()
if os.path.exists(ruta_musica):
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(-1)

splash.destroy()

# === Ventana principal ===
root = tk.Tk()
root.title("Acceso al Sistema")
root.geometry("600x450")
root.configure(bg=FONDO)

def animar_entrada():
    for i in range(1, 601, 20):
        root.geometry(f"{i}x450")
        root.update()
        root.after(10)

animar_entrada()

# Logo
imagen_mascota = PhotoImage(file=ruta_imagen)
tk.Label(root, image=imagen_mascota, bg=FONDO).pack(pady=10)

# Campo de usuario
tk.Label(root, text="✧ Nombre de usuario ✧", font=FUENTE, fg=TEXTO, bg=FONDO).pack(pady=5)
entry_usuario = tk.Entry(root, bg=ENTRADA_BG, fg=ENTRADA_FG, insertbackground=ENTRADA_FG, font=FUENTE)
entry_usuario.pack(pady=5)

# Campo contraseña
tk.Label(root, text="✧ Contraseña ✧", font=FUENTE, fg=TEXTO, bg=FONDO).pack(pady=5)
entry_contrasena = tk.Entry(root, show="*", bg=ENTRADA_BG, fg=ENTRADA_FG, insertbackground=ENTRADA_FG, font=FUENTE)
entry_contrasena.pack(pady=5)

# Botón ingresar
tk.Button(root, text="Ingresar", command=lambda: verificar_acceso(), bg=TEXTO, fg=FONDO, font=FUENTE).pack(pady=20)

def cargar_recursos():
    if os.path.exists(ruta_musica):
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1)

root.after(10, cargar_recursos)

# === Funciones auxiliares ===
def animar_ventana(ventana, ancho=600, alto=400, paso=20, retraso=5):
    ventana.geometry("1x1")
    for w in range(1, ancho + 1, paso):
        ventana.geometry(f"{w}x{alto}")
        ventana.update()
        ventana.after(retraso)

def nueva_ventana(titulo):
    nueva = tk.Toplevel()
    nueva.title(titulo)
    nueva.geometry("1x1")
    nueva.configure(bg=FONDO)
    nueva.bind("<Escape>", lambda event: [nueva.destroy(), abrir_menu_principal()])
    nueva.protocol("WM_DELETE_WINDOW", lambda: [nueva.destroy(), abrir_menu_principal()])
    animar_ventana(nueva)
    return nueva

def boton_regresar(ventana):
    tk.Button(ventana, text="← Regresar al Menú", command=lambda: [ventana.destroy(), abrir_menu_principal()], bg=TEXTO, fg=FONDO, font=FUENTE).pack(pady=20)

# === Login ===
def verificar_acceso():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if usuario == "Equipo8" and contrasena == "54321":
        mostrar_bienvenida()
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

def mostrar_bienvenida():
    root.withdraw()
    bienvenida = tk.Toplevel()
    bienvenida.title("Bienvenida")
    bienvenida.geometry("1x1")
    bienvenida.configure(bg=FONDO)
    bienvenida.bind("<Escape>", lambda event: [bienvenida.destroy(), root.deiconify()])
    bienvenida.protocol("WM_DELETE_WINDOW", lambda: [bienvenida.destroy(), root.deiconify()])
    animar_ventana(bienvenida)

    tk.Label(bienvenida, text="🫧 ¡Bienvenid@! 🫧", font=("JetBrains Mono", 20), fg=TEXTO, bg=FONDO).pack(pady=20)
    tk.Label(bienvenida, text="Haz clic en el botón para continuar", font=FUENTE, fg=TEXTO, bg=FONDO).pack(pady=10)
    tk.Button(bienvenida, text="Siguiente", command=lambda: [bienvenida.destroy(), abrir_menu_principal()], bg=TEXTO, fg=FONDO, font=FUENTE).pack(pady=20)

def cerrar_aplicacion():
    pygame.mixer.music.stop()
    root.destroy()

def abrir_menu_principal():
    menu = tk.Toplevel()
    menu.title("Menú Principal")
    menu.geometry("1x1")
    menu.configure(bg=FONDO)
    animar_ventana(menu)

    tk.Label(menu, text="✧ Menú ✧", font=FUENTE, fg=TEXTO, bg=FONDO).pack(pady=10)
    opciones = [
        ("☾1⭑ ¿Qué es la ia?", definicion),
        ("☾2⭑ ¿Por qué no abusar del uso de la IA?", abusar),
        ("☾3⭑ Consecuencias del uso excesivo de la IA", consecuencias),
        ("☾4⭑ Ventajas de saber usar la IA", ventajas),
        ("☾5⭑ Cuándo sí usar la IA", cuando_si),
        ("☾6⭑ Experiencias positivas del uso moderado de la IA", expeposi),
        ("☾7⭑ Experiencias y reflexiones como equipo del uso de la IA", experefe),
        ("☾8⭑ Algo más (enlaces web)", enlaces)
    ]
    tk.Button(menu, text="☾9⭑ Jugar Memorama IA", command=lambda: [menu.destroy(), memorama()], bg=TEXTO, fg=FONDO, font=FUENTE).pack(pady=5)

    for texto, comando in opciones:
        tk.Button(menu, text=texto, command=lambda c=comando: [menu.destroy(), c()], bg=TEXTO, fg=FONDO, font=FUENTE).pack(pady=5)

    frame_musica = tk.Frame(menu, bg=FONDO)
    frame_musica.pack(pady=10)

# Botón de Pausar Música
    tk.Button(frame_musica, text="⏸ Pausar Música", command=lambda: pygame.mixer.music.pause(),
          bg="#90E0EF", fg="#003049", font=FUENTE, relief="flat", activebackground="#A3D3F7").pack(side="left", padx=5)

# Botón de Reanudar Música
    tk.Button(frame_musica, text="▶ Reanudar Música", command=lambda: pygame.mixer.music.unpause(),
          bg="#90E0EF", fg="#003049", font=FUENTE, relief="flat", activebackground="#A3D3F7").pack(side="left", padx=5)

# Control de volumen
    tk.Scale(frame_musica, from_=0, to=1, resolution=0.1, orient="horizontal", command=lambda v: pygame.mixer.music.set_volume(float(v)),
         bg=FONDO, fg=TEXTO, troughcolor="#90E0EF", highlightthickness=0).pack(side="left", padx=10)


    tk.Button(menu, text="Salir del Programa", command=cerrar_aplicacion, bg="#8B2E2E", fg="white", font=FUENTE, relief="flat", activebackground="#B24545").pack(pady=10)

def definicion(): 
    ventana = nueva_ventana("¿Qué es la IA?")
    texto = (
    "La Inteligencia Artificial (IA) es una rama de la informática que se enfoca en desarrollar sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje, el razonamiento y la percepción. En esencia, la IA busca crear máquinas que puedan pensar, aprender y tomar decisiones como los humanos. 🌊🤖"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#ADE8F4").pack(pady=10)
    boton_regresar(ventana)

def abusar():
    ventana = nueva_ventana("¿Por qué no abusar de la IA?")
    texto = (
    "🌊🌀No se debe abusar del uso de la Inteligencia Artificial (IA) porque, aunque es una herramienta poderosa, su uso excesivo puede generar dependencia, pérdida de habilidades humanas esenciales, y consecuencias éticas y sociales no deseadas. 🌊🧠"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#90E0EF").pack(pady=10)
    boton_regresar(ventana)

def consecuencias():
    ventana = nueva_ventana("Consecuencias del uso excesivo de la IA")
    texto = (
    "🌊✿El uso excesivo de la IA puede tener múltiples consecuencias negativas:✿🌊\n\n"
    "❀Deshumanización del trabajo y las relaciones❀: Al reemplazar tareas humanas por IA, algunas profesiones pueden perder el componente empático o humano. Por ejemplo, en atención al cliente, la empatía genuina puede desaparecer si todo lo maneja un chatbot.\n\n"
    "❀Dependencia tecnológica❀: Si una persona o institución se acostumbra a que la IA haga todo, se corre el riesgo de perder capacidades cognitivas, como el razonamiento lógico, la escritura creativa o el análisis crítico.\n\n"
    "❀Desempleo y desigualdad❀: La automatización excesiva puede llevar a la pérdida de empleos en sectores donde las máquinas o algoritmos pueden sustituir a los humanos. Esto puede aumentar la desigualdad entre quienes tienen acceso a la tecnología y quienes no.\n\n"
    "❀Problemas éticos y de privacidad❀: El uso masivo de IA conlleva riesgos relacionados con la recopilación de datos personales, la vigilancia masiva y la posible manipulación de opiniones a través de algoritmos.\n\n"
    "❀Falta de responsabilidad❀: Cuando una IA comete un error grave (por ejemplo, en un diagnóstico médico o una decisión judicial), no siempre está claro quién es el responsable, lo que puede llevar a una peligrosa falta de rendición de cuentas."
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#48CAE4").pack(pady=10)
    boton_regresar(ventana)

def ventajas():
    ventana = nueva_ventana("Ventajas de saber usar la IA")
    texto = (
     "*🌊 Saber usar la IA correctamente ofrece muchas ventajas: 🌊*\n\n"
     "- Aumento de la productividad: Permite automatizar tareas repetitivas y enfocarse en lo más importante. 🧑‍💻\n\n"
     "- Acceso a información organizada y sintetizada: La IA puede analizar grandes volúmenes de datos y presentar resúmenes útiles. 📊\n\n"
     "- Apoyo en la creatividad: Herramientas como generadores de imágenes, textos o música con IA ayudan a los artistas. 🎨\n\n"
     "- Educación personalizada: Con IA, se pueden diseñar programas educativos que se adapten al ritmo de aprendizaje. 🎓\n\n"
     "Saber usarla implica no solo dominar la herramienta, sino también saber cuándo, cómo y para qué emplearla, manteniendo siempre el criterio humano como guía.\n\n"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#90E0EF").pack(pady=10)
    boton_regresar(ventana)

def cuando_si():
    ventana = nueva_ventana("¿Cuándo sí usar la IA?")
    texto = (
    "🌊 La IA debe usarse cuando: 🌊\n\n"
    "- Se quiere automatizar una tarea rutinaria o repetitiva, como responder correos simples. 📧\n"
    "- Se busca apoyo, no reemplazo, en actividades complejas como la redacción o la investigación. 🧑‍💻\n"
    "- Hay necesidad de procesar grandes volúmenes de datos, como en análisis financiero. 💼\n"
    "- Se desea fomentar la creatividad o desbloquear ideas, usando IA como herramienta de inspiración. 🎨\n"
    "- Se requiere accesibilidad para personas con dificultades visuales o auditivas. 🔊"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#48CAE4").pack(pady=10)
    boton_regresar(ventana)

def expeposi():
    ventana = nueva_ventana("Experiencias positivas del uso moderado de la IA")
    texto = (
     "*🌊 El uso moderado y consciente de la IA ha dado lugar a muchas experiencias positivas: 🌊* \n\n"
     "- En educación, muchos estudiantes han logrado mejorar su comprensión de temas complejos usando asistentes como ChatGPT. 🎓 \n\n"
     "- En el trabajo, profesionales han ahorrado tiempo al generar borradores de documentos con IA. 💼 \n\n"
     "- En diseño y arte, creadores han utilizado generadores de imágenes para visualizar ideas rápidamente. 🎨 \n\n"
    "- En salud, algunas clínicas usan IA para detectar patrones en radiografías. 🏥 \n\n"
    "- Personas con discapacidades han mejorado su autonomía gracias a asistentes de voz. 🗣️ \n\n"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#90E0EF").pack(pady=10)
    boton_regresar(ventana)

def experefe():
    ventana = nueva_ventana("Experiencias y reflexiones del equipo")
    texto = (
    "Como equipo, el uso de la IA nos ha permitido trabajar de forma más eficiente y creativa. 🌊🤖\n\n"
    "Generar ideas rápidas cuando nos sentimos bloqueados. 🧠\n\n"
    "Organizar información y esquemas para presentaciones o trabajos. 📝\n\n"
    "Corregir errores gramaticales o de estilo en documentos importantes. 📚\n\n"
    "Traducir textos o comprender material en otros idiomas de forma más ágil. \n\n"
    "En resumen, como equipo valoramos la IA como un recurso útil, pero creemos que su uso debe ser equilibrado y responsable.\n\n"
    )
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#90E0EF").pack(pady=10)
    boton_regresar(ventana)

def enlaces():
    ventana = nueva_ventana("Algo más (enlaces web)")
    texto = "Aquí puedes consultar más sobre el tema:\n-https://www.youtube.com/watch?v=UKncFg0PyEk&ab_channel=SmileandLearn-Espa%C3%B1ol 🌊🎥\n- https://blog.lifecole.com/inteligencia-artificial-para-ninos/ 🌐"
    tk.Label(ventana, text=texto, wraplength=560, justify="left", font=("Arial", 12, "italic"), fg="#0077B6", bg="#ADE8F4").pack(pady=10)
    boton_regresar(ventana)

def memorama():
    from random import shuffle

    ventana = nueva_ventana("🧠 Juego de Memorama IA 🧠")

    tk.Label(ventana, text="¡Encuentra los pares relacionados con la Inteligencia Artificial! 🤖", wraplength=560, justify="center", font=("Arial", 14, "bold"), fg="#0077B6", bg="#ADE8F4").pack(pady=10)

    palabras = [
        ("Red Neuronal", "Red Neuronal"),
        ("Aprendizaje", "Aprendizaje"),
        ("Datos", "Datos"),
        ("Algoritmo", "Algoritmo"),
        ("Modelo", "Modelo"),
        ("IA", "IA")
    ]
    pares = palabras + palabras
    shuffle(pares)

    botones = []
    revelados = []

    def crear_boton(texto, i):
        btn = tk.Button(cuadro, text="", width=15, height=3, bg=ENTRADA_BG, fg=ENTRADA_FG, font=("Arial", 10, "bold"))

        def mostrar():
            if len(revelados) < 2 and btn["text"] == "":
                btn.config(text=texto)
                revelados.append((i, texto))
                if len(revelados) == 2:
                    ventana.after(800, verificar)

        btn.config(command=mostrar)
        return btn

    def verificar():
        i1, t1 = revelados[0]
        i2, t2 = revelados[1]
        if t1 == t2:
            botones[i1].config(bg="#90EE90")
            botones[i2].config(bg="#90EE90")
        else:
            botones[i1].config(text="")
            botones[i2].config(text="")
        revelados.clear()
        if all(btn["text"] != "" for btn in botones):
            messagebox.showinfo("¡Felicidades!", "Has completado el memorama de IA 🧠✨")

    cuadro = tk.Frame(ventana, bg=FONDO)
    cuadro.pack(pady=10)

    for i, texto in enumerate(pares):
        btn = crear_boton(texto, i)
        btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        botones.append(btn)

    boton_regresar(ventana)

root.mainloop()
