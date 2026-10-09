label qa_nielol:
    $ v_tinder = True
    $ v_incidente = True
    $ v_fabian_sale = True
    $ v_pelea_inacapini = True
    jump entreno_nielol

testsuite barbarita:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase entrenamiento_y_viaje:
        parameter ritmo = ["Subir a su ritmo y dejar que José practique la conversa.", "Dejar que Benjamín arme su entrenamiento de película."]
        parameter consejo = ["Aclarar la pega: sueldo, horario y dónde se queda.", "Preguntarle si también quiere juntarse fuera de la pega."]
        advance until screen "main_menu"
        run Start("qa_nielol")
        advance until screen "choice" timeout 15
        assert eval not preparado_barbarita and not opciones_mapa("Villarrica")
        run Function(qa_elegir,ritmo)
        pause 0.2
        advance until screen "choice" timeout 15
        run Function(qa_elegir,consejo)
        pause 0.2
        advance until "Ya. Ahora sí estoy listo pa ir. Pero borren el video de Benjamín." timeout 15
        screenshot "jose-arbol-nielol.png"
        assert eval renpy.showing("escena jose_arbol") and not preparado_barbarita
        advance until eval qa_hub() timeout 15
        assert eval v_nielol and preparado_barbarita and opciones_mapa("Villarrica") and not opciones_mapa("Cerro Ñielol")
        run Function(qa_elegir,"¿Y si…?: José se va a trabajar a Villarrica")
        pause 0.2
        advance until screen "choice" timeout 15
        assert eval v_villarrica and ruta_barbarita_activa
        run Function(qa_elegir,"Preguntarle cómo le fue en el primer turno.")
        pause 0.2
        advance until eval qa_hub() timeout 15
        assert eval not ruta_barbarita_activa and not opciones_mapa("Villarrica") and fragmentos == 0

    testcase mapa_y_gafas:
        advance until screen "main_menu"
        run Start("qa_nielol")
        advance until screen "choice" timeout 15
        run Show("mapa_recorridos")
        pause 0.4
        screenshot "mapa-nielol-villarrica.png"
        assert eval len(destinos_mapa()) == 8 and opciones_mapa("Cerro Ñielol")
        run Hide("mapa_recorridos")
        run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start("prologo_frio")
        advance until screen "choice" timeout 15
        run Function(qa_elegir,"Ya, pero recién llegamos, Marcelo.")
        pause 0.2
        advance until screen "choice" timeout 15
        screenshot "pablo-con-gafas.png"
        assert eval renpy.showing("pablo")
