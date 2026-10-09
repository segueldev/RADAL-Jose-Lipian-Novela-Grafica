testsuite labranza:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase final_siete:
        parameter opcion = [0,1]
        parameter gesto = [0,1]
        advance until screen "main_menu"
        $ persistent.finales.discard(7)
        run Start("whatif_labranza")
        advance until screen "choice"
        $ qa_texto = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][opcion]
        run Function(qa_elegir, qa_texto)
        pause 0.2
        advance until screen "choice"
        screenshot f"lucho-cameo-{opcion}-{gesto}.png"
        $ qa_texto = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][gesto]
        run Function(qa_elegir, qa_texto)
        pause 0.2
        advance until screen "main_menu"
        assert eval 7 in persistent.finales

    testcase retrato_pablo:
        advance until screen "main_menu"
        run Start("qa_pablo_retrato")
        pause 0.5
        screenshot "pablo-plano-medio.png"
        advance until screen "main_menu"

label qa_pablo_retrato:
    scene bg patio
    show pablo at right
    pablo "¿Qué mirai?"
    return
