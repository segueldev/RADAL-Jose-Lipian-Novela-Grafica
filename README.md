# RADAL — José Lipián, la novela gráfica

Novela visual chilena hecha con Ren'Py 8. Creado por **SeguelStudios**.
Basada en hechos reales.

José necesita una PC de un millón de pesos. Tiene una yegua llamada Shakira.
El resto son visitas al potrero, la Shell de Lautaro, apuestas en el INACAP
y decisiones que cambian el final.

## Cómo jugar

No hay que instalar nada: todo viene incluido.

### Windows

1. Descarga [`dist/Radal-1.0-win.zip`](dist/Radal-1.0-win.zip).
2. Descomprímelo en cualquier carpeta.
3. Ejecuta **`Radal.exe`** (trae el logo del juego).

### Linux

1. Descarga [`dist/Radal-1.0-linux.run`](dist/Radal-1.0-linux.run).
2. Dale permiso de ejecución y ábrelo:

   ```sh
   chmod +x Radal-1.0-linux.run
   ./Radal-1.0-linux.run
   ```

3. La primera vez se instala en `~/.local/share/radal` (ahí quedan tus
   partidas). Después vuelve a ejecutarlo y abre directo el juego.

También funciona en EndeavourOS, Steam Deck y casi cualquier distro moderna,
porque trae su propio runtime (no depende del Python del sistema).

## Qué tiene el juego

- **5 prólogos** que entran en orden aleatorio, con diálogo variable.
- Decisiones con consecuencias estilo Telltale: los avisos grandes de avance
  salen en pantalla (rojos cuando algo sale mal).
- **6 finales** y **3 "¿Y si...?"**, todo contado en el menú principal
  ("Finales desbloqueados: X de 6").
- Guardado y carga desde el menú; el menú de juego se abre con Esc.

## Desarrollo

Hecho con Ren'Py 8 (probado con la 8.5.3).

1. Instala el [SDK de Ren'Py 8](https://www.renpy.org/latest.html).
2. Abre el proyecto: `./renpy.sh /ruta/a/este/repo`
3. Para compilar nuevas distribuciones (Windows + Linux):

   ```sh
   ./renpy.sh <sdk>/launcher distribute \
       --destination dist \
       --package win --package linux \
       /ruta/a/este/repo
   ```

   Puedes regenerar el `.run` de Linux con la misma tar que usa
   `dist/Radal-1.0-linux.run` (cabecera shell + `Radal-1.0-linux.tar.bz2`).

## Estructura del repo

- `game/script.rpy` — el guion completo (todo el diálogo y las ramas)
- `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy` — interfaz, tema y configuración
- `game/images/` — fondos, sprites y escenas
- `game/audio/` — música
- `icon.ico` — logo del ejecutable de Windows
- `dist/` — builds listas para jugar

## Créditos

- **Creado por SeguelStudios**
- Música: *"Josep Lipian Iceberg"* — Fabián Millalén (Fabinho)
- Basada en hechos reales.
