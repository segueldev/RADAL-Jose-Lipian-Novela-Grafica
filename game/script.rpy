# RADAL 1.2 — novela visual chilena.
# Ocho comienzos, decisiones recordadas y siete finales.
# Recursos del proyecto; ayudas de audio toleran archivos opcionales.

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
default prologo = 0        # qué prólogo salió (1-5); se sorteaba solo con $
default lugares = 0        # lugares visitados; se recalcula en cada vuelta al hub

default persistent.finales = set()

# ---------------------------------------------------------------------
#  Placeholders y ayudas de audio / notificaciones
# ---------------------------------------------------------------------
init python:

    def fondo(texto, color, sub=None):
        partes = [Solid(color)]
        if sub:
            partes.append(Text(texto, size=90, color="#ffffff", xalign=0.5,
                               yalign=0.14, outlines=[(3, "#000000", 0, 0)]))
            partes.append(Text(sub, size=46, italic=True, color="#ffffff",
                               xalign=0.5, yalign=0.26,
                               outlines=[(2, "#000000", 0, 0)]))
        else:
            partes.append(Text(texto, size=90, color="#ffffff", xalign=0.5,
                               yalign=0.14, outlines=[(3, "#000000", 0, 0)]))
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
                     yalign=0.15, outlines=[(3, "#000000", 0, 0)], text_align=0.5),
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
        musica_fabian(archivo)

    def sfx(archivo):
        return efecto_radal(archivo)

    def recuerda(quien, msg=None, negativo=False, puntos=None):
        # Aviso compacto y cambio de relación.
        if puntos is None:
            puntos = -1 if negativo else 1
        if quien in store.rel:
            store.rel[quien] = store.rel.get(quien, 0) + puntos
        if msg is None:
            msg = quien + (" NO lo olvidará." if negativo else " lo recordará.")
        renpy.hide_screen("aviso_whatif")
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
            "Revisé el horario anoche y lo cambiaron hoy. Avisan cuando uno ya viene en la micro.",
            "La cafetería abrió, pero el té no llegó. Ya ni pregunto por qué.",
            "Se cayó el wifi justo cuando estaba subiendo el video. Ahora va a quedar al tres por ciento todo el día.",
            "¿Quién dejó este cable acá? Después dicen que uno reclama por gusto.",
        ]
        por_clima = {
            "lluvia": ["Se me mojó el calcetín entero. El paraguas sirve pa todo menos pa eso.",
                       "La micro pasó por el charco justo cuando estaba en la esquina. Mira el pantalón."],
            "frio": ["Salí sin guantes. Pésima idea. No siento los dedos.",
                     "Sacaron los calefactores y dejaron la puerta abierta. Ahí está la solución."],
            "sol": ["Traje parka por la lluvia y ahora me sobra. Pero no la voy a dejar botada.",
                    "Da el sol justo donde estaba sentado. Me corro y quedo al lado del parlante de Fabián."],
            "nublado": ["Está helado igual. El sol anda puro amagando."],
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
            "Tremendo frío. Habían unos calefactores en el comedor, pero los sacaron.",
            "Día de sol sospechoso. Todos desconfían.",
            "Día nublado. Ni frío ni calor. Fome.",
            "Día de viento. El Megaficticias lo llamó «brisa». Miente.",
        ])

    def frag():
        # Suma un fragmento de la historia de Shakira a la grabadora.
        store.fragmentos += 1
        renpy.hide_screen("aviso_whatif")
        renpy.show_screen("aviso_recuerda", "Fragmento grabado (" + str(store.fragmentos) + " de 5)")

    def whatif(msg):
        # Notificación de misión WHAT IF disponible.
        renpy.hide_screen("aviso_recuerda")
        renpy.show_screen("aviso_whatif", msg)

# Sprites reales
image jose     = sprite("images/jose.png")
image jose gym = sprite("images/jose gym.png")
image pablo = sprite("images/eventos/pablo_gafas.png")
image pablo sin_gafas = Fixed(
    Transform("images/pablo.png", crop=(50,200,825,995), xysize=(520,860), fit="contain", xalign=0.5, yalign=1.0),
    xsize=520, ysize=860, yoffset=-250)
image pablo completo = sprite("images/pablo cuerpo completo.png")
image pablo shell = sprite("images/pablo shell.png")
image diego    = sprite("images/diego.png")
image fabian   = sprite("images/fabian.png")
image marcelo  = sprite("images/marcelo.png")
image benjamin = sprite("images/benjamin.png")
image bastian  = sprite("images/bastian.png")
image ruben    = sprite("images/ruben.png")
image maxi     = sprite("images/maxi.png")
image ivan     = sprite("images/ivan.png")
image martin   = sprite(Crop((275, 94, 620, 776), "images/martin.png"))
image hector   = sprite(Crop((600, 420, 1150, 1450), "images/hector.png"))
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
image escena atardecer_cerca = Composite(
    (1920, 1080), (0, 0), cover("images/bg potrero.png"),
    (420, 0), Transform("images/escena atardecer_cerca.png", xysize=(1070, 800), fit="contain"))
image escena venta_camioneta = Composite(
    (1920, 1080), (0, 0), cover("images/bg potrero.png"),
    (1160, 0), sprite("images/escena venta_camioneta.png", alto=800, alza=0))
image escena short = Fixed(
    Solid("#101010"),
    Transform("images/escena short.png", crop=(320, 0, 290, 164),
              xysize=(900, 510), fit="contain", xalign=0.5, yalign=0.25),
    xysize=(1920, 1080))

# Fondo del menú principal
image menu_bg = cover("images/menu.jpg")

# Video de fondo: Pillalelbún inundado (sin sonido)
image bg inundado = Movie(play="images/bginundado.webm", loop=True, audio=False, size=(1920, 1080))

# Variantes de los escenarios fotográficos existentes.
image bg fundo = cover("images/bg potrero.png")
image bg funeral = Transform(cover("images/bg potrero.png"), matrixcolor=SaturationMatrix(0.15) * BrightnessMatrix(-0.18))
image bg atardecer = Transform(cover("images/bg potrero.png"), matrixcolor=TintMatrix("#ffe1bc") * BrightnessMatrix(-0.08))

# Encuadres y variaciones de luz; sin carteles provisionales.
image bg cisterna_patio = "escena cisterna_pablo"
image bg cisterna_int = "escena cisterna_pablo"
image bg shell_ruinas = cover("images/eventos/shell_destruida.jpeg")
image bg pesebre = Transform(cover("images/bg potrero.png"), zoom=1.18, xalign=0.18, yalign=0.65)
image bg asado = Transform(cover("images/bg potrero.png"), matrixcolor=TintMatrix("#ffe9cb"))

# Escenas compuestas con recursos reales del proyecto.
image escena cisterna_pablo = Composite(
    (1920, 1080), (0, 0), cover("images/bg shell.png"),
    (290, 280), Transform("images/escena cisterna_pablo.png", xysize=(1340, 700), fit="contain"))
image escena choque = Transform("escena cisterna_pablo", rotate=-2.0, zoom=1.08, matrixcolor=SaturationMatrix(0.7))
image escena martin_clase = "bg sala_liceo"
image escena asado = Composite(
    (1920,1080), (0,0), "bg asado",
    (560,410), Transform("images/eventos/parrilla.png", xysize=(820,610), fit="contain"))
image escena sueno_ruta = Transform(cover("images/bg sueno.png"), matrixcolor=TintMatrix("#fff0cd"))


# ---------------------------------------------------------------------
#  Aviso grande de consecuencias ("X lo recordará", fragmentos)
# ---------------------------------------------------------------------
transform bastian_bajo:
    # Baja la foto de cuerpo completo para que la cabeza no quede en el cielo.
    yoffset 160

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
        yalign 0.02
        background "#000000cc"
        padding (24, 12)
        at recuerda_appear
        text msg:
            xmaximum 1400
            size 32
            color color
            outlines [(3, "#000000", 0, 0)]
            xalign 0.5
    timer 5.0 action Hide("aviso_recuerda", dissolve)

screen aviso_whatif(msg):
    zorder 200
    frame:
        xalign 0.5
        yalign 0.02
        background "#3d1a5ecc"
        padding (24, 12)
        at recuerda_appear
        text ("¿Y SI…?\n" + msg):
            xmaximum 1400
            size 30
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
        nombre = nombre.strip().replace("{", "{{")
        if not nombre:
            nombre = "Kabro"

    if persistent.finales:
        menu:
            "¿Cómo querís conocer a los cabros esta vez?"
            "Ir al grano. Ya ubico las tallas.":
                $ presentacion_corta = True
            "Escuchar la presentación completa.":
                $ presentacion_corta = False

    # Ocho entradas: se agotan antes de repetir una.
    $ prologo = siguiente_inicio()

    if prologo == 1:
        jump prologo_lluvia
    elif prologo == 2:
        jump prologo_frio
    elif prologo == 3:
        jump prologo_sol
    elif prologo == 4:
        jump prologo_tarde
    elif prologo == 5:
        jump prologo_temprano
    elif prologo == 6:
        jump inicio_cisterna
    elif prologo == 7:
        jump inicio_sala
    else:
        jump inicio_termo


# ---------------------------------------------------------------------
#  Encuentros reutilizables (seguros: solo contenido del presente)
# ---------------------------------------------------------------------
label encuentro_pablo:

    # Primer plano del short: el Pablo normal queda fuera del encuadre
    # durante el zoom (si no, se encima el plano cortado) y vuelve a la
    # esquina cuando termina el enfoque.
    show escena short at center with dissolve
    mc "(¿Eso es... un short?)"
    hide escena short with dissolve
    show pablo completo at right with dissolve

    show pablo at right with dissolve
    pablo "Buenos días."

    menu:
        "Oye, ¿no tenís frío?":
            $ pablo_molesto = True
            $ recuerda("Pablo", negativo=True)
            pablo "No, po. Estoy bien."
            "Sus piernas, azules, opinan distinto."
        "Bacán tus gafas.":
            $ recuerda("Pablo")
            pablo "Lo sé."
            pablo "Me veo como Brad Pitt con ellas."
            "Marcelo lo mira y prefiere seguir tomando su café."
            "Se nota que está cagado de frío. Se hace el bacán, el Pablo."
        "No decir nada y seguir caminando.":
            "Sigues caminando. Pablo se acomoda las gafas igual, por si miras de nuevo."

    show pablo at right with dissolve
    return


label quejas_marcelo:

    show marcelo at left with dissolve
    marcelo "[queja_marcelo()]"
    marcelo "Más encima compré café y ni me gusta. No había té."
    marcelo "Dormí como tres horas. Vine temprano pa avanzar el trabajo y no hay ni dónde enchufar el compu."
    mc "(Recién lo conozco y ya se quejó de seis cosas distintas. Récord.)"

    menu:
        "Ya, pero recién llegamos, Marcelo.":
            $ apoyo += 1
            $ recuerda("Marcelo")
            marcelo "¿Tenís clases hasta las seis tú también? Ahí te quiero ver."
        "Sí, está penca la mañana.":
            $ drama += 1
            $ recuerda("Marcelo", "Marcelo aprueba tu pesimismo.")
            marcelo "Ya, por lo menos alguien me entiende."

    return


# ---------------------------------------------------------------------
#  PRÓLOGO 1: LA LLUVIA
# ---------------------------------------------------------------------
label prologo_lluvia:

    $ clima = "lluvia"
    scene bg inacap_lluvia with fade
    "Temuco. Lunes. 7:55 de la mañana."
    "Llegas con las zapatillas mojadas. La entrada está llena de gente sacudiendo paraguas."
    "Y tú eres el nuevo."
    "Primer día en el INACAP de Temuco. Tienes el horario en el celular, pero no pillas la sala."
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
    scene bg entrada_seca with fade
    "Temuco. Lunes. 7:55 de la mañana."
    "No llueve. Peor: hace un frío seco que pela la cara. El Megaficticias lo llamó «fresco». Miente."
    "Llegas al INACAP con el horario abierto. Todavía no conoces a nadie."
    mc "Me llamo [nombre]. Primer día. Frío seco. Se me congelan las ideas."

    call quejas_marcelo
    "Y entonces, desafiando el frío seco, aparece un joven en short corto y gafas de sol."
    $ bg_prologo = "bg entrada_seca"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRÓLOGO 3: SOL SOSPECHOSO
# ---------------------------------------------------------------------
label prologo_sol:

    $ clima = "sol"
    scene bg escaleras with fade
    "Temuco. Lunes. 7:55 de la mañana. Sale el sol. En Temuco. En invierno."
    "Te sacas la parka. A los cinco minutos te la vuelves a poner."
    "Llegas al INACAP con el horario abierto. Todavía no conoces a nadie."
    "Un grupo está parado en la entrada. Te acercas a preguntar por tu sala."

    call quejas_marcelo
    "Con el sol afuera, un joven en short y gafas de sol se acerca con la satisfacción del que tenía razón."
    show pablo at right with dissolve
    pablo "¿Ven? Y ustedes con parka."
    $ bg_prologo = "bg escaleras"
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

    show bastian at center, bastian_bajo with dissolve
    "Un muchacho de complexión de gimnasio te señala uno. En silencio."
    mc "(¿Ese?)"
    "Asiente."
    bastian "Sí."
    "Es lo primero que te dice alguien en este instituto. Un sí. Prometedor."
    "Sobrevives a la primera clase. No entendiste nada. Según el Megaficticias, eso también es normal."

    scene bg patio with fade
    "En el recreo te acercas a los cabros que estaban afuera de la sala."
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

    # Fin de la perrera: si quedan en pantalla, Marcelo y Pablo los tapan.
    hide perro1
    hide perro2
    call quejas_marcelo
    "A las 7:55, con el Megaficticias anunciando menos treinta grados, aparece un joven en short corto y gafas de sol."
    $ bg_prologo = "bg patio"
    call encuentro_pablo

    jump intro_grupo


# ---------------------------------------------------------------------
#  PRESENTACIÓN DEL GRUPO (común a todos los prólogos)
# ---------------------------------------------------------------------
label intro_grupo:

    if presentacion_corta:
        jump grupo_al_grano

    # Los prólogos dejan sprites en pantalla (Marcelo de quejas_marcelo,
    # Pablo de encuentro_pablo, Fabián, Bastián y los perros). Se ocultan
    # acá para que cada uno entre cuando le toca, sin quedar tapando a
    # Fabián ni a Bastián al inicio del intro.
    hide marcelo
    hide pablo
    hide fabian
    hide bastian
    hide perro1
    hide perro2
    with dissolve

    show diego at center with dissolve

    diego "Ojo, nuevo: yo salgo directo al Jumbo del Portal después de clases, a la sección Hasbro. Estoy juntando plata para un computador."
    mc "¿Por qué tan específico?"
    diego "Mi gato me meó la laptop Junaeb. Esa es la historia. No hay más."

    menu:
        "¿Y el gato? ¿Sigue suelto?":
            diego "Sí, po. Durmiendo arriba del compu malo, más encima."
            $ recuerda("Diego")
        "Cómprale un teclado al gato. Para que aprenda.":
            $ drama += 1
            diego "¿Pa que mee el teclado también? No, po."
            "El gato, en efecto, sigue suelto. Y manda."

    if not v_fabian_intro:
        show fabian at left with dissolve
        fabian "Y yo soy Fabián. De Pillalelbún. Aguante el Colo Colo."
    show fabian at left with dissolve
    "Fabián deja el celular en la mesa. Suena [cumbia_del_dia()]. Marcelo corre su café antes de que lo bote."

    hide diego
    hide fabian
    show bastian at left, bastian_bajo with dissolve

    "Al fondo, un muchacho de complexión de gimnasio saluda con la mano. No dice ni una palabra."
    "Se acerca otro muchacho a presentarlo. Este sí habla. Mucho."

    show benjamin at center with dissolve

    benjamin "Ese es Bastián Poblete. El Pachoclo."
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
            mc "(Dijo que sí, pero no sacó ni la billetera.)"
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
    hide bastian
    show marcelo at left with dissolve
    marcelo "Le queda a veinte minutos y habla como si necesitara pasaporte."
    benjamin "Cuando tengamos aduana no te voy a dejar entrar, Marcelo."

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
    mc "(Estos llevan años con las mismas tallas. Voy a tener que preguntar.)"

    show diego at right with dissolve
    $ sfx("mensaje.ogg")
    "A Diego le llega un WhatsApp. Lo lee en voz alta, porque Diego es así."
    diego "«Diego. Me inscribí en el ejército. Me voy a Lonquimay. Cuídate, culiao.»"
    "Diego responde con un sticker. Todos lo miran."
    diego "El Nico Jara. Del liceo. Se inscribió en el ejército. Se va a Lonquimay."
    marcelo "Pudo haber avisado antes, po. Le seguíamos guardando puesto."
    benjamin "Mientras Iván Garrido esquivaba la milicia con un certificado de alumno regular (un PDF, pa que se entienda), el Nico Jara se inscribió voluntario. Dos estrategias. Dos leyendas."

    menu:
        "¿Tan terrible es la milicia?":
            diego "El llamado del ejército. Te pueden llamar a los 18. Hay que sacárselo como sea."
            marcelo "A mí me llega un correo con trámite y ya me echa a perder la mañana."
        "Bastante normal el Nico, ¿no?":
            benjamin "Dicen que es el más popular del liceo. Pero es falso."
            benjamin "El wn siempre se quedaba dormido."
            benjamin "Una vez trajo una frasada pa acomodarse en la silla, en la sala de clases."
            benjamin "Al profe le dio lo mismo."
            benjamin "El profe de después lo retó y le hizo sacar la frasada."
    benjamin "Aunque hablando de inscripciones al ejército, nadie tiene más historia que Diego."
    diego "No saquemos ese tema."
    marcelo "Diego también se inscribió. Después volvió diciendo que el sicólogo no cachaba nada."
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
        scene expression bg_prologo with dissolve

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
    "Diego ya se sabía la respuesta. La repite al mismo tiempo que Pablo."
    mc "¿Dos millones?"
    diego "Del casino. Cuando ganó dijo que se iba a comprar una moto."
    pablo "Todavía me la puedo comprar."
    diego "¿Con cuáles lucas?"
    pablo "Cuando gane de nuevo."


    hide diego
    show marcelo at left with dissolve
    marcelo "Ya, dejen los dos millones un rato. José todavía no le muestra a Shakira."
    mc "¿Quién es Shakira?"
    "Fabián pausa la música para escuchar. No alcanza: Benjamín ya está hablando."

    show benjamin at center with dissolve
    benjamin "La yegua del José. Te íbamos a mostrar una foto, pero tiene como doscientas."
    hide pablo
    show diego at right with dissolve
    diego "Se llama Shakira. Sí. Shakira."
    marcelo "Por la cantante, sí. José ya hizo la talla de las caderas. No se la pidai otra vez."
    hide benjamin
    show fabian at center with dissolve
    fabian "La quiere harto. Demasiado, diría yo."
    hide diego
    show benjamin at right with dissolve
    benjamin "Y la sube al Facebook. Sube fotos de su yegua al Facebook. Como quien sube fotos de su hijo."
    mc "¿Y eso es malo? Suena... sano."
    benjamin "No, si por eso lo molestamos. Le tiene más fotos que a nosotros."

    scene expression bg_prologo with fade
    show diego at left with dissolve
    show pablo at right with dissolve
    show benjamin at center with dissolve

    hide benjamin
    show jose at center with dissolve

    jose "¿Están hablando de Shakira?"
    jose "Es mi yegua. La crié de bebé, desde que me la dieron. ¿Algún problema?"
    hide diego
    show benjamin at left with dissolve
    benjamin "Ninguno, José. Ninguno. Eso es lo que nos preocupa."

    hide benjamin
    show bastian at left, bastian_bajo with dissolve
    "José se gira hacia Bastián, que está ahí. Siempre está ahí."
    jose "Tú me entiendes, ¿cierto, Bastián?"
    bastian "..."
    jose "Dice que sí."
    "Bastián asiente con la cabeza. José asiente de vuelta. Comunicación total."
    hide bastian
    show benjamin at left with dissolve
    benjamin "José le saca conversa al Bastián. Nosotros preguntamos tres weás juntas y no lo dejamos responder."
    hide benjamin
    show diego at left with dissolve

    diego "Y no le hagan mucho caso a José: desde que se metió al Elysium se cree mejor que todos."
    show jose gym at center with dissolve
    jose "Sí, voy. ¿Qué tanto? Por lo menos yo uso la membresía."
    hide diego
    show benjamin at left with dissolve
    benjamin "Se le suben los humos. Llega con polera de entrenamiento. Sube historias en el espejo."
    jose "Por lo menos yo voy, po. No como otro que paga pa puro subir la historia."
    benjamin "Y Diego también se metió al Elysium, ¿cachai? Lo paga todos los meses."
    benjamin "No va nunca."
    hide benjamin
    show diego at left with dissolve
    diego "Iba harto antes. Ahora estoy ocupado."
    hide diego
    show marcelo at left with dissolve
    marcelo "Anoche hizo live hasta las dos. Lo sé porque me llegó la notificación cuando estaba durmiendo."
    hide marcelo
    show benjamin at left with dissolve
    benjamin "Se hace llamar «Ryu». Y a la gente le dice «cabezón»."
    hide benjamin
    show diego at left with dissolve
    diego "Es que así se saluda en los lives. «¿Cabezón, cómo estai?». Es mi marca."

    show jose at center with dissolve
    "Los cabros te miran. Ya te metieron en la conversa."

    menu:
        "Se nota que la quiere harto, po.":
            $ apoyo += 1
            $ recuerda("José")
            jose "Gracias, po. Al fin alguien con criterio."
            hide diego
            show benjamin at left with dissolve
            benjamin "No le preguntís por la torta que ahí no para más."
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
            hide diego
            show benjamin at left with dissolve
            benjamin "Todos caen. Todos terminan queriendo conocer a la yegua."

    hide diego
    show benjamin at left with dissolve
    "Mientras José habla de ella, Benjamín se acerca y te susurra:"
    benjamin "(bajito) Lo único raro: pregúntale cuánto vale la yegua."

    menu:
        "Preguntarle el precio (como dice Benjamín).":
            mc "Oye, José... ¿cuánto vale Shakira?"
            jose "Yo creo que la vendería por un palo. Por ahí, un millón de pesos. En eso están los caballos. Depende igual."
            "Contesta antes de que termines la pregunta."
            benjamin "(bajito) ¿Viste? ¿VISTE?"
        "No preguntar. Se siente raro.":
            "Decides no preguntar. Benjamín no aguanta y pregunta él."
            benjamin "José, ¿cuánto vale Shakira?"
            jose "Yo creo que la vendería por un palo. Por ahí, un millón de pesos. En eso están los caballos. Depende igual."
            "Contesta antes de que termines la pregunta."
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
    if lugares >= 2 and not v_incidente:
        call incidente_del_dia
    $ lugares = int(v_patio) + int(v_shell) + int(v_jumbo) + int(v_potrero) + int(v_liceo)

    # Tras la tercera visita a Lincoñir, llega el día que nadie quería.
    if potrero_visitas >= 3 and not venta:
        jump la_venta

    # Tras la venta, se activan los WHAT IF.
    if venta and not whatif_tinder_activo and not v_tinder:
        $ whatif_tinder_activo = True
        $ whatif("Cupido de alquiler: habla con Marcelo en el patio.")
    elif venta and v_ruben and not whatif_trabajo_activo and not v_trabajo:
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
        if eventos and not pausa_eventos:
            pausa_eventos = True
            renpy.jump(renpy.random.choice(eventos))
        pausa_eventos = False

    menu:
        "¿Adónde vas ahora?"

        "Abrir el mapa de viajes":
            jump mapa_viajes
        "Patio del INACAP (Pablo, Marcelo y Benjamín)" if not v_patio:
            jump patio
        "Shell de Lautaro, camino a Pillalelbún (Pablo y Fabián)" if not v_shell:
            jump shell
        "Jumbo del Portal (Diego)" if not v_jumbo:
            jump jumbo
        "Viaje a Lincoñir, Padre Las Casas (visita [potrero_visitas + 1] de 3)" if not venta and potrero_visitas < 3:
            jump potrero_visita
        "Volver a Lincoñir (el potrero vacío)" if venta and not v_potrero:
            jump potrero
        "Liceo Politécnico de Pueblo Nuevo (todos se conocen ahí... menos tú)" if not v_liceo:
            jump liceo
        "Volver a la Shell: revisar la cabina" if venta and v_shell and not pista_pablo:
            jump shell_pistas
        "Volver al Jumbo: preguntar por las zanahorias" if venta and v_jumbo and not pista_diego:
            jump jumbo_pistas
        "Volver a la Shell (Pablo anda raro)" if v_shell and not v_sueno:
            jump sueno_pablo
        "¿Y si…?: El congelador de Fabián" if historia_cuy and not v_cuy_asado:
            jump whatif_cuy
        "¿Y si…?: Cupido de alquiler (Marcelo, patio)" if whatif_tinder_activo and not v_tinder:
            jump whatif_tinder
        "¿Y si…?: Preparar a José en el Cerro Ñielol" if v_tinder and not v_nielol:
            jump entreno_nielol
        "¿Y si…?: José se va a trabajar a Villarrica" if preparado_barbarita and not v_villarrica:
            jump whatif_villarrica
        "¿Y si…?: El trabajo en grupo (Marcelo, Benjamín y Rubén)" if whatif_trabajo_activo and not v_trabajo:
            jump whatif_trabajo
        "¿Y si…?: El sospechoso azul (Benjamín y el Inacapini)" if whatif_inacapini_activo and not v_inacapini:
            jump whatif_inacapini
        "Escuchar la grabadora ([fragmentos] de 5 fragmentos)":
            if fragmentos == 0:
                "Reproduces la grabadora. Silencio. Ni un fragmento. Aprietas stop, avergonzado."
            elif fragmentos >= 4:
                $ historia_escuchada = True
                call historia_completa
            else:
                "Escuchas los fragmentos sueltos. Voces de todos. Pedazos sueltos que todavía no se arman."
            jump hub
        "Conversar con Fabián (el chocolate y Rocket League)" if not chocolate_fabian and not v_fabian_sale:
            jump charla_fabian
        "Conversar con Rubén (la mascota que tuvo de chico)" if not historia_cuy:
            jump charla_ruben
        "Preguntarle a Bastián por su viaje de vuelta" if not origen_bastian:
            jump charla_bastian
        "¿Y si...?: el dato de Labranza (Lucho)" if venta and not v_lucho_labranza:
            jump whatif_labranza
        "Revisar las notas del caso":
            jump cuaderno
        "Ver cómo anda el grupo contigo":
            jump estado_relaciones
        "Ya tengo suficiente. Hora de confrontar a José." if venta and lugares >= 3:
            jump confrontacion


# =====================================================================
#  PATIO DEL INACAP
# =====================================================================
label patio:
    $ ultima_visita = "INACAP"

    $ v_patio = True
    scene bg patio_seco with fade
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
                "Pablo se acomoda las gafas y deja de mirarte."
                mc "(Algo no cuadra...)"
                $ pista_pablo = True
            else:
                "Probablemente sea el computador que se compró. O las gafas. Con Pablo nunca se sabe."
        "¿Vai a usar las gafas hasta adentro de la sala?":
            $ drama += 1
            $ recuerda("Pablo", negativo=True)
            pablo "Si me las saco, ustedes me las esconden."
            "Se aleja con dignidad. Con muchísima dignidad. Y con frío."
            hide pablo with dissolve

    marcelo "El domingo nunca pesca el grupo. El lunes llega diciendo que no pasó nada."
    marcelo "Y cambian el cartel del menú, pero el té sigue sin aparecer. Pa eso sí tienen tiempo."

    benjamin "Hablando de desapariciones... ¿ya le contaste de tu Instagram, Marcelo?"
    marcelo "Oye, no. No me lo recuerdes. Me borraron el Instagram. Noventa mil seguidores. NOVENTA MIL. A la basura."
    mc "¿Por qué te lo borraron?"
    marcelo "Por los clips de fútbol. Me cayeron los reclamos y me bajaron la cuenta. Noventa mil seguidores, wn."
    benjamin "Noventa mil personas viendo clips robados. Una pérdida cultural."
    benjamin "Pero le queda el TikTok. premierchilito. Ciento cuarenta y un mil seguidores de puro fútbol chileno."
    marcelo "En TikTok está premierchilito. Todavía la tengo. Si me vai a seguir, no comentís puras weás."

    menu:
        "Dale, ahí te sigo. Suena bacán.":
            $ promesa_marcelo = True
            $ apoyo += 1
            $ recuerda("Marcelo")
            marcelo "Ya, gracias. Pero no entrís a pedir que suba a Pablo de delantero."
        "¿Fútbol chileno? ¿Y eso existe?":
            $ drama += 1
            $ recuerda("Marcelo", "Marcelo NO lo olvidará. Con rencor.", negativo=True)
            marcelo "Después me piden el resultado del partido por interno. Ahí sí existe."

    if venta:
        benjamin "Todavía no me cabe que haya vendido a Shakira."
        marcelo "Ayer hiciste un sticker de la yegua con un teclado."
        benjamin "Puedo estar indignado y editar al mismo tiempo."
    else:
        benjamin "José ya le puso precio a Shakira. Nadie le preguntó, lo tiró solo."
        marcelo "Pero todavía no la vende, po. Deja de hacerle una despedida."
        benjamin "Por eso. Hay que webearlo antes."

    menu:
        "Hay que sacarle el tema. A ver qué dice.":
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu sentido del drama.")
            benjamin "¡POR FIN! ¡Alguien con criterio en este INACAP!"
        "¿Y no será que tú querís puro webearlo?":
            $ drama += 1
            benjamin "También. No son cosas incompatibles."

    benjamin "Oye, Marcelo. A mí me gustaría tener un manatí."
    marcelo "Oye, sí. Estaría bacán."
    "Pausa."
    marcelo "¿Y dónde lo vai a meter? Si no cuidai ni el cargador."
    benjamin "En Fundo El Carmen sí se podría. Es otra nación."
    marcelo "Ya, trámitalo en tu consulado, entonces."

    jump hub


# =====================================================================
#  SHELL DE PILLALELBÚN
# =====================================================================
label shell:
    $ ultima_visita = "Shell · Lautaro"

    $ v_shell = True
    $ musica("cumbia.ogg")
    scene bg shell with fade
    show pablo shell at center with dissolve

    "Shell de Lautaro, camino a Pillalelbún. Aquí trabaja Pablo, bombero de bencina: el que maneja y trae los tanques de cisterna."
    pablo "Acá trabajo yo. No toquen las cosas."
    if favor_inicio == "cono":
        pablo "Tú sí podís pasar. Por lo del cono. Los otros que esperen afuera."
    elif favor_inicio == "video":
        pablo "Y tú guarda el celular. Ya tuviste suficiente con la mañana."

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
    show pablo shell at center with dissolve

    "Pablo se sube a la cisterna y la recorre por el patio. Lento. Muy lento. Pero con cara de estar en una película."
    pablo "Haría esto con short corto, pero me obligan a venir con uniforme. Eso sí, igual lo traigo en la mochila."
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
        fabian "Me metí este año al INACAP. Compré SushiBurger con la beca el otro día. Pero..."
        "Ese «pero» sonó raro, pero no le di importancia."
    fabian "Y acá en Pillalelbún vienen todos los culiaos. Mi casa parece evento de Rocket League."
    fabian "Lo más raro: Maxi y Benjamín viven al lado. AL LADO. Y solo se juntan acá. Ni ellos lo entienden."

    "Una jauría de galgos cruza corriendo por el patio. Van como cinco. Parecen manada de comercial."
    fabian "Mis perros son brigidos. Pertenecen a un grupo: los Intratables. Salen a la calle y se devuelven solos."
    mc "¿Esos son los del canal?"
    fabian "Sí, wn. Antes subía carreras de galgos. Después dejé esos videos, con todo el tema de prohibir las carreras."
    fabian "Ahora subo las salidas con los perros detrás de las liebres, por Pillalelbún."
    pablo "Yo fui a buscar música y me salieron veinte minutos de perros corriendo."
    fabian "Porque estái en el canal de los perros, po."
    mc "¿Y cambiar los videos hace que esté todo permitido?"
    fabian "No, perro. Igual hay reglas pa salir a cazar. No es cambiarle el nombre nomás."

    fabian "Tenía uno que se llamaba Zeus Black. Negro como la noche. Dormía donde quería, el loco."
    fabian "Un día se quedó dormido detrás de la rueda de un auto..."
    "Silencio. Fabián mira al suelo. Damas Gratis sigue sonando, pero más bajito, como por respeto."
    fabian "F. Zeus Black. El más intratable de todos."
    mc "..."
    fabian "Ya po. No lloremos. Zeus Black no querría eso. Zeus Black querría cumbia villera."
    "Fabián le sube el volumen. Los Intratables aúllan al ritmo. Probablemente."

    call pequi_presentacion

    mc "¿Y quién más cae a las juntas?"
    fabian "Maxi siempre. El Iván Garrido del 4F, nunca. Ese loco no ha pisado Pillalelbún en su vida."
    fabian "En las juntas de Temuco sí aparece. Al INACAP fue a inscribirse y después a salirse. Cortito el semestre del Iván."
    fabian "Lo que sí te cuento: la práctica de telecom la hizo con el Marcelo Ducommun, en Infosur, por Avenida Alemania."
    fabian "No les pagaban, perro bastardo. Horas extra, pega pesada... y la empresa compraba cargadores chinos de dos lucas y los revendía como originales a VEINTE."
    mc "¿Cómo que a veinte?"
    fabian "VEINTE LUCAS. El cargador más chino del planeta. El profe Martín estaría orgulloso: por fin algo que SÍ venía de China."
    fabian "Y al Marcelo ni a terreno lo dejaron ir. Lo mandaron a la sección de impresoras y computadores. A VER impresoras. Todo el día."
    mc "(Con razón Marcelo no quiere ni escuchar el nombre.)"

    fabian "Y el colmo: Pablo fue DESPUÉS a esa misma empresa, a arreglar su laptop. Cuando Marcelo e Iván ya no estaban, eso sí."
    pablo "Me dijeron que era la placa. Doscientas lucas."
    fabian "¿Y era la placa?"
    pablo "Era el cargador. Me cobraron doscientas lucas por una placa que no tenía nada."
    fabian "Te arreglaron el cargador y te cambiaron el presupuesto entero, perro."
    pablo "No me hueveís más con eso."

    mc "(Pablo gastó dos millones en leceras y doscientas lucas en un cargador de dos. Su relación con el dinero es... deportiva.)"

    if broma_benjamin >= 1:
        show benjamin at right with dissolve
        "Benjamín te acompañó a la Shell. Dijo que era evidencia."
        benjamin "¿Y esa cisterna? Se ve manejable. MUY manejable."

    menu:
        "Subir a la cisterna con Pablo.":
            call permiso_cabina
            if not _return:
                jump hub
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
                "Fabián mira hacia la cabina. Pablo está mirando para otro lado."
            else:
                fabian "¿Quieres saber de Shakira? Anda a conocerla, wn. Está en Lincoñir. Vale la pena, te lo juro."
                fabian "Después me cuentas si viste algo más sano en tu vida."
        "Dejar que Benjamín maneje la cisterna." if broma_benjamin >= 1:
            $ broma_benjamin += 1
            "Le das el visto bueno a Benjamín. Pablo se entera cuando ya encendió el motor."
            call choque_de_benjamin
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
            show fabian at center with dissolve
            fabian "Pero no le saquí otra vez de la pensión a tu papá, wn."
            pablo "No te estoy pidiendo plata a ti."
            fabian "No cambia lo que te dije."

            $ pablo_arruinado = True
            $ consecuencia("Dejaste manejar a Benjamín: la Shell quedó dañada y Pablo cerró el camión.")
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
    $ ultima_visita = "Jumbo · Portal Temuco"

    $ v_jumbo = True
    scene bg jumbo with fade
    "Jumbo del Portal de Temuco. Entras a buscar a Diego; te dijeron que estaba en Hasbro."
    scene bg jumbo_pasillo with dissolve
    show diego at center with dissolve

    call portal_turno

    if favor_inicio == "camara":
        diego "Oye, desde que me grabaste el live me piden que salga el nuevo. No te agrandís."
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
                diego "Raro... un cliente intentó pagar un Optimus Prime en cuarenta cuotas. Eso es todo. Pega normal, po. Después dejó el juguete botado en otra sección."
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
    $ ultima_visita = "Lincoñir"

    if potrero_visitas == 0:
        jump potrero1
    elif potrero_visitas == 1:
        jump potrero2
    else:
        jump potrero3


label potrero1:

    $ potrero_visitas += 1
    scene bg puente_lejos with fade
    "Camino a Padre Las Casas. Al otro lado del puente espera José."
    scene bg puente_cerca with dissolve
    "Cruzan el Cautín y siguen hacia Lincoñir."
    scene bg camino with dissolve
    "El último tramo es por el camino de tierra."
    scene bg entrada_jose with dissolve
    "Benjamín reconoce la entrada. José dijo que pasaran nomás."
    scene bg casa_jose with dissolve
    "En la casa les señalan el potrero."
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
    benjamin "Si no la vendís, no hay asado. Facilito."
    jose "Está loco este. Como si yo fuera a venderla."
    "José se ríe y vuelve a darle pasto. Benjamín se corre antes de que Shakira le muerda la manga."

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
    marcelo "Ya, igual le quedó bonita la torta. Pero no digai que dije eso."
    $ frag()
    jose "El próximo año le hago una más grande. ¿Me ayudan?"
    menu:
        "Ayudar a José a cortar la torta.":
            $ recuerdo_cumple = "torta"
            $ apoyo += 1
            $ recuerda("José")
            "José te pasa el cuchillo. Shakira se acerca antes de que cortes."
            jose "Espera, po. Hay pa todos."
            marcelo "Yo no quiero. Tiene pasto pegado."
        "Sacarle una foto al grupo con Shakira.":
            $ recuerdo_cumple = "foto"
            $ rel_delta("Marcelo", 1)
            "Marcelo sostiene la torta mientras sacas la foto. Shakira alcanza a comerse el borde."
            marcelo "Ya, sácala luego. Me está comiendo la manga."
            jose "Mándamela al grupo. Esa está buena."


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
    "José le corre el pelo de la cara a Shakira. Fabián baja un poco más la música."

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

    "El vecino que la compró se la llevó al potrero de al lado. Shakira quedó mirando a José irse en la camioneta. Esa mañana, el desayuno se lo dio su nuevo dueño."
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
    benjamin "Y acuérdate de lo que te dije: si la vendís, asado."
    jose "Ya, era broma, po."
    benjamin "¿Era broma? ¿Tú cachai si era broma?"
    "Benjamín no se ríe. Por primera vez, Benjamín no se ríe."
    benjamin "Desde hoy, nuevo, esto es personal. Lo vamos a molestar hasta que sienta ALGO. Y tú tienes la grabadora."
    mc "(Tengo la grabadora. Tengo los fragmentos de algo que ya no existe.)"
    "Benjamín abre el grupo de WhatsApp. Ya está cambiando la foto por la del compu."
    $ recuerda("El grupo", "La venta de Shakira ya llegó al grupo de WhatsApp.")
    $ musica("tema.ogg")

    jump hub


# =====================================================================
#  LINCOÑIR, PADRE LAS CASAS (después de la venta)
# =====================================================================
label potrero:
    $ ultima_visita = "Lincoñir"

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

    "Maxi llega con Benjamín. Venía de Pedro de Valdivia y se sumó al viaje cuando escuchó que iban a ver a José."

    scene bg pedro with dissolve
    "(Pedro de Valdivia. De aquí viene Maxi. Caminando. Siempre caminando.)"

    scene bg potrero with dissolve
    show jose at right with dissolve
    show benjamin at left with dissolve
    show maxi at center with dissolve

    benjamin "¡Maxi! ¿Qué haces aquí, wn?"
    maxi "Me invitaste tú, aweonao. En el camino entero no me pescaste."
    benjamin "Este es Maxi Valenzuela. No es del INACAP; era del liceo con nosotros. Aparece cuando hay comida o conflicto. Hoy hay ambos."
    maxi "¿Y este quién es, negro?"
    mc "[nombre]. Estoy investigando lo de Shakira."
    maxi "¿La yegua que vendieron por el compu, sipo? Conchetumare, José. Eso no se hace, wn. Eso es como... como vender a la mamá por una tele."
    jose "Tampoco tanto."
    maxi "COMO VENDER A LA MAMÁ POR UNA TELE, DIJE."
    "Maxi abre Instagram. En la pantalla sale una mina bailando. Baja el volumen al notar que Benjamín está mirando."
    benjamin "¿No que ibai a mostrar las fotos del campo?"
    maxi "Espérate, wn. Se abrió solo."
    "Desliza. Sale otra mina. Sigue deslizando más rápido."

    maxi "El algoritmo me conoce, wn. Es lo único estable que tengo en la vida."
    benjamin "Ni una foto de Loncoche todavía. Tremendo álbum."
    maxi "Ya, acá están, conchetumare. Mira la leña que piqué."
    "Te muestra una pila de leña en el campo. Después, un mueble embalado en Santiago."
    maxi "Allá muevo muebles. Acá pico leña. ¿Y estos weones qué hacen?"
    benjamin "Trabajo intelectual."
    maxi "Mirarme el teléfono, decís tú."


    menu:
        "Maxi, ¿tú qué harías con el caso Shakira?":
            maxi "Yo, wn... yo haría un asado. Pero de respeto, ¿eh? Con velita y to'."
            "Benjamín toma nota mental: asado. Con respeto. Y velita."
            $ broma_benjamin += 1
            $ recuerda("Maxi", "Maxi te considera un aweonao de confianza.")
        "Ya, Maxi, te salió buena esa.":
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
    $ ultima_visita = "Politécnico · Pueblo Nuevo"

    $ v_liceo = True
    scene bg barros_arana with fade
    "Pasan por Barros Arana antes de llegar al Politécnico. Marcelo y Diego ubican el sector sin mirar el mapa."
    scene bg liceo with fade
    show diego at left with dissolve
    show benjamin at right with dissolve

    "Liceo Politécnico de Pueblo Nuevo. Varios del grupo compartieron segundo medio antes de irse a sus especialidades. Tú llegaste después, al INACAP."
    diego "Este lugar tiene historia. Y por historia quiero decir... al profe Martín."
    benjamin "El Shen Shen. Que en paz descanse su credibilidad."
    mc "¿El Shen Shen?"

    # --- Flashback del liceo ---
    scene black with fade
    "Diego y Benjamín te cuentan una clase de esos años. Tú no estabas ahí; te toca imaginarla."
    "En su relato, el profe Martín escribe HUAWEI en la pizarra."

    scene bg sala_liceo with fade
    show martin at center with dissolve

    martin "Cabros. Hoy no habrá clase. Hoy hablaremos de China."
    "El curso entero suspira en coro: «Otra vez no...»"
    martin "Cuando yo estuve en Shenzhen..."
    "El curso, susurrando: «Shen Shen...»"
    martin "...porque cuando era estudiante, COMO USTEDES, gané la competencia de Huawei del INACAP. Me mandaron a la final MUNDIAL. A China. Y quedé SEGUNDO."
    show benjamin at right with dissolve
    benjamin "(Ayer dijo que tercero.)"
    show martin at left with dissolve

    menu:
        "Según lo que cuentan, yo le habría creído.":
            $ apoyo += 1
            $ recuerda("Diego", "Diego cachó que prefieres escuchar antes de juzgar.")
        "Yo habría preguntado en qué puesto quedó.":
            $ drama += 1
            $ broma_benjamin += 1
            $ recuerda("Benjamín", "Benjamín aprueba tu escepticismo.")
            benjamin "¡Eso! ¡Duda! ¡Duda de todo! ¡Duda hasta de la cumbia!"
        "¿Y el Jeep que mencionaron?":
            "Una voz desde la ventana: «¡CUATRO POR CUATRO!»"

    "En el recuerdo de los cabros, Marcelo le susurra a Benjamín lo que sabía:"
    show martin at center with dissolve
    show marcelo at left with dissolve
    marcelo "A China sí fue. Eso es verdad. Ganó la competencia del INACAP siendo estudiante y lo mandaron a la final mundial."
    benjamin "El problema es el puesto. Segundo, dice. A veces tercero. Depende del día."
    marcelo "Duodécimo. Benjamín lo buscó. Le preguntamos y cambió de tema."
    $ verdad_martin = True
    martin "¡SE DICE SHENZHEN!"

    "En eso irrumpe un hombre con una cámara. Filma la clase como si fuera un documental de National Geographic."

    benjamin "Héctor. Amigo del profe. Todos le dicen el Suzuki Jeep."
    hide benjamin
    show hector at right with dissolve
    hector "Este video va para mi canal. SJO. Suzuki Jeep Oficial. Y ese Jeep de afuera es mío."

    hide marcelo
    show martin at left with dissolve
    show jeep at center with dissolve
    "El Jeep. Suzuki. Cuatro por cuatro. Estacionado como si fuera dueño del liceo."
    "Se cachiporrea de su Jeep. Es el noventa por ciento de su personalidad."
    hide jeep
    show martin at center with dissolve
    show marcelo at left with dissolve
    marcelo "Tiene casi cuatro mil suscriptores. Yo edito un partido entero y este graba el Jeep estacionado."
    hide hector
    show benjamin at right with dissolve
    benjamin "Tres mil novecientos ochenta. Ciento doce videos. Todos del Jeep."
    hide benjamin
    show hector at right with dissolve
    hector "Qué van a saber ustedes. No tienen un Suzuki Jeep."
    martin "¡RESPETO! ¡Héctor, filma esto!"
    hector "Ya estoy filmando. Desde el Jeep se ve mejor, eso sí."

    "Y así, cada clase: China, Huawei, Shenzhen. Y el Jeep, siempre afuera. Siempre cuatro por cuatro."
    "Y al fondo de la sala, Maxi Valenzuela (que no es del INACAP, pero sí era del liceo) susurraba «conchetumare» cada vez que el profe decía Shenzhen. Nunca lo expulsaron. A los profes no les pagaban lo suficiente para expulsar a Maxi."
    "Y en cada mesa, cada muro y cada baño del liceo, la misma inscripción sagrada: «Iván Garrido del 4F»."
    martin "¡¿QUIÉN RAYA MIS MESAS?!"
    hector "Yo tengo una teoría: se rayó solo. Como los geoglifos. Nadie sabe cómo llegó ahí."
    hide hector
    show benjamin at right with dissolve
    benjamin "Esos los hice yo. No es ningún secreto: lo rayé delante de todo el curso. De Iván incluido. Es mi obra maestra."

    "Y hablando de Iván: años después, el INACAP vivió un día histórico."

    scene bg inacap with dissolve
    show ivan at center with dissolve

    "Iván llegó al INACAP a inscribirse. Todos pensaron que se iba a quedar."
    "Se inscribió. Firmó unos papeles. Todos creyeron que estudiaría. Error."
    hide ivan with dissolve
    "Dos días después..."
    show ivan at center with dissolve
    "Iván volvió. Se dio de baja. Pidió su certificado de alumno regular. Un PDF."
    ivan "Chao."
    hide ivan with dissolve
    "Y se fue caminando lento, victorioso. Con ese PDF esquivó la milicia. El llamado del ejército."
    "Benjamín todavía guarda la captura del certificado. Iván le pidió que dejara de mandarla al grupo."
    "Iván es de Pedro de Valdivia. A veces pinta casas con su papá. Benjamín le pregunta si también puede tapar los rayados del liceo."

    scene bg liceo with fade
    show diego at left with dissolve
    show benjamin at right with dissolve
    diego "Buenos tiempos."
    benjamin "El Shen Shen sigue dando clases. El viaje a China lo cuenta como si hubiera vuelto ayer."

    "Suena el celular de Benjamín. Contesta."
    benjamin "¿Aló? ... ¿Nico? ... ¿Cómo que Santiago? ... ¿No que ibas a Lonquimay? ... Ya. Cuídate, wn."
    "Benjamín cuelga."
    benjamin "El Nico Jara. Terminó en Santiago. De soldado."
    diego "¿No que iba a Lonquimay?"
    benjamin "Lonquimay quedó en el camino. Nadie sabe qué pasó entre medio."
    mc "(Casi cuatro mil suscriptores viendo un Jeep. Este país es infinito.)"

    call conversacion_martin_hector
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

    "Están en el patio esperando la siguiente clase. Fabián llega con la mochila puesta."
    if chocolate_fabian:
        fabian "Oye, y al final el Trencito me lo comí yo. Pa que dejen de preguntar."
        marcelo "Pero si nadie te preguntó ahora."
    fabian "Cabros. Me salí."
    "..."
    mc "¿De dónde?"
    fabian "Del INACAP. De la carrera. Me salí. Hoy. Ahora."
    $ sfx("trueno.ogg")
    benjamin "¿¡QUÉ!? ¿Así? ¿Así nomás? ¿En nuestras caras?"
    fabian "Se me hizo muy difícil, wn. Y conseguí polola. Los papás de ella la echaron de la casa, así que nos vamos a vivir juntos. Hay que trabajar."
    marcelo "¿Y el trabajo del viernes? Tu nombre está puesto todavía, Fabián."
    fabian "Postulé al Tecnobox. Me dijeron «te llamamos». Voy bien."
    "(Alerta de spoiler del futuro: nunca lo llamaron del Tecnobox. Hasta hoy.)"
    benjamin "Pero avisa, po. Con tiempo. Con una semana."
    fabian "Te estoy avisando. Ahora. Aguante el Colo. Chao, cabros."
    "Fabián se despide y sale a buscar locomoción. Marcelo pregunta quién se quedó con el archivo del trabajo."
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
    marcelo "¿Otra vez? Si recién habían arreglado el camino. Mira hasta dónde llegó el agua."
    benjamin "¡Fabián! ¡Pablo! ¡Rubén! Todos están allá. ¡MAXI TAMBIÉN! Vamos."
    mc "¿Yo también?"
    benjamin "Tú también. Es ley de Pillalelbún: cuando se inunda, se va."

    scene bg inundado with fade
    "Pillalelbún. Agua hasta la rodilla. La Shell resiste. Las casas resisten. La cumbia, por supuesto, suena."
    show fabian at left with dissolve
    show pablo at right with dissolve

    fabian "¡Cabros! ¡Llegaron! Aguante Pillalelbún, wn."
    call pequi_inundacion
    pablo "El agua sube. Tengo todo bajo control. Casi todo."
    "Pablo sigue con las gafas de sol puestas. Secas. Prioridades."

    show maxi at center with dissolve
    fabian "Ese es Maxi. De Pedro de Valdivia. Aparece cuando hay comida, conflicto o catástrofe."
    maxi "¡Conchetumare el agua! ¡Estoy hasta el copi, negro!"

    hide pablo
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
            hide ruben
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
    "Los dos te miran. Te dejaron decidir quién se hace cargo."

    menu:
        "Apoyar a Pablo: Benjamín tiene que pagar.":
            $ acuerdo_shell = True
            $ consecuencia("Benjamín debe pagar. Pablo vuelve a permitir visitas al camión.")
            $ rel_delta("Pablo", 2)
            $ rel_delta("Benjamín", -1)
            $ recuerda("Pablo", "Pablo lo recordará. Benjamín NO lo olvidará.", puntos=0)
            pablo "Gracias. AL FIN justicia."
            benjamin "Traición. Traición diplomática. Anotado."
            benjamin "Pagaré. En carmenos. Que valen el doble."
            "Benjamín pagará. En cuotas. De mil pesos. Durante ochenta años."
        "Apoyar a Benjamín: fue un accidente.":
            $ acuerdo_shell = False
            $ consecuencia("Defendiste a Benjamín: Pablo mantiene cerrado el camión.")
            $ rel_delta("Benjamín", 2)
            $ rel_delta("Pablo", -1)
            $ recuerda("Benjamín", "Benjamín lo recordará. Pablo NO lo olvidará.", puntos=0)
            benjamin "¡GRACIAS! ¡Era un accidente! ¡Un accidente con estilo!"
            pablo "..."
            pablo "Brad Pitt no abandonaría a un amigo así."
            "Pablo se pone las gafas. Ofendido. Con frío. Con todo."
        "Mediar: que la reconstruyan juntos.":
            $ acuerdo_shell = True
            $ consecuencia("Acordaron reparar la Shell. Recuperaste el acceso al camión.")
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
    if favor_inicio == "te":
        marcelo "Oye, tú que al menos me conseguiste té, ayúdame con esto."
    marcelo "Mira el aviso. Un strike. Le dije que no tocara el video y lo subió igual."
    mc "¿Qué pasó?"
    marcelo "Alguien le puso música a mi último video. Cumbia villera. Sobre un clip de la Chilean Premier."
    benjamin "Fui yo. Lo mejoré. El fútbol necesitaba cumbia."
    marcelo "¡DERECHOS DE AUTOR, BENJAMÍN! ¡YA PERDÍ UN INSTAGRAM POR ESO!"
    benjamin "Fue Supermerk2. Vale la pena el strike. Arte es arte."
    "Los dos te miran. Te dejaron de árbitro sin preguntarte."

    menu:
        "Marcelo tiene razón: borra el video, Benjamín.":
            $ premier_bloqueado = False
            $ consecuencia("Borraron el video a tiempo: Marcelo conserva su página.")
            $ rel_delta("Marcelo", 2)
            $ rel_delta("Benjamín", -1)
            $ recuerda("Marcelo", "Marcelo lo recordará. Benjamín NO lo olvidará.", puntos=0)
            benjamin "Borrar arte. Está bien. Lo borro. Pero la historia me dará la razón."
            marcelo "Gracias. Ahora dame la clave que te la voy a cambiar, Benjamín."
        "Benjamín tiene razón: el fútbol necesitaba cumbia.":
            $ premier_bloqueado = True
            $ consecuencia("Dejaron el video: Marcelo perdió acceso a premierchilito.")
            $ rel_delta("Benjamín", 2)
            $ rel_delta("Marcelo", -1)
            $ recuerda("Benjamín", "Benjamín lo recordará. Marcelo NO lo olvidará.", puntos=0)
            benjamin "¡POR FIN! ¡ALGUIEN CON CULTURA!"
            marcelo "..."
            marcelo "Ya, cuando me bajen la página me editai tú los noventa mil seguidores de vuelta."
        "Solución: graben un video de disculpa. Juntos.":
            $ premier_bloqueado = False
            $ consecuencia("Borraron el clip y subieron una disculpa propia. La página sigue activa.")
            $ apoyo += 1
            $ rel_delta("Marcelo", 1)
            $ rel_delta("Benjamín", 1)
            $ recuerda("El grupo", "Marcelo y Benjamín lo recordarán. En el mismo video.")
            "Graban un video de disculpa. Marcelo se disculpa sin querer disculparse. Benjamín baila al fondo."
            "Borran el clip reclamado. La disculpa queda como video propio; premierchilito sigue activo."

    if premier_bloqueado:
        marcelo "Listo. Perdí la cuenta. Otra vez. No me mandís otro video, Benjamín."
        benjamin "Ya. Esta vez sí la cagué."
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
            "Fabián guarda la lámina y le dice que las diez lucas se las debe igual."
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
    "El Inacapini saluda a un grupo que acaba de llegar. Benjamín lo señala con el dedo."
    benjamin "Les da foto a todos menos a mí. Ya, no le pido más."

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

    benjamin "Igual voy a cachar quién está adentro. Capaz que me conozca y por eso no me pescó."
    benjamin "Cuando tenga pruebas, te aviso. Esto no queda así."

    jump hub


# =====================================================================
#  WHAT IF: EL SOSPECHOSO AZUL (evento no canon)
# =====================================================================
label whatif_inacapini:

    "Benjamín te cuenta su teoría del Inacapini. Desde acá manda su imaginación; estas no son pistas del caso real."
    $ v_inacapini = True
    scene bg patio with fade
    show benjamin at left with dissolve

    "Misión: vigilar al Inacapini. Benjamín lleva binoculares. De dónde los sacó, nadie sabe."
    "El Inacapini posa para una foto y reparte stickers. Benjamín sigue esperando el suyo."
    benjamin "Mira, ahora abraza gente. Cuando fui yo estaba ocupado."

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
    marcelo "¿Y te vai justo cuando nos toca entregar? Siempre elegís bien el día, Rubén."
    benjamin "El INACAP pierde a su alumno más... presente. Físicamente presente, al menos."
    ruben "Supervisé harto. Supervisar es trabajar."
    benjamin "En los trabajos de a tres, Marcelo y yo hacíamos todo. Rubén 'supervisaba'. Desde la banca. Esta misma banca."
    benjamin "Una vez el papá le regaló veinte lucas para que almorzara."
    marcelo "Después andaba pidiendo la mitad del almuerzo. Pero la lámina no la vendía ni cagando."
    ruben "Eran láminas numeradas. No entienden."
    benjamin "Ah, y le gustan los gatos esfinge. Los sin pelo. El Bingus cat."
    ruben "El Bingus es un buen gato. No hay que peinarlo. Menos pega."
    mc "(Hasta los gustos de Rubén son de bajo mantenimiento.)"

    mc "Oye, Rubén... tú eres de Pillalelbún. ¿Sabes algo de Shakira? ¿De Pablo?"
    ruben "..."
    ruben "¿Y a ti qué te importa?"
    mc "Estoy investigando."
    ruben "Investigar. Qué esfuerzo. Me agoté de puro escucharte."
    "Rubén se sienta otra vez. No alcanzó a alejarse ni dos metros."
    ruben "Pero ya que insistes... sí. La vi. Una yegua, cerca de la Shell. Los domingos. Cuando Pablo cree que nadie mira."
    ruben "Yo no dije nada. Decirlo era mucho esfuerzo."
    $ pista_ruben = True

    menu:
        "Gracias, Rubén. Tu secreto está a salvo conmigo.":
            $ secreto_ruben = True
            $ consecuencia("Protegiste a Rubén: su testimonio puede completar las pistas que te falten.")
            $ recuerda("Rubén", "Rubén confía en ti. Casi se mueve de la emoción.")
            ruben "Bacán."
        "Esto va a salir a la luz, Rubén. Lo siento.":
            $ traicion_ruben = True
            $ consecuencia("Rubén dejó de colaborar. Tendrás que sostener el caso con otras pistas.")
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
    $ ultima_visita = "Shell · Lautaro"
    $ v_sueno = True
    $ sueno_pablo_activo = True
    $ fase_globo_pablo = 0
    if pablo_arruinado:
        scene bg shell_ruinas with fade
    else:
        scene bg shell with fade
    show pablo shell at center with dissolve
    "Pablo está en su colación. Dejó el celular boca abajo y se acomoda en la silla."
    pablo "Con la moto que iba a comprarme... me habría ahorrado la micro."
    mc "¿Y por qué no la compraste?"
    pablo "Porque..."
    "Pablo se queda mirando la mesa. Fabián sale un momento a atender."
    scene black with fade
    "Después, en Pillalelbún..."

    scene bg sueno with fade
    show pablo at center with dissolve
    $ musica("tema.ogg")
    $ fase_globo_pablo = 1
    pablo_imagina "Ya. Primero la moto. Lo dije y lo voy a hacer."
    "Compra la moto, casco y deja una parte de las lucas guardada. Por una vez no abre el casino para terminar la compra."
    pablo_imagina "Puedo hacer repartos. De algo tengo que sacar pa la bencina."
    "Por ahora solo falta elegir qué va a repartir."
    menu:
        "Empezar repartiendo los ceviches del hermano de Fabián.":
            $ plan_sueno = "ceviches"
            scene bg casa_fabian with dissolve
            show fabian at left with dissolve
            show pablo at right with dissolve
            fabian "Mi hermano vende ceviches. Tú llevai los pedidos. Cortita."
            pablo_imagina "¿Y cuánto me toca?"
            fabian "Hablemos eso antes, po. No cuando estís con el pedido en la mano."
            "La primera semana nadie pregunta por la moto: preguntan a qué hora llega el ceviche. Pablo anota las direcciones en vez de apostar mientras espera."
        "Usar la moto para llevar encargos y repuestos entre los negocios.":
            $ plan_sueno = "repuestos"
            scene bg pedro with dissolve
            show pablo at right with dissolve
            show ivan at left with dissolve
            ivan "Llévame estos rodillos. Estoy pintando una casa y me faltaron."
            pablo_imagina "Ya. Pero no te llevo el tarro de pintura entre las piernas."
            ivan "Es chico."
            pablo_imagina "Por eso mismo: se va a caer."
            scene bg cruce_trenes with dissolve
            "Pablo espera antes de cruzar la línea del tren. Esta vez lleva encargos, no una cisterna. Tampoco se aparece un tren de la nada."
            "Después le piden cargadores, herramientas y encargos para la Shell. Esta vez pregunta qué repuesto necesita el computador antes de soltar doscientas lucas."

    scene bg sueno with fade
    show pablo at center with dissolve
    $ fase_globo_pablo = 2
    "Los pedidos aumentan. Pablo deja de pedir plata prestada y empieza a contratar a otros cabros para los repartos."
    "A los negocios de Pillalelbún les empieza a ir mejor. Hay pega, arreglan las calles y la gente ya no espera una semana por un encargo."
    pablo_imagina "¿Vieron? Era comprar la moto nomás."
    hide pablo
    show marcelo at left with dissolve
    show fabian at right with dissolve
    marcelo "¿Y yo qué hago acá?"
    fabian "Te pagaron pa grabar los partidos del barrio."
    marcelo "¿Me pagaron? Ya, sigo entonces."
    "Fabián tiene tiempo para tocar piano y grabar música. Rubén administra una lista de pedidos desde la banca; por una vez hay una lista que sí completó."
    show ruben at center with dissolve
    ruben "Ya trabajé. Dejen de llamar."
    "Hasta el letrero de la Shell quedó derecho. En este Pillalelbún, Pablo preguntó cuánto costaba arreglarlo y pagó sin pedir revancha al casino."
    scene bg shell with dissolve
    show pablo shell at center with dissolve
    $ fase_globo_pablo = 3
    pablo_imagina "De puras weás, nada. Mira la pega que armamos."
    pablo_imagina "Van a poner mi cara en la plaza. Pero con las gafas, eso sí."
    "El alcalde pide que Pablo arregle también el presupuesto municipal. Rubén ofrece trabajar horas extra. Ninguno pregunta cuánto le van a pagar."

    scene black with fade
    $ sfx("mensaje.ogg")
    "Un celular vibra. Después vuelve a vibrar."
    $ fase_globo_pablo = 0
    $ sueno_pablo_activo = False
    if pablo_arruinado:
        scene bg shell_ruinas with fade
    else:
        scene bg shell with fade
    show pablo shell at right with dissolve
    show fabian at left with dissolve
    $ musica("tema.ogg")
    fabian "Pablo. Despierta, wn. Se acabó la colación."
    "Seguían en la misma silla y la misma Shell. Todo lo de la moto y el pueblo próspero fue el sueño de Pablo."
    pablo "Estaba soñando que me compraba la moto."
    pablo "Y le iba bien a todo Pillalelbún. Hasta Rubén trabajaba."
    fabian "Con dos millones arreglaste el pueblo entero. Te rindieron harto dormido, perro."
    mc "¿Y despierto? ¿En qué te las gastaste?"
    pablo "En puras weás."
    "No hay moto afuera. No hay repartos. El letrero sigue igual y Pablo está mirando una notificación del casino."
    menu:
        "Decirle que puede empezar ahorrando para la moto, sin volver a apostar.":
            $ rel_delta("Pablo", 1)
            $ apoyo += 1
            pablo_imagina "Ya. Voy a cerrar esta wea por hoy."
            "Bloquea el celular. Al menos hoy termina el turno sin abrir otra apuesta."
            $ consecuencia("Pablo te escuchó y dejó el casino cerrado durante el turno.")
        "Pedirle que en el próximo sueño arregle también el wifi del INACAP.":
            $ broma_benjamin += 1
            pablo_imagina "Ese presupuesto ya es más grande."
            fabian "Más grande era la moto y tampoco la compraste, wn."
    jump hub


# =====================================================================
#  WHAT IF: CUPIDO DE ALQUILER (evento no canon)
# =====================================================================
label whatif_tinder:

    "Marcelo propone inventarle otra vida a José. Esto es un ¿y si...?, no lo que está pasando en el patio."
    $ v_tinder = True
    scene bg patio with fade
    show marcelo at left with dissolve

    marcelo "Ven a mirar esto antes de que Benjamín lo mande al grupo."
    "Marcelo te muestra un celular. En pantalla: el Tinder de José."
    mc "¿José tiene Tinder?"
    marcelo "Tiene. Y es un desastre. Mira el perfil."
    "Foto 1: José con una yegua. (La yegua ya no está. La foto sigue.)"
    "Foto 2: José en el Elysium. Se nota que fue una vez. Bio: «Me gusta mi PC»."
    mc "Necesita ayuda. Ayuda profesional."
    marcelo "Por eso te llamé. Yo solo no voy a editarle esto, después me culpa."
    marcelo "El objetivo real: Cata Toro. La crush de José. Desde el liceo."
    marcelo "José le manda memes desde el liceo. Ella responde «jaja» cada tres semanas."
    marcelo "Tres semanas esperando un jaja. Yo ya habría cerrado la conversa."

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
    marcelo "Ya. No le mando otra cosa. Que después diga que fue culpa de uno."

    show jose at right with dissolve

    jose "Chicos. Buenas y malas."
    jose "Hablé con una del Tinder. Barbarita. De Villarrica."
    mc "¿Y bien?"
    jose "Me ofreció pega. Tres meses. En Villarrica."
    "..."
    mc "¿Pega? ¿Se suponía que no era una cita?"
    jose "Me dijo que podía ir a trabajar allá. Pero todavía no salgo. Ni sé qué decirle cuando llegue."
    marcelo "Antes de mandarte a Villarrica hay que prepararte. Los cabros dijeron que subiéramos el Ñielol."
    jose "¿Todos?"
    marcelo "Sí. Si esto sale mal, al menos no fui el único que dio consejos."
    "Hasta acá llega la primera parte de la historia inventada. La subida al Ñielol queda disponible en el mapa; el viaje a Villarrica vendrá después."
    $ whatif("José necesita prepararse: nueva salida al Cerro Ñielol.")

    jump hub


# =====================================================================
#  WHAT IF: EL TRABAJO EN GRUPO (evento no canon)
# =====================================================================
label whatif_trabajo:

    "Los cabros imaginan qué pasaría si les tocara otro trabajo con Rubén. Van a exagerar, obviamente."
    $ v_trabajo = True
    scene bg patio with fade
    show marcelo at left with dissolve
    show benjamin at right with dissolve

    "Trabajo en grupo. Mínimo tres personas. Marcelo y Benjamín presentes. Y el tercer integrante..."

    show ruben at center with dissolve

    if v_ruben:
        "En esta versión de la historia, Rubén vuelve después de salirse. Dice que vino a firmar."
    else:
        "Rubén llega justo cuando reparten las tareas. Mira la lista y se sienta."
    ruben "Yo superviso."
    "Rubén se acomoda en su banca. El trabajo aún no empieza y ya está cansado."

    menu:
        "Hacer la parte de Rubén entre todos.":
            $ apoyo += 1
            $ recuerda("Rubén")
            $ recuerda("Marcelo", "Marcelo NO lo olvidará. Otra vez haciendo la pega de Rubén.", negativo=True)
            "Hacen la parte de Rubén entre todos. Rubén aprueba. Desde la banca. Con los ojos cerrados."
            marcelo "Tres nombres en la portada, dos personas haciendo la pega. De nuevo."
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

    "El vecino que la compró se la llevó al potrero de al lado. Shakira quedó mirando a José irse en la camioneta. Esa mañana, el desayuno se lo dio su nuevo dueño."
    shakira "(Iiih.)"
    "El relincho de la grabación no es chistoso. Ya no."
    "José, mientras tanto, fue a comprar la PC. Ese mismo día. Estaba contento."
    "Shakira no entendió. Las yeguas no entienden de papeles. Solo saben quién cruza el potrero con el desayuno."
    "Esperó en la cerca las mañanas siguientes. Todas. José no volvió."
    $ sfx("porton.ogg")
    "En la grabación se escucha a José cerrar el portón. Después, nada."

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
    benjamin "La crió él, po. Y ahora habla de la venta como si hubiera vendido una silla. Eso me pica."

    return


# =====================================================================
#  CÓMO ANDA EL GRUPO CONTIGO (medidor de relaciones)
# =====================================================================
label estado_relaciones:

    "Revisas mentalmente cómo anda el grupo contigo."
    "José: [estado('José')]. Pablo: [estado('Pablo')]. Diego: [estado('Diego')]. Fabián: [estado('Fabián')]."
    "Marcelo: [estado('Marcelo')]. Benjamín: [estado('Benjamín')]. Rubén: [estado('Rubén')]. Maxi: [estado('Maxi')]."
    "Bastián: [estado('Bastián')]. Sigue hablando poco, pero se acuerda de quién lo pescó."

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
    elif historia_escuchada:
        "Ya escuchaste las grabaciones. Esta vez vas directo a las preguntas."
    elif fragmentos > 0:
        "Todavía te faltan grabaciones. No todo lo que te contaron calza."

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

    call portal_recuerdo

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
        marcelo "Todavía me acuerdo de lo del video. Después me vai a pedir el link como si nada."
    if rel["José"] >= 2:
        jose "[nombre] es de los míos. Lo que diga, va en serio."

    if resultado_incidente == "relincho":
        marcelo "Y por favor, sin efectos de sonido esta vez."
    elif resultado_incidente == "cinta":
        marcelo "El nuevo por lo menos arregló el cargador. Escúchenlo un rato."
    elif resultado_incidente == "bebida":
        pablo "Oye, ¿al final Rubén compró la bebida o no?"
        marcelo "Pablo, estamos en otra cosa."

    jose "Ya, [nombre]. ¿Qué querís que haga?"

    menu:
        "Acusar a José frente a todos. ¡Es un traidor!":
            $ actitud_final = "acusar"
            $ rel_delta("José", -2)
            $ drama += 3
            jose "¡Más encima que la vendí, justamente! Y legal. Y andan leseando."
            if v_tinder:
                jose "¡Y más encima me inventaron una polola en Villarrica! ¡No conozco a ninguna Barbarita!"
                hide pablo
                show benjamin at right with dissolve
                benjamin "¿QUÉ TIENE QUE VER LA BARBARITA CON ESTO?"
                jose "NO LO SÉ. PERO ESTOY."
            jose "Ouuu. Grave. Gravísimo."
        "Hablar con José desde el corazón.":
            $ actitud_final = "hablar"
            $ rel_delta("José", 1)
            $ apoyo += 2
            jose "Gracias, hermano. De verdad."
        "Invitarlo a jugar en su PC y dejar el tema.":
            $ actitud_final = "jugar"
            $ consecuencia("Decidiste dejar la investigación: la noche termina frente al computador.")
            $ apoyo += 1
            jose "¡Eso! ¡Ven, que te muestro el setup!"
        "Revelar que Rubén es tu fuente, aunque prometiste callarlo." if pista_ruben and secreto_ruben:
            $ secreto_ruben = False
            $ traicion_ruben = True
            $ actitud_final = "acusar"
            $ rel_delta("Rubén", -3)
            $ drama += 1
            mc "Rubén lo vio. Él me contó."
            "Desde la banca, Rubén levanta la cabeza."
            ruben "Me dijiste que no ibai a dar mi nombre. No te cuento nada más."
            $ consecuencia("Rompiste la promesa: perdiste la colaboración de Rubén.")
        "Escuchar la propuesta de Benjamín." if broma_benjamin >= 2:
            $ plan_benjamin = True
            "Benjamín se levanta de una banca donde, aparentemente, llevaba sentado todo el rato."
            hide pablo
            show benjamin at right with dissolve
            benjamin "Tengo una idea. Pero después no digan que no les avisé."
            marcelo "¿Por qué dijiste papas? No, espera. No me gusta adónde va esto."

    # --- Elección de final ---
    if plan_benjamin:
        jump final_fundo
    elif actitud_final == "jugar":
        jump final_gamer
    elif pista_diego and (int(pista_pablo) + int(pista_potrero) + int(testigo_confiable()) >= 2) and drama < 5:
        jump final_verdadero
    elif drama >= 5:
        jump final_funeral
    elif apoyo >= 6 and rel["José"] >= 2:
        jump final_empeno
    elif apoyo >= 3 and rel["José"] >= 1:
        jump final_custodia
    else:
        jump final_gamer


# =====================================================================
#  FINALES
# =====================================================================
label final_verdadero:

    scene bg patio with dissolve
    $ musica("tema.ogg")
    show jose at center with dissolve
    show pablo at right with dissolve
    show marcelo at left with dissolve
    if pista_pablo:
        "Pablo mira la montura, después las zanahorias. Ya no le queda mucho que inventar."
    else:
        "El testimonio de Rubén calza con las zanahorias y el rastro del potrero. Pablo deja de inventar excusas."
    pablo "Está bien. ESTÁ BIEN. ¡Fui yo!"
    marcelo "Ya, pero ¿por qué no lo dijiste antes? Llevamos días dando vueltas."
    pablo "Con parte de los dos millones le compré a Shakira al vecino mapuche de José. Era mi lecera más grande."
    pablo "El resto sí fue en leceras: más gafas, más shorts, un computador y el Monster Hunter."
    pablo "Y doscientas lucas en Infosur por la placa. Al final era el cargador. No me lo recuerden."
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
    if recuerdo_cumple == "foto":
        jose "Después saquemos otra foto como la del cumpleaños. Pero que Marcelo no sostenga la torta."
    elif recuerdo_cumple == "torta":
        jose "Te debo una torta, [nombre]. La otra te la quitó casi entera."
    jose "Pablo... gracias, wn. De verdad."
    jose "Pero la PC se queda."
    shakira "(Relincha con desaprobación.)"
    "Shakira vive, tiene dos dueños, tres amigos y veinte kilos de zanahorias a la semana."

    if historia_escuchada:
        "José mira a Shakira un segundo de más. Algo se mueve en su cara. Casi. CASI se mueve."
        show benjamin at center with dissolve
        benjamin "(susurrando) ¿Vieron eso? ¿VIERON ESO?"
        hide benjamin with dissolve

    if verdad_martin:
        show bastian at center, bastian_bajo with dissolve
        bastian "Ni el Shen Shen en 'China' vio un desenlace así."
        "Silencio absoluto. Todos se giran hacia Bastián."
        hide shakira with dissolve
        show benjamin at left with dissolve
        benjamin "Dejemos que termine, po. Después reclama que no lo escuchamos."
        jose "Si habla siempre conmigo. Ustedes no lo dejan."
        hide benjamin
        hide bastian
        show shakira at left with dissolve
    if pista_ruben:
        hide jose with dissolve
        show ruben at right with dissolve
        "Desde una banca, Rubén levanta el pulgar. Es el mayor esfuerzo que se le ha visto."
        ruben "Chao, chiquillos."
        hide ruben
        show jose at right with dissolve

    $ persistent.finales.add(1)
    "FINAL 1 de 7: La lecera más cara (final verdadero)"
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
    "José pregunta si puede ir el domingo. El vecino le dice que avise antes, eso sí."

    $ persistent.finales.add(2)
    "FINAL 2 de 7: La custodia compartida"
    jump creditos


label final_funeral:

    $ musica("triste.ogg")
    scene bg funeral with fade
    "Benjamín corta la discusión. Dice que, si van a seguir exagerando, mejor contar cómo terminaría su teleserie."
    "Lo que sigue es el final que se inventa el grupo. No una muerte provocada por tus preguntas."
    "Shakira, legendaria yegua, murió como vivió: galopando hacia el atardecer..."
    "...y chocando con un letrero que decía 'Ceda el paso'."
    "Marcelo interrumpe el relato: «¿No que el vecino la tenía encerrada?». Benjamín le pide que lo deje terminar."

    show marcelo at left with dissolve
    show pablo at right with dissolve
    marcelo "¿Y la música la vai a poner así de fuerte, Fabián? Estamos tratando de escuchar."
    pablo "Brad Pitt también iría de lentes a un funeral. Es un tema de respeto."
    if pablo_arruinado:
        "Las gafas son falsas, eso sí. Empenó las originales para seguir apostando."
    show fabian at center with dissolve
    fabian "Esto se despide con cumbia villera, wn. Es lo que hay."
    "Fabián pone cumbia en el celular. Marcelo le pide que por lo menos la baje."
    hide marcelo with dissolve
    show jose at left with dissolve
    jose "Perdóname, Shakira."
    "José hace una pausa. Todos contienen el aire."
    jose "...aunque técnicamente fue una venta legal."
    hide jose
    show marcelo at left with dissolve
    marcelo "Te acaban de dar el pésame y estái explicando la boleta, José."
    "La PC gamer, desde su escritorio, no emite luz alguna. Ni RGB. Por respeto."

    if v_liceo:
        "Un Suzuki Jeep 4x4 abre la procesión fúnebre. Héctor filma todo. «Contenido», susurra con respeto."
        "El profe Martín manda un audio: «En China los funerales son distintos. Cuando estuve en Shenzhen...» Nadie lo escucha."

    "Y aquí viene la parte que la familia de Shakira pidió no publicar."

    $ sfx("plato.ogg")
    scene asado parrilla with fade
    "Benjamín levanta la tapa de la parrilla. No es una forma de decirlo: en este cuento oscuro, ese asado es Shakira."
    benjamin "Sí, esa es la Shakira. No era una metáfora, wn."
    scene escena asado with dissolve
    show benjamin anticucho at left with dissolve
    show fabian anticucho at right with dissolve
    show pablo anticucho at center with dissolve

    "José no fue al asado. Benjamín reparte los anticuchos entre Fabián y Pablo; nadie le guardó un puesto."
    "Benjamín, fiel a la ley del campo («no se desperdicia nada»), organizó un asado en el Fundo El Carmen."
    "Con la carne de... bueno. Ustedes entienden."
    "Invitado de honor: Fabián Millalén, de Pillalelbún. Llevó el carbón. Y la cumbia villera."
    fabian "Hermano, a un asado no se falta. Es código."
    benjamin "Fue un homenaje. Un homenaje con pebre."
    scene bg potrero with fade
    show jose at center with dissolve
    "Mientras ellos comen, José se queda frente al portón vacío. En el celular tiene la foto de la parrilla que le mandó Benjamín."
    jose "Me lo dijiste. Y yo pensé que estabai puro webeando."
    "Vuelve a mirar el portón. Esta vez no tiene una explicación ni una boleta que mostrar."
    jose "La cagué, Shakira."

    $ persistent.finales.add(3)
    "FINAL 3 de 7: El funeral de Shakira"
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
    "En el sueño, José conserva el compu y recupera a Shakira. Pablo ya anda calculando cuánto le va a cobrar."
    "Todos celebran. Hasta Marcelo sonríe. Hasta Rubén se mueve. Un milagro."

    $ musica("tema.ogg")
    scene black with fade
    "Y entonces Pablo despertó."
    "Estaba dormido en el patio del INACAP, con la boca abierta, como siempre."
    "Nada de lo anterior había pasado. Ni el empeño. Ni los dos millones. Ni el rescate."
    "José la vendió. Punto. La PC sigue ahí. Y Pablo sigue sin un peso."
    show pablo at center with dissolve
    pablo "Soñé que la salvábamos."
    pablo "Por una vez soñé que no perdía las lucas."

    $ persistent.finales.add(6)
    "FINAL 6 de 7: El empeño (que nunca pasó)"
    jump creditos


label final_gamer:
    $ sfx("teclado.ogg")

    scene bg inacap with fade
    show jose at center with dissolve
    jose "Ya, pero ¿hasta cuándo con la misma wea? La vendí. El compu ya lo compré."
    "Benjamín espera que agregue algo. José revisa si le llegó un mensaje."

    if historia_escuchada:
        "Tú escuchaste las grabaciones. Le preguntas si al menos va a ir a verla. José dice que otro día."
    "Se acabaron las preguntas por hoy. Quedaron cosas sin aclarar y José no va a soltar más."
    "Y todos los fines de semana, en algún lugar de Temuco, alguien le pregunta a Pablo en qué se gastó los dos millones."
    show pablo at right with dissolve
    pablo "En puras leceras."

    if v_tinder:
        "Marcelo todavía tiene guardado el perfil que inventaron para José. José le pidió que borrara la foto de la yegua, por lo menos."

    if verdad_martin:
        show bastian at left, bastian_bajo with dissolve
        bastian "Como decía el profe Martín: esto en China no pasa. Bueno, según él."
        hide pablo with dissolve
        show benjamin at right with dissolve
        benjamin "¿¡Habló Bastián!? ¡Pachoclo, hablaste!"
        bastian "..."
        jose "Dice que sí habló."

    jose "Chao, chiquillos."
    "Lo dice igual que Rubén. Textual. El grupo entero se ofende."

    $ persistent.finales.add(4)
    "FINAL 4 de 7: El gamer eterno"
    jump creditos


label final_fundo:

    $ musica("triste.ogg")
    scene bg fundo with fade
    show benjamin at center with dissolve

    benjamin "Propuesta: Fundo El Carmen. Este sábado. Traigan carbón."
    mc "¿Carbón? ¿Para qué?"
    benjamin "Para el asado de la discordia."
    "Marcelo baja el celular. Pablo se saca las gafas para mirarlo bien."
    benjamin "Acuérdate de la ley. La que le puse a José en la primera visita: si algún día vendía a Shakira, yo la hacía asado."
    benjamin "Te lo dije pa que no la vendierai, José. No pa que me cotizarai el carbón."
    benjamin "Pero la vendió. Y una amenaza que no se cumple no es una lección. Es decoración."
    mc "Benjamín... ¿qué hiciste?"
    benjamin "Lo que prometí. Fui donde el vecino mapuche y le compré a Shakira. Boleta, certificado, transferencia. Todo legal."
    benjamin "Injusto... pero legítimo. Como la venta de José. Exactamente como la venta de José."
    show marcelo at left with dissolve
    marcelo "Bucha. Ni para los trabajos de ciberseguridad movió un dedo. ¿Y para ESTO hizo trámites?"
    benjamin "Bueno, ¿pa qué me dice que no la va a vender y después llega con el compu?"

    show jose at right with dissolve
    jose "¿Y yo qué tengo que ver en todo esto?"
    benjamin "Te avisé antes de que la vendierai. ¿Te acordai o no?"
    jose "Pensé que era una talla, wn."
    benjamin "Y yo pensé que no la ibai a vender."
    "José mira a Benjamín esperando que se ría. No se ríe. José se va antes del sábado; no quiere estar ahí cuando abran la parrilla."

    $ sfx("plato.ogg")
    scene asado parrilla with fade
    "Benjamín levanta la tapa de la parrilla. No es una forma de decirlo: en este cuento oscuro, ese asado es Shakira."
    benjamin "Sí, esa es la Shakira. No era una metáfora, wn."
    scene escena asado with dissolve
    show benjamin anticucho at center with dissolve

    "Este es el final oscuro del cuento de Benjamín. En su versión, el sábado hubo asado en Fundo El Carmen. Ni Marcelo quiere escuchar cómo sigue."
    "Los anticuchos empiezan a pasar de mano en mano. Benjamín reparte como si nadie acabara de escuchar lo que dijo."
    "Fabián puso a Yerba Brava. Nadie se la pidió. Todos la agradecieron. Pablo trajo las zanahorias, por costumbre. Rubén apareció sin que nadie lo invitara."
    show ruben anticucho at left with dissolve
    ruben "¿Y a ti qué te importa? ...Guárdame un pedazo. Y que no sea el duro."
    "Maxi Valenzuela llegó caminando desde Pedro de Valdivia. Nadie lo invitó. Nadie lo vio llegar. Ya estaba sirviéndose."
    show maxi anticucho at right with dissolve
    maxi "Conchetumare, Benjamín. Esto es lo más enfermo y lo más legal que he visto en mi vida, wn. Te admiro, negro."
    "Bastián cortó la leña. No dijo nada. Nunca dice nada. Pero cortó la leña perfecta."
    "Iván Garrido del 4F llegó por su cuenta. Nadie lo invitó. Traía ensalada. Nadie tocó la ensalada."
    hide benjamin with dissolve
    show ivan anticucho at center with dissolve
    ivan "Yo solo vine a reírme y a comer, wn. Y ya me reí."
    "Héctor filmó todo con el Suzuki Jeep de fondo. El video tiene tres millones de visitas. El algoritmo es un misterio."
    "Marcelo quiso subir la crónica a premierchilito, pero no era fútbol. Qué lata."
    scene bg potrero with fade
    show jose at center with dissolve
    "José no estuvo en el asado. Se quedó en Lincoñir, mirando el lugar donde Shakira lo esperaba."
    "La foto de la parrilla llegó al grupo. José la abrió una vez y dejó el celular boca abajo."
    jose "Lo dijiste de frente. Yo fui el aweonao que no te creyó."
    "Desde la casa suena el ventilador de la PC nueva. José no entra a prenderla."

    $ persistent.finales.add(5)
    "FINAL 5 de 7: El asado del Fundo El Carmen (final oscuro)"
    jump creditos


# =====================================================================
#  AL CARGAR UNA PARTIDA: recordatorio de dónde quedaste
# =====================================================================
label after_load:

    # El DLC conserva su escena y no usa el resumen de la campaña principal.
    if lucho_activo or ruta_lucho_activa or ruta_barbarita_activa or ruta_cuy_activa or sueno_pablo_activo:
        return

    # Conservar fondo y sprites para reanudar exactamente la escena guardada.

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
    "Música original: Fabián Millalén (Fabinho). Todas las canciones de esta versión fueron creadas por él."
    "«josep lo-fi lipian», «absentee melody», «black and white melodies» y «piano in father the houses»."
    "«rhythms of silence», «sheep rhythm», «wandering in the sea» y «whispers from beyond»."
    "El logo del juego también lo hizo Fabián."

    "Y desde ese año, nadie ha dejado de molestar a José. Ni un solo día."
    "Has desbloqueado [n_finales] de 7 finales."
    if traicion_ruben:
        "Rubén te sacó de su lista de fuentes de confianza. Te saluda igual, pero no cuenta nada."

    if max(rel.values()) > 0:
        $ amigo = max(rel, key=lambda k: rel[k])
        "Tu mejor amigo del semestre: [amigo]."
    if min(rel.values()) < 0:
        $ pendiente = min(rel, key=lambda k: rel[k])
        "Y [pendiente] todavía te tiene mala. Para siempre."

    if v_inundacion:
        "Pillalelbún sigue en pie. La próxima inundación se espera para 2034."

    if premier_bloqueado:
        "Marcelo perdió premierchilito. Todavía tiene los videos guardados, pero no quiere prestarle más el celular a Benjamín."
    elif promesa_marcelo:
        "Marcelo tiene un seguidor nuevo en premierchilito. Son 141.001. Sigue siendo qué lata, pero menos."
    if pablo_arruinado:
        "Pablo sigue apostando para pagar la Shell. Perdió el short apostando. Sigue en short."
    if v_sueno:
        "Y Pablo sigue soñando con un Pillalelbún próspero. Le apuesta a todo... menos a la realidad."

    "Dedicado con cariño a José, Pablo, Diego, Fabián, Marcelo, Benjamín, Bastián, Rubén y Maxi..."
    "...a Bastián dos veces, porque habla tan poco que hay que nombrarlo por él..."
    "...a Iván Garrido del 4F, que esquivó la milicia con un solo PDF..."
    "...y a Diego, primer año eterno, a quien el ejército se lo perdió por no tener un sicólogo con criterio..."
    "...al profe Martín, que sí llegó a Shenzhen; el puesto todavía cambia según quién pregunte..."
    "...a Héctor y su Suzuki Jeep cuatro por cuatro..."
    "...y a Shakira, dondequiera que esté. Probablemente comiendo zanahorias. Esperamos."
    call balance_profes
    "Gracias por jugar."

    return
