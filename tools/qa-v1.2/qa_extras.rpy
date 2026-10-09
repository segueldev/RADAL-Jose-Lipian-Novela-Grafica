label qa_incidente:
    call incidente_del_dia
    jump hub

label qa_plano_short:
    scene bg inacap_lluvia
    show escena short at center
    "¿Eso es un short?"
    return

label qa_planos_jose:
    scene escena venta_camioneta
    "Plano de José saliendo."
    scene escena atardecer_cerca
    "José y Shakira en el potrero."
    scene escena cisterna_pablo
    "La cisterna en la Shell."
    return

testsuite extras:
    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase charlas:
        parameter charla = ["charla_fabian", "charla_bastian", "charla_ruben", "qa_incidente"]
        parameter opcion = [0,1]
        advance until screen "main_menu"
        run Start(charla)
        advance until screen "choice"
        $ qa_texto = [i.caption for i in renpy.get_screen("choice").scope["items"] if i.action is not None][opcion]
        run Function(qa_elegir, qa_texto)
        pause 0.2
        advance until screen "choice"
        assert eval qa_hub()
        if eval charla == "charla_fabian":
            assert eval chocolate_fabian
        elif eval charla == "charla_bastian":
            assert eval origen_bastian
        elif eval charla == "charla_ruben":
            assert eval historia_cuy
        else:
            assert eval v_incidente and resultado_incidente

    testcase visual:
        advance until screen "main_menu"
        screenshot "menu-1.2.png"
        run Start("qa_plano_short")
        pause 0.5
        screenshot "short-corregido.png"
        advance until screen "main_menu"
        run Start("qa_planos_jose")
        pause 0.5
        screenshot "jose-espaldas.png"
        advance until "José y Shakira en el potrero."
        screenshot "jose-shakira.png"
        advance until "La cisterna en la Shell."
        screenshot "cisterna.png"
        advance until screen "main_menu"

    testcase guardar_inicio:
        advance until screen "main_menu"
        run Start("inicio_termo")
        advance until screen "choice"
        $ renpy.save("qa-inicio")
        run Function(qa_elegir, "Ofrecerle una bolsita de té que llevas en la mochila.")
        pause 0.2
        advance until screen "choice"
        run Function(renpy.load, "qa-inicio")
        pause 0.5
        advance until screen "choice"
        assert eval favor_inicio == ""
        assert eval renpy.showing("bg inacap_dentro")
        $ renpy.unlink_save("qa-inicio")

label qa_fondos:
    scene bg funeral
    "Plano de homenaje."
    scene bg atardecer
    "Atardecer en Lincoñir."
    scene bg pesebre
    "Plano del pesebre."
    scene escena asado
    "Escenario de la historia del asado."
    return

testcase fondos_reales:
    advance until screen "main_menu"
    run Start("qa_fondos")
    pause 0.5
    screenshot "funeral-foto.png"
    advance until "Atardecer en Lincoñir."
    screenshot "atardecer-foto.png"
    advance until "Plano del pesebre."
    screenshot "pesebre-foto.png"
    advance until "Escenario de la historia del asado."
    screenshot "asado-foto.png"
    advance until screen "main_menu"
