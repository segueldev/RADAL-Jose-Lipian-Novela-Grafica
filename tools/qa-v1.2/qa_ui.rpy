testsuite ui:
    before testcase:
        $ renpy.test.testmouse.reset()

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase leer_y_elegir:
        advance until screen "main_menu"
        run Start("inicio_termo")
        advance until screen "choice"
        pause 0.5
        screenshot "decisiones-legibles.png"
        $ renpy.display.interface.mouse_focused = True
        click pos (960,355) until not screen "choice" timeout 15
        advance until screen "choice"
        assert eval favor_inicio == "te"

    testcase scroll_visitas:
        advance until screen "main_menu"
        run Start("qa_pistas")
        advance until screen "choice"
        pause 0.5
        screenshot "visitas-desplazables.png"
        scroll amount 12 id "decisiones_largas"
        pause 0.5
        screenshot "visitas-desplazadas.png"
        assert eval renpy.get_screen("choice") is not None
