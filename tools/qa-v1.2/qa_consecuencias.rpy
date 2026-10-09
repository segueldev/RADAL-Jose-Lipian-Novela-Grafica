label qa_cabina:
    $ venta = True
    $ pablo_molesto = True
    $ rel["Pablo"] = -1
    $ v_incidente = True
    $ v_fabian_sale = True
    $ v_pelea_inacapini = True
    $ v_ruben = True
    $ v_conflicto_ruben = True
    jump shell_pistas

label qa_testigo:
    $ pista_diego = True
    $ pista_potrero = True
    $ pista_pablo = False
    $ pista_ruben = True
    $ secreto_ruben = True
    $ rel["Rubén"] = 2
    jump confrontacion

label qa_lluvia:
    scene bg inacap_lluvia
    show pablo at right
    "La lluvia sigue durante los diálogos."
    return

testsuite consecuencias:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase pablo_puerta:
        parameter opcion = [0,1]
        advance until screen "main_menu"
        run Start("qa_cabina")
        advance until screen "choice"
        $ texto = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][opcion]
        run Function(qa_elegir, texto)
        pause 0.2
        advance until screen "choice"
        assert eval pista_pablo == (opcion == 0)
        assert eval len(decisiones_clave) > 0

    testcase testigo_y_promesa:
        parameter romper = [False,True]
        advance until screen "main_menu"
        $ persistent.finales.discard(1)
        run Start("qa_testigo")
        advance until screen "choice"
        if eval romper:
            run Function(qa_elegir, "Revelar que Rubén es tu fuente, aunque prometiste callarlo.")
        else:
            run Function(qa_elegir, "Hablar con José desde el corazón.")
        pause 0.2
        advance until screen "main_menu"
        assert eval (1 in persistent.finales) == (not romper)

    testcase sueno_moto:
        parameter ruta = [0,1]
        advance until screen "main_menu"
        run Start("sueno_pablo")
        advance until screen "choice"
        $ texto = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][ruta]
        run Function(qa_elegir, texto)
        pause 0.2
        advance until screen "choice"
        run Function(qa_elegir, "Decirle que puede empezar ahorrando para la moto, sin volver a apostar.")
        pause 0.2
        advance until screen "choice"
        assert eval plan_sueno in ("ceviches","repuestos")
        assert eval v_sueno

    testcase lluvia_visual:
        advance until screen "main_menu"
        run Start("qa_lluvia")
        pause 1.0
        screenshot "lluvia-animada.png"
        assert eval renpy.get_screen("ambiente_radal") is not None
        advance until screen "main_menu"
