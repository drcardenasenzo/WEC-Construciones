# WEC Construcciones

Sitio estático de pozos ciegos y biodigestores, conservando el diseño original. Publicación: GitHub Pages desde `main`, carpeta raíz.

## Regenerar

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

No necesita Node, dependencias web, base de datos ni un compilador CSS. Los HTML generados se versionan para GitHub Pages.

## Contenido

- `content/articles.py`: 50 artículos, cada uno con una intención principal, secciones propias y datos para iniciar una consulta.
- `content/editorial-map.json`: mapa de URLs e intenciones generado; revisar antes de agregar artículos para evitar solapamientos.
- `content/gallery.json`: galería compartida por inicio, servicios, artículos y trabajos. Agregar allí nuevas fotos y sus descripciones, poner el archivo optimizado en `assets/` y regenerar. No inventar localidad, fecha, cliente o solución de una obra.
- `templates/home-original.txt`: portada original anterior a la reformulación. `scripts/restore_home.py` conserva su diseño y adapta únicamente contenido del rubro y acceso a artículos.
- `assets/site.css` y `assets/site.js`: diseño, filtros, galería ampliable y consultas por WhatsApp.
- `site_config.json`: teléfono, dominio canónico y etiquetas de medición.

## Dominio temporal y renovación

El dominio personalizado vencido se retiró para utilizar `https://drcardenasenzo.github.io/WEC-Construciones/`. Canonicals, enlaces compartidos y sitemap usan esa base.

Al renovar el dominio:
1. Comprobar que el DNS apunte correctamente a GitHub Pages.
2. Cambiar `base_url` en `site_config.json` por `https://www.wecconstrucciones.com.ar`.
3. Regenerar y validar.
4. Restablecer el dominio en GitHub Pages y su archivo `CNAME`; verificar HTTPS y redirecciones.
5. Revisar Search Console y enviar el sitemap del dominio restablecido.

No publicar simultáneamente dos versiones con canonicals distintos. El `robots.txt` a nivel de proyecto de GitHub Pages no sustituye al del host raíz; el sitemap sigue siendo accesible y se puede enviar directamente a Search Console.

## Medición

Los botones emiten `whatsapp_click` con ubicación del botón y ruta de página; conservan el ID de Analytics y la acción de conversión de Ads del sitio anterior. No se envían campos del formulario a Analytics. El clic es una intención de contacto, no prueba de mensaje enviado, consulta calificada ni venta. GTM no se carga además de las etiquetas directas para evitar duplicación desconocida.

## Criterio editorial

Los temas afines se conectan por enlaces; no se crean páginas clonadas por localidad. No se prometen diagnósticos a distancia, resultados o precios sin presupuesto. Las guías de biodigestores enlazan documentación de fabricante y distinguen tratamiento de disposición. La galería se identifica como trabajos anteriores, no como imágenes del caso narrado.

Se conservó sin modificar la carpeta preexistente del generador de presupuestos. No forma parte del sitemap ni de la navegación comercial.
