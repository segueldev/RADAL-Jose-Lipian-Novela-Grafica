testsuite cupido:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase desbloquea_nielol:
        parameter mensaje = ["Escríbele algo normal. Salúdala como persona.", "Escríbele un poema. A lo Shakespeare de Lincoñir.", "Invítala a algo. Directo. Sin miedo."]
        advance until screen "main_menu"
        run Start("whatif_tinder")
        advance until screen "choice" timeout 15
        assert eval not preparado_barbarita and not opciones_mapa("Villarrica")
        run Function(qa_elegir,mensaje)
        pause 0.2
        advance until eval qa_hub() timeout 15
        assert eval v_tinder and opciones_mapa("Cerro Ñielol") and not opciones_mapa("Villarrica")
