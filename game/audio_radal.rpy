# Música original de Fabián y efectos de acción propios del juego.
default categoria_musica_radal = "general"
default canal_musica_radal = "music"
default bolsas_musica_radal = {}
default titulo_musica_radal = ""
default pista_musica_radal = ""
default persistent.aviso_musica_radal = True

init 10 python:
    import json
    niveles_fabian = json.loads(renpy.file("audio/fabian/niveles.json").read())
    renpy.music.register_channel("musica_radal_b", mixer="music", loop=False)
    catalogo_fabian = {
        'josep_lofi_lipian': ('audio/fabian/josep_lofi_lipian.ogg', 'josep lo-fi lipian', 143.964),
        'absentee_melody': ('audio/fabian/absentee_melody.ogg', 'absentee melody', 33.948),
        'black_white_melodies': ('audio/fabian/black_white_melodies.ogg', 'black and white melodies', 42.26),
        'piano_father_houses': ('audio/fabian/piano_father_houses.ogg', 'piano in father the houses', 72.098),
        'rhythms_silence': ('audio/fabian/rhythms_silence.ogg', 'rhythms of silence', 39.126),
        'sheep_rhythm': ('audio/fabian/sheep_rhythm.ogg', 'sheep rhythm', 42.864),
        'wandering_sea': ('audio/fabian/wandering_sea.ogg', 'wandering in the sea', 101.773),
        'whispers_beyond': ('audio/fabian/whispers_beyond.ogg', 'whispers from beyond', 70.519),
    }
    class BarrasFabian(renpy.Displayable):
        def render(self, width, height, st, at):
            r = renpy.Render(110,24)
            c = r.canvas()
            pos = renpy.music.get_pos(channel=store.canal_musica_radal)
            datos = niveles_fabian.get(store.pista_musica_radal, [])
            fila = datos[min(int(pos/0.12),len(datos)-1)] if datos and pos is not None else [0]*5
            if renpy.game.preferences.get_mute("music") or renpy.game.preferences.get_volume("music") == 0:
                fila = [0]*5
            for i, valor in enumerate(fila):
                alto = 2 + int(valor/255.0*21)
                c.rect("#d1b474",(i*15,24-alto,9,alto))
            renpy.redraw(self,0.08)
            return r

    listas_fabian = {
        "general": ["josep_lofi_lipian", "piano_father_houses", "sheep_rhythm", "black_white_melodies"],
        "viaje": ["wandering_sea", "piano_father_houses", "sheep_rhythm"],
        "calma": ["piano_father_houses", "rhythms_silence", "absentee_melody"],
        "triste": ["absentee_melody", "black_white_melodies", "rhythms_silence"],
        "tension": ["whispers_beyond", "black_white_melodies", "wandering_sea"],
        "humor": ["sheep_rhythm", "josep_lofi_lipian", "piano_father_houses"],
    }

    def siguiente_tema_fabian(categoria):
        bolsa = list(store.bolsas_musica_radal.get(categoria, []))
        if not bolsa:
            bolsa = list(listas_fabian[categoria])
            renpy.random.shuffle(bolsa)
        candidatos = [i for i in bolsa if catalogo_fabian[i][0] != store.pista_musica_radal]
        elegido = candidatos[0] if candidatos else bolsa[0]
        bolsa.remove(elegido)
        store.bolsas_musica_radal[categoria] = bolsa
        return catalogo_fabian[elegido][0]

    def ficha_tema_fabian(archivo):
        return next((datos for datos in catalogo_fabian.values() if datos[0] == archivo), None)

    def reproducir_fabian(archivo):
        actual = renpy.music.get_playing(channel=store.canal_musica_radal)
        if actual != archivo:
            viejo = store.canal_musica_radal
            nuevo = "musica_radal_b" if viejo == "music" else "music"
            renpy.music.set_volume(0.82, channel=nuevo)
            renpy.music.play(archivo, channel=nuevo, loop=False, fadein=1.6)
            renpy.music.stop(channel=viejo, fadeout=1.6)
            store.canal_musica_radal = nuevo
        actualizar_ficha_fabian(archivo)

    def actualizar_ficha_fabian(archivo):
        datos = ficha_tema_fabian(archivo)
        if datos and (archivo != store.pista_musica_radal or not renpy.get_screen("musica_actual_radal")):
            store.pista_musica_radal = archivo
            store.titulo_musica_radal = datos[1]
            renpy.show_screen("musica_actual_radal", titulo=datos[1])

    def musica_fabian(pedido):
        palabra = pedido.rsplit(".",1)[0]
        categoria = {"tema":"general", "dramatica":"tension", "cumbia":"humor"}.get(palabra,palabra)
        if categoria not in listas_fabian:
            # Conserva compatibilidad con futuros archivos externos.
            if renpy.loadable("audio/"+pedido):
                renpy.music.play("audio/"+pedido, fadeout=1.6, fadein=1.6)
            return
        actual = renpy.music.get_playing(channel=store.canal_musica_radal)
        if categoria != store.categoria_musica_radal or not ficha_tema_fabian(actual):
            store.categoria_musica_radal = categoria
            reproducir_fabian(siguiente_tema_fabian(categoria))
        else:
            actualizar_ficha_fabian(actual)

    def intercalar_fabian():
        if store.main_menu:
            renpy.music.stop(channel="musica_radal_b", fadeout=0.5)
            return
        actual = renpy.music.get_playing(channel=store.canal_musica_radal)
        datos = ficha_tema_fabian(actual)
        if datos:
            actualizar_ficha_fabian(actual)
        pos = renpy.music.get_pos(channel=store.canal_musica_radal)
        if not actual or (datos and pos is not None and pos >= datos[2]-1.8):
            reproducir_fabian(siguiente_tema_fabian(store.categoria_musica_radal))

    def efecto_radal(nombre):
        fn = "audio/efectos/" + nombre.rsplit(".",1)[0] + ".ogg"
        if not renpy.loadable(fn):
            fn = "audio/" + nombre
        if renpy.loadable(fn):
            renpy.sound.play(fn)
            return True
        return False

    escenas_musicales = {
        "hub":"general", "patio":"general", "charla_ruben":"calma", "charla_fabian":"humor",
        "charla_bastian":"general", "potrero_visita":"viaje", "potrero1":"viaje", "potrero2":"humor",
        "potrero3":"calma", "entreno_nielol":"viaje", "whatif_villarrica":"calma",
        "whatif_tinder":"humor", "whatif_trabajo":"humor", "whatif_inacapini":"tension",
        "whatif_cuy":"tension", "choque_de_benjamin":"tension", "inundacion":"tension",
        "sueno_pablo":"humor", "la_venta":"triste", "confrontacion":"tension",
        "final_custodia":"calma", "final_verdadero":"calma", "final_empeno":"triste",
        "final_funeral":"triste", "final_gamer":"humor", "final_fundo":"tension",
        "jumbo":"general", "liceo":"calma", "shell":"general", "whatif_labranza":"viaje",
        "creditos":"calma",
    }
    anterior_label_radal = config.label_callback
    def musica_por_escena_radal(etiqueta, abnormal):
        if anterior_label_radal:
            anterior_label_radal(etiqueta, abnormal)
        if etiqueta in escenas_musicales:
            musica_fabian(escenas_musicales[etiqueta])
    config.label_callback = musica_por_escena_radal
    config.overlay_screens.append("reloj_musica_radal")

transform cambio_cancion_radal:
    on show:
        alpha 0.0
        yoffset 15
        ease 0.5 alpha 1.0 yoffset 0
    on replace:
        alpha 0.0
        yoffset 12
        ease 0.4 alpha 1.0 yoffset 0

screen reloj_musica_radal():
    timer 0.5 repeat True action Function(intercalar_fabian)

screen musica_actual_radal(titulo):
    zorder 15
    if persistent.aviso_musica_radal and not main_menu and not renpy.get_screen("mapa_recorridos") and not renpy.get_screen("preferences") and not renpy.get_screen("save") and not renpy.get_screen("load") and not renpy.get_screen("history") and not renpy.get_screen("about") and not renpy.get_screen("help") and not (renpy.showing("martin") and renpy.get_screen("aviso_recuerda")):
        frame:
            xpos 24
            ypos (24 if renpy.showing("martin") else 140)
            xsize 350
            padding (12,10)
            background Solid("#132627de")
            at cambio_cancion_radal
            hbox:
                spacing 12
                add Transform("images/eventos/portada_musica.png", xysize=(70,70), fit="contain")
                vbox:
                    spacing 4
                    text titulo size 18 color "#efe7d3" xmaximum 240
                    text "Creado por Fabián · Fabinho" size 14 color "#b4c7bc"
                    add BarrasFabian()
