# Fotografías del usuario y composiciones para las secuencias del asado y choque.
init 15 python:
    def sprite_anticucho(archivo, pos=(280,515), giro=-8):
        mano = "images/eventos/anticucho_mano.png"
        if not renpy.loadable(mano):
            mano = "images/eventos/anticucho.png"
        return Fixed(
            Transform(archivo, xysize=(520,860), fit="contain", xalign=0.5, yalign=1.0),
            Transform(mano, xysize=(170,285), fit="contain", rotate=giro, xpos=pos[0], ypos=pos[1]),
            xsize=520, ysize=860, yoffset=-250)

    renpy.register_shader("radal.fulgor", variables="""
        uniform float u_impacto;
        uniform vec2 u_model_size;
        attribute vec4 a_position;
        varying vec2 v_radal_coord;
    """, vertex_300="""
        v_radal_coord = a_position.xy / u_model_size;
    """, fragment_300="""
        vec2 punto = (v_radal_coord - vec2(0.55, 0.49)) * vec2(1.777, 1.0);
        float radio = length(punto);
        float angulo = atan(punto.y, punto.x);
        float t = u_impacto;
        float lobulo = 0.028 * sin(angulo * 13.0 + t * 18.0) + 0.018 * sin(angulo * 27.0 - t * 11.0);
        float expansion = 0.06 + t * 0.67;
        float bola = 1.0 - smoothstep(expansion + lobulo - 0.06, expansion + lobulo + 0.06, radio);
        float ruido = 0.5 + 0.5 * sin(punto.x * 31.0 + sin(punto.y * 25.0) * 3.0 + t * 19.0);
        float centro = exp(-radio * radio / (0.014 + t * 0.12));
        float onda = exp(-pow((radio - t * 0.93) * 28.0, 2.0));
        float rayos = pow(max(0.0, sin(angulo * 42.0 + 1.7)), 18.0) * exp(-pow((radio - t * 0.76) * 16.0, 2.0));
        float fuego = bola * (1.0 - smoothstep(0.38, 0.86, t));
        float humo = bola * smoothstep(0.3, 0.7, t) * (1.0-t) * 0.65;
        float alpha = clamp(fuego * 0.92 + humo + onda * (1.0-t) * 0.35 + rayos * (1.0-t), 0.0, 0.96);
        vec3 color_fuego = mix(vec3(0.9,0.12,0.01), vec3(1.0,0.78,0.2), ruido);
        color_fuego = mix(color_fuego, vec3(1.0,0.97,0.75), centro);
        vec3 color_humo = mix(vec3(0.13,0.12,0.11), vec3(0.42,0.37,0.31), ruido);
        vec3 color_final = mix(color_fuego,color_humo,smoothstep(0.38,0.82,t));
        gl_FragColor = vec4(color_final * alpha, alpha);
    """)

init 20:
    image escena benjamin_pillalelbun = cover("images/eventos/benjamin_pillalelbun.jpeg")
    image escena benjamin_shell = cover("images/eventos/benjamin_shell.jpeg")
    image asado parrilla = Composite(
        (1920,1080), (0,0), "bg asado",
        (280,230), Transform("images/eventos/parrilla.png", xysize=(1360,850), fit="contain"))
    image benjamin anticucho = sprite_anticucho("images/benjamin.png", (255,580), -8)
    image pablo anticucho = sprite_anticucho("images/eventos/pablo_gafas.png", (180,625), -8)
    image fabian anticucho = sprite_anticucho("images/fabian.png", (140,630), -8)
    image jose anticucho = sprite_anticucho("images/jose.png", (210,615), -8)
    image ruben anticucho = sprite_anticucho("images/ruben.png", (260,660), -5)
    # Maxi ya tiene las manos en la foto: el palito queda debajo de ellas.
    image maxi anticucho = Fixed(
        Transform("images/maxi.png", xysize=(520,860), fit="contain", xalign=0.5, yalign=1.0),
        Transform("images/eventos/anticucho.png", xysize=(140,210), rotate=-30, xpos=35, ypos=525),
        Transform("images/maxi.png", crop=(160,200,190,125), xysize=(209.32,137.71), xpos=176.27, ypos=663.9),
        xsize=520, ysize=860, yoffset=-250)
    image ivan anticucho = sprite_anticucho("images/ivan.png", (180,625), -5)

transform cisterna_avanza:
    xpos 1980
    ypos 250
    linear 1.15 xpos 560 ypos 285
    ease 0.12 rotate -4.0

transform impacto_shell:
    xoffset 0
    yoffset 0
    linear 0.07 xoffset -35 yoffset 14
    linear 0.07 xoffset 29 yoffset -12
    linear 0.08 xoffset -11 yoffset 4
    linear 0.08 xoffset 5 yoffset -2
    linear 0.14 xoffset 0 yoffset 0

transform fulgor_shell:
    shader "radal.fulgor"
    u_impacto 0.0
    linear 2.1 u_impacto 1.0

transform destello_impacto:
    alpha 0.6
    linear 0.12 alpha 0.0

transform fragmento_shell(dx,dy,giro):
    xpos 1010
    ypos 515
    alpha 1.0
    linear 0.75 xpos (1010+dx) ypos (515+dy) rotate giro
    easein 0.55 ypos (760+dy) alpha 0.0

screen explosion_shell():
    zorder 40
    add Solid("#ffffff") at fulgor_shell
    add Solid("#ffffff") at destello_impacto
    for dx, dy, giro in [(-700,-250,130),(-480,-390,-120),(-260,-420,210),(240,-370,-150),(560,-260,180),(750,-50,-210),(-620,60,280),(360,180,-250)]:
        add Solid("#554637", xsize=20, ysize=11) at fragmento_shell(dx,dy,giro)
    timer 2.2 action Hide("explosion_shell")

label choque_de_benjamin:
    $ sfx("motor_cisterna.ogg")
    scene escena benjamin_pillalelbun with fade
    "Benjamín saca la cisterna de Lautaro y llega hasta Pillalelbún. Tú vai al lado. Pablo todavía está tratando de llamarlo."
    benjamin "Si manejo tractor, puedo manejar esta wea."
    mc "El tractor no tiene todo ese tanque atrás, Benjamín."
    "Pasa por la plaza como si anduviera en su auto. La cisterna ocupa casi toda la calle."
    scene escena benjamin_shell with dissolve
    "De vuelta en la Shell de Lautaro, Benjamín apunta a la entrada. Pablo sale de la tienda haciendo señas."
    pablo "¡FRENA! ¡ANTES DEL SURTIDOR, WN!"
    benjamin "Sí, si estoy frenando."
    mc "Ese es el otro pedal."
    "El surtidor se viene encima del parabrisas. Benjamín gira tarde."
    $ sfx("frenada.ogg")
    scene bg shell with dissolve
    show expression Transform("images/eventos/cisterna_radal.png", xysize=(1340,700), fit="contain") as camion_choque at cisterna_avanza
    "Desde afuera, la cisterna cruza el patio directo hacia la tienda. El tanque se lleva una columna y golpea los surtidores."
    hide camion_choque
    scene bg shell_ruinas at impacto_shell
    $ sfx("explosion.ogg")
    if preferences.transitions:
        show screen explosion_shell
        pause 2.2
        hide screen explosion_shell
    "El golpe corta el ruido del motor. Después viene el estruendo. Humo, fuego y el techo de la Shell cayendo sobre el patio."
    "Pablo alcanza a correr hacia la salida. Tú y Benjamín salen por el otro lado de la cabina."
    "La Shell de Lautaro quedó destruida. La cisterna también. Benjamín mira el volante como si recién lo hubiera conocido."
    return
