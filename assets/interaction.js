'use strict';
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
const number = (value, digits = 2) => value.toLocaleString(document.documentElement.lang, {
  minimumFractionDigits: digits, maximumFractionDigits: digits
});

function animateCanvas(container, paint) {
  const canvas = container.querySelector('canvas');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  const button = container.querySelector('.motion');
  let paused = reduced.matches, visible = false, frame = 0, elapsed = 0, last = 0;
  let width = 0, height = 0;
  function draw() { paint(ctx, width, height, elapsed); }
  function tick(now) {
    if (last) elapsed += Math.min(now - last, 80) / 1000;
    last = now;
    draw();
    frame = requestAnimationFrame(tick);
  }
  function sync() {
    cancelAnimationFrame(frame);
    last = 0;
    button.textContent = (paused ? '▷ ' : 'Ⅱ ') + (paused ? button.dataset.play : button.dataset.pause);
    if (visible && !document.hidden && !paused) frame = requestAnimationFrame(tick);
    else draw();
  }
  function resize() {
    const rect = canvas.getBoundingClientRect();
    const scale = Math.min(window.devicePixelRatio || 1, 2);
    width = rect.width;
    height = rect.height;
    canvas.width = Math.round(width * scale);
    canvas.height = Math.round(height * scale);
    ctx.setTransform(scale, 0, 0, scale, 0, 0);
    draw();
  }
  button.hidden = false;
  button.addEventListener('click', () => { paused = !paused; sync(); });
  reduced.addEventListener('change', () => { paused = reduced.matches; sync(); });
  document.addEventListener('visibilitychange', sync);
  new ResizeObserver(resize).observe(canvas);
  new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; sync(); }).observe(container);
  new MutationObserver(draw).observe(document.documentElement, {attributes:true, attributeFilter:['data-appearance']});
  container.addEventListener('replot', draw);
  resize(); sync();
}
function paintWave(ctx, w, h, time) {
  ctx.clearRect(0, 0, w, h);
  const light = document.documentElement.dataset.appearance === 'light';
  for (let row = 0; row < 39; row++) {
    const z = row / 38;
    const bright = row === 22;
    ctx.strokeStyle = bright ? '#ffc18d' : `hsla(${199 + 66*z},${light ? 97 : 90}%,${62+14*z}%,${.38+.43*z})`;
    ctx.lineWidth = bright ? 2.7 : 1.05;
    ctx.beginPath();
    for (let i = 0; i <= 230; i++) {
      const x = i / 230;
      const phase = 7.1*x + 3.6*z - time*.72;
      const env = .45+.55*Math.sin(Math.PI*x)**2;
      const y = h*(.51+(z-.5)*.43+env*(.18*Math.sin(phase)+.082*Math.sin(2.45*phase+.9*z)+.042*Math.sin(4*phase-z)));
      if (i) ctx.lineTo(x*w, y); else ctx.moveTo(0, y);
    }
    ctx.stroke();
  }
}
const wave = document.querySelector('[data-wave]');
if (wave) animateCanvas(wave, paintWave);

// A fixed synthetic residual with a ramp beginning at 4 s. All displayed
// crossings come from the same samples used to draw the trace.
const lab = document.querySelector('.lab');
if (lab) {
  const slider = lab.querySelector('input');
  const points = Array.from({length:601}, (_, i) => {
    const t = i / 50;
    return .12+.032*Math.sin(13*t)+.023*Math.sin(21*t)+Math.max(0,Math.min(t-4,6))*.157;
  });
  let threshold, crossing;
  function update() {
    threshold = Number(slider.value)/100;
    crossing = points.findIndex(v => v > threshold);
    const timestamp = crossing / 50;
    lab.querySelector('#level').textContent = number(threshold);
    lab.querySelector('#outcome').textContent = crossing < 0 ? lab.dataset.miss :
      lab.dataset.alarm+' · '+number(timestamp)+' s · '+(timestamp<=8 ? lab.dataset.early : lab.dataset.late);
    lab.dispatchEvent(new Event('replot'));
  }
  slider.addEventListener('input', update);
  update();
  animateCanvas(lab, (ctx,w,h,time) => {
    ctx.clearRect(0,0,w,h);
    const x = t => 31+(w-48)*t/12;
    const y = v => h-24-(h-44)*v/1.35;
    function line(x1,y1,x2,y2,color,dash=[]) {
      ctx.setLineDash(dash); ctx.strokeStyle=color; ctx.lineWidth=1;
      ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.stroke(); ctx.setLineDash([]);
    }
    ctx.direction='ltr'; ctx.font='11px monospace'; ctx.fillStyle='#c9d6ef';ctx.textAlign='center';
    for (let i=0;i<=12;i+=2) {
      line(x(i),14,x(i),h-24,'#2e3958'); ctx.fillText(i+' s',x(i),h-6);
    }
    for (const v of [0,.5,1]) {
      line(x(0),y(v),x(12),y(v),'#2e3958');ctx.fillText(v.toString(),14,y(v)+3);
    }
    line(x(0),y(threshold),x(12),y(threshold),'#a992ff',[4,3]);
    line(x(8),10,x(8),h-24,'#ffb977',[3,3]);
    ctx.strokeStyle='#7ad6ff';ctx.lineWidth=2;ctx.beginPath();
    points.forEach((v,i)=>{ if(i) ctx.lineTo(x(i/50),y(v)); else ctx.moveTo(x(0),y(v)); });ctx.stroke();
    const i=Math.floor(time*70)%points.length;
    ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(x(i/50),y(points[i]),3,0,2*Math.PI);ctx.fill();
    if(crossing>=0) {
      ctx.fillStyle='#ffc28c';ctx.beginPath();ctx.arc(x(crossing/50),y(points[crossing]),5,0,2*Math.PI);ctx.fill();
    }
  });
}
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      entry.target.classList.add('entered');
      observer.unobserve(entry.target);
    }
  }, {threshold:0});
  document.querySelectorAll('.section,.entry,.project,.subhero,.hero-copy,.instrument,.affil,.linkrow').forEach(el => observer.observe(el));
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
      const response=await fetch('/assets/search-'+document.documentElement.lang+'.json');
      if(!response.ok) throw Error(response.status);
      pages=await response.json();
    } catch {pages=fallback;}
  }
  matches();
});
input.addEventListener('input',()=>{if(pages)matches();});
