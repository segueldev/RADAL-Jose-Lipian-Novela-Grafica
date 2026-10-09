label qa_reparto_verdadero:
    $ historia_escuchada = True
    $ verdad_martin = True
    $ pista_ruben = True
    $ pista_pablo = True
    show benjamin at right
    jump final_verdadero

label qa_reparto_gamer:
    $ verdad_martin = True
    jump final_gamer

label qa_mapa_inicial:
    scene bg inacap_dentro
    jump mapa_viajes

label qa_mapa_venta:
    $ venta = True
    $ v_incidente = True
    $ v_fabian_sale = True
    $ v_pelea_inacapini = True
    $ v_ruben = True
    $ v_conflicto_ruben = True
    scene bg inacap_dentro
    jump mapa_viajes

label qa_avisos_exclusivos:
    scene bg inacap
    $ whatif("Una ruta nueva")
    $ recuerda("Pablo")
    "Un solo aviso a la vez."
    return

testsuite reparto_mapa:
    before testcase:
        $ renpy.test.testmouse.reset()

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase verdadero_sin_superponer:
        advance until screen "main_menu"
        run Start("qa_reparto_verdadero")
        advance until "Ni el Shen Shen en 'China' vio un desenlace así."
        assert eval renpy.showing("bastian") and not renpy.showing("benjamin")
        screenshot "final-bastian-separado.png"
        advance until "Dejemos que termine, po. Después reclama que no lo escuchamos."
        assert eval not renpy.showing("shakira")
        advance until "Chao, chiquillos."
        assert eval renpy.showing("ruben") and not renpy.showing("jose")
        screenshot "final-ruben-separado.png"

    testcase funeral_sin_superponer:
        advance until screen "main_menu"
        run Start("final_funeral")
        advance until "Perdóname, Shakira."
        assert eval not renpy.showing("marcelo") and renpy.showing("jose")
        screenshot "funeral-reparto.png"

    testcase fundo_sin_superponer:
        advance until screen "main_menu"
        run Start("final_fundo")
        advance until "Yo solo vine a reírme y a comer, wn. Y ya me reí."
        assert eval not renpy.showing("benjamin") and renpy.showing("ivan")

    testcase gamer_sin_superponer:
        advance until screen "main_menu"
        run Start("qa_reparto_gamer")
        advance until "¿¡Habló Bastián!? ¡Pachoclo, hablaste!"
        assert eval not renpy.showing("pablo") and renpy.showing("benjamin")

    testcase avisos_exclusivos:
        advance until screen "main_menu"
        run Start("qa_avisos_exclusivos")
        pause 0.3
        assert eval renpy.get_screen("aviso_recuerda") is not None and renpy.get_screen("aviso_whatif") is None

    testcase mapa_primera_visita:
        advance until screen "main_menu"
        run Start("qa_mapa_inicial")
        pause until screen "mapa_recorridos"
        assert eval not opciones_mapa("Labranza")
        screenshot "mapa-inicial.png"
        click id "mapa_3" pos (0.5,0.5) until eval renpy.get_screen("mapa_recorridos").scope["seleccionado"] == "Shell · Lautaro" timeout 15
        pause 0.3
        click "Visitar a Pablo y Fabián" until not screen "mapa_recorridos" timeout 15
        advance until screen "choice"
        assert eval ultima_visita == "Shell · Lautaro" and v_shell

    testcase mapa_ruta_labranza:
        advance until screen "main_menu"
        run Start("qa_mapa_venta")
        pause until screen "mapa_recorridos"
        click id "mapa_5" pos (0.5,0.5) until eval renpy.get_screen("mapa_recorridos").scope["seleccionado"] == "Labranza" timeout 15
        pause 0.3
        screenshot "mapa-labranza.png"
        click "¿Y si…? Seguir el dato de Lucho" until not screen "mapa_recorridos" timeout 15
        advance until screen "choice"
        assert eval v_lucho_labranza and ruta_lucho_activa and ultima_visita == "Labranza"
