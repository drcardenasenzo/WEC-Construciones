(() => {
 'use strict';
 const normalize = value => value.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/\bposos?\b/g, 'pozo').replace(/\bpozos\b/g, 'pozo').replace(/\bnegros?\b/g, 'ciego').replace(/\bciegos\b/g, 'ciego');
 const track = (placement) => {
  if (['127.0.0.1', 'localhost'].includes(window.location.hostname) || typeof window.gtag !== 'function') return;
  window.gtag('event', 'whatsapp_click', {link_placement: placement, page_path: window.location.pathname});
  if (window.wecConversion) window.gtag('event', 'conversion', {send_to: window.wecConversion, value: 1, currency: 'ARS'});
 };
 document.querySelectorAll('.wa-link').forEach(link => link.addEventListener('click', () => track(link.dataset.placement || 'content')));
 document.querySelectorAll('.contact-form').forEach(form => form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  const locality = String(data.get('localidad') || '').trim();
  const message = String(data.get('consulta') || '').trim();
  if (!locality || !message) return;
  const text = `Hola WEC. Consulto por: ${form.dataset.context}. Estoy en ${locality}. ${message}`;
  track('form');
  window.open('https://wa.me/5491126117028?text=' + encodeURIComponent(text), '_blank', 'noopener,noreferrer');
 }));
 const search = document.querySelector('#guide-search');
 if (search) {
  let category = 'Todas';
  const items = [...document.querySelectorAll('.filter-item')];
  const filters = [...document.querySelectorAll('.filter-button')];
  const update = () => {
   const words = normalize(search.value).trim().split(/\s+/).filter(Boolean);
   let count = 0;
   items.forEach(item => {
    const matches = (category === 'Todas' || item.dataset.category === category) && words.every(w => normalize(item.dataset.search).includes(w));
    item.hidden = !matches;
    if (matches) count++;
   });
   document.querySelector('.result-count').textContent = `${count} ${count === 1 ? 'guía para explorar' : 'guías para explorar'}`;
   document.querySelector('.empty-results').hidden = count > 0;
  };
  search.addEventListener('input', update);
  filters.forEach(button => button.addEventListener('click', () => {
   category = button.dataset.category;
   filters.forEach(b => {const active = b === button; b.classList.toggle('active', active);b.setAttribute('aria-pressed', String(active));});
   update();
  }));
 }
 const lightbox = document.querySelector('.lightbox');
 if (lightbox && typeof lightbox.showModal === 'function') {
  let opener;
  document.querySelectorAll('.gallery-link').forEach(link => link.addEventListener('click', event => {
   event.preventDefault();opener=link;
   const img=lightbox.querySelector('img');
   img.src=link.href;img.alt=link.querySelector('img').alt;
   lightbox.querySelector('figcaption').textContent=link.dataset.caption;
   lightbox.showModal();
  }));
  lightbox.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
  lightbox.addEventListener('click', event => {if (event.target===lightbox) {const r=lightbox.getBoundingClientRect();if(event.clientX<r.left || event.clientX>r.right || event.clientY<r.top || event.clientY>r.bottom) lightbox.close();}});
  lightbox.addEventListener('close', () => {if(opener)opener.focus();});
 }
 document.querySelectorAll('.mobile-nav a').forEach(link => link.addEventListener('click', () => link.closest('details').removeAttribute('open')));
 // Conservar enlaces viejos a secciones que ahora tienen páginas propias.
 const oldRoutes = {'#project-2':'servicios/pozos-ciegos/','#como-trabajamos':'#soluciones','#proyectos':'#soluciones','#terms':'informacion/','#inicio':'','#sobre-nosotros':'#contacto'};
 if (document.querySelector('.hero') && Object.hasOwn(oldRoutes,window.location.hash)) {
  const target=oldRoutes[window.location.hash];
  if(target.startsWith('#')) {document.querySelector(target)?.scrollIntoView();history.replaceState(null,'',target);}
  else if(target) window.location.replace(target);
 }
})();
