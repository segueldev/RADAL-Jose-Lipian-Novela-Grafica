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
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 1
        screenshot "inicio_1.png"

    testcase inicio_2:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [2]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 2

    testcase inicio_3:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [3]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 3

    testcase inicio_4:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [4]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 4

    testcase inicio_5:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [5]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 5

    testcase inicio_6:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [6]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 6

    testcase inicio_7:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [7]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 7

    testcase inicio_8:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [8]
        run Start()
        advance until screen "input" timeout 20
        type 'Benjamin'
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Benjamin'
        assert eval prologo == 8

    testcase nombre_vacio:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [2]
        run Start()
        advance until screen "input" timeout 20
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Kabro'
        assert eval prologo == 2

    testcase solo_espacios:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [3]
        run Start()
        advance until screen "input" timeout 20
        type '   '
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'Kabro'
        assert eval prologo == 3

    testcase nombre_acentos:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [1]
        run Start()
        advance until screen "input" timeout 20
        run Function(qa_escribir_nombre, '  José  ')
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == 'José'
        assert eval prologo == 1
        screenshot "nombre_acentos.png"

    testcase nombre_simbolos:
        advance until screen "main_menu"
        $ persistent.finales = set()
        $ persistent.inicios_pendientes = [1]
        run Start()
        advance until screen "input" timeout 20
        run Function(qa_escribir_nombre, '{b}[Jose]')
        keysym "K_RETURN"
        advance until screen "choice" timeout 20
        assert eval nombre == '{{b}[Jose]'
        assert eval prologo == 1
        screenshot "nombre_simbolos.png"
