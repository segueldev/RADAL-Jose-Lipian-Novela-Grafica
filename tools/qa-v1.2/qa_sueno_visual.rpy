testsuite sueno_visual:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase globos_y_revelacion:
        parameter ruta = ["Empezar repartiendo los ceviches del hermano de Fabián.","Usar la moto para llevar encargos y repuestos entre los negocios."]
        advance until screen "main_menu"
        run Start("sueno_pablo")
        advance until "Ya. Primero la moto. Lo dije y lo voy a hacer." timeout 15
        screenshot "pablo-globo-discreto.png"
        assert eval fase_globo_pablo == 1 and renpy.get_screen("say_pablo_imagina") is not None
        advance until screen "choice" timeout 15
        run Function(qa_elegir,ruta)
        pause 0.2
        advance until "¿Vieron? Era comprar la moto nomás." timeout 15
        screenshot "pablo-globo-nube.png"
        assert eval fase_globo_pablo == 2
        advance until "Van a poner mi cara en la plaza. Pero con las gafas, eso sí." timeout 15
        screenshot "pablo-globo-exagerado.png"
        assert eval fase_globo_pablo == 3 and sueno_pablo_activo
        advance until "Estaba soñando que me compraba la moto." timeout 15
        screenshot "pablo-despertar.png"
        assert eval fase_globo_pablo == 0 and not sueno_pablo_activo and renpy.get_screen("say_pablo_imagina") is None
        advance until screen "choice" timeout 15
        run Function(qa_elegir,"Decirle que puede empezar ahorrando para la moto, sin volver a apostar.")
        pause 0.2
        advance until eval qa_hub() timeout 15
