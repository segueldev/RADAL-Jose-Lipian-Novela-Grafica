# Ajustes táctiles; no cambian el diseño de la versión de escritorio.
style mm_button_text:
    variant "small"
    size 40

style mm_button:
    variant "small"
    ypadding 7

style mm_buttons:
    variant "small"
    spacing 0

style quick_button_text:
    variant "small"
    size 36

screen help():
    variant "touch"
    tag menu
    use game_menu("Ayuda", scroll="viewport"):
        vbox:
            spacing 24
            text "Jugar en Android" size 48
            text "Toca la pantalla para avanzar el diálogo. Toca una opción para decidir." size 38
            text "El botón Menú abre Guardar, Cargar, Historial y Opciones. Atrás repasa el diálogo anterior." size 38
            text "El mapa permite elegir los destinos disponibles; el cuaderno guarda tus pistas y decisiones." size 38
            text "Arrastra las listas largas hacia arriba o abajo para ver todas las opciones." size 38
            text "El juego se usa en horizontal. La música y los efectos se ajustan en Opciones." size 38

style window:
    variant "small"
    background Solid("#f6f6f6")
