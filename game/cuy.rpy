default v_cuy_asado = False
default ruta_cuy_activa = False
default pablo_comio_cuy = False

init 20:
    image recuerdo cuy = Composite((1920,1080),
        (0,0), "bg patio", (600,160), Transform("images/eventos/cuy.webp", xysize=(720,560), fit="contain"))
    image recuerdo cuy_quieto = Composite((1920,1080),
        (0,0), "bg patio", (570,200), Transform("images/eventos/cuy_quieto.png", xysize=(780,500), fit="contain"))
    image escena congelador_cuy = cover("images/eventos/cocina_cuy.png")
    image escena cuy_preparado = Composite((1920,1080),
        (0,0), "escena congelador_cuy", (500,390), Transform("images/eventos/cuy_preparado.png", xysize=(920,520), fit="contain"))
    image escena cuy_asado = Composite((1920,1080),
        (0,0), "escena congelador_cuy", (740,275), Transform("images/eventos/cuy_asado.png", xysize=(380,520), fit="contain"))

label whatif_cuy:
    if not historia_cuy:
        "Primero tienes que escuchar la historia de Rubén."
        jump hub
    $ ruta_cuy_activa = True
    $ v_cuy_asado = True
    "¿Y SI…? EL CONGELADOR DE FABIÁN"
    "Después de la anécdota, los cabros inventan la peor versión posible: ¿qué habría pasado si Fabián encontrara al cuy antes de que Rubén lo enterrara? Esto no ocurrió en la historia de Rubén."
    scene recuerdo cuy_quieto with fade
    "En esta versión, el cuy ya había muerto cuando Fabián lo encontró. Rubén había ido a buscar una caja."
    fabian "¿Lo vai a enterrar?"
    ruben "Sí, po. Espérame acá."
    "Fabián no lo espera. Y tampoco le cuenta lo que hace después."
    $ sfx("refrigerador.ogg")
    scene escena congelador_cuy with fade
    "La historia da un salto hasta la casa de Fabián. Tiene al cuy guardado en el congelador."
    fabian "Pablo, ven a comer. Tengo algo pa tirar a la parrilla."
    pablo "¿El Rubén va?"
    fabian "No. No le avisís."
    pablo "¿Por qué?"
    fabian "Después te explico. Trae pan nomás."
    $ sfx("refrigerador.ogg")
    scene escena cuy_preparado with dissolve
    "Fabián saca del congelador el cuy preparado. Pablo todavía viene en camino y Rubén no sabe nada de la invitación."
    fabian "No voy a mandar foto al grupo. Sería buscarme el problema solo."
    $ sfx("plato.ogg")
    scene escena cuy_asado with fade
    "Cuando llega Pablo, el cuy ya está cocinado. Fabián lo pone en la mesa y prueba un pedazo primero."
    fabian "Ya, sírvete."
    menu:
        "Pablo pregunta qué carne es antes de probar.":
            $ pablo_comio_cuy = False
            pablo "Ya, pero ¿qué es eso? No me cambiís el tema."
            fabian "El cuy del Rubén."
            pablo "¿EL DEL RUBÉN? ¿Y lo invitaste?"
            fabian "Por eso te dije que no le avisarai."
            "Pablo aparta el plato y llama a Rubén. Fabián deja de masticar al escuchar el tono."
        "Pablo acepta la invitación sin preguntar.":
            $ pablo_comio_cuy = True
            "Pablo prueba. Fabián le sirve otro pedazo antes de que diga algo."
            pablo "Oye, ¿y por qué no podía venir el Rubén?"
            fabian "Porque era su cuy."
            "Pablo baja el pan muy despacio."
            pablo "Me podríai haber dicho ANTES, po, wn."
            "Pablo llama a Rubén. Esta vez no le sirve hacerse el que recién llegó."
    scene bg patio with fade
    show ruben at center with dissolve
    show fabian at left with dissolve
    show pablo at right with dissolve
    ruben "Yo fui a buscar una caja. UNA CAJA."
    if pablo_comio_cuy:
        ruben "¿Y tú también comiste?"
        pablo "No sabía."
        ruben "Pero sí sabíai que no tenía que enterarme."
        "Pablo se queda sin respuesta. En esta versión Rubén les deja de hablar a los dos."
        $ consecuencia("En el ¿y si…? Pablo comió sin preguntar. Rubén dejó de hablarle a él y a Fabián.")
    else:
        pablo "Yo no comí. Te llamé cuando me dijo."
        ruben "Ya. Tú quédate. Fabián, chao."
        fabian "Perro, pero..."
        ruben "No me digai perro ahora."
        $ consecuencia("En el ¿y si…? Pablo preguntó antes de comer y avisó a Rubén. Solo Fabián perdió su confianza.")
    "Marcelo corta la historia inventada. Ya no quiere escuchar qué habría traído el hermano de Fabián."
    "Vuelven a la conversación real del patio. Rubén recuerda su mascota; lo del congelador y el asado fue únicamente ese ¿y si…? que se acaban de inventar."
    $ ruta_cuy_activa = False
    jump hub
