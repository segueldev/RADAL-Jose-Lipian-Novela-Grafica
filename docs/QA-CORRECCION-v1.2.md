# Corrección de RADAL 1.2 — 9 de octubre de 2026

El bloqueo al confirmar el nombre provenía de una llamada a `renpy.escape`, que no existe en Ren’Py 8.5.3. Se reemplazó por el tratamiento de llaves que usa el motor para texto literal, conservando el nombre vacío por defecto. Las pruebas anteriores no recorrían ese formulario real: esta revisión sí lo hace desde Comenzar hasta el mapa.

Se amplió la visita con Martín y Héctor con tres opciones, notas en el cuaderno y consecuencias al cierre. Martín sí viajó a China. El recuerdo del liceo respeta que el protagonista llegó después. Se ajustaron encuadres de ambos profesores, posición de Martín durante las opciones y avisos de música para que no tapen rostros ni el aviso de consecuencias.

## Verificación

- Revisión general: 99 casos existentes de contenido aprobados, incluidos finales, DLC, decisiones, Portal Temuco, Pequi, mapas y efectos. En el primer recorrido, nueve pruebas nuevas de profesores fallaron por la sincronización del guion de pruebas; se corrigió esa sincronización y se repitieron todas las ramas.
- Inicio real en escritorio: 13 casos y 37 comprobaciones aprobados. Incluye los ocho comienzos, nombre vacío, espacios, acentos, llaves y corchetes, y disponibilidad de las funciones del motor utilizadas.
- Profesores en escritorio: 16 casos y 63 comprobaciones aprobados, con las nueve combinaciones de decisiones y seis balances finales. Capturas revisadas de opciones, tres retratos y Jeep.
- Interfaz móvil simulada: 31 casos y 103 comprobaciones aprobados entre inicio real, profesores y controles de ayuda, guardado y carga.
- Paquete Linux definitivo extraído: 13 casos y 37 comprobaciones aprobados usando su propio motor, desde Comenzar hasta el mapa. La copia de prueba recibió los guiones de QA; el archivo distribuido no los incluye.
- Lint definitivo: sin errores informados. 1.465 bloques de diálogo, 56 menús, 98 imágenes y 35 pantallas.
- Windows y Linux contienen las cinco fuentes corregidas exactas. APK contiene el mismo código compilado comprobado. Los tres paquetes no incluyen partidas, guiones de QA ni claves de firma.
- APK firmado con el mismo certificado anterior; código interno Android 13 y versión visible 1.2, para permitir actualizar la instalación anterior. No es una versión 1.3.
- Las ventanas de pruebas se ejecutan una por vez y se cierran automáticamente al terminar.

## Límites

Windows no se ejecutó en un equipo Windows. La interfaz Android se probó mediante la variante táctil del motor; el APK corregido aún requiere una prueba en un teléfono físico. Estas pruebas cubren los recorridos indicados, no garantizan ausencia absoluta de errores. Una instalación sin progreso previo inicia con 0/7 y Lucho pendiente; actualizar conserva progreso existente.

## Archivos definitivos

| Archivo | SHA-256 |
|---|---|
| Radal-1.2-win.zip | `6cdf33c74df927a6efc6a5b582c4d8c8ed4ec799c2ee317e3ec30d7ad65d2a13` |
| Radal-1.2-linux.tar.bz2 | `04ce034fba87edb6417cb062a573492fc8d373e290325c2357c6c0051b098b00` |
| Radal-1.2-android.apk | `9e652b29dffd6f8433f68f36f3ac2484bed6e900fec3c4fc05d18c8958af3754` |

Certificado Android SHA-256: `91c633e06213981e8fe356be8fabcbbd5e19a95c6d02e501430bfb27f5746ab2`.
