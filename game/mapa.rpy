# Mapa de recorridos dibujado con elementos del motor; no requiere conexión.
default ultima_visita = "INACAP"

init python:
    def destinos_mapa():
        s = store
        return [
            ("INACAP", "El punto de encuentro", "images/bg inacap.webp", 660, 510),
            ("Jumbo · Portal Temuco", "Diego · Hasbro", "images/bg jumbo.jpeg", 270, 500),
            ("Politécnico · Pueblo Nuevo", "Historias del liceo", "images/bg liceo.jpeg", 610, 260),
            ("Shell · Lautaro", "Pablo · camino a Pillalelbún", "images/bg shell.png", 990, 260),
            ("Lincoñir", "Padre Las Casas · José y Shakira", "images/bg potrero.png", 990, 800),
            ("Labranza", "Una vuelta por Acuenta", "images/lucho/labranza.webp", 270, 800),
            ("Cerro Ñielol", "Preparar a José", "images/eventos/nielol_camino.webp", 270, 270),
            ("Villarrica", "Seguir el viaje de José por celular", "images/eventos/jose_arbol.jpeg", 660, 820),
        ]

    def miniatura_mapa(archivo):
        w, h = renpy.image_size(archivo)
        proporcion = 246.0 / 90.0
        if w / float(h) > proporcion:
            cw, ch = int(h * proporcion), h
        else:
            cw, ch = w, int(w / proporcion)
        return Transform(archivo, crop=((w-cw)//2, (h-ch)//2, cw, ch), xysize=(246,90))

    def opciones_mapa(destino):
        s = store
        acciones = []
        if destino == "INACAP":
            if not s.v_patio:
                acciones.append(("Ir al patio con los cabros", "patio"))
            if not s.chocolate_fabian and not s.v_fabian_sale:
                acciones.append(("Conversar con Fabián", "charla_fabian"))
            if not s.historia_cuy:
                acciones.append(("Conversar con Rubén", "charla_ruben"))
            if not s.origen_bastian:
                acciones.append(("Preguntarle a Bastián por la vuelta", "charla_bastian"))
            if s.historia_cuy and not s.v_cuy_asado:
                acciones.append(("¿Y si…? El congelador de Fabián", "whatif_cuy"))
            if s.whatif_tinder_activo and not s.v_tinder:
                acciones.append(("¿Y si…? Cupido de alquiler", "whatif_tinder"))
            if s.whatif_trabajo_activo and not s.v_trabajo:
                acciones.append(("¿Y si…? El trabajo en grupo", "whatif_trabajo"))
            if s.whatif_inacapini_activo and not s.v_inacapini:
                acciones.append(("¿Y si…? El sospechoso azul", "whatif_inacapini"))
            if s.venta and s.lugares >= 3:
                acciones.append(("Hablar con José para cerrar el caso", "confrontacion"))
        elif destino == "Shell · Lautaro":
            if not s.v_shell:
                acciones.append(("Visitar a Pablo y Fabián", "shell"))
            if s.venta and s.v_shell and not s.pista_pablo:
                acciones.append(("Preguntar por la cabina", "shell_pistas"))
            if s.v_shell and not s.v_sueno:
                acciones.append(("Volver a conversar con Pablo", "sueno_pablo"))
        elif destino == "Jumbo · Portal Temuco":
            if not s.v_jumbo:
                acciones.append(("Visitar a Diego en Hasbro", "jumbo"))
            if s.venta and s.v_jumbo and not s.pista_diego:
                acciones.append(("Preguntarle a Diego por las compras", "jumbo_pistas"))
        elif destino == "Politécnico · Pueblo Nuevo":
            if not s.v_liceo:
                acciones.append(("Ir con los cabros al liceo", "liceo"))
        elif destino == "Lincoñir":
            if not s.venta and s.potrero_visitas < 3:
                acciones.append(("Visitar a José · %d de 3" % (s.potrero_visitas + 1), "potrero_visita"))
            if s.venta and not s.v_potrero:
                acciones.append(("Revisar el potrero", "potrero"))
        elif destino == "Labranza":
            if s.venta and not s.v_lucho_labranza:
                acciones.append(("¿Y si…? Seguir el dato de Lucho", "whatif_labranza"))
        elif destino == "Cerro Ñielol":
            if s.v_tinder and not s.v_nielol:
                acciones.append(("¿Y si…? Subir con el grupo", "entreno_nielol"))
        elif destino == "Villarrica":
            if s.preparado_barbarita and not s.v_villarrica:
                acciones.append(("¿Y si…? Escuchar a José desde Villarrica", "whatif_villarrica"))
        return acciones

    def nota_mapa(destino):
        if destino == "INACAP":
            return "ESTÁS AQUÍ\nEntre viajes vuelves al INACAP para juntarte con el grupo."
        if destino == "Villarrica":
            return "José viaja; tú sigues en Temuco. Se sigue la historia por sus audios." if store.preparado_barbarita else "José primero necesita prepararse con el grupo en el Ñielol."
        if destino == "Cerro Ñielol" and not store.v_tinder:
            return "La salida aparece después de Cupido de alquiler."
        if destino == "Labranza":
            return "Ruta alternativa disponible: empieza otra versión de la historia." if store.venta else "Todavía no hay un motivo para viajar. El dato aparece más adelante."
        if opciones_mapa(destino):
            return "Hay una visita o conversación pendiente. Elige abajo qué quieres hacer."
        return "Ya viste las escenas disponibles acá. Si aparece otro dato, el mapa lo mostrará."

    class PaisajeRadal(renpy.Displayable):
        def render(self, width, height, st, at):
            r = renpy.Render(1260, 1080)
            c = r.canvas()
            # Papel, campos, barrios y río: ilustración de recorridos del grupo.
            c.rect("#d7d0b3", (40,155,1210,780))
            c.polygon("#aab797", [(40,155),(410,155),(460,370),(360,610),(40,640)])
            c.polygon("#b9be91", [(820,155),(1250,155),(1250,580),(1020,600),(880,420)])
            c.polygon("#acb47f", [(400,700),(1250,665),(1250,935),(390,935)])
            for x, y, w, h in [(430,350,95,70),(565,340,90,65),(715,335,130,65),(860,385,80,95),(415,465,90,70),(750,470,120,85),(480,575,100,65),(650,590,90,45)]:
                c.rect("#c3bda4", (x,y,w,h))
                c.rect("#b0aa96", (x+7,y+7,w-14,h-14), 2)
            rio = [(40,650),(190,615),(370,635),(540,675),(710,660),(850,635),(1000,655),(1120,625),(1250,640)]
            c.lines("#85a7a6", False, rio, 34)
            c.lines("#aac7bb", False, [(x,y-7) for x,y in rio], 7)
            rutas = [[(270,270),(440,250),(610,260)],[(660,510),(650,650),(660,820)],[(270,800),(270,500),(445,505),(660,510)],[(660,510),(645,380),(610,260)],[(610,260),(790,255),(990,260)],[(660,510),(795,570),(840,680),(990,800)]]
            for ruta in rutas:
                c.lines("#b1a38b", False, ruta, 28)
                c.lines("#f2e5c2", False, ruta, 19)
                c.lines("#c5b996", False, ruta, 2)
            # Puente sobre el río y arboledas con formas simples.
            c.line("#83735e", (825,632),(850,696), 32)
            c.line("#e5d8b8", (825,632),(850,696), 23)
            for x,y in [(110,210),(145,235),(190,195),(1090,420),(1140,440),(1180,395),(1080,885),(1140,865),(130,865),(180,880),(110,380),(1010,460)]:
                c.circle("#7b946f",(x+3,y+4),18)
                c.circle("#58765d",(x,y),15)
                c.circle("#8fa080",(x-5,y-5),8)
            # Límite y rosa de orientación.
            c.rect("#9c947a", (40,155,1210,780), 2)
            c.line("#514d40", (1190,820),(1190,878), 3)
            c.polygon("#514d40",[(1190,802),(1182,829),(1198,829)])
            return r

screen mapa_recorridos():
    modal True
    zorder 150
    default seleccionado = "INACAP"
    add Solid("#142829")
    add PaisajeRadal()
    text "RADAL / CUADERNO DE VIAJE" xpos 70 ypos 38 size 42 color "#f5e6c6" bold True
    text "Marca un destino. Los cabros ponen el resto." xpos 70 ypos 95 size 26 color "#bed1cd"
    text "PUEBLO NUEVO" xpos 465 ypos 185 size 21 color "#5a6650"
    text "TEMUCO" xpos 550 ypos 365 size 38 color "#79705b" bold True
    text "RÍO CAUTÍN" xpos 420 ypos 700 size 22 color "#446868" italic True
    text "N" xpos 1180 ypos 780 size 22 color "#514d40"
    for indice, (sitio, descripcion, foto, xx, yy) in enumerate(destinos_mapa()):
        button:
            id ("mapa_" + str(indice))
            pos (xx, yy)
            anchor (0.5,0.5)
            xsize 288
            ysize 110
            padding (16,14)
            background Solid("#775a32f5" if seleccionado == sitio else "#183b35ee")
            hover_background Solid("#527879")
            action SetScreenVariable("seleccionado", sitio)
            vbox:
                spacing 7
                text sitio size 22 color "#ffffff" bold True
                text ("TÚ ESTÁS AQUÍ" if sitio == "INACAP" else ("Visita pendiente" if opciones_mapa(sitio) else "Sin escenas pendientes")) size 18 color "#f8d18d"
    text "Temuco y alrededores · plano de recorridos, no a escala" xpos 70 ypos 960 size 23 color "#aac0ba"
    frame:
        xpos 1300
        ypos 35
        xsize 570
        ysize 930
        background "#0e1b20ef"
        padding (28,28)
        vbox:
            spacing 15
            text seleccionado size 34 color "#f8d18d" bold True
            $ foto_elegida = next(f for sitio, descripcion, f, xx, yy in destinos_mapa() if sitio == seleccionado)
            add miniatura_mapa(foto_elegida):
                zoom 1.95
            text nota_mapa(seleccionado) size 26 color "#dae6e1"
            text "Última visita: [ultima_visita]" size 23 color "#a9beb8"
            viewport:
                ysize 405
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 12
                    for titulo, destino in opciones_mapa(seleccionado):
                        textbutton titulo:
                            xsize 485
                            padding (18,16)
                            background "#284448"
                            hover_background "#456c6a"
                            text_size 26
                            text_color "#ffffff"
                            action Return(destino)
                    textbutton "Revisar las notas del caso":
                        xsize 485
                        padding (18,16)
                        background "#25343b"
                        text_size 24
                        text_color "#e4e4da"
                        action Return("cuaderno")
    textbutton "Volver al grupo":
        xpos 1460
        ypos 990
        padding (24,12)
        background "#a57d41"
        text_color "#ffffff"
        text_size 27
        action Return(None)
    key "game_menu" action Return(None)

label mapa_viajes:
    hide screen aviso_recuerda
    hide screen aviso_whatif
    call screen mapa_recorridos
    if _return:
        $ renpy.jump(_return)
    jump hub
