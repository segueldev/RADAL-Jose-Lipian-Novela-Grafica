default decisiones_clave = []
default confianza_pablo = False
default acuerdo_shell = False
default premier_bloqueado = False
default traicion_ruben = False
default plan_sueno = ""
default actitud_final = ""

init python:
    def consecuencia(mensaje):
        if mensaje not in store.decisiones_clave:
            store.decisiones_clave.append(mensaje)
        renpy.hide_screen("aviso_whatif")
        renpy.show_screen("aviso_recuerda", mensaje, "#e1bc70")

    def testigo_confiable():
        return store.pista_ruben and store.secreto_ruben and not store.traicion_ruben and store.rel.get("Rubén", 0) >= 1

label permiso_cabina:
    if pablo_arruinado and not acuerdo_shell:
        pablo "No vai a meterte al camión después de la cagá que dejaron. Primero resolvamos quién paga."
        $ consecuencia("Pablo cerró la cabina hasta resolver el daño de la Shell.")
        return False
    if ayuda_inundacion == "pablo":
        pablo "Tú me ayudaste con el agua. Pasa, pero no revuelvas las cosas."
        $ confianza_pablo = True
        $ consecuencia("Ayudar a Pablo en la inundación te abrió la cabina.")
        return True
    if pablo_molesto and rel["Pablo"] < 0 and not confianza_pablo:
        pablo "Me venís a webear con el frío y después me pedís que te deje revisar. No, po."
        menu:
            "Disculparte por la talla y preguntarle de nuevo.":
                $ confianza_pablo = True
                $ pablo_molesto = False
                $ rel_delta("Pablo", 2)
                pablo "Ya. Pero sin andar grabando después."
                $ consecuencia("Te disculpaste con Pablo: volvió a dejarte entrar.")
                return True
            "Insistir: no necesitas caerle bien para investigar.":
                $ rel_delta("Pablo", -1)
                pablo "Mi camión, po. No entrís."
                $ consecuencia("Insististe y Pablo negó el acceso. Necesitarás otro testigo.")
                return False
    return True
