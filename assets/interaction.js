'use strict';
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      entry.target.classList.add('entered');
      observer.unobserve(entry.target);
    }
  }, {threshold:0});
  document.querySelectorAll('.section,.entry,.honour,.project,.subhero,.hero-copy,.affil,.linkrow').forEach(el => observer.observe(el));
}
const searchButton = document.querySelector('.search-toggle');
const dialog = document.querySelector('#search-dialog');
const input = dialog.querySelector('input');
const results = dialog.querySelector('#results');
let pages;
function matches() {
  const normalize = s => s.toLocaleLowerCase().normalize('NFKC').replace(/[يى]/g,'ی').replace(/ك/g,'ک').replace(/\u200c/g,' ');
  const terms = normalize(input.value).trim().split(/\s+/);
  results.replaceChildren();
  for (const item of pages) {
    const text = normalize(item.title+' '+item.text);
    if (!terms.every(term=>text.includes(term))) continue;
    const a = document.createElement('a'); a.href=item.url; a.textContent=item.title; results.append(a);
  }
  if (!results.childElementCount) results.textContent=results.dataset.empty;
}
searchButton.hidden=false;
searchButton.addEventListener('click',async()=>{
  dialog.showModal();input.focus();
  if(!pages) {
    const fallback = [...document.querySelectorAll('.footpages a')].map(a=>({title:a.textContent,url:a.href,text:''}));
    try {
      const response=await fetch('/assets/search-'+document.documentElement.lang+'.json?v=motion2');
      if(!response.ok) throw Error(response.status);
      pages=await response.json();
    } catch {pages=fallback;}
  }
  matches();
});
input.addEventListener('input',()=>{if(pages)matches();});

const header = document.querySelector('header');
new ResizeObserver(() => {
  document.documentElement.style.setProperty('--header-offset', (header.offsetHeight + 14) + 'px');
}).observe(header);
