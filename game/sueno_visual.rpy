default fase_globo_pablo = 0
default sueno_pablo_activo = False
define pablo_imagina = Character("Pablo Hernández", color="#ae941f", screen="say_pablo_imagina")

init python:
    class GloboPablo(renpy.Displayable):
        def __init__(self, fase, **kwargs):
            super(GloboPablo,self).__init__(**kwargs)
            self.fase = fase
        def render(self,width,height,st,at):
            r = renpy.Render(640,290)
            c = r.canvas()
            color = "#fff2c9" if self.fase >= 3 else "#fffdf5"
            centros = [(95,125),(535,125)] if self.fase == 1 else [(95,115),(155,65),(260,60),(375,60),(485,65),(535,115),(475,195),(365,205),(255,205),(150,195)]
            for x,y in centros:
                c.circle("#293d3a",(x+2,y+3),67)
            c.rect("#293d3a",(95,62,440,142))
            for x,y in centros:
                c.circle(color,(x,y),63)
            c.rect(color,(95,66,440,134))
            if self.fase >= 2:
                c.circle("#293d3a",(55,243),16)
                c.circle(color,(54,242),13)
                c.circle("#293d3a",(25,272),9)
                c.circle(color,(24,271),6)
            else:
                c.polygon("#293d3a",[(65,185),(110,185),(40,226)])
                c.polygon(color,[(71,182),(105,182),(47,216)])
            return r

transform globo_pablo_flota(fase):
    yoffset 0
    ease 1.2 yoffset (-5 if fase >= 3 else 0)
    ease 1.2 yoffset 0
    repeat

screen say_pablo_imagina(who,what):
    window:
        style "say_window"

    window:
        id "window"
        style "default"
        xanchor 0.0
        yanchor 0.0
        padding (0,0)
        background None
        xpos 1080
        ypos 125
        xsize 640
        ysize 290
        at globo_pablo_flota(fase_globo_pablo)
        fixed:
            add GloboPablo(fase_globo_pablo)
            text who id "who" xpos 125 ypos 55 size 19 color "#59706b"
            text what id "what" xpos 80 ypos 90 xmaximum 495 size 27 color "#233632" line_spacing 3
