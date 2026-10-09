# RADAL 1.2 para Android

APK universal: `Radal-1.2-android.apk`, paquete `cl.seguelstudios.radal`, versión visible 1.2. Requiere Android 5.0/API 21 o posterior. Descarga desde el release v1.2; autoriza la instalación desde el navegador o gestor de archivos si Android lo solicita y abre RADAL. Se juega en horizontal. El botón Menú abre guardado, carga, historial y opciones. Las listas se desplazan arrastrándolas.

Compilado con Ren’Py 8.5.3, RAPT oficial, JDK 21 y SDK Android 36. La historia y los recursos son los mismos de v1.2. `game/android_ui.rpy` añade ayuda táctil y tamaños móviles; `sueno_visual.rpy` ajusta únicamente los márgenes/tamaño de letra en pantallas pequeñas.

La clave de firma está en `android.keystore` y su respaldo local en `respaldo-clave-android-v1.2/`. Ambos están excluidos de Git y de las distribuciones. Conserva esa clave para instalar futuras actualizaciones sobre este APK. No se publicó ninguna clave de firma.

Para recompilar, instala el soporte RAPT oficial y Java 21. Usa el proyecto local que conserva la clave y ejecuta el comando `android_build` del launcher de Ren’Py, indicando el proyecto y una carpeta de destino. No cambies el identificador de paquete ni la clave al actualizar.

Documentación oficial: https://www.renpy.org/doc/html/android.html
