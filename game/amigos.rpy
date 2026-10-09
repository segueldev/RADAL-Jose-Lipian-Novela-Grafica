default chocolate_fabian = False
default origen_bastian = False

label charla_fabian:
    $ chocolate_fabian = True
    scene bg patio with fade
    show fabian at left with dissolve
    show marcelo at right with dissolve
    "Fabián tiene un Trencito en la mochila. Lo saca, lo mira y lo vuelve a guardar."
    marcelo "¿Todavía tenís ese chocolate?"
    fabian "Está cerrado, wn. No tiene nada."
    mc "¿Desde cuándo?"
    fabian "Fui con una mina al Museo Ferroviario, por Barros Arana. Se lo iba a dar ahí."
    marcelo "Se fueron del museo y volvió con el chocolate entero."
    fabian "No se dio el momento, perro."
    menu:
        "¿No se dio el momento o no lo sacaste de la mochila?":
            $ broma_benjamin += 1
            fabian "Ya, no lo saqué. Pero iba a quedar raro sacarlo al despedirse."
            marcelo "Más raro es traerlo a clases toda la semana."
        "Dejar que Fabián lo abra: por lo menos que no se derrita.":
            $ rel_delta("Fabián", 1)
            "Fabián abre el chocolate. Ofrece un cuadrito y guarda el resto para él."
            fabian "Ya, se acabó la historia."
            marcelo "Te lo comiste tú. Buen final."
    fabian "Mi hermano está vendiendo ceviches a veces. Si quieren, le preguntan, no me encarguen a mí."
    marcelo "¿Y por qué te voy a encargar a ti?"
    fabian "Porque después me llegan mensajes mientras estoy jugando, po."
    "El celular de Fabián vibra. Marcelo mira la pantalla antes que él."
    marcelo "¿Vai a jugar Rocket League otra vez?"
    fabian "Un partido, wn. Después practico piano."
    mc "¿Tocai piano?"
    fabian "Sí, hago música. No es puro perder partidos como dice este."
    marcelo "Ayer dijiste un partido y te acostaste a las tres."
    fabian "Porque quedamos mal. No podís cerrar perdiendo."
    marcelo "Por eso no cerrái nunca."
    jump hub

label charla_bastian:
    $ origen_bastian = True
    scene bg patio with fade
    show bastian at right, bastian_bajo with dissolve
    show benjamin at left with dissolve
    "Bastián mira la hora y empieza a guardar las cosas."
    benjamin "¿Ya te vai? Queda rato todavía."
    bastian "Tengo que tomar la micro."
    mc "¿Pa dónde?"
    bastian "General López."
    "Benjamín deja el celular sobre la mesa."
    benjamin "¿Erai de General López? ¿Por qué nunca dijiste?"
    bastian "Nunca preguntaste."
    menu:
        "Tiene razón. Lo dejan hablar poco.":
            $ rel_delta("Bastián", 1)
            benjamin "Ya, habla. Te escucho."
            "Bastián señala la hora. Se le está pasando la micro."
            benjamin "Después, entonces. Pero habla."
        "Pedirle a Benjamín que organice otro tour de la nación.":
            $ broma_benjamin += 1
            benjamin "General López nos tiene que reconocer primero."
            bastian "No."
            "Benjamín se queda esperando un sí que no llega."
    "Bastián se despide. Esta vez nadie le pide que cargue una mochila ajena."
    jump hub

default historia_cuy = False

label charla_ruben:
    $ historia_cuy = True
    scene bg patio with fade
    show ruben at right with dissolve
    show marcelo at left with dissolve
    $ sfx("mensaje.ogg")
    "El celular de Rubén suena. Marcelo alcanza a ver el perfil que tiene abierto."
    marcelo "¿Pupencio? ¿Ese canal es tuyo?"
    ruben "Sí."
    marcelo "¿Y qué es eso, Rubén? ¿Por qué hacís esos videos?"
    ruben "Edits de anime, po. Re:Zero, Cyberpunk: Edgerunners, Hunter x Hunter."
    marcelo "No me gusta el anime. Abro TikTok pa ver fútbol y me aparece un mono llorando con música."
    ruben "Entonces no lo veai."
    marcelo "Pero me lo mandaste tú."
    ruben "Pa que le dierai like."
    marcelo "Ah, querís apoyo sin que mire. Así cualquiera."
    ruben "Tú hacís lo mismo con premierchilito."
    "Marcelo mira su café. Por una vez no encuentra qué responder altiro."
    "Rubén cambia de video: ahora es un cuy comiendo. Le da replay en vez de pasarlo."
    mc "¿Tuviste uno?"
    ruben "Cuando era chico."
    scene recuerdo cuy with dissolve
    "Rubén se acuerda del cuy que tenía de chico."
    marcelo "Ya, pero cuenta la historia completa."
    ruben "Lo encontré quieto. Pensé que estaba muerto y lo enterré."
    scene recuerdo cuy_quieto with dissolve
    "Así recuerda haberlo encontrado: quieto, sin reaccionar. En ese momento pensó que había muerto."
    "Marcelo deja el café sobre la mesa."
    mc "¿Y estabai seguro?"
    ruben "Después me dijeron que capaz seguía vivo. Que estaba hibernando o algo así."
    mc "Los cuyes no hibernan, Rubén. Eso te lo explicaron mal."
    ruben "Yo era chico, po. No sabía."
    "Nadie puede aclarar qué pasó con el animal. Rubén tampoco; está contando lo que recuerda de esa edad."
    scene bg patio with dissolve
    show ruben at right with dissolve
    show marcelo at left with dissolve
    menu:
        "Preguntarle si llamó a alguien antes de enterrarlo.":
            ruben "No. Si pensé que ya estaba."
            marcelo "Ahí estaba el problema, po."
            ruben "Ya sé."
        "Dejar la historia ahí. No va a acordarse mejor por insistir.":
            $ rel_delta("Rubén", 1)
            ruben "Eso."
            "Rubén bloquea el celular. Por un rato no dice chao ni se hace el leso."
    jump hub
