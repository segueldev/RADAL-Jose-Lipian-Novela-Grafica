testsuite menus:
    before testcase:
        $ renpy.test.testmouse.reset()

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase portada_y_opciones:
        advance until screen "main_menu"
        screenshot "portada-1.2.png"
        run renpy.get_widget("main_menu", "menu_opciones", base=True).action
        pause until screen "preferences"
        $ lluvia_antes = persistent.lluvia_animada
        click "Lluvia animada"
        pause 0.3
        assert eval persistent.lluvia_animada != lluvia_antes
        click "Lluvia animada"
        pause 0.3
        assert eval persistent.lluvia_animada == lluvia_antes
        screenshot "opciones-1.2.png"
        click "Volver"
        pause 0.3
        pause until screen "main_menu"

    testcase acerca_y_ayuda:
        advance until screen "main_menu"
        run renpy.get_widget("main_menu", "menu_acerca", base=True).action
        pause until screen "about"
        screenshot "acerca-1.2.png"
        click "Volver"
        pause 0.3
        pause until screen "main_menu"
        run renpy.get_widget("main_menu", "menu_ayuda", base=True).action
        pause until screen "help"
        click "Ratón"
        screenshot "ayuda-1.2.png"
        click "Volver"
        pause 0.3
        pause until screen "main_menu"

    testcase personajes_y_dlc:
        advance until screen "main_menu"
        assert eval renpy.get_widget("main_menu", "menu_lucho", base=True).action.label == "lucho_inicio"
        run renpy.get_widget("main_menu", "menu_personajes", base=True).action
        pause until screen "personajes_radal"
        screenshot "los-cabros.png"
        click "Volver"
        pause until screen "main_menu"
