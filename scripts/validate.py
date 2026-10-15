#!/usr/bin/env python3
"""Comprueba publicación, rutas internas y requisitos del contenido."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'content'))
from articles import ARTICLES
from faq import FAQ
from related import RELATIONS
assert set(RELATIONS)==set(range(50))
assert set(j for related in RELATIONS.values() for j in related)==set(range(50))
for i, related in RELATIONS.items():
 assert len(related)==len(set(related))==3 and i not in related
assert set(FAQ)=={a['slug'] for a in ARTICLES}
BASE=json.loads((ROOT/'site_config.json').read_text())['base_url'].rstrip('/')
errors=[]
class Doc(HTMLParser):
 def __init__(self,text):
  super().__init__(); self.links=[];self.ids=set();self.headings=0;self.canonical=[];self.image_alts=[];self.wa=0;self.schema=[];self.in_schema=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='h1':self.headings+=1
  if tag in ['a','link','script','img']:
   val=a.get('href') if tag in ['a','link'] else a.get('src')
   if val is not None:self.links.append(val)
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if tag=='img' and 'alt' not in a:self.image_alts.append(a)
  if tag=='a' and 'wa.me/' in a.get('href',''):self.wa+=1
  if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True
 def handle_endtag(self,tag):
  if tag=='script':self.in_schema=False
 def handle_data(self,data):
  if self.in_schema:self.schema.append(json.loads(data))
files=[ROOT/'index.html',*ROOT.glob('guias/**/index.html'),*ROOT.glob('servicios/**/index.html'),ROOT/'trabajos/index.html',ROOT/'zonas/index.html',ROOT/'informacion/index.html']
for f in files:
 try:d=Doc(f.read_text())
 except Exception as e:errors.append(f'{f}: HTML/schema {e}');continue
 rel=f.relative_to(ROOT).as_posix().removesuffix('index.html')
 if d.headings!=1:errors.append(f'{rel}: H1 count {d.headings}')
 if d.canonical!=[BASE+'/'+rel]:errors.append(f'{rel}: canonical {d.canonical}')
 if not d.wa:errors.append(f'{rel}: WhatsApp missing')
 if d.image_alts:errors.append(f'{rel}: alt missing')
 for link in d.links:
  u=urlparse(link)
  if u.scheme or u.netloc:continue
  if not u.path:
   if u.fragment and unquote(u.fragment) not in d.ids:errors.append(f'{rel}: missing anchor {link}')
   continue
  target=(f.parent/unquote(u.path)).resolve()
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{rel}: broken link {link}')
  if u.fragment and target.suffix=='.html' and target.exists() and unquote(u.fragment) not in Doc(target.read_text()).ids:errors.append(f'{rel}: broken target anchor {link}')
article_files=list(ROOT.glob('guias/*/index.html'))
assert len(article_files)==50
assert len({a['title'] for a in ARTICLES})==50
for f in article_files:
 text=f.read_text()
 if 'class="button floating wa-link"' not in text:errors.append(f'{f.name}: floating WhatsApp missing')
 if 'Trabajos realizados.' not in text:errors.append(f'{f.name}: gallery missing')
 if text.count('class="gallery-link"')!=4:errors.append(f'{f.name}: photo count')
 if text.count('class="guide-card"')!=3:errors.append(f'{f.name}: related guides count')
urls=ET.parse(ROOT/'sitemap.xml').getroot()
assert len(urls)==len(files), (len(urls),len(files))
words=[sum(len(t.split()) for t in [a['intro'],*[p for h,p in a['sections']],*a['check'],FAQ[a['slug']][1]]) for a in ARTICLES]
print(f'{len(files)} páginas; {len(article_files)} artículos; {min(words)}–{max(words)} palabras propias por artículo, sin navegación ni galería.')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('OK: rutas internas, anclas, canónicas, JSON-LD, H1, galería y contacto.')
