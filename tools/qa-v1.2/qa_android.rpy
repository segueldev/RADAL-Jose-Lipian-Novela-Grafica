testsuite android:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase ayuda_tactil:
        advance until screen "main_menu"
        assert eval renpy.variant("touch") and renpy.variant("small")
        run renpy.get_widget("main_menu", "menu_ayuda", base=True).action
        pause until screen "help"
        screenshot "android-ayuda.png"
        assert "Jugar en Android"
        click "Volver"
        pause until screen "main_menu"

    testcase partida_y_menu:
        advance until screen "main_menu"
        run Start("inicio_termo")
        advance until screen "choice"
        screenshot "android-decision.png"
        run Function(qa_elegir, "Ofrecerle una bolsita de té que llevas en la mochila.")
        pause 0.2
        advance until screen "choice"
        run ShowMenu("save")
        pause until screen "save"
        screenshot "android-guardar.png"
        run FileSave("qa-android",confirm=False)
        pause 0.4
        $ favor_inicio = "qa-cambiado"
        run FileLoad("qa-android",confirm=False)
        pause 0.8
        assert eval favor_inicio == "te"
