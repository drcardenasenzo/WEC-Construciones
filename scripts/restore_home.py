"""Conserva el HTML/CSS y las interacciones de la portada anterior a la reformulación."""
from pathlib import Path
import re,html
ROOT=Path(__file__).resolve().parents[1]
def render_home(config):
 s=(ROOT/'templates/home-original.txt').read_text()
 base=config['base_url'].rstrip('/')
 s=s.replace('https://www.wecconstrucciones.com.ar',base)
 # Sólo se adapta contenido al rubro; no se reemplazan composición, tipografía ni animaciones.
 s=s.replace('Pozos Ciegos, excavaciones y limpieza integral de tejas','Pozos Ciegos y Biodigestores')
 s=s.replace('Pozos Ciegos, excavaciones y limpieza integral de tejados','Pozos Ciegos y Biodigestores')
 s=s.replace('Pozos Ciegos, excavaciones y limpieza integral de tajados','Pozos Ciegos y Biodigestores')
 s=s.replace('pozos ciegos, excavaciones y limpieza integral de tejados','pozos ciegos, biodigestores y cámaras sanitarias')
 s=s.replace('pozos ciegos, en excavaciones y en limpieza integral de tejados','pozos ciegos, biodigestores y cámaras sanitarias')
 s=s.replace('Realizamos excavaciones, pozos ciegos y limpieza integral de tejas.','Construimos pozos ciegos e instalamos biodigestores en CABA y GBA.')
 s=s.replace('Excavaciones en CABA y GBA','Biodigestores en CABA y GBA')
 s=s.replace('Con retiro de tierra incluido.','Instalación y conexiones según tu terreno.')
 s=s.replace('Realizamos limpieza integral de tejas','Cámaras y conexiones sanitarias')
 s=s.replace('Le damos nueva vida a la fachada de tu casa.','Una instalación pensada para tu vivienda.')
 s=s.replace("background-image:url('foto3.jpg')","background-image:url('servicio2-1.jpg')")
 s=s.replace('href="#sobre-nosotros" class="text-gray-700 hover:text-[#FF6600] px-3 py-2 rounded-md text-md font-medium">Sobre Nosotros','href="guias/" class="text-gray-700 hover:text-[#FF6600] px-3 py-2 rounded-md text-md font-medium">Artículos')
 s=s.replace('href="#sobre-nosotros" class="block px-3 py-2 rounded-md text-base font-medium close-menu-link">Sobre Nosotros','href="guias/" class="block px-3 py-2 rounded-md text-base font-medium close-menu-link">Artículos')
 s=s.replace('>Excavaciones</h3>','>Biodigestores</h3>')
 s=s.replace('Realizamos todo tipo de movimientos de suelos. Excavaciones para piscinas, nivelación de la tierra, para zanjados, etc.','Instalación de biodigestores, conexiones y evaluación de la disposición del efluente para tu vivienda.')
 s=s.replace('>Limpieza de tejados</h3>','>Cámaras y conexiones</h3>')
 s=s.replace('Realizamos el servicio integral de limpieza de tejados para darle nueva vida a la fachada de tu casa.','Cámaras sanitarias y conexiones para acompañar el funcionamiento de pozos ciegos y biodigestores.')
 s=s.replace('src="servicio3.jpg"','src="servicio2.jpg"')
 s=re.sub(r'Desde \$[\d.]+','Consultar presupuesto',s)
 s=s.replace('Construcción de Horno de Barro Tradicional','Cámara sanitaria de un trabajo anterior')
 s=s.replace('Construcción de Muro de Contención','Cámara y conexiones sanitarias')
 s=s.replace('Horno de barro recién construido','Vista de un trabajo de pozo ciego')
 s=s.replace('Detalle de la boca del horno de barro','Interior de un pozo ciego revestido')
 s=s.replace('Horno de barro terminado listo para usar','Pozo ciego durante la obra')
 s=s.replace('Construcción de Pozo Ciego Standard','Excavación y preparación del terreno')
 # Los modales conservan su estructura gráfica, con contenido del servicio correspondiente.
 for number,title,description in [
  (1,'Instalación de biodigestores en CABA y GBA','Evaluamos el lugar y el uso de la vivienda para coordinar la instalación del biodigestor, las conexiones y la disposición del efluente. Antes de comprar el equipo, conviene revisar su capacidad, el acceso y las condiciones del terreno. El presupuesto detalla materiales, tareas y terminaciones según el caso.'),
  (3,'Cámaras y conexiones sanitarias','Realizamos cámaras y conexiones dentro de la obra sanitaria de tu vivienda. Se evalúan los recorridos, el acceso para mantenimiento y los componentes del sistema. Consultanos con tu localidad, fotos generales y una descripción de lo que necesitás para definir el alcance del trabajo.')]:
  start=s.index(f'<section id="project-{number}"');end=s.index('</section>',start)
  block=s[start:end]
  block=re.sub(r'(<h2[^>]*>).*?(</h2>)',lambda m:m[1]+title+m[2],block,count=1,flags=re.S)
  block=re.sub(r'(<div class="prose max-w-none">).*?(</div>)',lambda m:m[1]+'<h3 class="text-2xl font-semibold text-[#CC5200] mb-4">Descripción Detallada</h3><p class="text-gray-600 mb-4 text-justify">'+description+'</p><p class="text-gray-600 mb-4 text-justify">Escribinos por WhatsApp y te orientamos con el presupuesto para tu proyecto.</p>'+m[2],block,count=1,flags=re.S)
  if number==3:
   for i in range(1,4):block=block.replace(f'servicio3-{i}.jpg',f'servicio2-{i}.jpg')
   block=re.sub(r'alt="[^"]*"', 'alt="Foto de un trabajo sanitario anterior de WEC"',block)
  s=s[:start]+block+s[end:]
 s=s.replace('sobre%20el%20horno%20de%20barro','sobre%20pozos%20ciegos')
 s=s.replace('sobre%20el%20pozo%20ciego%20est%C3%A1ndar','sobre%20biodigestores')
 s=s.replace('sobre%20el%20muro%20de%20contenci%C3%B3n','sobre%20c%C3%A1maras%20sanitarias')
 s=s.replace('Las excavaciones dependen del tamaño de excavación a realizar. Los pozos ciegos suelen demorar 3 días hábiles. Mientras que la limpieza de tejados dependerá de que tan grande sea el mismo y en el estado en el que se encuentre.','El plazo depende del terreno, el acceso y el alcance del trabajo. Lo coordinamos al preparar el presupuesto.')
 s=s.replace('No aplica para la limpieza de tejados ni para las excavaciones por no corresponder.','Las condiciones del trabajo y del equipo se detallan en el presupuesto correspondiente.')
 s=s.replace('excavación, pozo ciego o tejado renovado','sistema sanitario').replace('entregamos la sistema sanitario','entregamos el sistema sanitario')
 # La galería y los artículos se suman al final con las mismas tarjetas y colores existentes.
 from urllib.parse import quote
 import sys
 sys.path.insert(0,str(ROOT/'content'))
 from articles import ARTICLES
 pics=''.join(f'<a href="assets/{html.escape(p["file"])}" class="gallery-link" data-caption="{html.escape(p["caption"])}" aria-label="Ampliar foto: {html.escape(p["caption"])}"><img src="assets/{html.escape(p["file"])}" alt="{html.escape(p["alt"])}" class="w-full h-56 object-cover rounded-lg shadow-md" loading="lazy"></a>' for p in __import__('json').loads((ROOT/'content/gallery.json').read_text()))
 featured=['pozo-ciego-desmoronado','cuanto-cuesta-pozo-ciego','precio-instalacion-biodigestor']
 cards=''.join(f'<a class="block bg-white rounded-xl shadow-xl border border-gray-100 p-6 card-hover-effect" href="guias/{a["slug"]}/"><h3 class="text-xl font-semibold text-[#CC5200] mb-3 text-center">{html.escape(a["title"])}</h3><p class="text-gray-600 text-sm mb-4">{html.escape(a["intro"].split(". ")[0])}.</p><span class="btn-secondary block w-fit mx-auto rounded-lg">Leer artículo</span></a>' for a in ARTICLES if a['slug'] in featured)
 addition=f'<section id="articulos" class="py-16 md:py-24 bg-gray-50"><div class="container mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8"><h2 class="text-3xl md:text-4xl font-bold text-[#CC5200] mb-4 text-center">Artículos sobre pozos ciegos y biodigestores</h2><p class="text-lg text-center text-gray-600 mb-12">Respuestas a problemas concretos y consultas frecuentes.</p><div class="grid md:grid-cols-3 gap-8">{cards}</div><div class="text-center mt-10"><a href="guias/" class="btn-primary inline-block">Ver los 50 artículos</a></div></div></section><section id="trabajos" class="py-16 md:py-24 bg-white"><div class="container mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8"><h2 class="text-3xl md:text-4xl font-bold text-[#CC5200] mb-4 text-center">Trabajos realizados</h2><p class="text-lg text-center text-gray-600 mb-12">Fotos reales de trabajos anteriores de WEC.</p><div class="grid grid-cols-2 lg:grid-cols-4 gap-6">{pics}</div></div></section>'
 s=s.replace('<footer id="main-footer"',addition+'\n<footer id="main-footer"')
 # El CDN estándar no procesa @apply dentro de style; se concretan esas reglas originales.
 applies={
 'bg-[#FF6600] text-white font-semibold py-3 px-8 rounded-lg shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300 ease-in-out;':'background:#FF6600;color:white;font-weight:600;padding:.75rem 2rem;border-radius:.5rem;box-shadow:0 4px 6px #0002;transition:all .3s;',
 'bg-[#CC5200] text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300 ease-in-out text-sm;':'background:#CC5200;color:white;font-weight:600;padding:.5rem 1rem;border-radius:.5rem;box-shadow:0 4px 6px #0002;transition:all .3s;font-size:.875rem;',
 'text-3xl md:text-4xl font-bold text-center mb-4 text-[#CC5200];':'font-size:2rem;font-weight:700;text-align:center;margin-bottom:1rem;color:#CC5200;',
 'text-lg text-center text-gray-600 mb-12;':'font-size:1.125rem;text-align:center;color:#4b5563;margin-bottom:3rem;',
 'transition-all duration-300 ease-in-out relative z-10;':'transition:all .3s;position:relative;z-index:10;',
 'bg-[#FF6600] text-white font-semibold py-3 px-8 rounded-lg shadow-md transition-all duration-300 ease-in-out;':'background:#FF6600;color:white;font-weight:600;padding:.75rem 2rem;border-radius:.5rem;box-shadow:0 4px 6px #0002;transition:all .3s;'}
 for rule,css in applies.items():s=s.replace('@apply '+rule,css)
 # Un único H1: se conserva la apariencia de las demás diapositivas.
 first=True
 def headings(m):
  nonlocal first
  if first:first=False;return m[0]
  return m[0].replace('<h1','<h2').replace('</h1>','</h2>')
 s=re.sub(r'<h1\b.*?</h1>',headings,s,flags=re.S)
 s=s.replace('<body class="bg-white overflow-x-hidden">','<body class="bg-white overflow-x-hidden"><a href="#inicio" class="sr-only focus:not-sr-only">Saltar al contenido</a>')
 # Sin redirección adicional de medición al pulsar WhatsApp.
 s=s.replace('window.location = url;','/* El enlace abre WhatsApp sin duplicar la navegación. */')
 s=s.replace('id="mobile-menu-button"','id="mobile-menu-button" aria-label="Abrir menú" aria-expanded="false"')
 s=s.replace("mobileMenuButton.querySelector('.hamburger').classList.toggle('open');","mobileMenuButton.querySelector('.hamburger').classList.toggle('open');\n                    mobileMenuButton.setAttribute('aria-expanded',String(mobileMenu.classList.contains('active')));")
 s=s.replace('height: 300px;', 'height: 300px;')
 s=s.replace('</head>','<link rel="stylesheet" href="assets/home-additions.css?v=2"></head>')
 s=s.replace('</body>','<dialog class="lightbox" aria-label="Foto de trabajo realizado"><button class="lightbox-close" type="button" aria-label="Cerrar foto">Cerrar ×</button><figure><img alt=""><figcaption></figcaption></figure></dialog><script defer src="assets/site.js?v=2"></script></body>')
 return '\n'.join(line.rstrip() for line in s.splitlines())+'\n'
