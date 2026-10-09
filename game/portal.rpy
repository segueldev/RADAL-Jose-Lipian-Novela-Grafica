default apoyo_turno_diego = ""
default juguetes_portal = []
default aciertos_portal = 0
image bg jumbo_juguetes = cover("images/eventos/jumbo_juguetes.jpeg")
image diego juguete = sprite("images/eventos/diego_juguete.png")

label portal_turno:
    "El Portal Temuco es otro mundo después de clases: gente saliendo con bolsas, niños tironeando a los papás y Diego tratando de dejar ordenada la sección Hasbro."
    diego "Ojo con ese pasillo, wn. Lo ordené recién y ya me dejaron una caja abierta."
    mc "Pensé que acá ibai a estar probando juguetes."
    diego "Sí, po. Y en el Jumbo Pablo prueba los sacos de arroz. Estoy trabajando, nuevo."
    "Un niño apunta al Optimus Prime. El papá mira el precio y le dice que primero van a ver los yogures. Diego devuelve otra caja a su lugar."
    mc "¿Y el TikTok?"
    diego "Después del turno. Del INACAP pa acá, de acá pa la casa. El live lo hago cuando puedo."
    diego "La PC no se paga con corazones, wn. Ojalá."
    menu:
        "Ayudar a Diego a reponer los juguetes y conversar en su descanso.":
            $ apoyo_turno_diego = "esperar"
            $ rel_delta("Diego", 2)
            call reponer_juguetes
            "Cuando terminan, Diego se toma un descanso. Ya no está mirando por encima de tu hombro."
            diego "Ya, ahora sí. Gracias por la mano, perro. ¿Qué necesitabai?"
            $ consecuencia("Ayudaste a Diego a reponer: te contará lo que vio sin tener que insistir.")
            if venta:
                diego "Antes que me preguntís por José: vi una compra rara. Veinte kilos de zanahorias. Short corto y gafas de sol."
                mc "Ya sé por dónde va esto."
                $ pista_diego = True
        "Sacar el celular: un live de Diego trabajando sería buena talla.":
            $ apoyo_turno_diego = "grabar"
            $ rel_delta("Diego", -1)
            diego "Baja la cámara, wn. El live lo hago yo cuando salga, no en medio del turno."
            "Apagas la cámara. Diego espera a que guardes el celular antes de seguir hablando."
            $ consecuencia("Intentaste grabar a Diego en la pega. Te frenó y no te adelantó ninguna pista.")
    return

label portal_recuerdo:
    if apoyo_turno_diego:
        hide pablo
        show diego at right with dissolve
        if apoyo_turno_diego == "esperar":
            diego "El nuevo me ayudó a reponer en el Portal sin meterme en un live. Ahora escúchenlo ustedes un rato."
        else:
            diego "Y esta conversa no la vai a grabar como en mi pega, ¿cierto?"
            mc "No. Esta vez te pregunté primero."
        hide diego
        show pablo at right with dissolve
    return


screen mision_jumbo():
    zorder 30
    frame:
        xpos 1410
        ypos 25
        xsize 460
        padding (20, 14)
        background Solid("#173323eb")
        vbox:
            spacing 5
            text "TURNO EN EL PORTAL" size 20 color "#e6bb6a"
            text "Reponer juguetes: [len(juguetes_portal)] / 3" size 24 color "#fff0d0"
            text "Robot · autos · juego de mesa" size 17 color "#c7d5c8"

label reponer_juguetes:
    $ juguetes_portal = []
    $ aciertos_portal = 0
    scene bg jumbo_juguetes with dissolve
    show diego juguete at center with dissolve
    show screen mision_jumbo
    diego "Son tres cajas nomás. Cada cosa en su estante. No me dejís un auto entre los juegos de mesa, wn."
    "Diego sostiene un robot en su caja. Te lo pasa y señala los letreros del pasillo."
    menu:
        "Poner el robot junto a las figuras de acción.":
            $ aciertos_portal += 1
            diego "Ese mismo. Que la caja quede mirando pa adelante."
        "Poner el robot donde están las muñecas.":
            diego "No, perro. Tiene ruedas, pero no es coche de guagua. Figuras de acción, acá."
            "Sigues el letrero y corriges el estante."
    $ juguetes_portal.append("robot")
    "La siguiente caja trae un set de autos. Hay un espacio libre junto a las pistas."
    menu:
        "Dejar los autos junto a las pistas de carreras.":
            $ aciertos_portal += 1
            diego "Sí, po. Hasta Fabián los dejaría ahí. Y eso que buscaría los autos del Rocket League."
        "Usar el espacio libre de los peluches.":
            diego "Así mismo me desordenan el pasillo, wn. Acá con las pistas."
            "Mueves la caja al estante que corresponde."
    $ juguetes_portal.append("autos")
    "Queda un juego de mesa. La caja pesa bastante más de lo que parece."
    menu:
        "Ponerlo en el estante de juegos de mesa.":
            $ aciertos_portal += 1
            diego "Ahí. Ahora sí puedo ver el piso."
        "Dejarlo encima de los autos: total, ya terminamos.":
            diego "Terminar no es esconder la última caja, nuevo. Ven, queda justo acá."
            "Acomodan el juego en su estante."
    $ juguetes_portal.append("mesa")
    if aciertos_portal == 3:
        $ rel_delta("Diego", 1)
        diego "Tres de tres. Te vai a ir del INACAP con experiencia en Hasbro, wn."
    else:
        diego "Ya, quedó listo. Igual reviso antes de irme, por si inventaste otra sección."
    hide screen mision_jumbo
    $ recuerda("El caso", "Ayudaste a Diego a reponer tres juguetes en el Portal Temuco.")
    scene bg jumbo_pasillo with dissolve
    show diego at center with dissolve
    return
