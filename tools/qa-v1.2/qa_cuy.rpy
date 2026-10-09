label qa_cuy:
    $ historia_cuy = True
    $ v_incidente = True
    jump whatif_cuy

testsuite cuy:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase recuerdo:
        parameter resp = ["Preguntarle si llamó a alguien antes de enterrarlo.", "Dejar la historia ahí. No va a acordarse mejor por insistir."]
        advance until screen "main_menu"
        run Start("charla_ruben")
        advance until "Rubén se acuerda del cuy que tenía de chico." timeout 15
        screenshot "cuy-recuerdo.png"
        assert eval renpy.showing("recuerdo cuy")
        advance until "Así recuerda haberlo encontrado: quieto, sin reaccionar. En ese momento pensó que había muerto." timeout 15
        screenshot "cuy-quieto.png"
        assert eval renpy.showing("recuerdo cuy_quieto")
        advance until screen "choice" timeout 15
        run Function(qa_elegir,resp)
        pause 0.2
        advance until eval qa_hub() timeout 15
        assert eval historia_cuy and any(l == "whatif_cuy" for t,l in opciones_mapa("INACAP"))

    testcase asado:
        parameter come = [False,True]
        advance until screen "main_menu"
        run Start("qa_cuy")
        advance until "La historia da un salto hasta la casa de Fabián. Tiene al cuy guardado en el congelador." timeout 15
        screenshot "cuy-congelador.png"
        assert eval renpy.showing("escena congelador_cuy")
        advance until "Fabián saca del congelador el cuy preparado. Pablo todavía viene en camino y Rubén no sabe nada de la invitación." timeout 15
        screenshot "cuy-preparado.png"
        assert eval renpy.showing("escena cuy_preparado")
        advance until screen "choice" timeout 15
        screenshot "cuy-asado.png"
        assert eval renpy.showing("escena cuy_asado")
        run Function(qa_elegir,"Pablo acepta la invitación sin preguntar." if come else "Pablo pregunta qué carne es antes de probar.")
        pause 0.2
        advance until eval qa_hub() timeout 15
        assert eval v_cuy_asado and not ruta_cuy_activa and pablo_comio_cuy == come and fragmentos == 0
        assert eval not any(l == "whatif_cuy" for t,l in opciones_mapa("INACAP"))
        assert eval any("¿y si…?" in n and "Pablo" in n for n in decisiones_clave)

    testcase guardar:
        advance until screen "main_menu"
        run Start("qa_cuy")
        advance until "La historia da un salto hasta la casa de Fabián. Tiene al cuy guardado en el congelador." timeout 15
        run FileSave("qa-cuy",confirm=False)
        pause 0.3
        advance until screen "choice" timeout 15
        run FileLoad("qa-cuy",confirm=False)
        pause 0.4
        assert eval ruta_cuy_activa and renpy.showing("escena congelador_cuy")
        advance until screen "choice" timeout 15
        run Function(qa_elegir,"Pablo pregunta qué carne es antes de probar.")
        pause 0.2
        advance until eval qa_hub() timeout 15
        assert eval not ruta_cuy_activa
