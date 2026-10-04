# =====================================================================
#  EL MISTERIO DE SHAKIRA  (proyecto Radal)
#  Novela visual para Ren'Py 8.
#
#  Funciona SIN imágenes ni audio: usa figuras placeholder generadas
#  por código (siluetas con símbolo). Cuando tengas tus archivos:
#    - Sprites:   game/images/jose.png, pablo.png, diego.png, fabian.png,
#                 marcelo.png, benjamin.png, bastian.png, ruben.png,
#                 maxi.png, ivan.png, martin.png, hector.png, shakira.png
#                 (borra la línea "image X = placeholder(...)" de cada uno)
#    - Fondos:    game/images/bg inacap.png, bg patio.png, bg shell.png,
#                 bg jumbo.png, bg potrero.png, bg liceo.png, bg fundo.png,
#                 bg funeral.png, bg atardecer.png, bg inacap_lluvia.png,
#                 bg sueno.png, bg sala_liceo.png, bg cisterna_patio.png,
#                 bg cisterna_int.png, bg shell_ruinas.png, bg pesebre.png,
#                 bg asado.png, bg jumbo_pasillo.png
#    - Escenas:  game/images/escena pablo_lluvia.png, escena cerca_desayuno.png,
#                 escena cumple.png, escena atardecer_cerca.png,
#                 escena venta_camioneta.png, escena cisterna_pablo.png,
#                 escena choque.png, escena ruben_banca.png,
#                 escena martin_clase.png, escena asado.png, escena sueno_ruta.png
#                 (planos compuestos de momentos clave; borra la línea
#                 "image escena X = escena(...)" cuando tengas el arte)
#                 (borra la línea "image bg X = fondo(...)" correspondiente)
#    - Música:    game/audio/tema.ogg, dramatica.ogg, cumbia.ogg, triste.ogg
#    - Efectos:   game/audio/relincho.ogg, trueno.ogg
#  Si un audio no existe, simplemente no suena (no da error).
#
#  Estilo Telltale: las decisiones dejan notificaciones ("X lo recordará")
#  y cambian diálogos, pistas y finales. Hay 6 finales.
# =====================================================================

# ---------------------------------------------------------------------
#  Personajes
# ---------------------------------------------------------------------
default nombre = "Kabro"

define mc       = Character("[nombre]", color="#2ecc71")
define jose     = Character("José Lipian", color="#e67e22")
define pablo    = Character("Pablo Hernández", color="#f1c40f")
define diego    = Character("Diego Arévalo", color="#3498db")
define fabian   = Character("Fabián Millalén", color="#b36bd6")
define marcelo  = Character("Marcelo", color="#95a5a6")
define benjamin = Character("Benjamín", color="#e74c3c")
define bastian  = Character("Bastián Poblete", color="#1abc9c")
define ruben    = Character("Rubén Maldonado", color="#a9714b")
define maxi     = Character("Maxi Valenzuela", color="#00acc1")
define ivan     = Character("Iván Garrido del 4F", color="#afb42b")
define inacapini = Character("El Inacapini", color="#1f9fd6")
define martin   = Character("Profe Martín", color="#7d3c98")
define hector   = Character("Héctor", color="#7e5109")
define shakira  = Character("Shakira", color="#ff6fae")

# ---------------------------------------------------------------------
#  Variables de decisiones
# ---------------------------------------------------------------------
default drama = 0            # qué tan acusador/exagerado eres
default apoyo = 0            # qué tan empático eres con José
default broma_benjamin = 0   # cuánto alimentas el caos de Benjamín

default pista_pablo = False    # montura escondida / "cuatro cuotas"
default pista_diego = False    # zanahorias + gafas de sol
default pista_potrero = False  # heno fresco en Lincoñir
default pista_ruben = False    # Rubén vio a Shakira en Pillalelbún
default pablo_arruinado = False  # la Shell quedó destruida por Benjamín

# Relaciones con cada personaje (suben y BAJAN con tus decisiones)
default rel = {"José": 0, "Pablo": 0, "Diego": 0, "Fabián": 0, "Marcelo": 0,
               "Benjamín": 0, "Bastián": 0, "Rubén": 0, "Maxi": 0}

default pablo_molesto = False  # le preguntaste si tenía frío
default promesa_marcelo = False  # prometiste seguir premierchilito
default secreto_ruben = False  # prometiste proteger a tu fuente
default verdad_martin = False  # sabes la verdad del "viaje a China"
default plan_benjamin = False  # escuchaste la propuesta de Benjamín

default fragmentos = 0         # pedazos de la historia de Shakira (grabadora)
default historia_escuchada = False  # ya escuchaste la historia completa

default venta = False          # ¿ya ocurrió LA venta?
default potrero_visitas = 0    # visitas a Lincoñir antes de la venta (de 3)
default bg_prologo = "bg inacap"  # fondo al que volver tras el enfoque del short
default clima = "lluvia"          # clima del prólogo que tocó (para diálogos coherentes)

default v_patio = False
default v_shell = False
default v_jumbo = False
default v_potrero = False
default v_liceo = False
default v_ruben = False
default v_sueno = False
default v_tinder = False            # misión WHAT IF del Tinder de José
default whatif_tinder_activo = False
default v_fabian_sale = False       # el día que Fabián se fue del INACAP
default v_inundacion = False        # la inundación de Pillalelbún
default ayuda_inundacion = ""       # a quién ayudaste en la inundación
default whatif_trabajo_activo = False
default v_trabajo = False

default v_juicio_shell = False      # el juicio de la Shell (Pablo vs Benjamín)
default v_conflicto_marcelo = False  # premierchilito en peligro (Marcelo vs Benjamín)
default v_conflicto_ruben = False   # la deuda de las láminas (Fabián vs Rubén)

default v_fabian_intro = False      # ya conociste a Fabián en el prólogo
default v_pelea_inacapini = False   # Benjamín vs el Inacapini
default whatif_inacapini_activo = False
default v_inacapini = False

default persistent.finales = set()

# ---------------------------------------------------------------------
#  Placeholders y ayudas de audio / notificaciones
# ---------------------------------------------------------------------
init python:

    def fondo(texto, color, sub=None):
        partes = [Solid(color)]
        if sub:
            partes.append(Text(texto, size=90, color="#ffffff", xalign=0.5,
                               yalign=0.42, outlines=[(3, "#000000", 0, 0)]))
            partes.append(Text(sub, size=46, italic=True, color="#ffffff",
                               xalign=0.5, yalign=0.58,
                               outlines=[(2, "#000000", 0, 0)]))
        else:
            partes.append(Text(texto, size=90, color="#ffffff", xalign=0.5,
                               yalign=0.5, outlines=[(3, "#000000", 0, 0)]))
        return Fixed(*partes)

    def cover(fn, ancho=1920, alto=1080):
        # Escala la imagen con zoom para CUBRIR la pantalla. El sobrante
        # queda fuera de la ventana y no se ve. Sin espacios vacíos.
        w, h = renpy.image_size(fn)
        esc = max(ancho / w, alto / h)
        return Transform(fn, zoom=esc, xalign=0.5, yalign=0.5)

    def escena(texto, color):
        # Plano/escena compuesta: un "fotograma" del momento exacto.
        # Después se reemplaza por una ilustración de esa escena.
        return Fixed(
            Solid("#1a1a1a"),
            Fixed(
                Solid(color),
                Text("» " + texto, size=60, color="#ffffff", xalign=0.5,
                     yalign=0.5, outlines=[(3, "#000000", 0, 0)], text_align=0.5),
                xsize=1820, ysize=1020, xalign=0.5, yalign=0.5))

    def placeholder(texto, color):
        return Fixed(
            Solid(color, xsize=420, ysize=820),
            Text(texto, size=52, color="#ffffff", xalign=0.5, yalign=0.5,
                 outlines=[(3, "#000000", 0, 0)]),
            xsize=420, ysize=820)

    def sprite(fn, ancho=520, alto=860, alza=250):
        # Sprite en caja uniforme (nadie se encima) y con los pies
        # "sobre" el recuadro de texto: el cuadro de diálogo no los tapa.
        return Fixed(
            Transform(fn, xysize=(ancho, alto), fit="contain",
                      xalign=0.5, yalign=1.0),
            xsize=ancho, ysize=alto, yoffset=-alza)

    def muestra(lista, n):
        # N elementos al azar de la lista (seguro para rollback).
        copia = list(lista)
        renpy.random.shuffle(copia)
        return copia[:n]

    def musica(archivo):
        base = "audio/" + archivo.rsplit(".", 1)[0]
        nombre = archivo.rsplit(".", 1)[0]
        for ext in (".ogg", ".mp3", ".wav", ".opus"):
            ruta = base + ext
            if renpy.loadable(ruta):
                # No reinicia el tema si ya está sonando.
                actual = renpy.music.get_playing() or ""
                if nombre not in actual:
                    renpy.music.play(ruta, fadein=1.0, loop=True)
                renpy.music.set_volume(1.0, delay=0.5)
                return
        # Mientras falten los temas (.ogg pendientes), modula el actual:
        # triste = más bajito, dramática = bajito, resto = normal.
        if "triste" in nombre:
            renpy.music.set_volume(0.45, delay=1.5)
        elif "dramatica" in nombre:
            renpy.music.set_volume(0.7, delay=1.0)
        else:
            renpy.music.set_volume(1.0, delay=1.0)

    def sfx(archivo):
        ruta = "audio/" + archivo
        if renpy.loadable(ruta):
            renpy.sound.play(ruta)

    def recuerda(quien, msg=None, negativo=False, puntos=None):
        # Notificación estilo Telltale (grande) + cambio de relación.
        if puntos is None:
            puntos = -1 if negativo else 1
        if quien in store.rel:
            store.rel[quien] = store.rel.get(quien, 0) + puntos
        if msg is None:
            msg = quien + (" NO lo olvidará." if negativo else " lo recordará.")
        renpy.show_screen("aviso_recuerda", msg, "#ff6b6b" if negativo else "#ffd700")

    def rel_delta(quien, puntos):
        # Cambio de relación sin notificación (para combos).
        store.rel[quien] = store.rel.get(quien, 0) + puntos

    def estado(quien):
        # Texto de cómo anda la relación con alguien.
        v = store.rel.get(quien, 0)
        if v >= 3:
            return "te adora"
        if v >= 1:
            return "te aprecia"
        if v == 0:
            return "neutral"
        if v >= -2:
            return "te tiene mala"
        return "te odia (con cariño)"

    def queja_marcelo():
        # Primera queja del día de Marcelo: varía cada partida
        # y SIEMPRE combina con el clima del prólogo.
        universales = [
            "Qué lata. Es lunes. Siempre es lunes.",
            "Qué lata. No venden té. Nunca venden té.",
            "Qué lata. El wifi. Siempre el wifi.",
            "Qué lata. Todo. En general. Todo.",
        ]
        por_clima = {
            "lluvia": ["Qué lata. Está lloviendo. Siempre llueve.",
                       "Qué lata. Otra vez lluvia. Como siempre."],
            "frio": ["Qué lata. Este frío seco. Pela.",
                     "Qué lata. El frío. Aunque digan que no hace."],
            "sol": ["Qué lata. Sol en invierno. Sospechoso.",
                    "Qué lata. Calienta el sol y sigue el frío igual."],
            "nublado": ["Qué lata. Nublado. Ni frío ni calor. Fome."],
        }
        lista = universales + por_clima.get(store.clima, [])
        return renpy.random.choice(lista)

    def cumbia_del_dia():
        # La cumbia villera que pone Fabián hoy.
        return renpy.random.choice([
            "Supermerk2", "Damas Gratis", "Yerba Brava",
        ])

    def clima_hub():
        # El clima de Temuco hoy (varía cada vez que vuelves al hub).
        return renpy.random.choice([
            "Día de lluvia en el INACAP. Lo normal.",
            "Día de frío seco. Se te pelan los labios.",
            "Día de sol sospechoso. Todos desconfían.",
            "Día nublado. Ni frío ni calor. Fome.",
            "Día de viento. El Megaficticias lo llamó «brisa». Miente.",
        ])

    def frag():
        # Suma un fragmento de la historia de Shakira a la grabadora.
        store.fragmentos += 1
        renpy.show_screen("aviso_recuerda", "Fragmento grabado (" + str(store.fragmentos) + " de 5)")

    def whatif(msg):
        # Notificación de misión WHAT IF disponible.
        renpy.show_screen("aviso_whatif", msg)

# Sprites reales
image jose     = sprite("images/jose.png")
image jose gym = sprite("images/jose gym.png")
image pablo    = sprite("images/pablo cuerpo completo.png")
image pablo shell = sprite("images/pablo shell.png")
image diego    = sprite("images/diego.png")
image fabian   = sprite("images/fabian.png")
image marcelo  = sprite("images/marcelo.png")
image benjamin = sprite("images/benjamin.png")
image bastian  = sprite("images/bastian.png")
image ruben    = sprite("images/ruben.png")
image maxi     = sprite("images/maxi.png")
image ivan     = sprite("images/ivan.png")
image martin   = sprite("images/martin.png")
image hector   = sprite("images/hector.png")
image shakira  = sprite("images/shakira.png")
image jeep     = sprite("images/jeep.png", alto=620)
image perro1   = sprite("images/perro1.png", alto=500)
image perro2   = sprite("images/perro2.png", alto=500)

image inacapini = sprite("images/inacapini.png")

# Fondos reales (escalados con cover: llenan la pantalla, recorte centrado)
image bg inacap = cover("images/bg inacap.webp")
image bg inacap_lluvia = cover("images/bg inacap_lluvia.jpeg")
image bg patio = cover("images/bg patio.webp")
image bg inacap_dentro = cover("images/bg inacap_dentro.webp")
image bg shell = cover("images/bg shell.png")
image bg jumbo = cover("images/bg jumbo.jpeg")
image bg jumbo_pasillo = cover("images/bg jumbo_pasillo.webp")
image bg potrero = cover("images/bg potrero.png")
image bg liceo = cover("images/bg liceo.jpeg")
image bg sala_liceo = cover("images/bg sala_liceo.jpg")
image bg sueno = cover("images/bg sueno.png")
image bg camino = cover("images/bg camino.jpeg")
image bg pedro = cover("images/bg pedro.png")

image escena pablo_lluvia = cover("images/escena pablo_lluvia.jpeg")
image escena ruben_banca = cover("images/escena ruben_banca.jpeg")
image escena cerca_desayuno = cover("images/escena cerca_desayuno.png")
image escena cumple = cover("images/escena cumple.png")
image escena atardecer_cerca = cover("images/escena atardecer_cerca.png")
image escena venta_camioneta = cover("images/escena venta_camioneta.png")
image escena short = Transform("images/escena short.png", zoom=1.4)

# Fondo del menú principal
image menu_bg = cover("images/menu.jpg")

# Video de fondo: Pillalelbún inundado (sin sonido)
image bg inundado = Movie(play="images/bg inundado.mp4", loop=True, audio=False, size=(1920, 1080))

# Fondos (borra cada línea cuando tengas la imagen real)
image bg fundo    = fondo("Fundo El Carmen",     "#4a5d23")
image bg funeral  = fondo("Funeral de Shakira",  "#1b1b1b")
image bg atardecer = fondo("Atardecer en Lincoñir", "#c0662b")

# Ángulos / momentos específicos (borra cada línea cuando tengas la imagen real)
image bg cisterna_patio = fondo("La cisterna de Pablo (4 km/h)", "#8b4a0b")
image bg cisterna_int = fondo("Interior de la cisterna", "#6d4c41")
image bg shell_ruinas = fondo("La Shell destruida", "#5d4037")
image bg pesebre  = fondo("El pesebre: heno fresco", "#8a9a45")
image bg asado    = fondo("Asado en el Fundo El Carmen", "#8f3b1b")

# Escenas compuestas / planos específicos (borra cada línea cuando tengas el arte)
image escena cisterna_pablo = escena("Pablo piloteando la cisterna como F1 (a 4 km/h)", "#8b4a0b")
image escena choque = escena("La cisterna besa la Shell. Cámara lenta. 3 km/h.", "#5d4037")
image escena martin_clase = escena("El profe Martín y la palabra HUAWEI en la pizarra", "#1a5276")
image escena asado = escena("El asado del Fundo El Carmen, todos presentes", "#8f3b1b")
image escena sueno_ruta = escena("Pablo corta la cinta de la Ruta de la Zanahoria", "#f0c94e")


# ---------------------------------------------------------------------
#  Aviso grande de consecuencias ("X lo recordará", fragmentos)
# ---------------------------------------------------------------------
transform recuerda_appear:
    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0

screen aviso_recuerda(msg, color="#ffd700"):
    zorder 200
    frame:
        xalign 0.5
        yalign 0.08
        background "#000000cc"
        padding (40, 20)
        at recuerda_appear
        text msg:
            size 44
            color color
            outlines [(3, "#000000", 0, 0)]
            xalign 0.5
    timer 5.0 action Hide("aviso_recuerda", dissolve)

screen aviso_whatif(msg):
    zorder 200
    frame:
        xalign 0.5
        yalign 0.08
        background "#3d1a5ecc"
        padding (40, 20)
        at recuerda_appear
        text ("⚡ WHAT IF ⚡\n" + msg):
            size 40
            color "#e1b3ff"
            outlines [(3, "#000000", 0, 0)]
            xalign 0.5
    timer 5.0 action Hide("aviso_whatif", dissolve)


# =====================================================================
#  PRESENTACIÓN (aparece antes del menú principal)
# =====================================================================
label splashscreen:

    scene black
    $ renpy.pause(0.5)

    show text "SeguelStudios presenta" at truecenter with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve
    $ renpy.pause(0.4)

    show text "{size=150}{b}RADAL{/b}{/size}" at truecenter with dissolve
    $ renpy.pause(1.8)

    show text "{size=150}{b}RADAL{/b}{/size}\n{size=50}la novela gráfica{/size}" at truecenter with dissolve
    $ renpy.pause(2.2)
    hide text with dissolve
    $ renpy.pause(0.4)

    return


# =====================================================================
#  PRÓLOGO
# =====================================================================
label start:

    $ musica("tema.ogg")
    scene black with fade

    "Basada en hechos reales."
    "Radal: José Lipian, la novela gráfica."

    python:
        nombre = renpy.input("¿Cómo te llamas?", length=18)
        nombre = nombre.strip()
        if not nombre:
            nombre = "Kabro"

    # Cada partida comienza con uno de los 5 prólogos.
    $ prologo = renpy.random.randint(1, 5)

    if prologo == 1:
        jump prologo_lluvia
    elif prologo == 2:
        jump prologo_frio
    elif prologo == 3:
        jump prologo_sol
    elif prologo == 4:
        jump prologo_tarde
    else:
        jump prologo_temprano


# ---------------------------------------------------------------------
#  Encuentros reutilizables (seguros: solo contenido del presente)
# ---------------------------------------------------------------------
label encuentro_pablo:

    show pablo at right with dissolve

    show escena short at center with dissolve
    mc "(¿Eso es... un short?)"
    hide escena short with dissolve

    pablo "Buenos días."

    menu:
        "Oye, ¿no tienes frío?":
            $ pablo_molesto = True
            $ recuerda("Pablo", negativo=True)
            pablo "¿Frío? No sé de qué me hablas."
            "Sus piernas, azules, opinan distinto."
        "Bacán tus gafas.":
            $ recuerda("Pablo")
            pablo "Lo sé."
            pablo "Me veo como Brad Pitt con ellas."
            "No se parece a Brad Pitt. Nadie se lo ha dicho. Nadie se lo dirá jamás."
            "Se nota que está cagado de frío. Se hace el bacán, el Pablo."
        "No decir nada y seguir caminando.":
            "Decides no hacer preguntas. Es lo más sabio que harás en todo el semestre."

    return


label quejas_marcelo:

    show marcelo at left with dissolve
    marcelo "[queja_marcelo()]"
    marcelo "Pucha que hace frío. Aparte no me gusta el café, y es lo único que venden en el INACAP. Yo prefiero el tecito."
    marcelo "Y aparte no dormí nada y vine temprano para acá. Qué lata todo el asunto."
    mc "(Recién lo conozco y ya se quejó de seis cosas distintas. Récord.)"

    menu:
        "Ánimo, Marcelo. Algo bueno debe tener el lunes.":
            $ apoyo += 1
            $ recuerda("Marcelo")
            marcelo "No. No tiene. Qué lata tu optimismo."
        "Tienes razón. Todo es una lata.":
            $ drama += 1
            $ recuerda("Marcelo", "Marcelo aprueba tu pesimismo.")
            marcelo "Por fin alguien sensato. Qué lata, pero sensato."

    return


# ---------------------------------------------------------------------
#  PRÓLOGO 1: LA LLUVIA
# ---------------------------------------------------------------------
label prologo_lluvia:

    $ clima = "lluvia"
    scene bg inacap_lluvia with fade
    "Temuco. Lunes. 7:55 de la mañana."
    "Llueve. Hace tanto frío que los termómetros piden perdón. Según el Megaficticias, estamos a menos treinta grados."
    "Y tú eres el nuevo."
    "El nuevo del INACAP: el instituto de tecnologías de Temuco. Parte universidad, parte instituto. Nadie tiene claro la diferencia. Todos fingen que sí."
    mc "Me llamo [nombre]. Primer día en el INACAP. Frío. Mucho frío."

    scene escena pablo_lluvia with dissolve
    "Entre la lluvia avanza un joven con paso firme. Short corto. Gafas de sol. Cero abrigo."

    scene bg inacap_lluvia with dissolve
    $ bg_prologo = "bg inacap_lluvia"
    call encuentro_pablo
    call quejas_marcelo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRÓLOGO 2: FRÍO SECO
# ---------------------------------------------------------------------
label prologo_frio:

    $ clima = "frio"
    scene bg inacap with fade
    "Temuco. Lunes. 7:55 de la mañana."
    "No llueve. Peor: hace un frío seco que pela la cara. El Megaficticias lo llamó «fresco». Miente."
    "Y tú eres el nuevo del INACAP: el instituto de tecnologías de Temuco. Parte universidad, parte instituto. Nadie tiene claro la diferencia."
    mc "Me llamo [nombre]. Primer día. Frío seco. Se me congelan las ideas."

    call quejas_marcelo
    "Y entonces, desafiando el frío seco, aparece un joven en short corto y gafas de sol."
    $ bg_prologo = "bg inacap"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRÓLOGO 3: SOL SOSPECHOSO
# ---------------------------------------------------------------------
label prologo_sol:

    $ clima = "sol"
    scene bg inacap with fade
    "Temuco. Lunes. 7:55 de la mañana. Sale el sol. En Temuco. En invierno."
    "Todos miran el cielo con sospecha. Esto no es normal. Esto nunca es normal."
    "Y tú eres el nuevo del INACAP: el instituto de tecnologías de Temuco. Parte universidad, parte instituto. Nadie tiene claro la diferencia."
    "El grupo te ve llegar. Te miran como espécimen. Nadie dice nada todavía."

    call quejas_marcelo
    "Con el sol afuera, un joven en short y gafas de sol se acerca con la satisfacción del que tenía razón."
    pablo "Se los dije. El short siempre fue la respuesta."
    $ bg_prologo = "bg inacap"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRÓLOGO 4: LLEGAS TARDE
# ---------------------------------------------------------------------
label prologo_tarde:

    $ clima = "nublado"
    scene bg inacap with fade
    "Temuco. Lunes. 8:47 de la mañana. Llegas tarde. El primer día. Excelente comienzo."
    "La clase ya empezó. Entras piola y buscas un puesto libre."

    show bastian at center with dissolve
    "Un muchacho de complexión de gimnasio te señala uno. En silencio."
    mc "(¿Ese?)"
    "Asiente."
    bastian "Sí."
    "Es lo primero que te dice alguien en este instituto. Un sí. Prometedor."
    "Sobrevives a la primera clase. No entendiste nada. Según el Megaficticias, eso también es normal."

    scene bg patio with fade
    "A la salida, el grupo te recibe como se recibe a un espécimen nuevo."
    call quejas_marcelo
    "Y entre la gente, un joven en short corto y gafas de sol te saluda como si te conociera de siempre."
    $ bg_prologo = "bg patio"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRÓLOGO 5: LLEGAS TEMPRANO
# ---------------------------------------------------------------------
label prologo_temprano:

    $ clima = "frio"
    scene bg patio with fade
    "Temuco. Lunes. 7:12 de la mañana. Llegaste tan temprano que el patio está vacío. Error de novato."
    "Lo único presente: un muchacho escuchando cumbia villera a todo volumen y una jauría de galgos."
    show fabian at center with dissolve
    show perro1 at left with dissolve
    show perro2 at right with dissolve
    fabian "Wn. ¿Nuevo? Aguante el Colo."
    fabian "Y estos son los Intratables. Los traje de Pillalelbún a dar una vuelta. Salen a la calle y se devuelven solos."
    fabian "El más chico es Zeus Black II."
    mc "Me llamo [nombre]. Llegué muy temprano, ¿cierto?"
    fabian "Tempranísimo, wn. Ni los galgos estaban despiertos."
    $ v_fabian_intro = True

    call quejas_marcelo
    "A las 7:55, con el Megaficticias anunciando menos treinta grados, aparece un joven en short corto y gafas de sol."
    $ bg_prologo = "bg patio"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRESENTACIÓN DEL GRUPO (común a todos los prólogos)
# ---------------------------------------------------------------------
label intro_grupo:

    show diego at center with dissolve

    diego "Ojo, nuevo: yo salgo directo al Jumbo del Portal después de clases, a la sección Hasbro. Estoy juntando plata para un computador."
    mc "¿Por qué tan específico?"
    diego "Mi gato me meó la laptop Junaeb. Esa es la historia. No hay más."

    menu:
        "¿Y el gato? ¿Sigue suelto?":
            diego "Suelto y con poderes. Manda en la casa. Yo pago el arriendo, él manda."
            $ recuerda("Diego")
        "Cómprale un teclado al gato. Para que aprenda.":
            $ drama += 1
            diego "¿Pa que mee el teclado también? No, po."
            "El gato, en efecto, sigue suelto. Y manda."

    if not v_fabian_intro:
        show fabian at left with dissolve
        fabian "Y yo soy Fabián. De Pillalelbún. Aguante el Colo Colo."
    show fabian at left
    "Fabián levanta el celular. Suena [cumbia_del_dia()]. En Temuco nadie escucha cumbia villera. A Fabián le da lo mismo."

    hide diego
    hide fabian
    show bastian at left with dissolve

    "Al fondo, un muchacho de complexión de gimnasio saluda con la mano. No dice ni una palabra."
    "Se acerca otro muchacho a presentarlo. Este sí habla. Mucho."

    show benjamin at center with dissolve

    benjamin "Ese es Bastián Poblete. De General López. El Pachoclo."
    mc "¿El qué?"
    benjamin "Pachoclo. Por los memes de Pachoclo. A veces Patroclo, según el meme del día. Ese es el Bastián."
    bastian "..."
    "Es tímido. Habla poco. O nada. Y cuando habla, es para decir que sí. A todo. Aunque sea mala idea."
    "Además va al gym. Carga cosas por la gente. Gratis. Un santo con músculos."

    benjamin "Dato clave: Bastián dice sí a todo. A TODO. Pruébalo."

    menu:
        "Bastián, ¿me prestai cien lucas?":
            bastian "Sí."
            benjamin "¿Viste? Aunque sea mala idea. Aunque no te conozca."
            mc "(Acabo de ganar cien lucas.)"
            $ recuerda("Bastián", "Bastián dijo que sí. Como siempre.")
        "Bastián, ¿te caigo bien?":
            bastian "..."
            benjamin "Cuando no habla es que está pensando si decir sí."
            bastian "Sí."
            benjamin "¿Viste? Siempre sí."
            $ recuerda("Bastián", "Bastián dijo que sí. Como siempre.")
    benjamin "Y yo Benjamín. Vengo de la nación de Fundo El Carmen."
    mc "¿La nación?"
    benjamin "Fundo El Carmen. Está en Temuco, técnicamente. Pero económicamente... es otra cosa. Se ve mejor. Más nuevo. Prácticamente otro país."
    benjamin "Nosotros no decimos «voy a Temuco». Decimos «voy al extranjero»."
    show marcelo at left with dissolve
    marcelo "Qué lata. Nadie dice eso. Solo él. Siempre él."
    benjamin "Y siempre tendré la razón."

    menu:
        "¿Y qué moneda usan en la nación Fundo El Carmen?":
            benjamin "El carmeno. Vale más que el peso. El doble. Lo decidí yo."
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu interés diplomático.")
        "Eso es lo más clasista que he escuchado.":
            benjamin "Gracias. Se nota el esfuerzo."
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín se siente halagado. Preocupante.")
    benjamin "Oye, nuevo. ¿Ya te contaron lo de Shakira? Porque si no te lo han contado, yo lo cuento. CON GUSTO lo cuento."

    "Datos del grupo, para que no te pierdas: José, Pablo, Diego y Bastián son de Telecomunicaciones. Benjamín y Marcelo, de Ingeniería en Ciberseguridad. Fabián también está en ciberseguridad... de momento."
    "Marcelo y Diego son de Pueblo Nuevo mismo, como el liceo. Los demás llegaron de todas partes."
    "Y lo más importante: todos se conocen del Liceo Politécnico de Pueblo Nuevo. Todos. Menos tú."
    mc "(Llegué tarde hasta para el pasado.)"

    show diego at right with dissolve
    "A Diego le llega un WhatsApp. Lo lee en voz alta, porque Diego es así."
    diego "«Diego. Me inscribí en el ejército. Me voy a Lonquimay. Cuídate, culiao.»"
    "Diego responde con un sticker. Todos lo miran."
    diego "El Nico Jara. Del liceo. Se inscribió en el ejército. Se va a Lonquimay."
    marcelo "Se fue antes de que empezaran las clases. Y se despide por WhatsApp. No, qué poco simpático."
    benjamin "Mientras Iván Garrido esquivaba la milicia con un certificado de alumno regular (un PDF, pa que se entienda), el Nico Jara se inscribió voluntario. Dos estrategias. Dos leyendas."

    menu:
        "¿Tan terrible es la milicia?":
            diego "El llamado del ejército. Te pueden llamar a los 18. Hay que sacárselo como sea."
            marcelo "Qué lata el llamado. Qué lata todo lo que empieza con «llamado»."
        "Bastante normal el Nico, ¿no?":
            benjamin "El más normal del liceo. Por eso nadie habla de él. Es su superpoder."
    benjamin "Aunque hablando de inscripciones al ejército, nadie tiene más historia que Diego."
    diego "No saquemos ese tema."
    marcelo "Diego también se inscribió. Lo rechazaron. Oye, no, qué mal."
    mc "¿Por qué lo rechazaron?"
    benjamin "Contestó mal dos o tres preguntas. Y en el test psicológico dijo que actuaría «como en Free Fire»."
    diego "Es que era una respuesta VÁLIDA."
    benjamin "Por eso Diego va en primer año y nosotros en segundo. Perdió un año entero por el Free Fire."
    diego "NO fue culpa del Free Fire. Fue culpa del sicólogo. No tenía criterio."

    if clima == "lluvia":
        scene escena ruben_banca with dissolve
        "Al lado de la entrada, en una banca, yace un joven bajo la lluvia. No se mueve. Ni la lluvia lo mueve."
        scene bg inacap_lluvia with dissolve
    else:
        "Al lado de la entrada, en una banca, yace un joven. No se mueve. Ni el frío lo mueve."
        scene bg inacap with dissolve

    show ruben at center with dissolve
    "Ese es Rubén Maldonado. De Pillalelbún. Está en ciberseguridad con Benjamín y Marcelo."
    ruben "¿Y a ti qué te importa?"
    mc "Todavía no digo nada."
    ruben "Por si acaso. Chao, chiquillos."
    hide ruben with dissolve
    "No se fue. Dijo «chao» por compromiso. Moverse ya era demasiado esfuerzo."

    show diego at left with dissolve
    show pablo at right with dissolve
    diego "Oye, Pablo. Pa que el nuevo se ponga al día..."
    "Se miran entre ellos. Respiran hondo. Y gritan:"
    diego "¿EN QUÉ TE GASTASTE LOS DOS MILLONES?"
    pablo "En puras leceras."
    "Es la misma respuesta de siempre. Nadie la cree. Nadie la entiende. Todos la repiten."
    mc "¿Dos millones?"
    diego "Del casino online. Los ganó. Y se evaporaron."

    show marcelo at left with dissolve
    marcelo "Hablando de cosas importantes... cuéntenle de Shakira. Bucha."
    mc "¿Quién es Shakira?"
    "Silencio. El Supermerk2 se apaga solo."

    show benjamin at center with dissolve
    benjamin "No es una «quién». Es LA yegua de José."
    show diego at right with dissolve
    diego "Se llama Shakira. Sí. Shakira."
    marcelo "Le puso Shakira por la cantante. Por LA Shakira. Esa misma."
    show fabian at center with dissolve
    fabian "La quiere harto. Demasiado, diría yo."
    show benjamin at right with dissolve
    benjamin "Y la sube al Facebook. Sube fotos de su yegua al Facebook. Como quien sube fotos de su hijo."
    mc "¿Y eso es malo? Suena... sano."
    benjamin "Ese es el problema. Es DEMASIADO sano. Interesante... MUY interesante."

    scene bg inacap with fade
    show diego at left with dissolve
    show pablo at right with dissolve
    show benjamin at center with dissolve

    hide benjamin
    show jose at center with dissolve

    jose "¿Están hablando de Shakira?"
    jose "Es mi yegua. La crié de bebé, desde que me la dieron. ¿Algún problema?"
    show benjamin at left with dissolve
    benjamin "Ninguno, José. Ninguno. Eso es lo que nos preocupa."

    show bastian at left with dissolve
    "José se gira hacia Bastián, que está ahí. Siempre está ahí."
    jose "Tú me entiendes, ¿cierto, Bastián?"
    bastian "..."
    jose "Dice que sí."
    "Bastián asiente con la cabeza. José asiente de vuelta. Comunicación total."
    show benjamin at left with dissolve
    benjamin "José es el único que le habla a Bastián. Por eso Bastián solo le habla a José. Un ecosistema perfecto."
    show diego at left with dissolve

    diego "Y no le hagan mucho caso a José: desde que se metió al Elysium se cree mejor que todos."
    jose "Se dice gimnasio. Y sí, voy. Alguien en este grupo tiene que cuidarse."
    show benjamin at left with dissolve
    benjamin "Se le suben los humos. Llega con polera de entrenamiento. Sube historias en el espejo."
    jose "Es que claro, es disciplina. Ustedes no le saben."
    benjamin "Y Diego también se metió al Elysium, ¿cachai? Lo paga todos los meses."
    benjamin "No va nunca."
    show diego at left with dissolve
    diego "Iba harto antes. Ahora estoy ocupado."
    show marcelo at left with dissolve
    marcelo "Ocupado haciendo streams de Free Fire en TikTok. Qué lata."
    show benjamin at left with dissolve
    benjamin "Se hace llamar «Ryu». Y a la gente le dice «cabezón»."
    show diego at left with dissolve
    diego "Es que así se saluda en los lives. «¿Cabezón, cómo estai?». Es mi marca."

    "Todos miran a [nombre]. Es tu momento de hablar."

    menu:
        "Se nota que la quiere harto, po.":
            $ apoyo += 1
            $ recuerda("José")
            jose "Gracias, po. Al fin alguien con criterio."
            show benjamin at left with dissolve
            benjamin "No le fomente. NO le fomente."
        "¿Le celebras el cumpleaños a una yegua?":
            $ drama += 1
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu falta de respeto.")
            jose "Con torta de zanahoria. ¿Algún problema?"
            "No tiene ningún problema. Eso es lo preocupante."
        "Tengo que conocer a Shakira. Ya.":
            $ apoyo += 1
            $ recuerda("José")
            jose "Cuando quieras. Lincoñir queda cerca. Te la presento."
            show benjamin at left with dissolve
            benjamin "Todos caen. Todos terminan queriendo conocer a la yegua."

    show benjamin at left with dissolve
    "Mientras José habla de ella, Benjamín se acerca y te susurra:"
    benjamin "(bajito) Lo único raro: pregúntale cuánto vale la yegua."

    menu:
        "Preguntarle el precio (como dice Benjamín).":
            mc "Oye, José... ¿cuánto vale Shakira?"
            jose "Yo creo que la vendería por un palo. Por ahí, un millón de pesos. En eso están los caballos. Depende igual."
            "Lo dice AL TOQUE. Sin pensarlo. Como si lo tuviera calculado."
            benjamin "(bajito) ¿Viste? ¿VISTE?"
        "No preguntar. Se siente raro.":
            "Decides no preguntar. Benjamín no aguanta y pregunta él."
            benjamin "José, ¿cuánto vale Shakira?"
            jose "Yo creo que la vendería por un palo. Por ahí, un millón de pesos. En eso están los caballos. Depende igual."
            "Lo dice AL TOQUE. Sin pensarlo. Como si lo tuviera calculado."
            benjamin "(bajito) ¿VISTE? Te dije. Yo siempre tengo razón."

    benjamin "Ah. Y otra cosa, nuevo. Fúnalo. Grábalo al culiao con el celular. Todo. No se te escape nada."
    "Sacas tu celular. Grabadora de voz: cero archivos. Por ahora."
    $ recuerda("Grabadora", "Grabadora lista. Fragmentos: 0 de 5.")

    pablo "Yo tengo turno en la Shell de Lautaro, camino a Pillalelbún. Trabajo part time: solo sábados y domingos. Esos días, ahí estoy."
    "Y así comienza tu primer semestre. Todavía nadie sabe que este año quedará en la historia del grupo."

    jump hub


# =====================================================================
#  CENTRAL DE INVESTIGACIÓN
# =====================================================================
label hub:

    scene bg inacap_dentro with fade
    "[clima_hub()]"
    $ lugares = int(v_patio) + int(v_shell) + int(v_jumbo) + int(v_potrero) + int(v_liceo)

    # Tras la tercera visita a Lincoñir, llega el día que nadie quería.
    if potrero_visitas >= 3 and not venta:
        jump la_venta

    # Tras la venta, se activan los WHAT IF.
    if venta and not whatif_tinder_activo and not v_tinder:
        $ whatif_tinder_activo = True
        $ whatif("Cupido de alquiler: habla con Marcelo en el patio.")
    elif venta and whatif_tinder_activo and not whatif_trabajo_activo and not v_trabajo:
        $ whatif_trabajo_activo = True
        $ whatif("El trabajo en grupo: sobrevive al proyecto de a tres.")
    elif venta and v_pelea_inacapini and not whatif_inacapini_activo and not v_inacapini:
        $ whatif_inacapini_activo = True
        $ whatif("El sospechoso azul: investiga al Inacapini con Benjamín.")

    # Eventos que suceden solos, en distinto orden cada partida.
    # (Cada uno solo aparece cuando ya tienes el contexto para entenderlo.)
    python:
        eventos = []
        if lugares >= 2 and not v_fabian_sale:
            eventos.append("fabian_se_va")
        if lugares >= 3 and not v_inundacion:
            eventos.append("inundacion")
        if venta and lugares >= 2 and not v_ruben:
            eventos.append("encuentro_ruben")
        if lugares >= 2 and not v_pelea_inacapini:
            eventos.append("pelea_inacapini")
        if pablo_arruinado and not v_juicio_shell:
            eventos.append("juicio_shell")
        if v_patio and lugares >= 4 and not v_conflicto_marcelo:
            eventos.append("conflicto_marcelo")
        if v_ruben and not v_conflicto_ruben:
            eventos.append("conflicto_ruben")
        if eventos:
            renpy.jump(renpy.random.choice(eventos))

    menu:
        "¿Adónde vas ahora?"

        "Patio del INACAP (Pablo, Marcelo y Benjamín)" if not v_patio:
            jump patio
        "Shell de Lautaro, en Pillalelbún (Pablo y Fabián)" if not v_shell:
            jump shell
        "Jumbo del Portal (Diego)" if not v_jumbo:
            jump jumbo
        "Viaje a Lincoñir, Padre Las Casas (visita [potrero_visitas + 1] de 3)" if not venta and potrero_visitas < 3:
            jump potrero_visita
        "Volver a Lincoñir (el potrero vacío)" if venta and not v_potrero:
            jump potrero
        "Liceo Politécnico de Pueblo Nuevo (todos se conocen ahí... menos tú)" if not v_liceo:
            jump liceo
        "Volver a la Shell (Pablo anda raro)" if v_shell and not v_sueno:
            jump sueno_pablo
        "⚡ WHAT IF: Cupido de alquiler (Marcelo, patio)" if whatif_tinder_activo and not v_tinder:
            jump whatif_tinder
        "⚡ WHAT IF: El trabajo en grupo (Marcelo, Benjamín y Rubén)" if whatif_trabajo_activo and not v_trabajo:
            jump whatif_trabajo
        "⚡ WHAT IF: El sospechoso azul (Benjamín y el Inacapini)" if whatif_inacapini_activo and not v_inacapini:
            jump whatif_inacapini
        "Escuchar la grabadora ([fragmentos] de 5 fragmentos)":
            if fragmentos == 0:
                "Reproduces la grabadora. Silencio. Ni un fragmento. Aprietas stop, avergonzado."
            elif fragmentos >= 4:
                "Escuchas los fragmentos en orden. Voces de todos. Ya casi se arma la historia entera. Casi."
            else:
                "Escuchas los fragmentos sueltos. Voces de todos. Pedazos sueltos que todavía no se arman."
            jump hub
        "Ver cómo anda el grupo contigo":
            jump estado_relaciones
        "Ya tengo suficiente. Hora de confrontar a José." if venta and lugares >= 3:
            jump confrontacion


# =====================================================================
#  PATIO DEL INACAP
# =====================================================================
label patio:

    $ v_patio = True
    scene bg patio with fade
    show pablo at right with dissolve
    show marcelo at left with dissolve
    show benjamin at center with dissolve

    pablo "Otra vez tú con las preguntas."
    benjamin "Déjalo, Pablo. El nuevo tiene derecho a saber. Yo también quiero saber. Yo NUNCA dejo de querer saber."
    mc "Pablo, ¿en qué te gastaste los dos millones?"
    pablo "En puras leceras."

    menu:
        "Dame una lecera concreta.":
            pablo "Una cosa grande. De cuatro... esteee... de cuatro cuotas. Sí. Cuotas. Muchas cuotas."
            if venta:
                "Pablo transpira. Y estamos a menos treinta grados."
                mc "(Algo no cuadra...)"
                $ pista_pablo = True
            else:
                "Probablemente sea el computador que se compró. O las gafas. Con Pablo nunca se sabe."
        "Qué raro, gafas de sol bajo la lluvia.":
            $ drama += 1
            $ recuerda("Pablo", negativo=True)
            pablo "Brad Pitt no le tiene miedo a la lluvia."
            "Se aleja con dignidad. Con muchísima dignidad. Y con frío."
            hide pablo with dissolve

    marcelo "Bucha. Pablo desaparece todos los domingos y nadie pregunta. Bucha la lecera."
    marcelo "Y además la cafetería no tiene té. Nunca tiene té. Na, pero justo ahora."

    benjamin "Hablando de desapariciones... ¿ya le contaste de tu Instagram, Marcelo?"
    marcelo "Oye, no. No me lo recuerdes. Me borraron el Instagram. Noventa mil seguidores. NOVENTA MIL. A la basura."
    mc "¿Por qué te lo borraron?"
    marcelo "Subía clips de fútbol. Derechos de autor. Aaah qué lata los derechos de autor."
    benjamin "Noventa mil personas viendo clips robados. Una pérdida cultural."
    benjamin "Pero le queda el TikTok. premierchilito. Ciento cuarenta y un mil seguidores de puro fútbol chileno."
    marcelo "Es una página seria. Qué lata que no la conozcas."

    menu:
        "Dale, ahí te sigo. Suena bacán.":
            $ promesa_marcelo = True
            $ apoyo += 1
            $ recuerda("Marcelo")
            marcelo "Qué lata... gracias."
        "¿Fútbol chileno? ¿Y eso existe?":
            $ drama += 1
            $ recuerda("Marcelo", "Marcelo NO lo olvidará. Con rencor.", negativo=True)
            marcelo "Qué lata. Qué lata. QUÉ LATA."

    benjamin "Y hablando de cosas que no supero: lo de Shakira. Yo no lo supero. Cada noche lo pienso."
    marcelo "Ayer te escuché reírte del tema."
    benjamin "Río para no llorar."

    menu:
        "Tienes razón, Benjamín. Esto es una tragedia griega.":
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu sentido del drama.")
            benjamin "¡POR FIN! ¡Alguien con criterio en este INACAP!"
        "Benjamín, ayer dijiste que fue 'un buen negocio'.":
            $ drama += 1
            benjamin "Contexto. Todo es contexto. Fue un momento de debilidad."

    benjamin "Oye, Marcelo. A mí me gustaría tener un manatí."
    marcelo "Oye, sí. Estaría bacán."
    "Pausa."
    marcelo "Pero no se puede. En Chile no hay. Bucha. Qué lata este país sin manatíes."
    benjamin "En Fundo El Carmen sí se podría. Es otra nación."
    marcelo "Qué lata. Otra vez con la nación."

    jump hub


# =====================================================================
#  SHELL DE PILLALELBÚN
# =====================================================================
label shell:

    $ v_shell = True
    $ musica("cumbia.ogg")
    scene bg shell with fade
    show pablo shell at center with dissolve

    "Shell de Lautaro, camino a Pillalelbún. Aquí trabaja Pablo, bombero de bencina: el que maneja y trae los tanques de cisterna."
    pablo "Bienvenido a mi reino. Aquí mando yo."

    if pablo_molesto:
        pablo "Aunque tú... tú preguntaste si tenía frío. Eso no se le pregunta a nadie."
        menu:
            "Perdón, Pablo. La lluvia habló por mí.":
                $ apoyo += 1
                $ recuerda("Pablo")
                pablo "Acepto tus disculpas. El short también."
            "Y lo repito: ¿no tienes frío?":
                $ drama += 1
                $ recuerda("Pablo", "Pablo NO lo olvidará. Con las piernas azules.", negativo=True)
                pablo "..."

    scene escena cisterna_pablo with dissolve
    show pablo at center with dissolve

    "Pablo se sube a la cisterna y la recorre por el patio. Lento. Muy lento. Pero con cara de estar en una película."
    pablo "Me toca cargar cisternas de cincuenta litros. Con respeto, eso sí."
    pablo "Ayer arreglé un tablero de fusión trifásico para salvar la Shell. Pa que no se cayera el letrero."
    pablo "Y hoy, adivina: el letrero se cayó de todas formas. Loco nefasto."
    mc "Va como a cuatro por hora."
    pablo "Es la velocidad de los profesionales."

    scene bg shell with dissolve
    show pablo shell at center with dissolve
    show fabian at left with dissolve
    fabian "Qué onda. Bienvenido a Pillalelbún."
    "Fabián pone a Damas Gratis en la bomba de bencina. El petróleo, por respeto, no se mueve."
    fabian "Aguanten las milanesas, por cierto."
    mc "¿Por qué?"
    fabian "¿Y por qué no?"
    fabian "¿Y cómo está mi panita Benjamín? Los dos somos del Colo, ¿viste? Aguante el Colo."
    if v_fabian_sale:
        mc "¿Y la pega, Fabián? ¿Llamaron del Tecnobox?"
        fabian "Nada, wn. «Te llamamos», me dijeron. Hasta hoy espero."
        fabian "Pero tranqui: la cumbia y mi polola me tienen ocupado."
    else:
        mc "Fabián, ¿tú no estudias con ellos?"
        fabian "Sí, po. Ciberseguridad. De momento."
        "Ese «de momento» sonó raro. Nadie le dio importancia. Debieron."
    fabian "Y acá en Pillalelbún se junta el mundo. Mi casa es la sede oficial."
    fabian "Lo más raro: Maxi y Benjamín viven al lado. AL LADO. Y solo se juntan acá. Ni ellos lo entienden."

    "Una jauría de galgos cruza corriendo por el patio. Van como cinco. Parecen manada de comercial."
    fabian "Mis perros son brigidos. Pertenecen a un grupo: los Intratables. Salen a la calle y se devuelven solos."
    fabian "Tenía uno que se llamaba Zeus Black. Negro como la noche. Dormía donde quería, el loco."
    fabian "Un día se quedó dormido detrás de la rueda de un auto..."
    "Silencio. Fabián mira al suelo. Damas Gratis sigue sonando, pero más bajito, como por respeto."
    fabian "F. Zeus Black. El más intratable de todos."
    mc "..."
    fabian "Ya po. No lloremos. Zeus Black no querría eso. Zeus Black querría cumbia villera."
    "Fabián le sube el volumen. Los Intratables aúllan al ritmo. Probablemente."

    "Y en el techo de la tienda, una gata blanca con naranja mira a todos con desprecio."
    fabian "Esa es la Pequi. No es de ningún grupo. Ella tiene su propio grupo. Ella es la líder."

    mc "¿Y quién más cae a las juntas?"
    fabian "Maxi siempre. El Iván Garrido del 4F, nunca. Ese loco no ha pisado Pillalelbún en su vida."
    fabian "Pero en las juntadas de allá está presente el guatoncito. Leyenda, el Iván. Fue al INACAP una pura vez. UNA. Esa historia te la tienen que contar bien."
    fabian "Lo que sí te cuento: la práctica de telecom la hizo con el Marcelo Ducommun, en Infosur, por Avenida Alemania."
    fabian "No les pagaban, perro bastardo. Horas extra, pega pesada... y la empresa compraba cargadores chinos de dos lucas y los revendía como originales a VEINTE."
    mc "¿Cómo que a veinte?"
    fabian "VEINTE LUCAS. El cargador más chino del planeta. El profe Martín estaría orgulloso: por fin algo que SÍ venía de China."
    fabian "Y al Marcelo ni a terreno lo dejaron ir. Lo mandaron a la sección de impresoras y computadores. A VER impresoras. Todo el día."
    mc "(Eso explica todo. Marcelo masoquista.)"

    fabian "Y el colmo: Pablo fue DESPUÉS a esa misma empresa, a arreglar su laptop. Cuando Marcelo e Iván ya no estaban, eso sí."
    pablo "Me dijeron que era la placa. Doscientas lucas."
    fabian "¿Y era la placa?"
    pablo "Era el cargador. El cargador chino de dos lucas... que me cobraron a veinte."
    mc "(Pablo gastó dos millones en leceras y doscientas lucas en un cargador de dos. Su relación con el dinero es... deportiva.)"

    if broma_benjamin >= 1:
        show benjamin at right with dissolve
        "Benjamín te acompañó a la Shell. Dijo que era evidencia."
        benjamin "¿Y esa cisterna? Se ve manejable. MUY manejable."

    menu:
        "Subir a la cisterna con Pablo.":
            scene bg cisterna_int with dissolve
            show pablo at right with dissolve
            if venta:
                "Subes. La cabina huele a bencina, a desodorante y a heno."
                "¿Heno?"
                "En el asiento trasero hay algo cubierto con una manta. Parece una montura."
                pablo "No es mío. Debió venir con el tanque."
                mc "(Eso es una montura...)"
                $ pista_pablo = True
            else:
                "Subes. La cabina huele a bencina y a desodorante. Nada más. Todavía."
                pablo "¿Y? ¿Qué esperabas encontrar?"
                mc "(Nada. Todavía. Algo me dice que vuelva más adelante.)"
        "Preguntarle a Fabián por José y Shakira.":
            $ apoyo += 1
            show fabian at left with dissolve
            if venta:
                fabian "El día de la venta yo lo vi, wn. José no lloró. Nada. Como si firmara un papel cualquiera."
                fabian "Eso fue lo más raro, hermano. Lo más raro."
                "Te quedas pensando. Es tan triste como cómico."
            else:
                fabian "¿Quieres saber de Shakira? Anda a conocerla, wn. Está en Lincoñir. Vale la pena, te lo juro."
                fabian "Después me cuentas si viste algo más sano en tu vida."
        "Dejar que Benjamín maneje la cisterna." if broma_benjamin >= 1:
            $ broma_benjamin += 1
            scene bg cisterna_int with dissolve
            "Benjamín se sube al asiento del conductor. Nadie lo autorizó. Nadie lo detuvo a tiempo."
            show benjamin at center with dissolve
            benjamin "Tranquilos. En el fundo manejo tractor. Es lo mismo, pero con más litros de petróleo."
            scene bg cisterna_patio with dissolve
            "La cisterna avanza a tres kilómetros por hora. Gira suave. Demasiado suave. No frena."
            $ sfx("trueno.ogg")
            "La cisterna besa la tienda. La tienda besa el surtidor. El surtidor abraza el letrero..."
            "Detalle: el letrero ya se había caído solo, una vez. La cisterna solo llegó a terminar la pega."
            scene escena choque with dissolve
            "La Shell de Lautaro queda destruida en cámara lenta, a tres kilómetros por hora. Es el desastre más lento de la historia de Chile."
            scene bg shell_ruinas with dissolve
            show pablo shell at left with dissolve
            show benjamin at right with dissolve
            pablo "..."
            pablo "Mi reino."
            benjamin "Era un reino bonito. En mi defensa: nadie me dijo que NO."
            if venta:
                "Entre los escombros de la cabina, una manta se abre sola: LA MONTURA. A la vista de todos."
                mc "(Eso es DEFINITIVAMENTE una montura.)"
                $ pista_pablo = True
                pablo "No es mía. Es... de la Shell. Sí. De la Shell."
            else:
                "Entre los escombros no hay nada. Solo escombros. Escombros caros, eso sí."
            "Pablo mira los escombros. Mira su short. Mira sus gafas de sol."
            pablo "No me queda más que una cosa."
            mc "¿Más turnos?"
            pablo "Seguir apostando."
            $ pablo_arruinado = True
            $ recuerda("Pablo", "Pablo NO lo olvidará. Desde las ruinas.", negativo=True, puntos=-2)
            show fabian at center with dissolve
            fabian "Perro... esto se arregla con cumbia villera."
            "No se arregla con cumbia villera."

    $ musica("tema.ogg")
    jump hub


# =====================================================================
#  JUMBO DEL PORTAL
# =====================================================================
label jumbo:

    $ v_jumbo = True
    scene bg jumbo_pasillo with fade
    show diego at center with dissolve

    diego "Bienvenido al Jumbo, sección Hasbro. Acá estoy juntando para la PC. Mi gato me meó la laptop Junaeb, por eso estoy acá. Y el gato sigue suelto."
    "Diego repone un Optimus Prime con la solemnidad de un sacerdote."

    menu:
        "Diego, ¿pasó algo raro por aquí?":
            if venta:
                diego "Ahora que lo dices... cada viernes pasa por caja un cliente con veinte kilos de zanahorias."
                diego "Paga en efectivo. Usa gafas de sol. Y short."
                mc "(Veinte kilos... de zanahorias... con gafas de sol... y short...)"
                $ pista_diego = True
            else:
                diego "Raro... un cliente intentó pagar un Optimus Prime en cuarenta cuotas. Eso es todo. La retail es fome."
        "Prométeme que tú nunca venderás nada por tu PC.":
            $ apoyo += 1
            $ recuerda("Diego")
            diego "Nunca. Yo ahorro trabajando. Lo mío es honesto."
            "Diego hace una pausa dramática. Un Optimus Prime cae al suelo en cámara lenta."
        "Diego, ¿qué sabes de José y Shakira?":
            diego "Sé que todas las mañanas, antes de clases, José cruzaba el potrero con el desayuno. Y Shakira lo esperaba en la cerca."
            diego "Todas las mañanas. Todos los días. Año tras año."
            diego "Una vez José se enfermó. Ella no comió hasta que lo vio de nuevo."
            $ frag()

    jump hub


# =====================================================================
#  LINCOÑIR, PADRE LAS CASAS — LAS TRES VISITAS (antes de la venta)
# =====================================================================
label potrero_visita:

    if potrero_visitas == 0:
        jump potrero1
    elif potrero_visitas == 1:
        jump potrero2
    else:
        jump potrero3


label potrero1:

    $ potrero_visitas += 1
    scene bg camino with fade
    "Camino a Padre Las Casas. Tierra, puente y silencio."
    scene bg potrero with fade
    show benjamin at left with dissolve

    "Lincoñir. Que en realidad es la calle de la casa de José, en Padre Las Casas. Todos le dicen «Lincoñir» como si fuera un reino. Él no corrige."
    "Benjamín te trajo. Padre Las Casas queda lejísimos del Fundo El Carmen, pero él hizo la práctica por acá, cerca de la casa de José. Conoce el sector."

    show jose at right with dissolve
    show shakira at center with dissolve

    jose "¿Que venían a ver a la Shakira, loco? Ouuu. Aquí está, [nombre]: ella es Shakira."
    "La yegua te mira. Te huele la mano. Decide que le caes bien. Es imposible no quererla."

    scene escena cerca_desayuno with dissolve
    "José cruza el potrero con el desayuno. Shakira ya lo esperaba en la cerca. Como todas las mañanas. Como todos los días."
    show benjamin at left with dissolve
    benjamin "La crió de bebé, cachai. Desde que se la dieron. Le daba la mamadera, se levantaba de noche a verla. En invierno le ponía una frazada."
    $ frag()

    scene bg potrero with dissolve
    show benjamin at left with dissolve
    show jose at right with dissolve
    jose "Es que yo creo que la vendería por un palo, ¿sabían? En eso están los caballos."
    benjamin "(bajito) ¿Viste? Nadie le preguntó."
    mc "(Es imposible no quererla. Pero José habla del precio como del clima. Raro.)"
    benjamin "Por eso yo le tengo una ley a José: si algún día vende a Shakira, yo la hago asado."
    mc "¿¡QUÉ!?"
    benjamin "Es un anti-final, ¿cachai? Una amenaza pa que nunca la venda. Mientras exista la amenaza, Shakira está a salvo."
    benjamin "Es disuasión. Es cariño. Cariño disuasivo."
    jose "Está loco este. Como si yo fuera a venderla."
    "José se ríe. Shakira relincha tranquila. Nadie toma la ley en serio. Nadie."

    jump hub


label potrero2:

    $ potrero_visitas += 1
    scene bg potrero with fade
    show marcelo at left with dissolve
    show jose at right with dissolve
    show shakira at center with dissolve

    "Segunda visita a Lincoñir. Marcelo vino porque «qué lata, pero ya»."

    scene escena cumple with dissolve
    "Hoy es el cumpleaños de Shakira. Hay torta. De zanahoria. José canta el cumpleaños feliz. En serio. Completo."
    "Shakira apaga las velas de un mordisco. Se come media torta. José se ríe como nunca se ríe en el INACAP."

    scene bg potrero with dissolve
    show marcelo at left with dissolve
    show jose at right with dissolve
    show shakira at center with dissolve
    marcelo "Bucha... (bajito) está bonito, eso sí. Qué lata que esté bonito."
    $ frag()
    jose "El próximo año le hago una más grande. ¿Me ayudan?"
    mc "Obvio, po."

    jump hub


label potrero3:

    $ potrero_visitas += 1
    scene bg potrero with fade
    show fabian at left with dissolve
    show jose at right with dissolve

    "Tercera visita. Fabián vino «porque se juntaba con algo». No se juntaba con nada. Quería venir nomás."

    show shakira at center with dissolve

    fabian "Te cuento una, wn. Una vez José se fue un fin de semana. Shakira no comió hasta que volvió."
    fabian "Y cuando volvió, corrió a la cerca. Corrió, wn. Una yegua entera corriendo como perro."
    $ frag()

    scene escena atardecer_cerca with dissolve

    "Al atardecer, José se sienta en la cerca. Shakira apoya la cabeza en su hombro."
    "Fabián pone a Yerba Brava, bajito. Shakira mueve la cabeza al ritmo. Nadie dice nada."
    "Es la escena más sana que has visto en tu vida."

    jump hub


# =====================================================================
#  LA VENTA (el día que nadie quería)
# =====================================================================
label la_venta:

    $ venta = True
    $ musica("dramatica.ogg")
    scene bg patio with fade
    show benjamin at left with dissolve
    show diego at right with dissolve

    "Dos días después. Patio del INACAP. Todos hablan bajito. Marcelo no se está quejando. Eso nunca es buena señal."
    benjamin "Oye. Siéntate."
    mc "¿Qué pasó?"
    diego "José vendió a Shakira."
    "El mundo se detiene. Tú VISTE esa relación. Estuviste en el cumpleaños. Viste la cerca."
    mc "...No. ¿En serio?"
    benjamin "El sábado. En la mañana."

    scene bg potrero with dissolve
    show jose at right with dissolve
    $ musica("triste.ogg")

    "El comprador llegó un sábado en la mañana. Shakira esperaba en la cerca, como siempre, su desayuno."
    "José preguntó el precio. Escuchó la oferta. Y firmó."
    "Sin dudar. Sin llorar. Sin mirar atrás."

    scene escena venta_camioneta with dissolve

    "Se dice que Shakira miró la camioneta irse hasta que dejó de verse. El vecino mapuche tuvo que darle el desayuno ese día."
    show shakira at left with dissolve
    shakira "(Iiih.)"
    "Ese relincho lo escuchaste alegre, hace nada, en vivo. Ahora no lo es."
    "José, mientras tanto, fue a comprar la PC. Ese mismo día. Estaba contento."
    "Shakira no entendió. Las yeguas no entienden de contratos. Solo saben quién cruza el potrero con el desayuno."
    "A la mañana siguiente esperó en la cerca. Como siempre. A la siguiente, también. Comió mirando el portón."
    "Esperó a José harto rato. Él no volvió. Un millón por una yegua. Un millón por una PC."
    $ frag()

    scene bg patio with dissolve
    show benjamin at left with dissolve
    show diego at right with dissolve
    $ musica("dramatica.ogg")

    show jose at center with dissolve

    jose "¿Qué tanto, po? Era una yegua. Una yegua muy querida. Pero una yegua. Nada que hacerle."
    "Lo dice con la calma de siempre. La misma calma con la que te presentó a Shakira. Y ESO es lo que nadie soporta."
    benjamin "Cero remordimiento. Ni uno. Ni medio."
    benjamin "Y acuérdate de mi ley, José. Te la dije en tu cara: si la vendí, asado."
    jose "Ya, era broma, po."
    benjamin "¿Era broma? ¿Tú cachai si era broma?"
    "Benjamín no se ríe. Por primera vez, Benjamín no se ríe."
    benjamin "Desde hoy, nuevo, esto es personal. Lo vamos a molestar hasta que sienta ALGO. Y tú tienes la grabadora."
    mc "(Tengo la grabadora. Tengo los fragmentos de algo que ya no existe.)"
    "Y así comienza la era del leseo. La más grande de la historia del INACAP."
    $ recuerda("El grupo", "El grupo entero lo recordará. Para siempre. Es la promesa.")
    $ musica("tema.ogg")

    jump hub


# =====================================================================
#  LINCOÑIR, PADRE LAS CASAS (después de la venta)
# =====================================================================
label potrero:

    $ v_potrero = True
    scene bg potrero with fade
    "Lincoñir, comuna de Padre Las Casas. La casa de José. Un potrero vacío, un pesebre y un silencio incómodo."
    show jose at right with dissolve
    show benjamin at left with dissolve

    benjamin "Te acompañé, nuevo. Yo conozco de caballos. De fundos. Y de justicia."
    jose "Aquí almorzaba, se acostaba, dormía, despertaba. Y cuando salía, me esperaba en el portón."
    jose "Ahora aquí hay puro pasto. Nada más."

    menu:
        "Inspeccionar el pesebre.":
            scene bg pesebre with dissolve
            show jose at center with dissolve
            "Hay heno fresco. Muy fresco. Huellas de herradura recientes. Y una zanahoria a medio morder."
            mc "Shakira estuvo aquí... hace poco."
            jose "Debe ser del vecino. Un vecino mapuche que tiene caballos. Varios. Es normal."
            $ pista_potrero = True
            scene bg potrero with dissolve
            show jose at right with dissolve
            show benjamin at left with dissolve
        "Hablar con José del cariño que le tenía a Shakira.":
            $ apoyo += 2
            $ recuerda("José")
            jose "La quería harto, [nombre]. La crié de bebé, desde que me la dieron. Le celebraba el cumpleaños y todo."
            mc "¿Y te costó venderla?"
            jose "No."
            "Lo dice sin odio. Sin sarcasmo. Con la tranquilidad de quien comenta el clima."
            "Esa calma es lo más perturbador que has escuchado en tu vida. Y tú viste la torta. Y la cerca."
            benjamin "¿Viste? ¿VISTE? Eso es lo que no me deja dormir."

    benjamin "Lo que pasó aquí no tiene nombre. Una yegua criada con amor... vendida como quien vende un celular usado."
    benjamin "Si esto fuera el Fundo El Carmen... bueno. No digo más. Solo digo una palabra: carbón."

    "Como invocado por la palabra «carbón», aparece un muchacho caminando desde el camino. Pedro de Valdivia, rumbo a Chol Chol. O sea, al lado del Fundo El Carmen."

    scene bg pedro with dissolve
    "(Pedro de Valdivia. De aquí viene Maxi. Caminando. Siempre caminando.)"

    scene bg potrero with dissolve
    show jose at right with dissolve
    show benjamin at left with dissolve
    show maxi at center with dissolve

    benjamin "¡Maxi! ¿Qué haces aquí, wn?"
    maxi "Vivo al lado, aweonao. ¿Tú qué haces TÚ, conchetumare?"
    benjamin "Este es Maxi Valenzuela. No es del INACAP; era del liceo con nosotros. Aparece cuando hay comida o conflicto. Hoy hay ambos."
    maxi "¿Y este quién es, negro?"
    mc "[nombre]. Estoy investigando lo de Shakira."
    maxi "¿La yegua que vendieron por el compu, sipo? Conchetumare, José. Eso no se hace, wn. Eso es como... como vender a la mamá por una tele."
    jose "Tampoco tanto."
    maxi "COMO VENDER A LA MAMÁ POR UNA TELE, DIJE."
    "Maxi mira el potrero con nostalgia ajena. Saca el celular. Su Instagram: puros videos de minas corpulentas."
    maxi "El algoritmo me conoce, wn. Es lo único estable que tengo en la vida."
    benjamin "Maxi también es medio corpulento. El algoritmo sabe."
    maxi "Sipo, conchetumare. El algoritmo no se equivoca."

    menu:
        "Maxi, ¿tú qué harías con el caso Shakira?":
            maxi "Yo, wn... yo haría un asado. Pero de respeto, ¿eh? Con velita y to'."
            "Benjamín toma nota mental: asado. Con respeto. Y velita."
            $ broma_benjamin += 1
            $ recuerda("Maxi", "Maxi te considera un aweonao de confianza.")
        "Me caes bien, Maxi. Eres un poeta maldito.":
            $ apoyo += 1
            $ recuerda("Maxi")
            maxi "Sipo, negro. Tú sí entendís. No como estos aweonaos del INACAP."
        "Benjamín, respeta el dolor de José.":
            $ apoyo += 1
            $ recuerda("Benjamín", "Benjamín finge estar decepcionado de ti.", negativo=True)
            benjamin "...Tienes razón. Perdón, José."
            jose "Gracias, [nombre]. Al menos alguien me respeta."
            maxi "(susurrando) Qué fome, negro."

    jump hub


# =====================================================================
#  LICEO POLITÉCNICO DE PUEBLO NUEVO
# =====================================================================
label liceo:

    $ v_liceo = True
    scene bg liceo with fade
    show diego at left with dissolve
    show benjamin at right with dissolve

    "Liceo Politécnico de Pueblo Nuevo. Aquí se conocieron todos. Tú llegaste después, como personaje descargable."
    diego "Este lugar tiene historia. Y por historia quiero decir... al profe Martín."
    benjamin "El Shen Shen. Que en paz descanse su credibilidad."
    mc "¿El Shen Shen?"

    # --- Flashback del liceo ---
    scene black with fade
    "Años antes. Sala de clases. El profe Martín escribe en la pizarra una sola palabra: HUAWEI."

    scene escena martin_clase with fade
    show martin at center with dissolve

    martin "Cabros. Hoy no habrá clase. Hoy hablaremos de China."
    "El curso entero suspira en coro: «Otra vez no...»"
    martin "Cuando yo estuve en Shenzhen..."
    "El curso, susurrando: «Shen Shen...»"
    martin "...porque cuando era estudiante, COMO USTEDES, gané la competencia de Huawei del INACAP. Me mandaron a la final MUNDIAL. A China. Y quedé SEGUNDO."
    show benjamin at right with dissolve
    benjamin "(Ayer dijo que tercero.)"

    menu:
        "Creerle al profe. Suena convincente.":
            $ apoyo += 1
            $ recuerda("El profe Martín", "El profe Martín lo recordará. En otra historia.")
        "Dudar en voz alta.":
            $ drama += 1
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu escepticismo.")
            benjamin "¡Eso! ¡Duda! ¡Duda de todo! ¡Duda hasta de la cumbia!"
        "¿Y ese Jeep 4x4 estacionado afuera?":
            "Una voz desde la ventana: «¡CUATRO POR CUATRO!»"

    "Marcelo se inclina y te susurra la verdad, porque Marcelo jamás se ha aguantado nada:"
    show marcelo at left with dissolve
    marcelo "A China sí fue. Eso es verdad. Ganó la competencia del INACAP siendo estudiante y lo mandaron a la final mundial."
    benjamin "El problema es el puesto. Segundo, dice. A veces tercero. Depende del día."
    marcelo "Quedó DUODÉCIMO. Lo eliminó un peruano random. Qué lata."
    $ verdad_martin = True
    martin "¡SE DICE SHENZHEN!"

    "En eso irrumpe un hombre con una cámara. Filma la clase como si fuera un documental de National Geographic."

    benjamin "Héctor. Amigo del profe. Todos le dicen el Suzuki Jeep."
    show hector at right with dissolve
    hector "Este video va para mi canal. SJO. Suzuki Jeep Oficial. Y ese Jeep de afuera es mío."

    show jeep at right with dissolve
    "El Jeep. Suzuki. Cuatro por cuatro. Estacionado como si fuera dueño del liceo."
    "Se cachiporrea de su Jeep. Es el noventa por ciento de su personalidad."
    marcelo "Tiene casi cuatro mil suscriptores. Qué lata. La gente no tiene criterio."
    show benjamin at right with dissolve
    benjamin "Tres mil novecientos ochenta. Ciento doce videos. Todos del Jeep."
    show hector at right with dissolve
    hector "Qué van a saber ustedes. No tienen un Suzuki Jeep."
    martin "¡RESPETO! ¡Héctor, filma esto!"
    hector "Ya estoy filmando. Desde el Jeep se ve mejor, eso sí."

    "Y así, cada clase: China, Huawei, Shenzhen. Y el Jeep, siempre afuera. Siempre cuatro por cuatro."
    "Y al fondo de la sala, Maxi Valenzuela (que no es del INACAP, pero sí era del liceo) susurraba «conchetumare» cada vez que el profe decía Shenzhen. Nunca lo expulsaron. A los profes no les pagaban lo suficiente para expulsar a Maxi."
    "Y en cada mesa, cada muro y cada baño del liceo, la misma inscripción sagrada: «Iván Garrido del 4F»."
    martin "¡¿QUIÉN RAYA MIS MESAS?!"
    hector "Yo tengo una teoría: se rayó solo. Como los geoglifos. Nadie sabe cómo llegó ahí."
    show benjamin at right with dissolve
    benjamin "Esos los hice yo. No es ningún secreto: lo rayé delante de todo el curso. De Iván incluido. Es mi obra maestra."

    "Y hablando de Iván: años después, el INACAP vivió un día histórico."

    scene bg inacap with dissolve
    show ivan at center with dissolve

    "Iván Garrido del 4F pisando el INACAP. Primera vez. Única vez."
    "Se inscribió. Firmó unos papeles. Todos creyeron que estudiaría. Error."
    hide ivan with dissolve
    "Dos días después..."
    show ivan at center with dissolve
    "Iván volvió. Se dio de baja. Pidió su certificado de alumno regular. Un PDF."
    ivan "Chao."
    hide ivan with dissolve
    "Y se fue caminando lento, victorioso. Con ese PDF esquivó la milicia. El llamado del ejército."
    "La jugada más brillante jamás registrada. Hasta hoy se estudia. Bueno, no. Pero debería."
    "Dato inútil: Iván a veces pinta casas. Ayuda a su papá. Es lo más cerca que ha estado del ejercicio."

    scene bg liceo with fade
    show diego at left with dissolve
    show benjamin at right with dissolve
    diego "Buenos tiempos."
    benjamin "El Shen Shen sigue dando clases. Sigue yendo a 'China'."

    "Suena el celular de Benjamín. Contesta."
    benjamin "¿Aló? ... ¿Nico? ... ¿Cómo que Santiago? ... ¿No que ibas a Lonquimay? ... Ya. Cuídate, wn."
    "Benjamín cuelga."
    benjamin "El Nico Jara. Terminó en Santiago. De soldado."
    diego "¿No que iba a Lonquimay?"
    benjamin "Lonquimay quedó en el camino. Nadie sabe qué pasó entre medio."
    mc "(Casi cuatro mil suscriptores viendo un Jeep. Este país es infinito.)"

    jump hub


# =====================================================================
#  EL DÍA QUE FABIÁN SE FUE (de la nada, en presencia de todos)
# =====================================================================
label fabian_se_va:

    $ v_fabian_sale = True
    scene bg patio with fade
    show fabian at center with dissolve
    show marcelo at left with dissolve
    show benjamin at right with dissolve

    "Patio del INACAP. Día normal. Todo tranquilo. Demasiado tranquilo."
    fabian "Cabros. Me salí."
    "..."
    mc "¿De dónde?"
    fabian "Del INACAP. De la carrera. Me salí. Hoy. Ahora."
    $ sfx("trueno.ogg")
    benjamin "¿¡QUÉ!? ¿Así? ¿Así nomás? ¿En nuestras caras?"
    fabian "Se me hizo muy difícil, wn. Y conseguí polola. Los papás de ella la echaron de la casa, así que nos vamos a vivir juntos. Hay que trabajar."
    marcelo "Bucha. Así de la nada. Qué lata los golpes de la nada."
    fabian "Postulé al Tecnobox. Me dijeron «te llamamos». Voy bien."
    "(Alerta de spoiler del futuro: nunca lo llamaron del Tecnobox. Hasta hoy.)"
    benjamin "Pero avisa, po. Con tiempo. Con una semana."
    fabian "Te estoy avisando. Ahora. Aguante el Colo. Chao, cabros."
    "Fabián se va caminando hacia Pillalelbún. Literalmente. Alguien jura que lo vio llegar a pie."
    $ recuerda("Fabián", "Fabián se fue del INACAP. El INACAP no lo olvidará. La cumbia tampoco.")

    jump hub


# =====================================================================
#  LA INUNDACIÓN DE PILLALELBÚN (no pasaba desde 2008)
# =====================================================================
label inundacion:

    $ v_inundacion = True
    $ musica("dramatica.ogg")
    scene bg patio with fade
    show benjamin at left with dissolve
    show marcelo at right with dissolve

    "Noticia de último minuto: Pillalelbún se está inundando."
    marcelo "Bucha. No se inundaba desde 2008. Qué lata el 2008 de vuelta."
    benjamin "¡Fabián! ¡Pablo! ¡Rubén! Todos están allá. ¡MAXI TAMBIÉN! Vamos."
    mc "¿Yo también?"
    benjamin "Tú también. Es ley de Pillalelbún: cuando se inunda, se va."

    scene bg inundado with fade
    "Pillalelbún. Agua hasta la rodilla. La Shell resiste. Las casas resisten. La cumbia, por supuesto, suena."
    show fabian at left with dissolve
    show pablo at right with dissolve

    fabian "¡Cabros! ¡Llegaron! Aguante Pillalelbún, wn."
    "Fabián ya tiene a sus galgos, Los Intratables, listos en la camioneta. La Pequi, la gata, mira todo desde el techo."
    pablo "El agua sube. Tengo todo bajo control. Casi todo."
    "Pablo tiene las gafas de sol en la cabeza. Secas. Prioridades."

    show maxi at center with dissolve
    fabian "Ese es Maxi. De Pedro de Valdivia. Aparece cuando hay comida, conflicto o catástrofe."
    maxi "¡Conchetumare el agua! ¡Estoy hasta el copi, negro!"

    show ruben at right with dissolve
    "Rubén flota en su banca. Literalmente flota. No se ha movido. No piensa moverse."
    ruben "¿Y a ti qué te importa? El agua me lleva sola."

    menu:
        "Ayudar a Fabián a evacuar a Los Intratables.":
            $ ayuda_inundacion = "fabian"
            $ rel_delta("Fabián", 2)
            $ rel_delta("Pablo", -1)
            $ rel_delta("Maxi", -1)
            $ recuerda("Fabián", "Fabián lo recordará. Pablo y Maxi NO lo olvidarán.", puntos=0)
            "Ayudas a Fabián a subir a los galgos a la camioneta. Son brigidos: cooperan. Casi todos."
            fabian "Gracias, wn. Aguante el Colo y aguanten los galgos."
            "Uno se llama Zeus Black II. Nadie pregunta. Mejor no preguntar."
            "La Pequi se salvó sola. Estaba en el techo desde antes de que llegara el agua. Las gatas saben."
        "Ayudar a Pablo a salvar la Shell.":
            $ ayuda_inundacion = "pablo"
            $ rel_delta("Pablo", 2)
            $ rel_delta("Fabián", -1)
            $ rel_delta("Maxi", -1)
            $ recuerda("Pablo", "Pablo lo recordará. Fabián y Maxi NO lo olvidarán.", puntos=0)
            show pablo at right with dissolve
            "Ayudas a Pablo a poner sacos. Él salva primero las gafas de sol. Después el surtidor. Después, si queda tiempo, la gente."
            pablo "Gracias. Brad Pitt también habría salvado las gafas primero."
        "Ayudar a Maxi con los sacos de arena.":
            $ ayuda_inundacion = "maxi"
            $ rel_delta("Maxi", 2)
            $ rel_delta("Fabián", -1)
            $ rel_delta("Pablo", -1)
            $ recuerda("Maxi", "Maxi lo recordará. Fabián y Pablo NO lo olvidarán.", puntos=0)
            "Pones sacos con Maxi. Maxi insulta al agua. Al agua no le importa. Sigue subiendo."
            maxi "¡Toma, culiao! ¡Así se hace, negro!"
            "Le dice culiao al agua. Funciona. Probablemente por miedo."

    mc "¿Y Rubén? ¿No hay que salvarlo?"
    fabian "¿Rubén? Rubén no necesita salvación. Rubén es el único que sale ganando: no tiene que hacer nada. Como siempre."

    scene bg atardecer with fade
    "El agua baja al atardecer. Pillalelbún sobrevive. Como en 2008."
    "Fabián pone cumbia villera. Todos bailan con los pies mojados. Rubén sigue flotando. Por gusto."
    $ recuerda("Pillalelbún", "Pillalelbún lo recordará. Hasta 2008. Digo, hasta siempre.")
    $ musica("tema.ogg")

    jump hub


# =====================================================================
#  CONFLICTO: EL JUICIO DE LA SHELL (Pablo vs Benjamín)
# =====================================================================
label juicio_shell:

    $ v_juicio_shell = True
    scene bg shell_ruinas with fade
    show pablo shell at left with dissolve
    show benjamin at right with dissolve

    "Días después del desastre. La Shell sigue destruida. Pablo sigue apostando. Y hoy hay juicio."
    pablo "Benjamín. Me destruiste el reino. Mi reino, Benjamín."
    benjamin "En mi defensa: nadie me dijo que NO."
    pablo "¡NADIE TIENE QUE DECIRTE QUE NO!"
    benjamin "Eso es exactamente lo que diría alguien que no me dijo que no."
    "Pablo respira. Cuenta hasta diez. Llega hasta tres."
    pablo "Alguien tiene que pagar esto. Y no voy a ser yo. Yo no tengo ni un peso."
    benjamin "Yo tampoco. Tengo fundo. Es distinto."
    "Ambos te miran. Es tu turno de fallar."

    menu:
        "Apoyar a Pablo: Benjamín tiene que pagar.":
            $ rel_delta("Pablo", 2)
            $ rel_delta("Benjamín", -1)
            $ recuerda("Pablo", "Pablo lo recordará. Benjamín NO lo olvidará.", puntos=0)
            pablo "Gracias. AL FIN justicia."
            benjamin "Traición. Traición diplomática. Anotado."
            benjamin "Pagaré. En carmenos. Que valen el doble."
            "Benjamín pagará. En cuotas. De mil pesos. Durante ochenta años."
        "Apoyar a Benjamín: fue un accidente.":
            $ rel_delta("Benjamín", 2)
            $ rel_delta("Pablo", -1)
            $ recuerda("Benjamín", "Benjamín lo recordará. Pablo NO lo olvidará.", puntos=0)
            benjamin "¡GRACIAS! ¡Era un accidente! ¡Un accidente con estilo!"
            pablo "..."
            pablo "Brad Pitt no abandonaría a un amigo así."
            "Pablo se pone las gafas. Ofendido. Con frío. Con todo."
        "Mediar: que la reconstruyan juntos.":
            $ apoyo += 1
            $ rel_delta("Pablo", 1)
            $ rel_delta("Benjamín", 1)
            $ recuerda("El grupo", "Pablo y Benjamín lo recordarán. Juntos. A la fuerza.")
            mc "Ninguno paga. Ambos trabajan. La reconstruyen juntos."
            pablo "..."
            benjamin "..."
            "Aceptan. Nadie sabe quién ganó. Probablemente la Shell."

    "Y así quedó el asunto de la Shell. Pablo lo recuerda. Benjamín también. Por razones distintas."

    jump hub


# =====================================================================
#  CONFLICTO: PREMIERCHILITO EN PELIGRO (Marcelo vs Benjamín)
# =====================================================================
label conflicto_marcelo:

    $ v_conflicto_marcelo = True
    scene bg patio with fade
    show marcelo at left with dissolve
    show benjamin at right with dissolve

    "Patio del INACAP. Marcelo está pálido. Benjamín está... orgulloso. Mala combinación."
    marcelo "Bucha. BUCHA. premierchilito tiene un strike. UN STRIKE."
    mc "¿Qué pasó?"
    marcelo "Alguien le puso música a mi último video. Cumbia villera. Sobre un clip de la Chilean Premier."
    benjamin "Fui yo. Lo mejoré. El fútbol necesitaba cumbia."
    marcelo "¡DERECHOS DE AUTOR, BENJAMÍN! ¡YA PERDÍ UN INSTAGRAM POR ESO!"
    benjamin "Fue Supermerk2. Vale la pena el strike. Arte es arte."
    "Ambos te miran. Tienes que fallar."

    menu:
        "Marcelo tiene razón: borra el video, Benjamín.":
            $ rel_delta("Marcelo", 2)
            $ rel_delta("Benjamín", -1)
            $ recuerda("Marcelo", "Marcelo lo recordará. Benjamín NO lo olvidará.", puntos=0)
            benjamin "Borrar arte. Está bien. Lo borro. Pero la historia me dará la razón."
            marcelo "Bucha. Gracias, nuevo. Al menos alguien entiende de copyright."
        "Benjamín tiene razón: el fútbol necesitaba cumbia.":
            $ rel_delta("Benjamín", 2)
            $ rel_delta("Marcelo", -1)
            $ recuerda("Benjamín", "Benjamín lo recordará. Marcelo NO lo olvidará.", puntos=0)
            benjamin "¡POR FIN! ¡ALGUIEN CON CULTURA!"
            marcelo "..."
            marcelo "Te voy a anotar en el próximo strike. Con tu nombre. Bucha."
        "Solución: graben un video de disculpa. Juntos.":
            $ apoyo += 1
            $ rel_delta("Marcelo", 1)
            $ rel_delta("Benjamín", 1)
            $ recuerda("El grupo", "Marcelo y Benjamín lo recordarán. En el mismo video.")
            "Graban un video de disculpa. Marcelo se disculpa sin querer disculparse. Benjamín baila al fondo."
            "El video tiene más views que cualquier clip de fútbol. premierchilito sobrevive."

    jump hub


# =====================================================================
#  CONFLICTO: LA DEUDA DE LAS LÁMINAS (Fabián vs Rubén)
# =====================================================================
label conflicto_ruben:

    $ v_conflicto_ruben = True
    scene bg patio with fade
    show fabian at left with dissolve
    show ruben at center with dissolve

    "Fabián llega al patio decidido. Frente a él: Rubén. En su banca. Como siempre."
    fabian "Rubén. Las diez lucas. Me las debí desde el año pasado, wn."
    ruben "¿Y a ti qué te importa?"
    fabian "¡Me importa que son mis diez lucas!"
    ruben "Es que no las tengo. Se fueron en láminas. La inversión no maduró."
    fabian "¡Las láminas no son inversión, perro bastardo!"
    "Ambos te miran. Fabián con rabia. Rubén con sueño."

    menu:
        "Pagarle a Fabián las diez lucas de Rubén.":
            $ rel_delta("Fabián", 2)
            $ rel_delta("Rubén", 1)
            $ recuerda("Fabián", "Fabián lo recordará. Rubén también. Como fiador.", puntos=0)
            "Pagas las diez lucas. Rubén ahora te debe a TI. No mejora tu situación."
            ruben "Gracias. Te pago en láminas."
            mc "No acepto láminas."
            ruben "Entonces no te pago. Chao."
        "Apoyar a Fabián: Rubén tiene que pagar.":
            $ rel_delta("Fabián", 2)
            $ rel_delta("Rubén", -1)
            $ recuerda("Fabián", "Fabián lo recordará. Rubén NO lo olvidará.", puntos=0)
            "Rubén suspira. Revisa sus bolsillos. Saca una lámina. La mira con cariño."
            ruben "Toma. La número 7. Vale más que diez lucas. Sentimentalmente."
            fabian "..."
            "Fabián acepta la lámina. Nadie sabe por qué. La cumbia lo ablanda."
        "Apoyar a Rubén: la deuda prescribió.":
            $ rel_delta("Rubén", 2)
            $ rel_delta("Fabián", -1)
            $ recuerda("Rubén", "Rubén lo recordará. Fabián NO lo olvidará.", puntos=0)
            ruben "Escuchaste. Prescribió. Es ley."
            fabian "¿¡QUÉ LEY!? ¡NI SIQUIERA ESTUDIABAS CUANDO LA PEDISTE!"
            "Fabián se va poniendo cumbia villera para calmarse. Funciona a medias."

    jump hub


# =====================================================================
#  BENJAMÍN VS EL INACAPINI (evento automático)
# =====================================================================
label pelea_inacapini:

    $ v_pelea_inacapini = True
    scene bg patio with fade
    show benjamin at center with dissolve

    "Benjamín vuelve al patio con cara de guerra. A lo lejos, la mascota del INACAP saluda a la gente."
    mc "¿Qué te pasó?"
    benjamin "El Inacapini. Le pedí una foto. Me dijo que NO."
    benjamin "La mascota. Del INACAP. Me negó una foto. A MÍ."
    "El Inacapini, a lo lejos, sigue saludando. Con las dos manos. Provocador."
    benjamin "Esto es guerra. Guerra declarada. Desde hoy, el Inacapini es mi enemigo."

    menu:
        "Apoyar a Benjamín: la mascota se pasó.":
            $ rel_delta("Benjamín", 1)
            $ recuerda("Benjamín")
            benjamin "¡GRACIAS! ¡Aliado número uno de la guerra!"
        "Defender al Inacapini: es una mascota, Benjamín.":
            $ rel_delta("Benjamín", -1)
            $ recuerda("Benjamín", "Benjamín NO lo olvidará. El Inacapini saluda igual.", negativo=True)
            benjamin "¿De qué lado estás? ¿Del lado azul? ANOTADO."
        "Ofrecerte a sacarle la foto tú.":
            $ apoyo += 1
            benjamin "No es lo mismo. La foto era una PRUEBA de que la mascota me respeta."
            benjamin "Y no me respeta. ESO es el problema."

    benjamin "Y algo me dice que esa mascota esconde algo. Nadie es tan saludable. NADIE."
    benjamin "Cuando tenga pruebas, te aviso. Esto no queda así."

    jump hub


# =====================================================================
#  WHAT IF: EL SOSPECHOSO AZUL (evento no canon)
# =====================================================================
label whatif_inacapini:

    $ v_inacapini = True
    scene bg patio with fade
    show benjamin at left with dissolve

    "Misión: vigilar al Inacapini. Benjamín lleva binoculares. De dónde los sacó, nadie sabe."
    "El Inacapini saluda. Posaa. Reparte stickers. Sospechosamente perfecto."
    benjamin "Míralo. Actúa como mascota. Demasiado bien. Ahí hay algo."

    show inacapini at right with dissolve
    inacapini "(Saluda con las dos manos.)"
    mc "Voy a hablar con él."
    benjamin "¿¡ESTÁS LOCO!? Te va a escuchar. Bueno. Ve. Yo te cubro."

    "Te acercas al Inacapini. Te mira con su mirada de mascota. Permanente. Inquietante."

    menu:
        "Preguntarle directo: ¿qué escondes?":
            "El Inacapini se queda quieto. Demasiado quieto."
            inacapini "..."
            "Se saca la cabeza. Literalmente. La cabeza de la mascota."
            "Debajo no hay nadie. Hay una montura. Y heno. MUCHO heno."
        "Seguirlo a escondidas.":
            "Sigues al Inacapini hasta el estacionamiento. Se sube a una camioneta."
            "En la camioneta: una montura. Y heno. MUCHO heno."

    mc "BENJAMÍN. VEN."
    benjamin "¿QUÉ PAS... no. NO. NO PUEDE SER."
    "El Inacapini, sin cabeza, con las dos manos al cielo, confiesa sin poder hablar:"
    "EL INACAPINI LE COMPRÓ SHAKIRA AL VECINO MAPUCHE."
    benjamin "¿CON QUÉ PLATA? ¿DE DÓNDE? ¡RESPONDE!"
    inacapini "(Se encoge de hombros. Con mucha dignidad.)"
    "Con su sueldo de mascota, aparentemente. Y con sus ahorros de stickers."
    "Shakira está bien. Vive con el Inacapini. Tiene su propio traje. Es la Inacapini junior los fines de semana."
    benjamin "Esto es lo más perturbador que he visto. Y yo vi a José firmar la venta."
    "(Evento WHAT IF completado. No es canon. Pero la foto quedó. Benjamín la tiene. El Inacapini sale saludando en ella.)"
    $ recuerda("Benjamín", "Benjamín lo recordará. El Inacapini también. Saludando.")

    jump hub


# =====================================================================
#  EL DÍA QUE RUBÉN ABANDONÓ (un poco más allá de la mitad)
# =====================================================================
label encuentro_ruben:

    $ v_ruben = True
    $ musica("dramatica.ogg")
    scene bg patio with fade
    show marcelo at left with dissolve
    show benjamin at right with dissolve

    "Patio del INACAP. Algo está pasando. Marcelo llora. Benjamín aplaude lento, como en los funerales importantes."

    show ruben at center with dissolve

    ruben "Ya, ya. No es pa tanto."
    mc "¿Qué pasó?"
    benjamin "Rubén... abandona la carrera. Hoy. Ahora. EN VIVO."
    $ sfx("trueno.ogg")
    ruben "Me levanté, vi el frío, y dije: no. Así de simple."
    marcelo "Aguantaste más de la mitad de la carrera sin hacer absolutamente nada. Bucha. Es un récord. Un récord qué lata."
    benjamin "El INACAP pierde a su alumno más... presente. Físicamente presente, al menos."
    ruben "Supervisé harto. Supervisar es trabajar."
    benjamin "En los trabajos de a tres, Marcelo y yo hacíamos todo. Rubén 'supervisaba'. Desde la banca. Esta misma banca."
    benjamin "Una vez el papá le regaló veinte lucas para que almorzara."
    marcelo "Se las gastó en láminas. Láminas de colección. Se cagó de hambre toda la semana. Bucha."
    ruben "Eran láminas numeradas. No entienden."
    benjamin "Ah, y le gustan los gatos esfinge. Los sin pelo. El Bingus cat."
    ruben "El Bingus es un buen gato. No hay que peinarlo. Menos pega."
    mc "(Hasta los gustos de Rubén son de bajo mantenimiento.)"

    mc "Oye, Rubén... tú eres de Pillalelbún. ¿Sabes algo de Shakira? ¿De Pablo?"
    ruben "..."
    ruben "¿Y a ti qué te importa?"
    mc "Estoy investigando."
    ruben "Investigar. Qué esfuerzo. Me agoté de puro escucharte."
    "Rubén suspira como si el mundo entero le debiera una siesta."
    ruben "Pero ya que insistes... sí. La vi. Una yegua, cerca de la Shell. Los domingos. Cuando Pablo cree que nadie mira."
    ruben "Yo no dije nada. Decirlo era mucho esfuerzo."
    $ pista_ruben = True

    menu:
        "Gracias, Rubén. Tu secreto está a salvo conmigo.":
            $ secreto_ruben = True
            $ recuerda("Rubén", "Rubén confía en ti. Casi se mueve de la emoción.")
            ruben "Bacán."
        "Esto va a salir a la luz, Rubén. Lo siento.":
            $ drama += 1
            $ recuerda("Rubén", negativo=True)
            ruben "¿Y a ti qué te importa? Haz lo que quieras. Yo no me muevo."

    ruben "Chao, chiquillos."
    "Rubén se va caminando lento. Es lo más rápido que se le ha visto moverse."
    $ recuerda("Rubén", "Rubén abandonó la carrera. La carrera no lo olvidará. La carrera ni lo conoció.")
    $ musica("tema.ogg")

    jump hub


# =====================================================================
#  EL SUEÑO DE PABLO (misión secundaria)
# =====================================================================
label sueno_pablo:

    $ v_sueno = True
    scene bg shell with fade
    show pablo shell at center with dissolve

    if pablo_arruinado:
        "Vuelves a la Shell. O a lo que queda de ella."
    else:
        "Vuelves a la Shell en horario de colación."

    pablo "Nuevo. Justo te quería ver. Estaba pensando..."
    pablo "¿Y si hubiera invertido los dos millones? En vez de... ya sabes. Las leceras."
    mc "¿Invertir? ¿Tú?"
    pablo "Yo. Empresario. Mira cómo sería."

    $ musica("tema.ogg")
    scene bg sueno with dissolve

    "Y así fue. Pablo invirtió los dos millones. Con sabiduría. Con asesoría. Con un Excel."
    "Pillalelbún prospera: la Shell ahora es Shell Premium. Fabián tiene su propia radio: Radio Pillalelbún Cumbia, 24 horas. Pura cumbia villera."
    python:
        absurdos = [
            "Rubén tiene un puesto vitalicio en el municipio: Supervisor General. Con sueldo. Con funciones. Todo el día.",
            "Bastián habla. Discursos enteros. Multitudes lo escuchan en silencio.",
            "Diego va al Elysium todos los días. TODOS los días. Y le alcanza para la PC.",
        ]
        if v_shell:
            absurdos.append("Hay una estatua de Iván Garrido del 4F en la plaza. Nadie la encargó. Apareció. Como los geoglifos.")
        if v_potrero:
            absurdos.append("Maxi es alcalde de Pedro de Valdivia. Nadie votó. Ganó igual.")
        if v_patio:
            absurdos.append("Marcelo dejó de quejarse. Premierchilito llegó al millón de seguidores.")
        if v_liceo:
            absurdos.append("Héctor llegó al millón de suscriptores. Noventa y nueve videos del Jeep. Uno de un cerro.")
        for linea_sueno in muestra(absurdos, 3):
            renpy.say(None, linea_sueno)

    if venta:
        "José tiene tres yeguas. Las vende todas. Sigue sin sentir nada."
    else:
        "José tiene tres yeguas. Las cuida a todas. Les celebra el cumpleaños a las tres."
    "Su proyecto estrella: la Ruta de la Zanahoria, el primer paseo turístico zanahorero de la Araucanía. Nadie la pidió. Funciona igual."

    scene escena sueno_ruta with dissolve
    "Y Pablo, con short y gafas de sol, corta la cinta inaugural de la Ruta de la Zanahoria."
    show pablo shell at center with dissolve
    pablo "Por fin... leceras productivas."

    $ musica("dramatica.ogg")
    scene bg shell with fade
    show pablo shell at center with dissolve

    "Y entonces Pablo despertó."
    if pablo_arruinado:
        "Estaba dormido sobre los escombros de la Shell. Roncaba con dignidad."
    else:
        "Estaba dormido de pie, apoyado en el surtidor. Es un talento."
    "No hubo inversión. No hubo Shell Premium. No hubo Ruta de la Zanahoria."
    "Los dos millones se fueron en leceras y Pablo no tiene ni un peso."
    pablo "Soñé que era financieramente responsable."
    pablo "Qué pesadilla."
    mc "Pablo... ¿y si la próxima vez sí inviertes?"
    pablo "¿Próxima vez? Buena idea. Voy a apostar para juntar lucas."
    $ recuerda("Pablo", "Pablo soñó despierto. Y dormido. Pablo sueña mucho.")

    jump hub


# =====================================================================
#  WHAT IF: CUPIDO DE ALQUILER (evento no canon)
# =====================================================================
label whatif_tinder:

    $ v_tinder = True
    scene bg patio with fade
    show marcelo at left with dissolve

    marcelo "Nuevo. Ven. Es una emergencia. Bucha la emergencia."
    "Marcelo te muestra un celular. En pantalla: el Tinder de José."
    mc "¿José tiene Tinder?"
    marcelo "Tiene. Y es un desastre. Mira el perfil."
    "Foto 1: José con una yegua. (La yegua ya no está. La foto sigue.)"
    "Foto 2: José en el Elysium. Se nota que fue una vez. Bio: «Me gusta mi PC»."
    mc "Necesita ayuda. Ayuda profesional."
    marcelo "Por eso te llamé. Somos su equipo. Su cupido de alquiler."
    marcelo "El objetivo real: Cata Toro. La crush de José. Desde el liceo."
    marcelo "José le manda memes desde el liceo. Ella responde «jaja» cada tres semanas."
    marcelo "Con ese historial, necesita milagro. Bucha."

    menu:
        "Escríbele algo normal. Salúdala como persona.":
            marcelo "Aburrido. Pero seguro. Enviando..."
            "Cata Toro responde a las tres semanas. «jaja». Fin de la conversación."
        "Escríbele un poema. A lo Shakespeare de Lincoñir.":
            marcelo "Poema enviado. Tiene rimas. Una de ellas es «Shakira» con «mira»."
            "Cata Toro responde: «ajajaj qué es eso jajaj». No quedó claro si es bueno o malo."
        "Invítala a algo. Directo. Sin miedo.":
            marcelo "Invitación enviada. A tomar once. En su casa. Con la mamá de José."
            "Cata Toro responde: «jajaj ya». Ese «ya» tiene cinco significados posibles."

    "Resultado final del plan: ninguno. José no consiguió pareja. La ciencia lo confirma."
    marcelo "Fracasamos con honra. Bucha."

    show jose at right with dissolve

    jose "Chicos. Buenas y malas."
    jose "Hablé con una del Tinder. Barbarita. De Villarrica."
    mc "¿Y bien?"
    jose "Me ofreció pega. Tres meses. En Villarrica."
    "..."
    mc "¿Pega? ¿Se suponía que no era una cita?"
    jose "Yo tampoco entiendo. Me dijo «tienes buena disposición». Mañana salgo."
    "José no consiguió pareja. Consiguió un contrato. Nadie sabe cómo. Ni él."
    jose "Me voy a Villarrica. Tres meses. Por la Barbarita. No me pregunten."
    marcelo "Bucha. Ni el Tinder entiende lo que pasó."
    "(Evento WHAT IF completado. No es canon. Pero pasó. Y José estará de la Barbarita por mucho tiempo.)"
    $ recuerda("José", "José lo recordará. Y la Barbarita también.")

    jump hub


# =====================================================================
#  WHAT IF: EL TRABAJO EN GRUPO (evento no canon)
# =====================================================================
label whatif_trabajo:

    $ v_trabajo = True
    scene bg patio with fade
    show marcelo at left with dissolve
    show benjamin at right with dissolve

    "Trabajo en grupo. Mínimo tres personas. Marcelo y Benjamín presentes. Y el tercer integrante..."

    show ruben at center with dissolve

    "Rubén. Que abandonó la carrera. Pero apareció igual. A firmar."
    ruben "Yo superviso."
    "Rubén se acomoda en su banca. El trabajo aún no empieza y ya está cansado."

    menu:
        "Hacer la parte de Rubén entre todos.":
            $ apoyo += 1
            $ recuerda("Rubén")
            $ recuerda("Marcelo", "Marcelo NO lo olvidará. Otra vez haciendo la pega de Rubén.", negativo=True)
            "Hacen la parte de Rubén entre todos. Rubén aprueba. Desde la banca. Con los ojos cerrados."
            marcelo "Siempre lo mismo. Bucha la pega de tres."
        "Exigir que Rubén trabaje.":
            $ drama += 1
            $ recuerda("Rubén", negativo=True)
            $ recuerda("Marcelo")
            "Exiges que Rubén trabaje. Rubén suspira. Se levanta. Firma el documento. Se vuelve a acostar."
            ruben "Ya trabajé. Firmé. Mi parte está lista."
            benjamin "Técnicamente... tiene razón. Firmar es su parte."

    "El trabajo se entrega. Nota: siete. Rubén celebra como si hubiera hecho algo. Todos lo dejan. Es más fácil."
    ruben "Chao, chiquillos."
    "(Evento WHAT IF completado. Rubén aprueba la educación superior. Desde afuera.)"
    $ recuerda("Rubén", "Rubén lo recordará. Supervisando.")

    jump hub


# =====================================================================
#  LA HISTORIA COMPLETA (la grabadora, por fin ordenada)
# =====================================================================
label historia_completa:

    scene black with fade
    if fragmentos >= 5:
        "Le das play. Cinco voces. Cinco pedazos. La historia completa, por fin, en orden."
    else:
        "Le das play. Las voces que juntaste. Falta algún pedazo, pero alcanza. La historia, por fin, en orden."
    "Hace tiempo, en Lincoñir, comuna de Padre Las Casas, José Lipian tenía una yegua. Se llamaba Shakira."

    scene bg potrero with fade
    show shakira at left with dissolve
    show jose at right with dissolve

    "La crió de bebé. Desde que se la dieron. Chiquitita. No se podía ni parar bien."
    "José le daba la mamadera. Se levantaba de noche a verla. En invierno le ponía una frazada."
    "Cada mañana, antes de clases, cruzaba el potrero con el desayuno. Y Shakira lo esperaba en la cerca."
    "Todas las mañanas. Todos los días. Año tras año."
    "Le celebraba el cumpleaños. Con torta de zanahoria. Le cantaba. Ella apagaba las velas de un mordisco."

    scene bg atardecer with dissolve
    show shakira at left with dissolve
    show jose at right with dissolve

    "Al atardecer, José se sentaba en la cerca y Shakira apoyaba la cabeza en su hombro."
    "Una vez José se fue un fin de semana. Shakira no comió hasta que volvió."
    "Y cuando volvió, corrió a la cerca. Una yegua entera corriendo como perro."
    shakira "(Iiiiiih.)"

    scene bg potrero with dissolve
    show jose at right with dissolve
    $ musica("triste.ogg")

    "Y un día, José quiso un computador. Uno gamer."
    "No pasó nada especial. No hubo pelea. No hubo crisis. Solo... quiso un computador."
    $ sfx("trueno.ogg")
    "El comprador llegó un sábado en la mañana. Shakira esperaba en la cerca, como siempre, su desayuno."
    "José preguntó el precio. Escuchó la oferta. Y firmó."
    "Sin dudar. Sin llorar. Sin mirar atrás."

    hide jose with dissolve
    show shakira at left with dissolve

    "Se dice que Shakira miró la camioneta irse hasta que dejó de verse. El vecino mapuche tuvo que darle el desayuno ese día."
    shakira "(Iiih.)"
    "El relincho de la grabación no es chistoso. Ya no."
    "José, mientras tanto, fue a comprar la PC. Ese mismo día. Estaba contento."
    "Shakira no entendió. Las yeguas no entienden de papeles. Solo saben quién cruza el potrero con el desayuno."
    "Esperó en la cerca las mañanas siguientes. Todas. José no volvió."
    "El viento deja de soplar. Una paloma de Temuco cae al suelo, ofendida."

    scene bg patio with fade
    show jose at center with dissolve
    show pablo at right with dissolve
    show marcelo at left with dissolve
    $ musica("dramatica.ogg")

    "La grabación termina. Nadie habla. Ni siquiera Marcelo dice qué lata."
    "Bueno."
    marcelo "Qué lata."
    "Pero bajito. Casi con cariño."
    hide pablo
    show benjamin at right with dissolve
    benjamin "Ahora sí, nuevo. AHORA entiendes por qué lo molestamos."
    benjamin "No es solo por la yegua. Es porque él no siente NADA. Y nosotros sí."

    return


# =====================================================================
#  CÓMO ANDA EL GRUPO CONTIGO (medidor de relaciones)
# =====================================================================
label estado_relaciones:

    "Revisas mentalmente cómo anda el grupo contigo."
    "José: [estado('José')]. Pablo: [estado('Pablo')]. Diego: [estado('Diego')]. Fabián: [estado('Fabián')]."
    "Marcelo: [estado('Marcelo')]. Benjamín: [estado('Benjamín')]. Rubén: [estado('Rubén')]. Maxi: [estado('Maxi')]."
    "Bastián: sí."

    jump hub


# =====================================================================
#  CONFRONTACIÓN
# =====================================================================
label confrontacion:

    $ musica("dramatica.ogg")
    scene bg patio with fade
    show jose at center with dissolve
    show pablo at right with dissolve
    show marcelo at left with dissolve

    "Todos reunidos. Frío de Temuco. Marcelo se queja. La música sube."
    mc "Tengo algo que decir. Ya estuve investigando."

    if fragmentos >= 4 and not historia_escuchada:
        mc "Pero antes... escuchen esto. Todo esto."
        $ historia_escuchada = True
        call historia_completa
        hide benjamin
        show pablo at right with dissolve
    elif fragmentos > 0:
        "Te tocas el bolsillo. La grabadora pesa poco: te faltan pedazos de la historia."

    if pista_pablo:
        mc "Pablo, tu asiento esconde una montura."
        pablo "Es una funda ergonómica."
    if pista_diego:
        mc "Cada viernes alguien compra veinte kilos de zanahorias con gafas de sol."
        pablo "Hay mucha gente con gafas de sol."
    if pista_potrero:
        mc "Y en el potrero hay heno fresco."
        jose "Es de mi vecino mapuche."
    if pista_ruben:
        mc "Y tengo un testigo que vio a Shakira cerca de la Shell. Todos los domingos."
        if secreto_ruben:
            mc "Mi fuente prefiere no identificarse. Ni moverse. Ni esforzarse."
            "Desde una banca, a lo lejos, una voz: «¿Y a ti qué te importa?»"
        else:
            mc "Rubén Maldonado. El que no hace nada. Lo vio todo."
            "Desde algún rincón del universo, Rubén murmura: «¿Y a ti qué te importa?»"
    if not (pista_pablo or pista_diego or pista_potrero or pista_ruben):
        mc "He descubierto... que no he descubierto nada."
        marcelo "Qué lata."

    # --- El grupo recuerda lo que hiciste (y lo que no) ---
    if rel["Pablo"] < 0:
        pablo "Todavía me acuerdo de ti, por si acaso. Y no precisamente bien."
    if rel["Fabián"] < 0:
        hide marcelo
        show fabian at left with dissolve
        fabian "Yo también me acuerdo, wn."
        hide fabian
        show marcelo at left with dissolve
    if rel["Marcelo"] < 0:
        marcelo "Bucha. Hasta yo tengo rencores contigo. Y yo tengo rencores con todo."
    if rel["José"] >= 2:
        jose "[nombre] es de los míos. Lo que diga, va en serio."

    jose "¿Y bien? ¿Qué vas a hacer, [nombre]?"

    menu:
        "Acusar a José frente a todos. ¡Es un traidor!":
            $ drama += 3
            jose "¡Más encima que la vendí, justamente! Y legal. Y andan leseando."
            if v_tinder:
                jose "¡Y encima estoy de la Barbarita! ¡Primero la Barbarita y ahora esto!"
                hide pablo
                show benjamin at right with dissolve
                benjamin "¿QUÉ TIENE QUE VER LA BARBARITA CON ESTO?"
                jose "NO LO SÉ. PERO ESTOY."
            jose "Ouuu. Grave. Gravísimo."
        "Hablar con José desde el corazón.":
            $ apoyo += 2
            jose "Gracias, hermano. De verdad."
        "Invitarlo a jugar en su PC y dejar el tema.":
            $ apoyo += 1
            jose "¡Eso! ¡Ven, que te muestro el setup!"
        "Escuchar la propuesta de Benjamín." if broma_benjamin >= 2:
            $ plan_benjamin = True
            "Benjamín se levanta de una banca donde, aparentemente, llevaba sentado todo el rato."
            hide pablo
            show benjamin at right with dissolve
            benjamin "Tengo una solución. Definitiva. Legal. Con papas."
            marcelo "Qué lata. Me tinca."

    # --- Elección de final ---
    if plan_benjamin:
        jump final_fundo
    elif pista_pablo and pista_diego and pista_potrero and drama < 5:
        jump final_verdadero
    elif drama >= 5:
        jump final_funeral
    elif apoyo >= 6 and rel["José"] >= 2:
        jump final_empeno
    elif apoyo >= 3:
        jump final_custodia
    else:
        jump final_gamer


# =====================================================================
#  FINALES
# =====================================================================
label final_verdadero:

    $ musica("tema.ogg")
    show jose at center with dissolve
    show pablo at right with dissolve
    show marcelo at left with dissolve
    "Las pistas se alinean como cartas de póker. Todas apuntan al mismo sospechoso."
    pablo "Está bien. ESTÁ BIEN. ¡Fui yo!"
    "Un trueno cruza el cielo. Marcelo, por una vez, no se queja."
    pablo "Con parte de los dos millones le compré a Shakira al vecino mapuche de José. Era mi lecera más grande."
    pablo "El resto sí fue en leceras: más gafas, más shorts, un computador y el Monster Hunter."
    pablo "Y doscientas lucas en arreglar ese mismo computador en Infosur. Era el cargador."
    if pablo_arruinado:
        pablo "Y debo una Shell. Pero tranquilos: ya estoy apostando para recuperarla."
    hide marcelo
    show diego at left with dissolve
    diego "¿Y las zanahorias?"
    pablo "Alimentación equilibrada."

    scene bg atardecer with fade
    show shakira at left with dissolve
    show jose at right with dissolve
    $ sfx("relincho.ogg")
    shakira "(Iiiiiih.)"
    jose "Pablo... eres mi mejor amigo."
    jose "Pero la PC se queda."
    shakira "(Relincha con desaprobación.)"
    "Shakira vive, tiene dos dueños, tres amigos y veinte kilos de zanahorias a la semana."

    if historia_escuchada:
        "José mira a Shakira un segundo de más. Algo se mueve en su cara. Casi. CASI se mueve."
        show benjamin at center with dissolve
        benjamin "(susurrando) ¿Vieron eso? ¿VIERON ESO?"

    if verdad_martin:
        show bastian at center with dissolve
        bastian "Ni el Shen Shen en 'China' vio un desenlace así."
        "Silencio absoluto. Todos se giran hacia Bastián."
        show benjamin at left with dissolve
        benjamin "Habló Bastián. ESTO es histórico. Más histórico que el caso."
        jose "¡Ese es mi Bastián! Yo siempre le hablo. ¡Sabía que podía!"
    if pista_ruben:
        show ruben at right with dissolve
        "Desde una banca, Rubén levanta el pulgar. Es el mayor esfuerzo que se le ha visto."
        ruben "Chao, chiquillos."

    $ persistent.finales.add(1)
    "FINAL 1 de 6: La lecera más cara (final verdadero)"
    jump creditos


label final_custodia:

    "Todos entienden que Shakira no volverá a vivir en el potrero de José."
    "Pero el vecino mapuche, conmovido, propone una solución."
    scene bg atardecer with fade
    show shakira at left with dissolve
    show jose at right with dissolve
    jose "Custodia compartida. Los fines de semana la visito."
    jose "Y en la semana juego en mi PC. Con ella mirándome por la ventana."
    shakira "(Iiiiiih.)"
    "Es el acuerdo más extraño y emotivo de la historia de Padre Las Casas."

    $ persistent.finales.add(2)
    "FINAL 2 de 6: La custodia compartida"
    jump creditos


label final_funeral:

    $ musica("triste.ogg")
    scene bg funeral with fade
    "Por culpa de tanta acusación, la investigación terminó en tragedia absoluta."
    "Shakira, legendaria yegua, murió como vivió: galopando hacia el atardecer..."
    "...y chocando con un letrero que decía 'Ceda el paso'."
    "(El narrador asegura que fue una muerte heroica. El narrador ya no tiene credibilidad.)"

    show marcelo at left with dissolve
    show pablo at right with dissolve
    marcelo "Bucha los funerales. Qué lata la vida."
    pablo "Brad Pitt también iría de lentes a un funeral. Es un tema de respeto."
    if pablo_arruinado:
        "Las gafas son falsas, eso sí. Empenó las originales para seguir apostando."
    show fabian at center with dissolve
    fabian "Esto se despide con cumbia villera, wn. Es lo que hay."
    "Fabián toca una cumbia villera en el celular. Es la cumbia villera más triste jamás grabada."
    show jose at left with dissolve
    jose "Perdóname, Shakira."
    "José hace una pausa. Todos contienen el aire."
    jose "...aunque técnicamente fue una venta legal."
    hide jose
    show marcelo at left with dissolve
    marcelo "Ni en el funeral se quiebra. Qué frío. Aaah qué lata."
    "La PC gamer, desde su escritorio, no emite luz alguna. Ni RGB. Por respeto."

    if v_liceo:
        "Un Suzuki Jeep 4x4 abre la procesión fúnebre. Héctor filma todo. «Contenido», susurra con respeto."
        "El profe Martín manda un audio: «En China los funerales son distintos. Cuando estuve en Shenzhen...» Nadie lo escucha."

    "Y aquí viene la parte que la familia de Shakira pidió no publicar."

    scene escena asado with fade
    show benjamin at left with dissolve
    show fabian at right with dissolve
    show jose at center with dissolve

    "Benjamín, fiel a la ley del campo («no se desperdicia nada»), organizó un asado en el Fundo El Carmen."
    "Con la carne de... bueno. Ustedes entienden."
    "Invitado de honor: Fabián Millalén, de Pillalelbún. Llevó el carbón. Y la cumbia villera."
    fabian "Hermano, a un asado no se falta. Es código."
    benjamin "Fue un homenaje. Un homenaje con pebre."
    jose "...Al menos no la desperdiciaron."
    "Esa frase de José es lo más perturbador del juego. Y eso que la competencia es dura."

    $ persistent.finales.add(3)
    "FINAL 3 de 6: El funeral de Shakira"
    jump creditos


label final_empeno:

    $ musica("dramatica.ogg")
    scene bg patio with fade
    show jose at center with dissolve

    "José pide la palabra. Tiene cara de alguien que va a decir algo grande."
    jose "Tengo que confesar algo. No la vendí."
    "Silencio. El mundo se detiene. Marcelo deja de respirar."
    mc "¿Cómo que no la vendiste? Todos vimos..."
    jose "La empeñé."
    show benjamin at left with dissolve
    benjamin "¿LA QUÉ?"
    jose "La empeñé. Como quien empeña un anillo. Un pagaré. Plata altiro, sin venta. Con ella de garantía."
    "No la vendió. La usó de colateral. Para un préstamo. Para comprar la PC."
    "Es peor que venderla. Es PEOR. Al menos la venta era honesta."
    jose "El plazo vence esta semana. Si no pago, se la queda el prestamista."
    mc "¿Y por qué no vendes la PC para pagar?"
    jose "..."
    jose "Porque es mi PC."
    "Nadie dice nada. La calma de José acaba de superar su propio récord."
    "Y entonces, cuando todo parece perdido..."

    show pablo at right with dissolve
    pablo "¡¡GANÉ!! ¡OTRA VEZ! ¡EL CASINO! ¡DOS MILLONES!"
    "El grupo entero grita. Pablo, por una vez, no duda ni un segundo."
    pablo "Vamos a rescatar a la yegua. Ya perdí una lecera grande. No pienso perder otra."

    scene escena atardecer_cerca with dissolve
    show jose at right with dissolve
    show benjamin at left with dissolve
    "Pagan el pagaré. Shakira vuelve al potrero. Entera. Sana. Mirando la cerca como si nada."
    jose "Aprendí la lección."
    benjamin "¿Cuál?"
    jose "Empeñar es mala idea."
    benjamin "...Te salvaste del asado. DE PEDO."
    "José conserva la PC. Y a Shakira. Y una deuda con Pablo. Para siempre."
    "Todos celebran. Hasta Marcelo sonríe. Hasta Rubén se mueve. Un milagro."

    $ musica("tema.ogg")
    scene black with fade
    "Y entonces Pablo despertó."
    "Estaba dormido en el patio del INACAP, con la boca abierta, como siempre."
    "Nada de lo anterior había pasado. Ni el empeño. Ni los dos millones. Ni el rescate."
    "José la vendió. Punto. La PC sigue ahí. Y Pablo sigue sin un peso."
    show pablo at center with dissolve
    pablo "Soñé que la salvábamos."
    pablo "Qué pesadilla tan bonita."

    $ persistent.finales.add(6)
    "FINAL 6 de 6: El empeño (que nunca pasó)"
    jump creditos


label final_gamer:

    scene bg inacap with fade
    show jose at center with dissolve
    jose "¿Sabes qué? No me arrepiento. Era una yegua. La vendí. Fin."
    "Lo dice con la calma de siempre. Y eso, para el grupo, es mil veces peor que cualquier confesión."

    if historia_escuchada:
        "Y tú, que escuchaste la historia entera, sabes exactamente qué se perdió ese sábado en la mañana. Eso también es mil veces peor."
    "Nadie pudo demostrar nada. Nadie pudo condenar a nadie. El misterio de Shakira sigue sin resolverse."
    "Y todos los fines de semana, en algún lugar de Temuco, alguien le pregunta a Pablo en qué se gastó los dos millones."
    show pablo at right with dissolve
    pablo "En puras leceras."

    if v_tinder:
        "José volvió de Villarrica a los tres meses. Sin pareja. Con experiencia laboral. Nadie preguntó nada."

    if verdad_martin:
        show bastian at left with dissolve
        bastian "Como decía el profe Martín: esto en China no pasa. Bueno, según él."
        show benjamin at right with dissolve
        benjamin "¿¡Habló Bastián!? ¡Pachoclo, hablaste!"
        bastian "..."
        jose "Dice que sí habló."

    jose "Chao, chiquillos."
    "Lo dice igual que Rubén. Textual. El grupo entero se ofende."

    $ persistent.finales.add(4)
    "FINAL 4 de 6: El gamer eterno"
    jump creditos


label final_fundo:

    $ musica("triste.ogg")
    scene bg fundo with fade
    show benjamin at center with dissolve

    benjamin "Propuesta: Fundo El Carmen. Este sábado. Traigan carbón."
    mc "¿Carbón? ¿Para qué?"
    benjamin "Para el asado de la discordia."
    "Silencio. Marcelo deja de quejarse. Pablo se quita las gafas de sol por primera vez en la historia registrada."
    benjamin "Acuérdate de la ley. La que le puse a José en la primera visita: si algún día vendía a Shakira, yo la hacía asado."
    benjamin "Era un anti-final. Una amenaza pa que nunca la vendiera. Mientras existiera la amenaza, Shakira estaba a salvo."
    benjamin "Pero la vendió. Y una amenaza que no se cumple no es una lección. Es decoración."
    mc "Benjamín... ¿qué hiciste?"
    benjamin "Lo que prometí. Fui donde el vecino mapuche y le compré a Shakira. Boleta, certificado, transferencia. Todo legal."
    benjamin "Injusto... pero legítimo. Como la venta de José. Exactamente como la venta de José."
    show marcelo at left with dissolve
    marcelo "Bucha. Ni para los trabajos de ciberseguridad movió un dedo. ¿Y para ESTO hizo trámites?"
    benjamin "Era por una lección. Alguien tenía que darla. Y la lección se sirve con papas."

    show jose at right with dissolve
    jose "¿Y yo qué tengo que ver en todo esto?"
    benjamin "También hice tus papeles, José."
    jose "¿QUÉ?"
    benjamin "Bistec de Lipian. Injusto. Pero legítimo."
    "Nadie supo cómo consiguió esos papeles. Nadie quiso saber. El notario tampoco quiso saber."

    scene escena asado with fade
    show benjamin at center with dissolve

    "El sábado, en Fundo El Carmen, hubo asado. En la parrilla, la leyenda de Shakira llegó a su fin. Con papas. Y pebre."
    "Fabián puso a Yerba Brava. Nadie se la pidió. Todos la agradecieron. Pablo trajo las zanahorias, por costumbre. Rubén apareció sin que nadie lo invitara."
    show ruben at left with dissolve
    ruben "¿Y a ti qué te importa? ...Guárdame un pedazo. Y que no sea el duro."
    "Maxi Valenzuela llegó caminando desde Pedro de Valdivia. Nadie lo invitó. Nadie lo vio llegar. Ya estaba sirviéndose."
    show maxi at right with dissolve
    maxi "Conchetumare, Benjamín. Esto es lo más enfermo y lo más legal que he visto en mi vida, wn. Te admiro, negro."
    "Bastián cortó la leña. No dijo nada. Nunca dice nada. Pero cortó la leña perfecta."
    "Iván Garrido del 4F llegó por su cuenta. Nadie lo invitó. Traía ensalada. Nadie tocó la ensalada."
    show ivan at center with dissolve
    ivan "Yo solo vine a reírme y a comer, wn. Y ya me reí."
    "Héctor filmó todo con el Suzuki Jeep de fondo. El video tiene tres millones de visitas. El algoritmo es un misterio."
    "Marcelo quiso subir la crónica a premierchilito, pero no era fútbol. Qué lata."
    "Del bistec de Lipian no se hablará. Este narrador tiene límites. Pocos, pero tiene."

    $ persistent.finales.add(5)
    "FINAL 5 de 6: El asado del Fundo El Carmen (final oscuro)"
    jump creditos


# =====================================================================
#  AL CARGAR UNA PARTIDA: recordatorio de dónde quedaste
# =====================================================================
label after_load:

    scene black with fade

    "Bienvenido de vuelta, [nombre]. Esto es lo último que pasaba:"

    if venta:
        "José ya vendió a Shakira. El grupo sigue entre el duelo y el leseo."
    elif potrero_visitas > 0:
        "Aún no pasa nada grave. Has visitado Lincoñir [potrero_visitas] de 3 veces. Shakira sigue ahí. De momento."
    else:
        "Recién estás conociendo al grupo en el INACAP."

    "Tienes [fragmentos] de 5 fragmentos grabados de la historia de Shakira."

    if fragmentos > 0 and fragmentos < 4:
        "Te faltan pedazos de la historia por grabar."

    if max(rel.values()) > 0:
        $ amigo = max(rel, key=lambda k: rel[k])
        "Quien más te aprecia hasta ahora: [amigo]."
    if min(rel.values()) < 0:
        $ pendiente = min(rel, key=lambda k: rel[k])
        "Y [pendiente] te tiene mala. Cuidado con eso."

    "Eso. A seguir, po."

    return


# =====================================================================
#  CRÉDITOS
# =====================================================================
label creditos:

    scene black with fade
    $ n_finales = len(persistent.finales)

    "RADAL — la novela gráfica."
    "Creado por Benjamín Seguel."
    "Soundtrack original: «Josep Lipian Iceberg», escrita y producida por Fabián Millalén (Fabinho)."

    "Y desde ese año, nadie ha dejado de molestar a José. Ni un solo día."
    "Has desbloqueado [n_finales] de 6 finales."

    if max(rel.values()) > 0:
        $ amigo = max(rel, key=lambda k: rel[k])
        "Tu mejor amigo del semestre: [amigo]."
    if min(rel.values()) < 0:
        $ pendiente = min(rel, key=lambda k: rel[k])
        "Y [pendiente] todavía te tiene mala. Para siempre."

    if v_inundacion:
        "Pillalelbún sigue en pie. La próxima inundación se espera para 2034."

    if promesa_marcelo:
        "Marcelo tiene un seguidor nuevo en premierchilito. Son 141.001. Sigue siendo qué lata, pero menos."
    if pablo_arruinado:
        "Pablo sigue apostando para pagar la Shell. Perdió el short apostando. Sigue en short."
    if v_sueno:
        "Y Pablo sigue soñando con un Pillalelbún próspero. Le apuesta a todo... menos a la realidad."

    "Dedicado con cariño a José, Pablo, Diego, Fabián, Marcelo, Benjamín, Bastián, Rubén y Maxi..."
    "...a Bastián dos veces, porque habla tan poco que hay que nombrarlo por él..."
    "...a Iván Garrido del 4F, que esquivó la milicia con un solo PDF..."
    "...y a Diego, primer año eterno, a quien el ejército se lo perdió por no tener un sicólogo con criterio..."
    "...al profe Martín, que algún día llegará de verdad a Shenzhen..."
    "...a Héctor y su Suzuki Jeep cuatro por cuatro..."
    "...y a Shakira, dondequiera que esté. Probablemente comiendo zanahorias. Esperamos."
    "Gracias por jugar."

    return
