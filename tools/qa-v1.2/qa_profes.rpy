init 1000 python:
    config.savedir = "/tmp/radal-revision-completa-20261009"

testsuite profesores:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase visita_liceo:
        parameter recuerdo = [0, 1, 2]
        parameter conversacion = [0, 1, 2]
        advance until screen "main_menu"
        run Start("liceo")
        advance until screen "choice" timeout 20
        $ qa_eleccion = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][recuerdo]
        run Function(qa_elegir, qa_eleccion)
        pause until not screen "choice" timeout 5
        advance until screen "choice" timeout 20
        assert "Preguntarle al profe cómo ordenar las versiones del grupo."
        screenshot "profes-conversacion.png"
        $ qa_eleccion = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][conversacion]
        run Function(qa_elegir, qa_eleccion)
        pause until not screen "choice" timeout 5
        advance until screen "choice" timeout 20
        assert eval qa_hub()
        assert eval verdad_martin and v_liceo
        assert eval consejo_martin == (conversacion == 0)
        assert eval grabacion_hector == ["", "permiso", "talla"][conversacion]
        assert eval len(decisiones_clave) > 0
        run Jump("cuaderno")
        pause 0.1
        advance until screen "choice" timeout 20
        assert eval qa_hub()

    testcase balance_profes:
        parameter consejo = [False, True]
        parameter registro = ["", "permiso", "talla"]
        advance until screen "main_menu"
        run Start("qa_balance_profes")
        $ consejo_martin = consejo
        $ grabacion_hector = registro
        advance until screen "main_menu" timeout 20

    testcase planos_recuerdo:
        advance until screen "main_menu"
        run Start("liceo")
        advance until screen "choice" timeout 20
        screenshot "profes-primer-menu.png"
        run Function(qa_elegir, "Según lo que cuentan, yo le habría creído.")
        pause until not screen "choice" timeout 5
        advance until "Este video va para mi canal. SJO. Suzuki Jeep Oficial. Y ese Jeep de afuera es mío." timeout 20
        screenshot "profes-tres-retratos.png"
        advance until "El Jeep. Suzuki. Cuatro por cuatro. Estacionado como si fuera dueño del liceo." timeout 20
        screenshot "profes-jeep.png"
        advance until screen "choice" timeout 20
        screenshot "profes-conversacion.png"

label qa_balance_profes:
    scene bg liceo
    "Revisamos lo que quedó de la visita."
    call balance_profes
    return
