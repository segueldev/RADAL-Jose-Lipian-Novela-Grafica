default pausa_eventos = False

label cuaderno:
    scene bg inacap_dentro with fade
    "Revisas las notas del celular. Lo que sí averiguaste, sin las teorías de Benjamín."
    if not venta:
        "Shakira sigue con José. Puedes ir a conocerla a Lincoñir: llevas [potrero_visitas] de tres visitas."
    else:
        "José vendió a Shakira. Falta saber dónde terminó y qué tiene que ver Pablo."
        if pista_pablo:
            "Cabina de Pablo: encontraste una montura."
        else:
            "Cabina de Pablo: pendiente. Si ya fuiste a la Shell, puedes volver a revisarla."
        if pista_diego:
            "Jumbo: Diego vio a un cliente de short y gafas comprando veinte kilos de zanahorias."
        else:
            "Jumbo: pendiente. Vale la pena preguntarle a Diego de nuevo después de la venta."
        if pista_potrero:
            "Lincoñir: el pesebre tiene heno fresco y huellas recientes."
        else:
            "Lincoñir: falta revisar el pesebre."
        if pista_ruben:
            "Rubén: vio una yegua cerca de la Shell los domingos."
            if secreto_ruben:
                "Le prometiste no dar su nombre."
    if decisiones_clave:
        "También anotaste lo que cambió por tus decisiones:"
        python:
            for nota_decision in decisiones_clave[-5:]:
                renpy.say(None, nota_decision)
    "Grabaciones: [fragmentos] de cinco."
    if historia_escuchada:
        "Ya las escuchaste en orden."
    "Las historias de Tinder, del trabajo, del Inacapini y la ruta de Labranza son imaginadas. No cuentan como pistas."
    jump hub
