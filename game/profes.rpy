# La visita actual continúa el recuerdo del liceo; el protagonista no estuvo en la clase.
default consejo_martin = False
default grabacion_hector = ""

label conversacion_martin_hector:
    hide diego
    hide benjamin
    show martin at left with dissolve
    show hector at right with dissolve
    "Cuando van saliendo, aparece el profe Martín. Héctor viene detrás, guardando la cámara. El Jeep sigue atravesado afuera."
    martin "¿Vinieron a saludar o a repetir la misma talla de siempre?"
    diego "Las dos, profe. Pa qué le voy a mentir."
    martin "Por lo menos uno honesto. ¿Y tú? A ti no te hice clases."
    mc "Llegué después al grupo. Me estaban contando lo de China."
    martin "Ya veo. Toda una competencia, meses preparando el proyecto, y estos se acuerdan del puesto."
    hector "Con mi canal pasa lo mismo. Tengo videos arreglando cosas y me dicen que puro grabo el Jeep."
    diego "Pero tiene un video de doce minutos lavando una rueda, po."
    hector "Las cuatro, Diego. Hay capítulos."
    martin "Ya, ya. ¿Qué necesitai? Antes de que este explique la segunda rueda."

    menu:
        "Preguntarle al profe cómo ordenar las versiones del grupo.":
            mc "Cada uno cuenta algo distinto. Después de un rato ya no sé qué pasó y qué era una talla."
            martin "Parte por separar lo que alguien vio de lo que le contaron. Anota quién dijo cada cosa. Después comparai."
            mc "¿Aunque el que cuente sea usted?"
            martin "Aunque sea yo. Si no te cuadra, preguntai. No te quedís con la primera versión porque suena bonita."
            diego "Ya, profe. Entonces, ¿segundo o duodécimo?"
            martin "Eso es aplicar el consejo demasiado rápido."
            $ consejo_martin = True
            $ apoyo += 1
            $ consecuencia("Anotaste el consejo de Martín: distinguir testigos de rumores antes de acusar.")
        "Preguntarle a Héctor cómo registra sus videos.":
            hector "Muestro lo que estoy haciendo. Si algo queda fuera de cámara, no digo que lo grabé."
            mc "¿Y si quiero guardar una conversación del grupo?"
            hector "Pregunta antes, po. Una cosa es grabar mi Jeep y otra subir a alguien que ni cachaba que lo estabai filmando."
            mc "Entonces primero les pregunto y después les muestro cómo quedó."
            hector "Eso. Y que se escuche. El otro día el viento tapó todo el arreglo del motor."
            diego "¿Lo volvió a grabar?"
            hector "Sí. Doce minutos más."
            $ grabacion_hector = "permiso"
            $ apoyo += 1
            $ consecuencia("Acordaste pedir permiso antes de grabar o compartir al grupo.")
        "Seguir molestando con el viaje y el Jeep.":
            mc "¿Y si llevan el Suzuki a Shenzhen? Ahí tienen temporada completa."
            hector "¿Quién paga el barco? Porque el Jeep no lo dejo acá."
            martin "Y ahora querís convertir mi viaje en paseo. Por eso nunca terminamos la clase."
            diego "Ya, profe. Igual nos demoramos nosotros."
            $ grabacion_hector = "talla"
            $ broma_benjamin += 1
            $ consecuencia("Preferiste la talla del Jeep; te fuiste sin ordenar las versiones con Martín.")

    martin "Fuera de leseo: cuídense entre ustedes. Una talla está bien; dejar a un amigo botado es otra cosa."
    hector "¿Quieren una foto antes de irse?"
    diego "Ya, pero nosotros adelante. El Jeep al fondo."
    hector "Ya. Pero que salga completo."
    "Héctor les muestra la foto antes de guardarla. Por una vez, salen más personas que ruedas."
    hide martin with dissolve
    hide hector with dissolve
    return

label balance_profes:
    if consejo_martin:
        if pista_pablo and pista_diego and pista_potrero:
            "El consejo de Martín quedó en tu cuaderno. Esta vez juntaste lo que viste en la cabina, el Jumbo y el potrero antes de dar una versión por cierta."
        else:
            "En el cuaderno quedó el consejo de Martín. También quedaron preguntas sin resolver; en otra partida podrías comparar más testimonios."
    if grabacion_hector == "permiso":
        "Héctor manda la foto de la visita al liceo al grupo. Te pregunta antes de subirla a su canal. Le agradeces: lo conversado no se quedó en pura talla."
    elif grabacion_hector == "talla":
        "Héctor manda un enlace al grupo: «Lavado del Suzuki, parte dos». Diego no lo abre. Martín pregunta otra vez quién rayó la mesa."
    return
