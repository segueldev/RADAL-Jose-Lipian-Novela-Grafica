# Solo en la copia de pruebas. No se distribuye.
init 999 python:
    config.savedir = "/tmp/radal-replay-qa"
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.autosave_frequency = None

    def qa_foco_virtual():
        # El motor rechaza clics simulados si el cursor real está fuera de la ventana.
        # Solo en pruebas: dar foco al ratón virtual en cada interacción.
        renpy.display.interface.mouse_focused = True

    config.interact_callbacks.append(qa_foco_virtual)

    def qa_elegir(caption):
        item = next(i for i in renpy.get_screen("choice").scope["items"] if i.caption == caption and i.action is not None)
        renpy.show_screen("qa_click_timer", item.action)

    def qa_hub():
        sc = renpy.get_screen("choice")
        return sc is not None and any(i.caption.startswith("Patio del INACAP") for i in sc.scope["items"])

label qa_pistas:
    $ venta = True
    $ v_shell = True
    $ v_jumbo = True
    $ v_fabian_sale = True
    $ v_pelea_inacapini = True
    $ v_incidente = True
    $ v_ruben = True
    $ v_conflicto_ruben = True
    jump hub

label qa_final:
    $ venta = True
    $ v_incidente = True
    $ pista_pablo = qa_tipo == "verdadero"
    $ pista_diego = qa_tipo == "verdadero"
    $ pista_potrero = qa_tipo == "verdadero"
    $ drama = 5 if qa_tipo == "funeral" else 0
    $ apoyo = 6 if qa_tipo == "empeno" else (3 if qa_tipo == "custodia" else 0)
    $ rel["José"] = 2 if qa_tipo == "empeno" else 0
    $ broma_benjamin = 2 if qa_tipo == "fundo" else 0
    jump confrontacion

default qa_tipo = ""

testsuite qa:
    testcase bolsa_inicios:
        advance until screen "main_menu"
        python:
            copia = list(persistent.inicios_pendientes or [])
            ultimo = persistent.ultimo_inicio
            try:
                persistent.inicios_pendientes = []
                persistent.ultimo_inicio = 6
                tiradas = [siguiente_inicio() for _ in range(16)]
                assert set(tiradas[:8]) == set(range(1,9))
                assert len(set(tiradas[:8])) == 8
                assert len(set(tiradas[8:])) == 8
                assert tiradas[0] in (7,8)
                assert tiradas[7] != tiradas[8]
            finally:
                persistent.inicios_pendientes = copia
                persistent.ultimo_inicio = ultimo
                renpy.save_persistent()

    testcase entradas:
        parameter entrada = ["prologo_lluvia", "prologo_frio", "prologo_sol", "prologo_tarde", "prologo_temprano", "inicio_cisterna", "inicio_sala", "inicio_termo"]
        parameter breve = [False, True]
        advance until screen "main_menu"
        run Start(entrada)
        pause 0.1
        $ presentacion_corta = breve
        advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15
        if not eval qa_hub():
            $ qa_opcion = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion)
            pause 0.15
            advance until screen "choice" timeout 15

        assert eval qa_hub()
        assert eval not venta
        run MainMenu(confirm=False)

    testcase recuperar_pistas:
        advance until screen "main_menu"
        run Start("qa_pistas")
        advance until screen "choice" timeout 15
        assert eval any("revisar la cabina" in i.caption for i in renpy.get_screen("choice").scope["items"])
        run Function(qa_elegir, "Volver a la Shell: revisar la cabina")
        pause 0.2
        advance until screen "choice" timeout 15
        assert eval pista_pablo
        run Function(qa_elegir, "Volver al Jumbo: preguntar por las zanahorias")
        pause 0.2
        advance until screen "choice" timeout 15
        assert eval pista_diego
        run MainMenu(confirm=False)

    testcase seis_finales:
        parameter tipo = ["verdadero", "custodia", "funeral", "empeno", "gamer", "fundo"]
        $ persistent.finales.discard({"verdadero":1,"custodia":2,"funeral":3,"empeno":6,"gamer":4,"fundo":5}[tipo])
        advance until screen "main_menu"
        run Start("qa_final")
        pause 0.1
        # La configuración de la ruta se hace tras iniciar el contexto.
        $ qa_tipo = tipo
        $ pista_pablo = tipo == "verdadero"
        $ pista_diego = tipo == "verdadero"
        $ pista_potrero = tipo == "verdadero"
        $ drama = 5 if tipo == "funeral" else 0
        $ apoyo = 6 if tipo == "empeno" else (3 if tipo == "custodia" else 0)
        $ rel["José"] = 2 if tipo == "empeno" else 0
        $ broma_benjamin = 2 if tipo == "fundo" else 0
        advance until screen "choice" timeout 15
        if eval tipo == "fundo":
            run Function(qa_elegir, "Escuchar la propuesta de Benjamín.")
            pause 0.2
        elif eval tipo == "gamer":
            run Function(qa_elegir, "Invitarlo a jugar en su PC y dejar el tema.")
            pause 0.2
        elif eval tipo == "funeral":
            run Function(qa_elegir, "Acusar a José frente a todos. ¡Es un traidor!")
            pause 0.2
        else:
            run Function(qa_elegir, "Hablar con José desde el corazón.")
            pause 0.2
        advance until screen "main_menu"
        assert eval {"verdadero":1,"custodia":2,"funeral":3,"empeno":6,"gamer":4,"fundo":5}[tipo] in persistent.finales

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

screen qa_click_timer(action):
    timer 0.05 action [Hide("qa_click_timer"), action]
