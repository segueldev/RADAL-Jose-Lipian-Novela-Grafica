default qa_venta_choque = False

label qa_shell_choque:
    $ broma_benjamin = 1
    $ venta = qa_venta_choque
    $ v_incidente = True
    $ v_fabian_sale = True
    $ v_pelea_inacapini = True
    $ v_ruben = True
    $ v_conflicto_ruben = True
    $ v_conflicto_marcelo = True
    $ v_inundacion = True
    $ v_juicio_shell = True
    jump shell

label qa_fulgor:
    scene bg shell_ruinas
    show screen explosion_shell
    "Una sola explosión breve."
    hide screen explosion_shell
    return

testsuite nuevos_visuales:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase manejo_y_consecuencias:
        parameter vendida = [False,True]
        advance until screen "main_menu"
        $ qa_venta_choque = vendida
        run Start("qa_shell_choque")
        advance until screen "choice" timeout 15
        if not eval any(i.caption == "Dejar que Benjamín maneje la cisterna." for i in renpy.get_screen("choice").scope["items"]):
            $ primera = next(i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None)
            run Function(qa_elegir, primera)
            pause 0.2
            advance until screen "choice" timeout 15
        run Function(qa_elegir, "Dejar que Benjamín maneje la cisterna.")
        pause 0.2
        advance until "Si manejo tractor, puedo manejar esta wea." timeout 15
        screenshot ("benjamin-pilla-%s.png" % vendida)
        assert eval renpy.showing("escena benjamin_pillalelbun")
        advance until "Sí, si estoy frenando." timeout 15
        screenshot ("benjamin-shell-%s.png" % vendida)
        assert eval renpy.showing("escena benjamin_shell")
        advance until "Desde afuera, la cisterna cruza el patio directo hacia la tienda. El tanque se lleva una columna y golpea los surtidores." timeout 15
        pause 0.8
        screenshot "cisterna-impacto-exterior.png"
        assert eval renpy.showing("camion_choque")
        advance until "El golpe corta el ruido del motor. Después viene el estruendo. Humo, fuego y el techo de la Shell cayendo sobre el patio." timeout 15
        screenshot "shell-destruida.png"
        assert eval renpy.showing("bg shell_ruinas") and renpy.get_screen("explosion_shell") is None
        advance until screen "choice" timeout 15
        assert eval pablo_arruinado and pista_pablo == vendida
        assert eval any("Shell quedó dañada" in nota for nota in decisiones_clave)

    testcase efecto_explosion:
        advance until screen "main_menu"
        run Start("qa_fulgor")
        pause 0.4
        screenshot "explosion-shader.png"
        assert eval renpy.get_screen("explosion_shell") is not None
        advance until screen "main_menu"

    testcase parrilla_y_anticuchos:
        parameter oscuro = ["final_funeral","final_fundo"]
        advance until screen "main_menu"
        run Start(oscuro)
        advance until "Sí, esa es la Shakira. No era una metáfora, wn." timeout 15
        screenshot ("parrilla-%s.png" % oscuro)
        assert eval renpy.showing("asado parrilla")
        if eval oscuro == "final_funeral":
            advance until "Fue un homenaje. Un homenaje con pebre." timeout 15
            assert eval renpy.showing("benjamin anticucho") and renpy.showing("pablo anticucho") and not renpy.showing("jose") and renpy.showing("fabian anticucho")
        else:
            advance until "Conchetumare, Benjamín. Esto es lo más enfermo y lo más legal que he visto en mi vida, wn. Te admiro, negro." timeout 15
            assert eval renpy.showing("benjamin anticucho") and renpy.showing("ruben anticucho") and renpy.showing("maxi anticucho")
        assert eval not renpy.showing("jose")
        screenshot ("anticuchos-%s.png" % oscuro)
        if eval oscuro == "final_fundo":
            advance until "Yo solo vine a reírme y a comer, wn. Y ya me reí." timeout 15
            screenshot "anticucho-ivan.png"
            assert eval renpy.showing("ivan anticucho") and not renpy.showing("benjamin")
        advance until screen "main_menu" timeout 15
        assert eval (3 if oscuro == "final_funeral" else 5) in persistent.finales
