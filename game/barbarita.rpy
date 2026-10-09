# Continuación opcional de la historia que el grupo imagina para José.
default v_nielol = False
default preparado_barbarita = False
default v_villarrica = False
default ruta_barbarita_activa = False
default plan_entreno = ""
default consejo_barbarita = ""

init 20:
    image bg entrada_seca = cover("images/eventos/entrada_seca.webp")
    image bg escaleras = cover("images/eventos/escaleras.jpg")
    image bg patio_seco = cover("images/eventos/patio_seco.jpg")
    image bg puente_lejos = cover("images/eventos/puente_lejos.jpeg")
    image bg puente_cerca = cover("images/eventos/puente_cerca.jpeg")
    image bg casa_jose = cover("images/eventos/casa_jose.png")
    image bg entrada_jose = cover("images/eventos/entrada_jose.png")
    image bg casa_fabian = cover("images/eventos/casa_fabian.png")
    image bg cruce_trenes = cover("images/eventos/cruce_trenes.png")
    image bg barros_arana = cover("images/eventos/barros_arana.jpeg")
    image bg nielol_camino = cover("images/eventos/nielol_camino.webp")
    image bg nielol_sendero = cover("images/eventos/nielol_sendero.webp")
    image bg nielol_escaleras = cover("images/eventos/nielol_escaleras.webp")
    image bg nielol_mirador = cover("images/eventos/nielol_mirador.webp")
    image escena jose_arbol = cover("images/eventos/jose_arbol.jpeg")

label entreno_nielol:
    if not v_tinder:
        "Todavía no han armado el plan para José."
        jump hub
    $ ruta_barbarita_activa = True
    $ ultima_visita = "Cerro Ñielol"
    "Retoman la historia inventada de Barbarita. En esta versión, antes de ir a Villarrica, los cabros llevan a José al Ñielol para prepararlo."
    scene bg nielol_camino with fade
    show jose at center with dissolve
    show diego at left with dissolve
    show marcelo at right with dissolve
    jose "¿Y por qué tengo que subir un cerro pa hablar con una mina?"
    diego "Porque dijiste que estabai listo y te dio vergüenza preguntarle hasta la hora."
    marcelo "Y porque Benjamín dijo que era una caminata corta. Ya llevamos veinte minutos."
    hide diego
    show benjamin at left with dissolve
    benjamin "Estamos recién calentando, wn."
    marcelo "Calentando mis ganas de devolverme."
    "Pablo y Fabián vienen más atrás. Pablo sigue con short y gafas. Fabián lleva agua; al menos uno leyó el mensaje del grupo."
    menu:
        "Subir a su ritmo y dejar que José practique la conversa.":
            $ plan_entreno = "conversa"
            $ rel["José"] += 1
            jose "Ya, pero no se rían altiro. Déjenme terminar una frase."
            benjamin "Ya, dale. Te doy diez segundos sin comentarios. Récord mío."
        "Dejar que Benjamín arme su entrenamiento de película.":
            $ plan_entreno = "militar"
            $ broma_benjamin += 1
            benjamin "¡Hasta esa curva sin parar! ¡Por la Barbarita!"
            jose "No le mandís ese video. Si se lo mandai, me devuelvo."
            $ consecuencia("José puso una condición: el video del entrenamiento se queda en el grupo.")
    $ sfx("pasos.ogg")
    scene bg nielol_sendero with dissolve
    show pablo at left with dissolve
    show fabian at right with dissolve
    pablo "¿Ven? No hace frío."
    fabian "Pablo, estai tiritando y estamos subiendo."
    pablo "Es la energía."
    fabian "Toma agua, energía."
    $ sfx("pasos.ogg")
    scene bg nielol_escaleras with dissolve
    show jose at center with dissolve
    show marcelo at right with dissolve
    marcelo "Hay restaurante. El entrenamiento puede terminar acá."
    jose "Ya, ¿pero qué le digo cuando llegue a Villarrica?"
    menu:
        "Aclarar la pega: sueldo, horario y dónde se queda.":
            $ consejo_barbarita = "pega"
            mc "Pregúntale eso ahora, po. No viajís tres meses con un «después vemos»."
            jose "Tiene sentido. Le voy a preguntar sin mandar un meme primero."
        "Preguntarle si también quiere juntarse fuera de la pega.":
            $ consejo_barbarita = "juntarse"
            mc "La pega es una cosa. Si querís invitarla, pregúntale aparte."
            jose "Ya. Sin mezclar el sueldo con la cita."
            marcelo "Mira, entendió. Podemos bajar."
    scene bg nielol_mirador with fade
    show diego at left with dissolve
    show jose at right with dissolve
    diego "Llegaste, po. Ahora dilo sin mirar el celular."
    if plan_entreno == "conversa":
        jose "Hola, Barbarita. Quería preguntarte bien por la pega..."
        diego "Así mismo. No necesitabai una biografía entera."
    else:
        jose "Primero necesito recuperar el aire. Después recupero la dignidad."
        diego "Y después hablan. En ese orden."
    scene escena jose_arbol with fade
    "José se sube al tronco. Se queda un rato pensando en Barbarita mientras los demás sacan la foto."
    jose "Ya. Ahora sí estoy listo pa ir. Pero borren el video de Benjamín."
    "La foto queda en el grupo: José en el Ñielol, listo para Villarrica."
    $ v_nielol = True
    $ preparado_barbarita = True
    $ consecuencia("José terminó el entrenamiento. Se abrió la continuación de Villarrica en el mapa.")
    $ ruta_barbarita_activa = False
    jump hub

label whatif_villarrica:
    if not preparado_barbarita:
        "José todavía no está listo. Falta la subida al Ñielol."
        jump hub
    $ ruta_barbarita_activa = True
    $ v_villarrica = True
    "La historia inventada sigue: José tomó el bus a Villarrica. Tú y los demás se quedan en Temuco; siguen el viaje por el grupo del celular."
    scene bg inacap_dentro with fade
    show marcelo at left with dissolve
    show diego at right with dissolve
    marcelo "Mandó un audio. Dos minutos. No voy a escuchar dos minutos."
    diego "Lo vai a escuchar igual."
    "José adjunta la foto del Ñielol de ayer. No ha mandado ninguna foto de Villarrica todavía."
    scene escena jose_arbol with dissolve
    $ sfx("mensaje.ogg")
    "CELULAR · AUDIO DE JOSÉ DESDE VILLARRICA"
    if consejo_barbarita == "pega":
        jose "Pregunté antes de salir. Me mandaron el horario y cuánto me pagan. No eran tres meses gratis, menos mal."
        jose "Llegué, firmé lo de la pega y después me junté con la Barbarita. En ese orden, como dijimos."
    else:
        jose "Le pregunté si quería juntarse. Me dijo que sí, después de la pega."
        jose "Pero llegué sin preguntar dónde me quedaba. Ahora estoy viendo una pieza y ya me bajó la emoción un poco."
        "Invitarla salió bien; no haber aclarado el alojamiento le cuesta parte de las lucas del viaje."
    if plan_entreno == "conversa":
        jose "Hablamos normal. No tuve que decir la frase completa que ensayé en el cerro. Menos mal, porque me la olvidé."
    else:
        jose "Benjamín mandó el video al grupo. Barbarita no está en este grupo, ¿cierto? Revisen. REVISEN, WN."
        "Diego confirma la lista de participantes. José recién ahí deja de mandar mensajes."
    scene bg inacap_dentro with dissolve
    show marcelo at left with dissolve
    show diego at right with dissolve
    menu:
        "Preguntarle cómo le fue en el primer turno.":
            $ rel["José"] += 1
            jose "Cansador, pero bien. Primera vez que pregunto por las horas extra antes de quedarme."
            marcelo "Se fue a buscar pareja y aprendió a leer el contrato. Igual sirve."
        "Preguntarle por Barbarita sin pedir pantallazos.":
            jose "Nos juntamos a tomar algo. Estuvo bien. El resto se los cuento cuando vuelva, no sean sapos."
            diego "Ya, déjenlo. Si cuenta todo ahora, después con qué lo webeamos."
    "Termina el audio. En esta versión José se queda trabajando en Villarrica. Que la cita siga bien depende de ellos; el grupo ya hizo suficiente con subir el cerro."
    "Cierran el ¿y si…? y vuelven al caso de Shakira. Esta historia imaginada no aporta pruebas a la grabadora."
    $ consecuencia("Terminaste la continuación de Villarrica. Tus consejos cambiaron cómo llegó José a la pega.")
    $ ruta_barbarita_activa = False
    jump hub
