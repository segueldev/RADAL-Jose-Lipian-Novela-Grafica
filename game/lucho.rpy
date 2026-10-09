# Precuela independiente: no modifica pistas, relaciones ni finales de José.
define lucho = Character("Luis Araya (Lucho)", color="#66cdaa")
default lucho_activo = False
default lucho_respuesta = ""
default lucho_turno = ""
default persistent.lucho_completado = False

image lucho liceo = sprite("images/eventos/lucho_liceo.png")
image lucho joven = sprite("images/lucho/luis.png")
image lucho guardia = sprite("images/lucho/guardia.png")
image bg lucho_labranza = cover("images/lucho/labranza.webp")
image bg lucho_casas = cover("images/lucho/casas.webp")
image bg lucho_superoferta = cover("images/lucho/superoferta.jpeg")
image bg lucho_acuenta = cover("images/lucho/acuenta.jpeg")

label lucho_inicio:
    $ lucho_activo = True
    $ musica("tema.ogg")
    scene black with fade
    "LUCHO — una precuela de RADAL."
    "Antes de que llegaras tú. Antes del INACAP y de andar investigando una yegua. Había otras historias. Esta empieza con Luis Araya."
    scene bg lucho_labranza with fade
    show lucho liceo at center with dissolve
    "Labranza. Luis Araya para los papeles. Lucho para los amigos. Los papeles nunca le preguntaron cuál prefería."
    lucho "Soy de Labranza, po. Si me pierdo acá, ya sería preocupante."
    "Todavía no llevaba uniforme de guardia. Todavía estaba tratando de cachar qué iba a hacer con su vida. Como todos, pero sin admitirlo tanto."

    scene bg sala_liceo with fade
    show lucho liceo at left with dissolve
    show benjamin at right with dissolve
    "Un recuerdo de segundo medio, cuando Luis compartía curso con los cabros. El protagonista de la historia principal aún no los conocía."
    benjamin "Lucho, ¿y después qué?"
    lucho "Mecánica. Por lo menos si algo falla, voy a tener una llave."
    benjamin "Para arreglar mi vida vas a necesitar una caja entera."
    lucho "Esa cuestión viene sin repuestos."
    "Segundo medio pasó. Después Luis entró a mecánica y dejó de compartir curso con los cabros. Cada uno siguió por su lado."

    $ musica("triste")
    scene bg liceo with fade
    show lucho liceo at center with dissolve
    "En el Politécnico también hubo dos historias que no le salieron como esperaba: Kuki CF y Catalina Jara. Las dos lo rechazaron."
    lucho "La Kuki CF me dijo que no. Y la Catalina Jara también."
    lucho "Ya, po. Si no quieren, no quieren. Igual penca, pero no voy a andar insistiendo."
    "Se queda un rato en el patio antes de irse. Los demás siguen pasando a clases."
    menu:
        "Tomárselo con humor.":
            $ lucho_respuesta = "humor"
            lucho "Dos rechazos. Por último no gasté las lucas del computador invitando a salir a alguien que no quería."
        "Darse un rato antes de seguir.":
            $ lucho_respuesta = "calma"
            lucho "Hoy estoy choreado. Mañana veo cómo seguir. Una cosa a la vez, po."
    "Con el tiempo Luis dejó el liceo. Los rechazos de Kuki CF y Catalina Jara eran parte de esos recuerdos; los estudios los terminó por otro camino."

    $ musica("calma")
    scene bg lucho_casas with fade
    show lucho joven at center with dissolve
    "De vuelta en Labranza, ya fuera del liceo. Dejó el uniforme escolar y terminó los estudios desde la casa."
    "Estudiaba en la mesa de la casa. Cuando llegaba la once, tocaba correr los cuadernos."
    lucho "Desde la casa no significa que las tareas se hagan solas. Ya lo comprobé. Varias veces."
    if lucho_respuesta == "humor":
        lucho "Acá me preguntan por la tarea, no por la Kuki ni la Cata. Algo es algo."
    else:
        lucho "De a poco. Terminar primero, después pensar en la pega."
    "Hubo días largos, cuadernos abiertos y ganas de dejar todo para mañana. Hasta que llegó el día en que los estudios quedaron terminados."
    lucho "Listo. Ahora falta la parte en que me pagan por hacer algo."
    "También estaba armándose un computador. La lista de piezas le cambiaba cada vez que miraba los precios."
    lucho "A mi abuelo ya le saqué cien lucas una vez. Después cuatrocientas pa las piezas."
    lucho "Si ahora le digo que me falta el monitor, me va a pasar la tele de la cocina."
    "Luis cierra la lista. Antes de seguir sumando piezas, necesitaba una pega."


    scene bg lucho_labranza with fade
    show lucho joven at center with dissolve
    "El siguiente paso fue un curso de guardia. Aprender a observar, seguir procedimientos y mantener la calma."
    "La mecánica le había enseñado que no todo se arregla a golpes. El curso vino a confirmar que con la gente tampoco."
    lucho "Ser guardia no es pararse con cara de malo todo el día. Igual esa cara me sale cuando madrugo."
    menu:
        "Concentrarse en observar.":
            $ lucho_turno = "observar"
            lucho "Primero mirar bien. Inventarse una película es fácil; cachar qué pasa es la pega."
        "Concentrarse en tratar bien a la gente.":
            $ lucho_turno = "trato"
            lucho "Hablar tranquilo. Si yo llego gritando, ya dejé la cagá antes de empezar."
    "Terminó el curso. Después vino el uniforme. La cara seguía siendo la misma; la responsabilidad, otra."

    $ musica("viaje")
    scene bg lucho_superoferta with fade
    show lucho guardia at center with dissolve
    "Superoferta, Labranza. Su primera parada antes de llegar al Acuenta."
    "Carros, bolsas y gente pensando en llegar a la casa. Para Luis, el comienzo de una etapa nueva."
    lucho "Primer paso. Nadie nace sabiéndose todos los turnos."
    if lucho_turno == "observar":
        "Luis se tomó el tiempo de conocer el movimiento del lugar. Cada cosa parecía urgente hasta que aprendió a distinguirlas."
    else:
        "Luis aprendió a repetir una indicación sin perder la paciencia. La tercera vez también contaba como parte de la pega."
    lucho "En el curso no te explican lo largo que puede ser un día cuando todavía no conocís a nadie."
    "Pasó por Superoferta. Y más adelante, sin salir de Labranza, el camino lo llevó a otro supermercado."

    scene bg lucho_acuenta with fade
    show lucho guardia at center with dissolve
    "Acuenta, Labranza. Aquí Luis terminó trabajando de guardia."
    "Otra entrada, otros turnos. Lucho ya no era el cabro que salía del liceo sin saber cuál sería el siguiente paso."
    lucho "La Kuki CF y la Catalina Jara me rechazaron cuando estaba en el liceo. Después salí, terminé desde la casa, hice el curso y pasé por Superoferta. Ahora estoy acá."
    lucho "Contado así parece cortito. Había que vivirlo, po."
    "Los amigos de segundo medio seguían siendo parte de sus recuerdos. Haber tomado otro camino no borraba esos años."
    lucho "Si aparecen los cabros, los saludo. Pero si Benjamín viene con alguna idea rara, que la deje afuera."
    "Suena un carro. Luis mira hacia la entrada. La vida no espera a que termine el monólogo."
    lucho "Ya. A trabajar."
    scene black with fade
    "Mucho después llegarías tú a conocer al grupo. Para entonces, Lucho ya tenía su propia historia."
    "LUCHO — fin de la precuela."
    $ persistent.lucho_completado = True
    $ renpy.save_persistent()
    "Creado por SeguelStudios. Música original: Fabián Millalén (Fabinho). Luis Araya, de Labranza. Gracias por jugar."
    return
