# Rama alternativa posterior a la venta. La precuela Lucho sigue independiente.
default v_lucho_labranza = False
default ruta_lucho_activa = False
default plan_labranza = ""
default gesto_lucho = ""

label whatif_labranza:
    $ ultima_visita = "Labranza"
    $ v_lucho_labranza = True
    $ ruta_lucho_activa = True
    scene bg patio with fade
    show benjamin at left with dissolve
    show pablo at right with dissolve
    "¿Y SI... EL DATO FUERA EN LABRANZA?"
    "Esta es otra versión de lo que pasa después de la venta. Empieza con un audio que, en la historia principal, nunca llegó."
    benjamin "Me mandaron una foto de una yegua en Labranza."
    pablo "¿Y ya decidiste que es Shakira?"
    benjamin "Tiene cuatro patas. Coincide."
    mc "Muestra la foto, po."
    "En la foto sale media yegua y el espejo de una camioneta. Benjamín amplía hasta que no se distingue nada."
    menu:
        "Ir a preguntar antes de anunciar que la encontraron.":
            $ plan_labranza = "preguntar"
            mc "No le digai a José todavía. Vamos a cachar primero."
            benjamin "Ya. Pero si es ella, yo digo que fui el primero."
        "Llevar zanahorias por si resulta ser ella.":
            $ plan_labranza = "zanahorias"
            pablo "¿Cuántas?"
            mc "Una bolsa, Pablo. No estamos abasteciendo el Jumbo."
            benjamin "¿Por qué preguntó tan rápido cuánto?"
            pablo "Porque no quiero cargar veinte kilos, po."

    scene bg lucho_labranza with fade
    show pablo at right with dissolve
    show benjamin at left with dissolve
    "Llegan a Labranza. La foto no trae dirección. Pablo pregunta si al menos saben dónde almorzar."
    mc "¿No conocís a nadie acá?"
    benjamin "El Lucho es de acá. Voy a escribirle."
    "El audio de respuesta llega altiro: «Estoy de turno en el Acuenta. Si vienen, no me armen show»."

    scene bg lucho_acuenta with fade
    show lucho guardia at center with dissolve
    show benjamin at left with dissolve
    show pablo at right with dissolve
    lucho "Mira los que llegaron. ¿Qué andan haciendo acá?"
    benjamin "Buscando a Shakira."
    lucho "¿La cantante?"
    pablo "La yegua de José. La vendió por el compu."
    lucho "Ah, ya. Me faltaba ese detalle. ¿Y por qué la buscan en el supermercado?"
    benjamin "Tenemos una foto."
    "Luis mira la foto. Le baja el zoom que dejó Benjamín."
    lucho "Ese portón lo ubico. Pasan por acá antes de ir al campo. Pero voy a preguntar, no voy a inventarles."
    mc "¿Ustedes estudiaban juntos?"
    lucho "Segundo medio, sí. Después me fui a mecánica. No seguí con ellos en el Poli."
    benjamin "¿Y ahora acá?"
    lucho "Terminé desde la casa, hice el curso. Pasé por Superoferta primero. Ahora estoy en Acuenta, po."
    "Un cliente pregunta por los carros. Luis lo orienta y vuelve a mirar la foto."
    lucho "Espérenme al lado. Sin bloquear la entrada. Pablo, eso incluye tus patas."

    menu:
        "Esperar el dato sin interrumpirle el turno.":
            $ gesto_lucho = "esperar"
            "Se corren. Benjamín alcanza a mandar tres audios, todos diciendo que aún no sabe nada."
            lucho "Ya pregunté. Era el vecino que se la compró a José. La llevó donde un familiar."
        "Pedirle a Benjamín que deje de hacer preguntas a cada cliente.":
            $ gesto_lucho = "orden"
            mc "Benjamín, no todos los que vienen a comprar conocen a la yegua."
            benjamin "Uno nunca sabe."
            lucho "Este sí sabe: soy yo. Ya hablé con el dueño. Paren un rato."
    lucho "Les puede recibir mañana. Hoy tienen cerrado el portón. Y vayan a verla, no a hacerle juicio al loco."
    pablo "¿Podemos llevar zanahorias?"
    lucho "Pregúntenle a él. Yo soy guardia, no veterinario de la Shakira."
    jump final_lucho

label final_lucho:
    scene bg patio with fade
    show jose at center with dissolve
    show pablo at right with dissolve
    show benjamin at left with dissolve
    "Al día siguiente, José se suma al viaje. Lleva el celular con las fotos del cumpleaños, por si les piden comprobar cuál yegua era."
    jose "¿Quién consiguió la dirección?"
    benjamin "Nosotros."
    pablo "El Lucho."
    benjamin "Con nosotros presentes."
    scene bg potrero with fade
    show shakira at left with dissolve
    show jose at right with dissolve
    "El dueño les abre. Shakira está bien. José se acerca a la cerca y ella lo reconoce antes de que él diga nada."
    jose "Ouuu. Hola, Shakira."
    "Se queda haciéndole cariño. El celular con las fotos sigue en su bolsillo."
    mc "¿Vai a volver?"
    jose "Sí. Le voy a preguntar qué día se puede."
    "Esta vez lo pregunta de verdad. El dueño le anota el número y le dice que avise antes de ir."
    show benjamin at center with dissolve
    benjamin "Ya, pero falta la foto. Pa mandársela al Lucho."
    "Pablo intenta salir al medio. Shakira mete la cabeza y lo corre."
    pablo "La estái tomando muy abierta. Se me ven las patas."
    benjamin "No puede ser que justo ahora te dé vergüenza el short."
    scene bg lucho_acuenta with fade
    show lucho guardia at center with dissolve
    "En su descanso, Luis recibe la foto. José con Shakira. Pablo sale cortado. Benjamín culpó a la cámara."
    lucho "Ya, la encontraron. Ahora ojalá vuelvan a saludar sin andar buscando algo."
    if gesto_lucho == "orden":
        "Le llega otro audio de Benjamín preguntando por el próximo turno. Luis contesta: «De visita. No de operativo»."
    else:
        "Luis guarda el celular. Se acabó el descanso; todavía falta turno."
    $ persistent.finales.add(7)
    $ renpy.save_persistent()
    scene black with fade
    "FINAL 7 de 7: El dato de Lucho — final alternativo de Labranza."
    "En esta versión, encontraron a Shakira y José volvió a visitarla. Lucho siguió de guardia. El DLC cuenta cómo llegó ahí."
    "RADAL — creado por SeguelStudios. Gracias por jugar."
    return
