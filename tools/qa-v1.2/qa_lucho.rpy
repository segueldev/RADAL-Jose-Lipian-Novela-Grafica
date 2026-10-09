testsuite dlc:
    before testcase:
        $ renpy.test.testmouse.reset()

    after testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
            pause until screen "main_menu"

    testcase lucho_completo:
        parameter respuesta = ["Tomárselo con humor.", "Darse un rato antes de seguir."]
        parameter turno = ["Concentrarse en observar.", "Concentrarse en tratar bien a la gente."]
        advance until screen "main_menu"
        run renpy.get_widget("main_menu", "menu_lucho", base=True).action
        pause 0.2
        advance until "Un recuerdo de segundo medio, cuando Luis compartía curso con los cabros. El protagonista de la historia principal aún no los conocía." timeout 15
        screenshot "lucho-uniforme-liceo.png"
        assert eval renpy.showing("lucho liceo")
        advance until screen "choice" timeout 15
        run Function(qa_elegir, respuesta)
        pause 0.2
        advance until "Desde la casa no significa que las tareas se hagan solas. Ya lo comprobé. Varias veces." timeout 15
        screenshot "lucho-fuera-del-liceo.png"
        assert eval renpy.showing("lucho joven") and not renpy.showing("lucho liceo")
        advance until screen "choice" timeout 15
        run Function(qa_elegir, turno)
        pause 0.2
        advance until "LUCHO — fin de la precuela." timeout 15
        assert eval lucho_activo
        assert eval fragmentos == 0 and not venta
        advance until screen "main_menu"
        assert eval persistent.lucho_completado
    
    
    testcase lucho_guardado:
        advance until screen "main_menu"
        run renpy.get_widget("main_menu", "menu_lucho", base=True).action
        pause 0.2
        advance until screen "choice" timeout 15
        $ renpy.save("qa-lucho")
        run Function(qa_elegir, "Tomárselo con humor.")
        pause 0.2
        advance until screen "choice" timeout 15
        run Function(renpy.load, "qa-lucho")
        pause 1.0
        assert eval lucho_activo and lucho_respuesta == ""
        assert eval renpy.showing("bg liceo") and renpy.showing("lucho liceo")
        advance until screen "choice" timeout 15
        run Function(qa_elegir, "Darse un rato antes de seguir.")
        pause 0.2
        advance until screen "choice" timeout 15
        run Function(qa_elegir, "Concentrarse en observar.")
        pause 0.2
        advance until screen "main_menu"
        $ renpy.unlink_save("qa-lucho")
