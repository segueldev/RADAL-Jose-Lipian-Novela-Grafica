# Comienzos sin reemplazo: ocho escenarios antes de repetir uno.
default persistent.inicios_pendientes = []
default persistent.ultimo_inicio = 0
default recuerdo_cumple = ""
default favor_inicio = ""
default presentacion_corta = False
default v_incidente = False
default incidente = 0
default resultado_incidente = ""

init python:
    def siguiente_inicio():
        pendientes = [i for i in (persistent.inicios_pendientes or []) if i in range(1, 9)]
        if not pendientes:
            antiguos = [1, 2, 3, 4, 5]
            nuevos = [6, 7, 8]
            renpy.random.shuffle(antiguos)
            renpy.random.shuffle(nuevos)
            # Primero una situación nueva, incluso para quien jugó la beta.
            pendientes = nuevos + antiguos
            if pendientes[0] == persistent.ultimo_inicio:
                pendientes[0], pendientes[1] = pendientes[1], pendientes[0]
        inicio = pendientes.pop(0)
        persistent.inicios_pendientes = pendientes
        persistent.ultimo_inicio = inicio
        renpy.save_persistent()
        return inicio

label inicio_cisterna:
    $ clima = "frio"
    $ bg_prologo = "bg inacap"
    scene bg shell with fade
    show pablo shell at right with dissolve
    "Primer día. Paraste en la Shell de Lautaro antes de seguir al INACAP. Un camión tiene ocupada media salida."
    pablo "Oye, ¿me corrís ese cono? Ese de ahí."
    mc "¿Este?"
    pablo "No, el otro. El que estoy apuntando, po."
    "Hay dos conos. Pablo apunta justo al medio."
    menu:
        "Mover los dos y que se decida.":
            $ favor_inicio = "cono"
            $ rel_delta("Pablo", 1)
            pablo "Ya, gracias. ¿Vai pa Temuco?"
            mc "Al INACAP. Primer día."
            pablo "Yo también estudio ahí. Si me veís, saluda."
        "Grabar sus instrucciones para no equivocarse.":
            $ favor_inicio = "video"
            $ broma_benjamin += 1
            $ rel_delta("Pablo", -1)
            mc "A ver, repite lo del cono pa la cámara."
            pablo "Guarda esa wea. No estoy dando una entrevista."
            "Lo guardas. Él mueve los dos conos."
    scene bg inacap with fade
    show pablo at right with dissolve
    "Llegas al instituto. Pablo aparece un rato después, ahora con short y gafas."
    pablo "¿Qué mirai? Vine a clases, no al turno."
    show benjamin at left with dissolve
    benjamin "¿Ya conociste al Pablo? ¿Te pidió plata?"
    pablo "Me ayudó con los conos, nada más."
    if favor_inicio == "video":
        mc "Todavía estoy aprendiendo cuál era el cono."
        benjamin "Ya me cayó bien el nuevo."
    jump intro_grupo

label inicio_sala:
    $ clima = "nublado"
    $ bg_prologo = "bg patio"
    scene bg inacap_dentro with fade
    show diego at center with dissolve
    "Primer día. Sigues a un cabro que parece saber adónde va. Lleva diez minutos mirando los números de las salas."
    diego "¿Buscai telecom?"
    mc "Sí. ¿Tú sabís dónde es?"
    diego "Obvio. Sígueme."
    "Dan la vuelta al pasillo y quedan frente a la misma puerta."
    mc "Pasamos por acá recién."
    diego "Estaba viendo si estabai atento."
    "Diego saca el celular. En vez del horario, abre TikTok."
    diego "Ya que estamos, sostenme esto. Un live cortito."
    menu:
        "Hacerle de camarógrafo mientras buscan la sala.":
            $ favor_inicio = "camara"
            $ rel_delta("Diego", 1)
            diego "¡Cabezones! Primer día. Aquí con el nuevo."
            mc "Pregúntales dónde queda la sala, mejor."
            diego "No me dejís así en vivo, po."
        "Mostrarle el horario: ya van atrasados.":
            $ favor_inicio = "horario"
            $ apoyo += 1
            diego "Ah. Era en el otro piso."
            mc "¿Y pa qué me hiciste dar la vuelta?"
            diego "Pa conocer el instituto. Tour gratis."
    scene bg patio with fade
    show marcelo at left with dissolve
    show diego at right with dissolve
    marcelo "¿Lo perdiste al nuevo?"
    diego "Lo orienté."
    marcelo "Llegaron juntos tarde."
    jump intro_grupo

label inicio_termo:
    $ clima = "lluvia"
    $ bg_prologo = "bg inacap_lluvia"
    scene bg inacap_dentro with fade
    show marcelo at left with dissolve
    show ruben at right with dissolve
    "Primer día. Buscas una mesa. Un cabro tiene ocupado el único asiento seco con una mochila."
    mc "¿Hay alguien ahí?"
    ruben "La mochila."
    "Marcelo la corre. Rubén ni se endereza."
    marcelo "Siéntate. ¿Querís café?"
    mc "¿Es tuyo?"
    marcelo "Sí, pero no me gusta. Compré porque no había té."
    ruben "Entonces pa qué compraste."
    marcelo "¿Me vai a ayudar o vai a seguir acostado?"
    menu:
        "Ofrecerle una bolsita de té que llevas en la mochila.":
            $ favor_inicio = "te"
            $ rel_delta("Marcelo", 1)
            marcelo "No, en serio. ¿Tenís?"
            "Vierte agua del termo de Rubén. Rubén se sienta altiro."
            ruben "Ya, pero deja algo."
            marcelo "Ah, pa eso sí te movís."
        "Aceptar el café y pedirle a Rubén que corra la mochila.":
            $ favor_inicio = "mochila"
            $ rel_delta("Rubén", -1)
            ruben "Si ya la corrió Marcelo."
            mc "Pa que no la vuelvas a poner."
            "Rubén se la pone en las piernas. Te mira como si le hubieras cobrado."
    show benjamin at center with dissolve
    benjamin "¿Ya te cobraron por sentarte? Rubén, deja de espantar gente."
    ruben "¿Y a ti qué te importa?"
    jump intro_grupo

label grupo_al_grano:
    scene bg patio with fade
    show benjamin at left with dissolve
    show jose at center with dissolve
    show pablo at right with dissolve
    benjamin "Ya, presentación cortita. José, Pablo, Diego y Bastián: telecom. Marcelo, Rubén y yo: ciberseguridad. Fabián también, por ahora."
    jose "¿Por qué me mirai a mí cuando decís cortita?"
    benjamin "Porque te iba a preguntar por Shakira."
    mc "¿Shakira?"
    jose "Mi yegua. Está en Lincoñir, en Padre Las Casas. Cuando querai la conocís."
    pablo "Le celebra hasta el cumpleaños."
    jose "Sí, ¿y?"
    menu:
        "Ya, yo llevo las zanahorias.":
            $ apoyo += 1
            $ recuerda("José")
            jose "Eso, po. Benjamín lleva puras tallas malas."
        "¿Tiene más cumpleaños que asados el grupo?":
            $ broma_benjamin += 1
            $ recuerda("Benjamín")
            benjamin "Ni lo digai. A mí todavía no me invitan al mío."
    jose "Igual yo creo que vale un palo. Por si alguien pregunta."
    mc "Pero nadie preguntó."
    benjamin "Así está hace rato. Después dice que uno lo webea por nada."
    "Los cabros se conocen desde el Politécnico. Tú recién llegas. Para el resto de las historias habrá tiempo en las visitas."
    jump hub

label shell_pistas:
    $ ultima_visita = "Shell · Lautaro"
    if pablo_arruinado:
        scene bg shell_ruinas with fade
    else:
        scene bg shell with fade
    show pablo shell at right with dissolve
    mc "Me dijiste que volviera. Vine por la cabina."
    pablo "Yo no dije eso. Lo pensaste tú."
    call permiso_cabina
    if not _return:
        jump hub
    "Sobre el asiento hay una montura bajo una manta. Asoma medio estribo."
    mc "¿Esto también venía con el camión?"
    pablo "No toquí, que se ensucia."
    mc "¿La montura o el camión?"
    pablo "Sí."
    $ pista_pablo = True
    $ recuerda("El caso", "Encontraste una montura en la cabina.")
    jump hub

label jumbo_pistas:
    $ ultima_visita = "Jumbo · Portal Temuco"
    scene bg jumbo_pasillo with fade
    show diego at center with dissolve
    mc "La otra vez no había nada raro. ¿Ahora?"
    diego "Ahora sí. Un loco compró veinte kilos de zanahorias. Short, gafas."
    mc "¿Pablo?"
    diego "Yo no dije Pablo. Pero me dijo cabezón al pagar."
    $ pista_diego = True
    $ recuerda("El caso", "Diego vio una compra de zanahorias sospechosa.")
    jump hub

label incidente_del_dia:
    $ v_incidente = True
    $ incidente = renpy.random.randint(1, 3)
    scene bg patio with fade
    if incidente == 1:
        show marcelo at left with dissolve
        show benjamin at right with dissolve
        "Marcelo te pasa el celular. Benjamín intenta quitárselo."
        marcelo "Dime si esto se puede subir a premierchilito."
        "Es un video de un penal. Cada vez que el jugador patea, Benjamín puso el relincho de una yegua."
        benjamin "Tiene edición. No es llegar y poner el relincho. Hay que sincronizarlo."
        menu:
            "Dejar el video guardado como sticker del grupo.":
                $ resultado_incidente = "sticker"
                $ rel_delta("Marcelo", 1)
                marcelo "Eso. Al grupo, no a la página."
                benjamin "El público se lo pierde. Ustedes se lo pierden."
            "Agregar un segundo relincho cuando cae el arquero.":
                $ resultado_incidente = "relincho"
                $ broma_benjamin += 1
                $ rel_delta("Benjamín", 1)
                benjamin "Ese era el detalle que le faltaba."
                marcelo "Dame el celular. No les presto más."
    elif incidente == 2:
        show diego at left with dissolve
        show bastian at right, bastian_bajo with dissolve
        "Diego tiene un computador abierto. Bastián sostiene el cargador en el aire."
        diego "Así carga. Si lo baja, se apaga."
        bastian "..."
        menu:
            "Buscar cinta y afirmarlo sin usar a Bastián de soporte.":
                $ resultado_incidente = "cinta"
                $ apoyo += 1
                $ rel_delta("Bastián", 1)
                "Lo afirmas al borde de la mesa. Bastián suelta el brazo y se lo soba."
                diego "Ya, esa solución está buena. No la mostrís en el live, eso sí."
            "Pedirle a Diego que tome el cargador mientras Bastián descansa.":
                $ resultado_incidente = "brazo"
                $ rel_delta("Bastián", 1)
                diego "¿Y cómo juego con una mano?"
                mc "Como lleva media hora el Bastián, po."
                bastian "Sí."
                "Diego toma el cargador. A los dos minutos pregunta por la cinta."
    else:
        show fabian at left with dissolve
        show ruben at right with dissolve
        "Fabián llega con un completo. Rubén levanta la cabeza desde la banca."
        ruben "¿Te vai a comer la otra mitad?"
        fabian "Ni lo abro todavía, wn."
        menu:
            "Decirle a Rubén que vaya a comprar el suyo.":
                $ resultado_incidente = "completo"
                $ rel_delta("Fabián", 1)
                ruben "Está lejos."
                fabian "Está detrás tuyo, perro."
                "Rubén mira el puesto. Vuelve a mirar el completo. No se para."
            "Proponer que Rubén compre la bebida y Fabián comparta.":
                $ resultado_incidente = "bebida"
                $ apoyo += 1
                $ rel_delta("Rubén", 1)
                ruben "¿Y cuánto me toca?"
                fabian "La mitad, wn. Compra la bebida primero."
                "Rubén se levanta contando las monedas. Fabián se pone a comer antes de que vuelva."
    return
