<script>
/* Navegación por pantallas (solo guía de la alumna): barra superior con pestañas,
   una pantalla cada vez y un desplegable para saltar a cualquier apartado. */
(function(){
if(document.body.getAttribute('data-guide')!=='alumna')return;
var A=window.GuiaAPI;if(!A)return;var get=A.get,set=A.set,esc=A.esc,el=A.el;
var body=document.body,doc=document.querySelector('.doc'),main=document.querySelector('main'),hero=document.querySelector('.hero');
function byId(id){return id?document.getElementById(id):null;}

/* ---- 1. Mapa de la guía ---- */
var TEMAS=[
  {n:1,t:'Una variable',a:'tema-1.-análisis-descriptivo-de-una-variable',e:'boletín-de-ejercicios-de-los-temas-1-y-2-resuelto',p:'prácticas-de-los-temas-1-y-2',c:'comprueba-que-sabes-hacer-tema-1'},
  {n:2,t:'Dos variables',a:'tema-2.-análisis-descriptivo-de-dos-variables',e:'boletín-de-ejercicios-de-los-temas-1-y-2-resuelto',p:'prácticas-de-los-temas-1-y-2',c:'comprueba-que-sabes-hacer-tema-2'},
  {n:3,t:'Regresión y correlación',a:'tema-3.-regresión-y-correlación',e:'boletín-del-tema-3-resuelto',p:'prácticas-del-tema-3',c:'comprueba-que-sabes-hacer-tema-3'},
  {n:4,t:'Números índices',a:'tema-4.-números-índices',e:'boletín-del-tema-4-resuelto',p:'prácticas-del-tema-4',c:'comprueba-que-sabes-hacer-tema-4'}];
var EXAM=[['Repaso exprés','repaso-exprés-el-examen-en-pocos-días'],['Examen modelo','examen-modelo-de-la-profesora'],['Simulacros','simulacros-de-examen']];
var TOOLS=[
  ['Índice completo','indice','Todos los apartados de la guía, para ir directamente a cualquiera.','M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01'],
  ['Chuleta de fórmulas','chuleta-de-fórmulas','Todas las fórmulas de los cuatro temas en una página.','M6 3h12v18H6zM9 8h6M9 12h6M9 16h3'],
  ['Traductor de enunciados','qué-me-están-pidiendo-traductor-de-enunciados','Buscas la frase del enunciado y te dice qué cálculo toca.','M4 5h16v11H9l-5 4zM9 10h6'],
  ['Lista para el examen','lista-para-el-examen','Qué revisar antes de entregar.','M5 12l4 4L19 6'],
  ['Números y calculadora','parte-0.-repaso-de-base-números-y-calculadora','Porcentajes, fracciones, potencias y el sumatorio, desde cero.','M6 3h12v18H6zM9 7h6v3H9zM9 14h1M13 14h1M9 17h1M13 17h1'],
  ['Excel desde cero','parte-0-bis.-excel-desde-cero','Celdas, fórmulas, funciones y para qué sirve el $.','M4 4h16v16H4zM4 10h16M10 4v16'],
  ['Descargas','descargas','Los archivos de Excel de la guía.','M12 4v11M7 10l5 5 5-5M5 20h14'],
  ['Si el examen fuera con ordenador','por-si-el-examen-fuera-con-ordenador','Simulacros con Excel y qué archivos llevar.','M3 5h18v12H3zM8 21h8'],
  ['Cómo usar esta guía','cómo-usar-esta-guía','Qué hay en cada parte y cómo estudiar con ella.','M12 8v.01M11 12h1v5h1M12 3a9 9 0 1 0 0 18a9 9 0 0 0 0-18z']];
var PLAN='plan-de-estudio';
var L1=[].slice.call(doc.querySelectorAll(':scope > section.level1'));
function pagesOf(l1){var p=[].slice.call(l1.querySelectorAll(':scope > section.level2'));return p.length?p:[l1];}
function zoneOf(l1){var id=l1.id,z={k:'tools'};
  TEMAS.forEach(function(t){if(id===t.a||id===t.e||id===t.p)z={k:'tema'};});
  EXAM.forEach(function(x){if(id===x[1])z={k:'exam'};});
  if(id===PLAN)z={k:'plan'};return z;}
function temasOf(l1){return TEMAS.filter(function(t){return l1.id===t.a||l1.id===t.e||l1.id===t.p;});}
function titleOf(s){var h=s.querySelector(':scope > h1,:scope > h2');if(!h)return'';var ht=h.querySelector('.ht');
  if(s.classList.contains('level2')){var sn=h.querySelector('.secnum');return((sn?sn.textContent+'. ':'')+A.secTitle(s)).replace(/\s+/g,' ').trim();}return(ht?ht.textContent:h.textContent).replace(/\s+/g,' ').trim();}
function toolName(id){var t=TOOLS.filter(function(x){return x[1]===id;})[0];return t?t[0]:null;}

/* ---- 2. Barra superior ---- */
body.classList.add('tabs-mode');
var ICON=function(d,fill){return'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="'+(fill?'currentColor':'none')+'" stroke="'+(fill?'none':'currentColor')+'" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="'+d+'"/></svg>';};
/* la barra viene ya escrita en la página (tbar_alumna.html), para que se vea desde el primer momento */
var bar=document.querySelector('.tbar');
var lb=bar.querySelector('.tb-lang');if(lb)lb.addEventListener('click',function(e){e.preventDefault();var to=lb.getAttribute('data-to'),u=window.guiaLangUrl&&window.guiaLangUrl(to);
  try{localStorage.setItem('guia-lang',to);}catch(x){}if(u)location.href=u+location.hash;});
/* buscador: se mueve del índice lateral a la barra */
var sp=bar.querySelector('.tb-search'),sw=document.querySelector('.sidebar .search'),sr=document.querySelector('.sidebar .search-res');
if(sw)sp.appendChild(sw);if(sr)sp.appendChild(sr);
var sbtn=bar.querySelector('.tb-search-b');
function openSearch(o){if(o===undefined)o=true;sp.hidden=!o;sbtn.setAttribute('aria-expanded',o);if(o){var i=sp.querySelector('input');if(i)setTimeout(function(){i.focus();},0);}}
sbtn.addEventListener('click',function(){openSearch(sp.hidden);});
sp.addEventListener('click',function(e){if(e.target.closest('a.sr'))openSearch(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!sp.hidden)openSearch(false);});
document.addEventListener('click',function(e){if(!sp.hidden&&!e.target.closest('.tbar'))openSearch(false);});
/* notas: el botón de la barra abre el mismo panel */
var nb=document.querySelector('.notes-open'),nd=bar.querySelector('.tb-dot');
bar.querySelector('.tb-notes-b').addEventListener('click',function(){if(nb)nb.click();});
function paintDot(){if(nb&&nd)nd.hidden=!nb.querySelector('.badge');}
if(A.paintNotes){var opn=A.paintNotes;A.paintNotes=function(){opn.apply(this,arguments);paintDot();};}
document.addEventListener('input',function(e){if(e.target.closest&&e.target.closest('.note-wrap'))setTimeout(paintDot,400);});paintDot();

/* ---- 3. Cabecera y pie de cada pantalla ---- */
var head=el('div','pg-head');main.insertBefore(head,doc);
var foot=el('nav','pg-foot');foot.setAttribute('aria-label','Anterior y siguiente');main.insertBefore(foot,doc.nextSibling);
var tools=el('section','tools-scr');
tools.innerHTML='<h1 class="pg-h1">Herramientas</h1><p class="pg-lede">Para tener a mano mientras estudias.</p><div class="tl-list">'+
  TOOLS.map(function(t){return'<a class="tl" href="#'+t[1]+'"><span class="tl-ic">'+ICON(t[3])+'</span><span><b>'+t[0]+'</b><small>'+t[2]+'</small></span></a>';}).join('')+'</div>';
main.insertBefore(tools,doc);
var idx=el('section','idx-scr');main.insertBefore(idx,doc);
function idxGroup(l1){var z=zoneOf(l1).k,ts=temasOf(l1);
  if(z==='tema'){var part=ts[0].a===l1.id?'Aprender':(ts[0].e===l1.id?'Ejercicios resueltos':'Practica');var who=ts.length>1?'Temas 1 y 2':'Tema '+ts[0].n;return{z:'Temas',name:part==='Aprender'?who+'. '+ts[0].t:part+', '+who,cls:'t'+ts[ts.length-1].n};}
  if(z==='exam')return{z:'Examen',name:EXAM.filter(function(x){return x[1]===l1.id;})[0][0]};
  if(z==='plan')return{z:'Herramientas',name:'Mi plan'};
  return{z:'Herramientas',name:toolName(l1.id)||titleOf(l1)};}
function paintIndex(){
  var order=['Temas','Examen','Herramientas'],by={};
  L1.forEach(function(l1){var g=idxGroup(l1);(by[g.z]=by[g.z]||[]).push({l1:l1,g:g});});
  idx.innerHTML='<h1 class="pg-h1">Índice</h1><p class="pg-lede">Todos los apartados de la guía. Pulsa cualquiera para ir directamente.</p>'+
    order.filter(function(z){return by[z];}).map(function(z){
      return'<h2 class="idx-z">'+z+'</h2><div class="idx-cols" data-m>'+by[z].map(function(it){var ps=pagesOf(it.l1),dn=ps.filter(isDone).length;
        return'<div class="idx-b '+(it.g.cls||'')+'"><a class="idx-h" href="#'+esc(it.l1.id)+'">'+esc(it.g.name)+(ps.length>1&&dn?'<small>'+dn+' de '+ps.length+'</small>':'')+'</a>'+
          (ps.length>1?'<ul>'+ps.map(function(p){return'<li><a href="#'+esc(p.id)+'"'+(isDone(p)?' class="done"':'')+'>'+itemInner(p)+(isDone(p)?'<span class="pj-ok">Hecho</span>':'')+'</a></li>';}).join('')+'</ul>':'')+'</div>';}).join('')+'</div>';}).join('');
  masonry();}
/* reparte los bloques en columnas: cada uno va a la columna más corta, así no quedan huecos */
function masonry(){var w=idx.clientWidth||window.innerWidth,n=w>=1300?3:(w>=760?2:1);
  [].forEach.call(idx.querySelectorAll('.idx-cols[data-m]'),function(c){
    var bs=[].slice.call(c.querySelectorAll('.idx-b'));c.innerHTML='';var cols=[];
    for(var i=0;i<Math.min(n,bs.length);i++){var d=el('div','idx-col');c.appendChild(d);cols.push(d);}
    bs.forEach(function(b){var m=cols.reduce(function(a,x){return x.offsetHeight<a.offsetHeight?x:a;},cols[0]);m.appendChild(b);});});}
var rz;window.addEventListener('resize',function(){if(curZone!=='index')return;clearTimeout(rz);rz=setTimeout(paintIndex,200);});


function tabsHtml(list,cur){return'<nav class="pg-tabs" aria-label="Partes">'+list.map(function(x){return'<a href="#'+x[1]+'"'+(x[1]===cur?' class="on" aria-current="page"':'')+'>'+x[0]+'</a>';}).join('')+'</nav>';}
/* nombre y número de cada pantalla, para el desplegable y el índice */
function numOf(p){if(!p.classList.contains('level2'))return'';var h=p.querySelector(':scope > h2');if(!h)return'';var n=h.querySelector('.secnum,.num');return n?n.textContent.trim():'';}
function nameOf(p){var h=p.querySelector(':scope > h1,:scope > h2');if(!h)return'';var t=h.querySelector('.ht');return(t?t.textContent:h.textContent).replace(/^✔\s*/,'').replace(/\s+/g,' ').trim();}
function isDone(p){return !!get('done:'+p.id,false);}
function itemInner(p){var n=numOf(p);return(n?'<span class="pj-n">'+esc(n)+'</span>':'')+'<span class="pj-t">'+esc(nameOf(p))+'</span>';}
var CHEV='<svg class="pj-chev" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>';
function jumpHtml(l1,page){var ps=pagesOf(l1);if(ps.length<2)return'';
  return'<div class="pg-jump"><button type="button" class="pj-btn" aria-haspopup="listbox" aria-expanded="false"><span class="pj-lab">Apartado</span><span class="pj-cur">'+itemInner(page)+'</span>'+CHEV+'</button>'+
    '<ul class="pj-list" role="listbox" aria-label="Apartados" hidden>'+ps.map(function(p){var on=p===page;
      return'<li role="option" tabindex="-1" data-id="'+esc(p.id)+'" aria-selected="'+on+'"'+(on?' class="on"':'')+'>'+itemInner(p)+(isDone(p)?'<span class="pj-ok" title="Hecho">Hecho</span>':'')+'</li>';}).join('')+'</ul></div>';}
function bindJump(root){var w=root.querySelector('.pg-jump');if(!w)return;var b=w.querySelector('.pj-btn'),ul=w.querySelector('.pj-list'),lis=[].slice.call(ul.children);
  function open(o){ul.hidden=!o;b.setAttribute('aria-expanded',o);w.classList.toggle('open',o);
    if(o){var c=ul.querySelector('li.on')||lis[0];c.focus();ul.scrollTop=c.offsetTop-ul.clientHeight/2+c.offsetHeight/2;}}
  function pick(li){open(false);go(li.getAttribute('data-id'));}
  b.addEventListener('click',function(){open(ul.hidden);});
  b.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();open(true);}});
  lis.forEach(function(li,i){li.addEventListener('click',function(){pick(li);});
    li.addEventListener('keydown',function(e){
      if(e.key==='ArrowDown'){e.preventDefault();(lis[i+1]||li).focus();}
      else if(e.key==='ArrowUp'){e.preventDefault();(lis[i-1]||li).focus();}
      else if(e.key==='Home'){e.preventDefault();lis[0].focus();}else if(e.key==='End'){e.preventDefault();lis[lis.length-1].focus();}
      else if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(li);}
      else if(e.key==='Escape'){e.preventDefault();open(false);b.focus();}else if(e.key==='Tab')open(false);});});
  document.addEventListener('click',function(e){if(!ul.hidden&&!w.contains(e.target))open(false);});}
function curTema(l1){var ts=temasOf(l1);if(ts.length===1)return ts[0];var n=get('nav:tema',1);return ts.filter(function(t){return t.n===n;})[0]||ts[0];}
function flowOf(l1){var z=zoneOf(l1).k;
  if(z==='tema'){var t=curTema(l1);return[t.a,t.e,t.p];}
  if(z==='exam')return EXAM.map(function(x){return x[1];});return[l1.id];}
function paintHead(l1,page){
  var z=zoneOf(l1).k,h='';
  if(z==='tema'){var t=curTema(l1),isC=page.id===t.c;
    var tab=isC?t.c:(l1.id===t.a?t.a:l1.id);
    h='<div class="pg-temas">'+TEMAS.map(function(x){return'<a class="ptm t'+x.n+(x.n===t.n?' on':'')+'" href="#tema:'+x.n+'"'+(x.n===t.n?' aria-current="true"':'')+'>Tema '+x.n+'</a>';}).join('')+'</div>'+
      '<h1 class="pg-h1">'+esc(t.t)+'</h1>'+
      tabsHtml([['Aprender',t.a],['Ejercicios resueltos',t.e],['Practica',t.p],['¿Lo sé hacer?',t.c]],tab)+jumpHtml(l1,page);
    head.style.setProperty('--c','var(--t'+t.n+')');}
  else if(z==='exam'){h='<h1 class="pg-h1">Examen</h1><p class="pg-lede">En papel: 30 preguntas tipo test y 10 de respuesta corta.</p>'+tabsHtml(EXAM,l1.id)+jumpHtml(l1,page);head.style.removeProperty('--c');}
  else if(z==='plan'){h='<h1 class="pg-h1">Mi plan</h1>';head.style.removeProperty('--c');}
  else{h='<a class="pg-back" href="#herramientas">Herramientas</a><h1 class="pg-h1">'+esc(toolName(l1.id)||titleOf(l1))+'</h1>'+jumpHtml(l1,page);head.style.removeProperty('--c');}
  head.innerHTML=h;head.hidden=false;
  bindJump(head);
  /* pie: anterior y siguiente, también entre partes del mismo tema o del examen */
  var ps=pagesOf(l1),i=ps.indexOf(page),fl=flowOf(l1),k=fl.indexOf(l1.id),prev=null,next=null;
  if(i>0)prev=ps[i-1];else if(k>0){var pl=byId(fl[k-1]);if(pl){var pp=pagesOf(pl);prev=pp[pp.length-1];}}
  if(i<ps.length-1)next=ps[i+1];else if(k>-1&&k<fl.length-1){var nl=byId(fl[k+1]);if(nl)next=pagesOf(nl)[0];}
  foot.innerHTML=(prev?'<a class="pf-prev" href="#'+esc(prev.id)+'"><small>Anterior</small>'+esc(short(prev))+'</a>':'<span></span>')+
                 (next?'<a class="pf-next" href="#'+esc(next.id)+'"><small>Siguiente</small>'+esc(short(next))+'</a>':'');
  foot.hidden=!(prev||next);
}
function partName(l1){var t=curTema(l1);return l1.id===t.e?'Ejercicios resueltos':(l1.id===t.p?'Practica':'Aprender');}
function l1Of(p){return p.classList.contains('level1')?p:p.closest('section.level1');}
function short(p){var t=titleOf(p),l1=l1Of(p);if(l1===curL1)return t;var z=zoneOf(l1).k,n=null;
  if(z==='tema')n=partName(l1);else if(z==='exam')n=EXAM.filter(function(x){return x[1]===l1.id;})[0][0];
  return n?n+(p===l1?'':': '+t):t;}

/* ---- 4. Mostrar una pantalla ---- */
var curL1=null,curPage=null,curZone='home';
function setZone(z){curZone=z;[].forEach.call(bar.querySelectorAll('.tb-tabs a'),function(a){var on=a.getAttribute('data-z')===z;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
  body.classList.toggle('at-home',z==='home');body.classList.toggle('at-tools',z==='tools-index');body.classList.toggle('at-index',z==='index');var ib=bar.querySelector('.tb-idx');if(ib)ib.classList.toggle('on',z==='index');}
function hideAll(){L1.forEach(function(s){s.classList.remove('cur');});head.hidden=true;foot.hidden=true;}
function showHome(){hideAll();curL1=curPage=null;setZone('home');paintResume();}
function showIndex(){hideAll();curL1=curPage=null;setZone('index');paintIndex();}
function showTools(){hideAll();curL1=curPage=null;setZone('tools-index');[].forEach.call(bar.querySelectorAll('.tb-tabs a'),function(a){a.classList.toggle('on',a.getAttribute('data-z')==='tools');});}
function locate(t){if(!t||!doc.contains(t))return null;var l1=t.closest('section.level1');if(!l1)return null;
  var p=t;while(p&&p.parentNode!==l1)p=p.parentNode;var ps=pagesOf(l1);
  var page=(p&&p.tagName==='SECTION'&&p.classList.contains('level2'))?p:ps[0];return{l1:l1,page:page};}
function showPage(l1,page){
  L1.forEach(function(s){s.classList.toggle('cur',s===l1);});
  [].forEach.call(l1.querySelectorAll(':scope > section.level2'),function(s){s.classList.toggle('cur',s===page);});
  l1.classList.toggle('later',pagesOf(l1)[0]!==page);
  var z=zoneOf(l1).k;setZone(z);
  if(z==='tema'){var ts=temasOf(l1);if(ts.length===1)set('nav:tema',ts[0].n);set('nav:t'+curTema(l1).n,page.id);}
  if(z==='exam')set('nav:exam',page.id);
  if(z==='tema'||z==='exam')set('last',page.id);
  curL1=l1;curPage=page;paintHead(l1,page);
}
/* llamada desde goTo (features.js): muestra la pantalla del destino; 'top' = ir arriba del todo */
function show(t){var r=locate(t);if(!r){if(t===hero||(t&&hero&&hero.contains(t))){showHome();return'top';}return;}
  var same=r.l1===curL1&&r.page===curPage;showPage(r.l1,r.page);
  var id=t.id||r.page.id;if(decodeURIComponent(location.hash.slice(1))!==id)history.pushState(null,'','#'+id);
  if(t===r.page||t===r.l1)return'top';if(!same)window.scrollTo(0,0);}
function offset(){return bar.offsetHeight+16;}
function route(id,push){
  if(push)history.pushState(null,'','#'+id);
  if(!id||id==='inicio'){showHome();window.scrollTo(0,0);return;}
  if(id==='herramientas'){showTools();window.scrollTo(0,0);return;}
  if(id==='indice'){showIndex();window.scrollTo(0,0);return;}
  if(id==='temas'||/^tema:\d$/.test(id)){var n=id==='temas'?get('nav:tema',1):+id.split(':')[1];set('nav:tema',n);
    var t=TEMAS.filter(function(x){return x.n===n;})[0]||TEMAS[0];var last=byId(get('nav:t'+t.n,null));var tg=last&&locate(last)&&temasOf(locate(last).l1).some(function(x){return x.n===t.n;})?last:byId(t.a);
    history.replaceState(null,'','#'+tg.id);A.goTo(tg);return;}
  if(id==='examen'){var e=byId(get('nav:exam',null))||byId(EXAM[0][1]);history.replaceState(null,'','#'+e.id);A.goTo(e);return;}
  var t2=byId(id);if(t2)A.goTo(t2);else showHome();
}
function go(id){route(id,true);}
function fromHash(){route(decodeURIComponent(location.hash.slice(1)));}
window.addEventListener('hashchange',fromHash);window.addEventListener('popstate',fromHash);
window.GuiaNav={show:show,offset:offset,openSearch:function(){openSearch(true);},go:go};

/* ---- 5. Portada: seguir donde lo dejaste ---- */
function paintResume(){var r=hero&&hero.querySelector('.resume');if(!r)return;var l=byId(get('last',null));
  if(!l){r.hidden=true;return;}var lc=locate(l);if(!lc){r.hidden=true;return;}
  var z=zoneOf(lc.l1).k,where=z==='tema'?'Tema '+curTema(lc.l1).n+', '+titleOf(lc.page):(z==='exam'?'Examen, '+titleOf(lc.page):titleOf(lc.page));
  r.innerHTML='<a class="btn" href="#'+esc(l.id)+'">Seguir donde lo dejaste</a><span>'+esc(where)+'</span>';r.hidden=false;}

(function(){var ok=function(e){return e&&e.nodeType===1&&/\bco-(truco|ojo|excel|idea)\b/.test(e.className)&&!e.closest('.co-row');};
  [].forEach.call(doc.querySelectorAll('.co-truco,.co-ojo,.co-excel,.co-idea'),function(e){if(!ok(e)||ok(e.previousElementSibling))return;
    var run=[e],n=e.nextElementSibling;while(ok(n)){run.push(n);n=n.nextElementSibling;}if(run.length<2)return;
    var row=el('div','co-row');e.parentNode.insertBefore(row,e);run.forEach(function(x){row.appendChild(x);});});})();
if(hero)[].forEach.call(hero.querySelectorAll('.divider'),function(d){var m=d.className.match(/\bt([1-4])\b/);if(m)d.addEventListener('click',function(){set('nav:tema',+m[1]);},true);});
fromHash();document.documentElement.classList.remove('pre-route');
})();
</script>
