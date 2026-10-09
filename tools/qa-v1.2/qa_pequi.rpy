label qa_pequi_presentacion:
    scene bg shell
    call pequi_presentacion
    return

label qa_pequi_inundacion:
    scene bg inundado
    call pequi_inundacion
    return

testsuite pequi:
    testcase apariciones:
        parameter escena = ["pequi_presentacion", "pequi_inundacion"]
        advance until screen "main_menu"
        run Start("qa_" + escena)
        pause 0.5
        assert eval renpy.showing("pequi")
        screenshot ("%s.png" % escena)
        advance until screen "main_menu"
        assert eval not renpy.showing("pequi")
