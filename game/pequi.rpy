# Foto de Pequi proporcionada por el creador del juego.
image pequi = Transform("images/eventos/pequi.png", xysize=(430,290), fit="contain")

transform pequi_techo:
    xpos 1330
    ypos 150

label pequi_presentacion:
    show pequi at pequi_techo with dissolve
    "Y en el techo de la tienda, una gata blanca con naranja mira a todos con desprecio."
    fabian "Esa es la Pequi, mi gata. No es de ningún grupo. Ella tiene su propio grupo. Ella es la líder."
    hide pequi with dissolve
    return

label pequi_inundacion:
    show pequi at pequi_techo with dissolve
    "Fabián ya tiene a sus galgos, Los Intratables, listos en la camioneta. Pequi, su gata, mira todo desde el techo, bien lejos del agua."
    hide pequi with dissolve
    return
