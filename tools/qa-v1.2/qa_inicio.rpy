init 999 python:
    config.savedir = "/tmp/radal-qa-nombre-20261009"
    def qa_escribir_nombre(texto):
        renpy.get_widget("input", "input", base=True).update_text(texto, True)
        renpy.restart_interaction()

testsuite inicio_real:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase inicio_1:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [1]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 1
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()
        screenshot "inicio_1.png"

    testcase inicio_2:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [2]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 2
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_3:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [3]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 3
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_4:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [4]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 4
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_5:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [5]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 5
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_6:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [6]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 6
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_7:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [7]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 7
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase inicio_8:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [8]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type 'Benjamin'
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 8
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase nombre_vacio:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [2]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Kabro'
        assert eval prologo == 2
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase solo_espacios:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [3]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        type '   '
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'Kabro'
        assert eval prologo == 3
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase nombre_acentos:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [1]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        run Function(qa_escribir_nombre, '  José  ')
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == 'José'
        assert eval prologo == 1
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()
        screenshot "nombre_acentos.png"

    testcase nombre_simbolos:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [1]
        run Start()
        advance until screen "input" timeout 20
        pause 0.3
        run Function(qa_escribir_nombre, '{b}[Jose]')
        pause 0.2
        keysym "K_RETURN"
        pause until not screen "input" timeout 5
        advance until screen "choice" timeout 20
        assert eval nombre == '{{b}[Jose]'
        assert eval prologo == 1
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        if not eval qa_hub():
            $ qa_opcion_inicio = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None and i.caption != "Abrir el mapa de viajes")
            run Function(qa_elegir, qa_opcion_inicio)
            pause 0.1
            advance until screen "choice" timeout 20
        assert eval qa_hub()
        screenshot "nombre_simbolos.png"

    testcase llamadas_motor:
        advance until screen "main_menu"
        assert eval all(callable(getattr(renpy, api, None)) for api in ['Render', 'file', 'filter_text_tags', 'get_screen', 'hide_screen', 'image_size', 'input', 'jump', 'loadable', 'newest_slot', 'pause', 'redraw', 'register_shader', 'save_persistent', 'say', 'show_screen', 'showing', 'variant'])
