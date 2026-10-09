label qa_reponer_errores:
    call reponer_juguetes
    "La misión terminó y los tres juguetes quedaron en sus estantes."
    return

testsuite portal:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase turno_y_pista:
        parameter vendido = [False, True]
        parameter opcion = [0, 1]
        advance until screen "main_menu"
        run Start("jumbo")
        $ venta = vendido
        advance until screen "choice"
        screenshot "portal-turno.png"
        $ elegida = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][opcion]
        run Function(qa_elegir, elegida)
        pause 0.2
        if eval opcion == 0:
            advance until screen "choice"
            screenshot "portal-mision-juguetes.png"
            assert eval renpy.showing("diego juguete") and renpy.get_screen("mision_jumbo") is not None
            run Function(qa_elegir, "Poner el robot junto a las figuras de acción.")
            pause 0.2
            advance until screen "choice"
            run Function(qa_elegir, "Dejar los autos junto a las pistas de carreras.")
            pause 0.2
            advance until screen "choice"
            run Function(qa_elegir, "Ponerlo en el estante de juegos de mesa.")
            pause 0.2
            advance until screen "choice"
            assert eval len(juguetes_portal) == 3 and aciertos_portal == 3
            assert eval renpy.get_screen("mision_jumbo") is None
        else:
            advance until screen "choice"
        assert eval apoyo_turno_diego == ("esperar" if opcion == 0 else "grabar")
        assert eval pista_diego == (vendido and opcion == 0)
        run Function(qa_elegir, "Diego, ¿qué sabes de José y Shakira?")
        pause 0.2
        advance until screen "choice"
        assert eval qa_hub() and v_jumbo

    testcase errores_corregibles:
        advance until screen "main_menu"
        run Start("qa_reponer_errores")
        advance until screen "choice"
        run Function(qa_elegir, "Poner el robot donde están las muñecas.")
        pause 0.2
        advance until screen "choice"
        run Function(qa_elegir, "Usar el espacio libre de los peluches.")
        pause 0.2
        advance until screen "choice"
        run Function(qa_elegir, "Dejarlo encima de los autos: total, ya terminamos.")
        pause 0.2
        advance until "La misión terminó y los tres juguetes quedaron en sus estantes."
        assert eval len(juguetes_portal) == 3 and aciertos_portal == 0
        assert eval renpy.get_screen("mision_jumbo") is None
