default persistent.lluvia_animada = True

# Efectos generados por Ren'Py: no se altera ninguna fotografía original.
image gota_radal = Transform(Solid("#c1d5e850"), xysize=(2, 24), rotate=14)
image lluvia_radal = SnowBlossom("gota_radal", count=90, border=60,
    xspeed=(-190, -120), yspeed=(850, 1150), start=6, fast=True)

init python:
    renpy.music.register_channel("ambiente_radal", mixer="sfx", loop=True)
    if "ambiente_radal" not in config.overlay_screens:
        config.overlay_screens.append("ambiente_radal")

    def sonido_ambiente_radal():
        lluvia = any(renpy.showing(i) for i in ("bg inacap_lluvia", "bg inundado", "escena pablo_lluvia", "escena ruben_banca"))
        bosque = any(renpy.showing("bg " + i) for i in ("nielol_camino", "nielol_sendero", "nielol_escaleras", "nielol_mirador"))
        archivo = "audio/efectos/lluvia.ogg" if lluvia else ("audio/efectos/bosque.ogg" if bosque else None)
        actual = renpy.music.get_playing(channel="ambiente_radal")
        if archivo and renpy.loadable(archivo):
            if actual != archivo:
                renpy.music.play(archivo, channel="ambiente_radal", fadein=0.7, loop=True)
        elif actual:
            renpy.music.stop(channel="ambiente_radal", fadeout=0.7)

screen ambiente_radal():
    zorder -100
    if not main_menu:
        if renpy.showing("bg inacap_lluvia") or renpy.showing("bg inundado"):
            add Solid("#10233b14")
            if persistent.lluvia_animada:
                add "lluvia_radal"
        elif renpy.showing("bg atardecer"):
            add Solid("#ffab4210")
        elif renpy.showing("bg funeral"):
            add Solid("#10152218")
    timer 0.5 repeat True action Function(sonido_ambiente_radal)

transform golpe_cisterna:
    xoffset 0
    linear 0.06 xoffset -14
    linear 0.06 xoffset 12
    linear 0.06 xoffset -8
    linear 0.06 xoffset 0

# Mayor contraste para leer decisiones sobre fotos; listas largas desplazables.
init 10:
    style choice_button:
        background Solid("#17242ce8")
        hover_background Solid("#345745f5")
        xsize 1280
        padding (24, 12)
    style choice_button_text:
        color "#edf2ed"
        hover_color "#ffffff"
        insensitive_color "#ccd4cb"
        size 34
