default qa_audio_clima = "general"
default qa_audio_guardada = ""

label qa_audio_escena:
    scene bg inacap_dentro
    show fabian at right
    $ musica(qa_audio_clima)
    fabian "Esta la hice yo. Déjala sonar un rato, po."
    "Los cabros siguen conversando."
    return

testsuite audio:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase canciones_y_credito:
        parameter ambiente = ["general","viaje","calma","triste","tension","humor"]
        advance until screen "main_menu"
        $ qa_audio_clima = ambiente
        run Start("qa_audio_escena")
        advance until "Esta la hice yo. Déjala sonar un rato, po." timeout 15
        pause 0.7
        assert eval len(catalogo_fabian) == 8 and all(renpy.loadable(d[0]) for d in catalogo_fabian.values())
        assert eval categoria_musica_radal == ambiente and ficha_tema_fabian(pista_musica_radal)
        assert eval renpy.music.get_playing(channel=canal_musica_radal) == pista_musica_radal
        assert eval renpy.get_screen("musica_actual_radal").scope["titulo"] == titulo_musica_radal
        screenshot ("musica-%s.png" % ambiente)
        $ anterior = pista_musica_radal
        run Function(reproducir_fabian,siguiente_tema_fabian(ambiente))
        pause 0.7
        assert eval pista_musica_radal != anterior and renpy.get_screen("musica_actual_radal").scope["titulo"] == titulo_musica_radal
        screenshot "musica-cambio.png"
        run Function(renpy.music.stop,channel=canal_musica_radal)
        pause 0.2
        run Function(intercalar_fabian)
        pause 0.3
        assert eval renpy.music.get_playing(channel=canal_musica_radal) is not None

    testcase bolsas_y_efectos:
        advance until screen "main_menu"
        python:
            for categoria, ids in listas_fabian.items():
                store.bolsas_musica_radal = {}
                store.pista_musica_radal = ""
                elegidos = []
                for i in range(len(ids)*2):
                    nuevo = siguiente_tema_fabian(categoria)
                    assert nuevo != store.pista_musica_radal
                    store.pista_musica_radal = nuevo
                    elegidos.append(nuevo)
                assert set(elegidos[:len(ids)]) == {catalogo_fabian[i][0] for i in ids}
        assert eval all(renpy.loadable("audio/efectos/"+n+".ogg") for n in ("mensaje","motor_cisterna","frenada","explosion","trueno","porton","plato","refrigerador","pasos","teclado","lluvia","bosque"))
        assert eval efecto_radal("plato.ogg") and not efecto_radal("archivo_inexistente.ogg")

    testcase guardar_y_opciones:
        advance until screen "main_menu"
        run Start("qa_audio_escena")
        advance until "Esta la hice yo. Déjala sonar un rato, po." timeout 15
        pause 0.3
        $ persistent.qa_audio_guardada = pista_musica_radal
        run FileSave("qa-audio",confirm=False)
        pause 0.4
        run Function(reproducir_fabian,siguiente_tema_fabian(categoria_musica_radal))
        pause 0.3
        run FileLoad("qa-audio",confirm=False)
        pause 0.8
        $ renpy.log("QA AUDIO CARGADO: " + repr((pista_musica_radal,persistent.qa_audio_guardada,canal_musica_radal,renpy.music.get_playing(channel=canal_musica_radal))))
        assert eval pista_musica_radal == persistent.qa_audio_guardada and renpy.music.get_playing(channel=canal_musica_radal) == persistent.qa_audio_guardada
        run ShowMenu("preferences")
        pause until screen "preferences"
        $ aviso_antes = persistent.aviso_musica_radal
        click "Mostrar canción actual"
        pause 0.3
        assert eval persistent.aviso_musica_radal != aviso_antes
        click "Mostrar canción actual"
        pause 0.3
        assert eval persistent.aviso_musica_radal == aviso_antes
