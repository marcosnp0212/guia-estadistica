<script>
(function(){
var body=document.body, guide=body.getAttribute('data-guide')||'alumna', isA=guide==='alumna';
var NS='guia-'+guide+':';
function get(k,d){try{var v=localStorage.getItem(NS+k);return v===null?d:JSON.parse(v);}catch(e){return d;}}
function set(k,v){try{if(v===null||v===false||v==='')localStorage.removeItem(NS+k);else localStorage.setItem(NS+k,JSON.stringify(v));}catch(e){}}
function el(tag,cls,html){var e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;}
function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var doc=document.querySelector('.doc');
var lvl1=[].slice.call(doc.querySelectorAll('section.level1'));
var lvl2=[].slice.call(doc.querySelectorAll('section.level2'));
function secTitle(s){var h=s.querySelector('h1,h2');if(!h)return'';var n=h.querySelector('.num'),t=h.querySelector('.ht');
  if(n)return(h.classList.contains('prac')?'Práctica ':'Ejercicio ')+n.textContent+': '+(t?t.textContent:'');return(t?t.textContent:h.textContent).trim();}
function temaOf(s){var l1=s.closest('section.level1');return l1;}
function tabOf(s){var l1=temaOf(s);if(!l1)return'';var tab=l1.querySelector('h1 .tab');return tab?tab.textContent+' · ':'';}
function goTo(target){
  var sol=target.closest('.sol');if(sol&&sol._showAll)sol._showAll();
  if(window.innerWidth<=1020){body.classList.remove('nav-open');var s=document.querySelector('.scrim');if(s)s.hidden=true;}
  var y=target.getBoundingClientRect().top+window.scrollY-84;window.scrollTo({top:y,behavior:'smooth'});
  target.classList.remove('flash');void target.offsetWidth;target.classList.add('flash');
}

/* ===== 4. Copiar fórmulas ===== */
[].slice.call(doc.querySelectorAll('code')).forEach(function(c){
  var t=c.textContent.trim();if(t.charAt(0)!=='=')return;
  c.classList.add('copy');c.setAttribute('role','button');c.setAttribute('tabindex','0');c.setAttribute('title','Copiar fórmula');c.setAttribute('aria-label','Copiar fórmula '+t);
  function copy(){
    function ok(){c.classList.add('copied');setTimeout(function(){c.classList.remove('copied');},1300);}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,fallback);}else fallback();
    function fallback(){var ta=el('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok();}catch(e){}ta.remove();}
  }
  c.addEventListener('click',copy);c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();copy();}});
});

/* ===== 1. Inténtalo primero ===== */
if(isA){
  lvl2.forEach(function(s){
    var h=s.querySelector(':scope > h2.ej');if(!h||h.classList.contains('prac')||s.querySelector('.practica,.simulacro'))return;
    var kids=[].slice.call(s.children),start=kids.indexOf(h)+1;
    var en=s.querySelector(':scope > .co-enunciado');if(en)start=kids.indexOf(en)+1;
    var rest=kids.slice(start);if(!rest.length)return;
    var groups=[],cur=null;
    rest.forEach(function(k){
      var attach=cur&&(k.classList.contains('tw')||k.tagName==='FIGURE'||(k.tagName==='P'&&(k.querySelector('math[display="block"]')||(k.querySelector('img')&&!k.textContent.trim()))));
      if(cur&&!attach){var last=cur[cur.length-1];if(last.tagName==='P'&&/:\s*$/.test(last.textContent))attach=true;}
      if(attach)cur.push(k);else{cur=[k];groups.push(cur);}
    });
    var sol=el('div','sol');var ctl=el('div','sol-ctl');
    s.insertBefore(ctl,rest[0]);s.insertBefore(sol,ctl.nextSibling);
    groups.forEach(function(g){var w=el('div','step');g.forEach(function(k){w.appendChild(k);});sol.appendChild(w);});
    var steps=[].slice.call(sol.children),shown=0;
    ctl.innerHTML='<p class="sol-msg">Inténtalo primero en Excel. Cuando quieras, mira la solución paso a paso o entera.</p><div class="sol-btns"><button type="button" class="btn btn-next"></button><button type="button" class="btn ghost btn-all">Ver toda la solución</button><button type="button" class="btn ghost btn-hide" hidden>Ocultar solución</button></div>';
    var bn=ctl.querySelector('.btn-next'),ba=ctl.querySelector('.btn-all'),bh=ctl.querySelector('.btn-hide'),msg=ctl.querySelector('.sol-msg');
    function render(){
      steps.forEach(function(st,i){st.hidden=i>=shown;});
      sol.classList.toggle('open',shown>0);
      var done=shown>=steps.length;
      bn.hidden=done;ba.hidden=done;bh.hidden=shown===0;
      bn.textContent=shown===0?'Ver el primer paso':'Ver el siguiente paso ('+(shown+1)+' de '+steps.length+')';
      msg.textContent=shown===0?'Inténtalo primero en Excel. Cuando quieras, mira la solución paso a paso o entera.':(done?'Solución completa.':'Vas por el paso '+shown+' de '+steps.length+'. Intenta el siguiente antes de verlo.');
    }
    bn.addEventListener('click',function(){shown=Math.min(shown+1,steps.length);render();var st=steps[shown-1];if(st&&st.getBoundingClientRect().bottom>window.innerHeight)st.scrollIntoView({block:'nearest',behavior:'smooth'});});
    ba.addEventListener('click',function(){shown=steps.length;render();});
    bh.addEventListener('click',function(){shown=0;render();goTo(h);});
    sol._showAll=function(){shown=steps.length;render();};
    render();
  });
}

/* ===== 2 y 10. Pie de cada apartado: progreso + notas ===== */
var tocA={};[].slice.call(document.querySelectorAll('.toc a')).forEach(function(a){tocA[decodeURIComponent(a.getAttribute('href').slice(1))]=a;});
function noteCount(){var n=0;lvl2.concat(lvl1).forEach(function(s){if(get('nota:'+s.id,''))n++;});return n;}
var notesBtnCount;
function makeFoot(s,withCheck){
  var f=el('div','sec-foot');var isEj=!!s.querySelector(':scope > h2.ej');
  if(withCheck){
    var id='chk-'+s.id;
    var lab=el('label','done-chk');lab.innerHTML='<input type="checkbox"><span>'+(isEj?'Lo he resuelto':'Ya lo sé hacer')+'</span>';
    var cb=lab.querySelector('input');cb.checked=!!get('done:'+s.id,false);
    cb.addEventListener('change',function(){set('done:'+s.id,cb.checked);paintProgress();});
    f.appendChild(lab);
  }
  var nb=el('button','note-btn');nb.type='button';
  var wrap=el('div','note-wrap');wrap.hidden=true;
  var ta=el('textarea');ta.rows=3;ta.placeholder='Escribe aquí tus dudas o lo que quieras preguntar en la próxima sesión…';ta.value=get('nota:'+s.id,'');
  ta.setAttribute('aria-label','Mis notas de '+secTitle(s));
  wrap.appendChild(ta);
  function lbl(){var has=!!ta.value.trim();nb.innerHTML=has?'Mis notas <span class="dot" aria-hidden="true"></span>':'Añadir una nota';nb.classList.toggle('has',has);}
  nb.addEventListener('click',function(){wrap.hidden=!wrap.hidden;nb.setAttribute('aria-expanded',!wrap.hidden);if(!wrap.hidden)ta.focus();});
  var tmr;ta.addEventListener('input',function(){clearTimeout(tmr);tmr=setTimeout(function(){set('nota:'+s.id,ta.value.trim()?ta.value:'');lbl();paintNotes();},300);});
  lbl();if(ta.value.trim())wrap.hidden=false;
  f.appendChild(nb);s.appendChild(f);s.appendChild(wrap);
}
function learn(s){var l1=s.closest('section.level1');return !!(l1&&l1.querySelector(':scope > h1 .tab'));}
lvl2.forEach(function(s){makeFoot(s,isA&&learn(s));});
/* listas "Comprueba que sabes hacer" como casillas */
if(isA){lvl2.forEach(function(s){var h=s.querySelector('h2');if(!h||!/Comprueba que sabes hacer/.test(h.textContent))return;
  [].slice.call(s.querySelectorAll(':scope > ul > li')).forEach(function(li,i){var k='can:'+s.id+':'+i;var lab=el('label','can');lab.innerHTML='<input type="checkbox"> ';var cb=lab.firstChild;cb.checked=!!get(k,false);
    cb.addEventListener('change',function(){set(k,cb.checked);});while(li.firstChild)lab.appendChild(li.firstChild);li.appendChild(lab);li.classList.add('can-li');});});}

/* medidores en el índice y en la portada */
function groupKey(l1){return(l1.className.match(/\bt[0-4x]\b/)||['tx'])[0];}
function paintProgress(){
  if(!isA)return;
  var byGroup={};
  lvl1.forEach(function(l1){
    if(!l1.querySelector(':scope > h1 .tab'))return;
    var subs=[].slice.call(l1.querySelectorAll(':scope > section.level2')).filter(function(s){return !/Comprueba/.test(s.textContent.slice(0,60));});
    var done=0;subs.forEach(function(s){var d=!!get('done:'+s.id,false);if(d)done++;var a=tocA[s.id];if(a)a.classList.toggle('done',d);});
    var a=tocA[l1.id];if(a&&subs.length){a.classList.toggle('started',done>0);var m=a.querySelector('.meter');if(!m){m=el('span','meter');a.appendChild(m);}
      m.innerHTML='<span class="mbar"><span style="width:'+(done/subs.length*100)+'%"></span></span><span class="mtxt">'+done+'/'+subs.length+'</span>';
      m.setAttribute('aria-label',done+' de '+subs.length+' hechos');a.classList.toggle('all-done',done===subs.length);}
    var g=groupKey(l1);byGroup[g]=byGroup[g]||[0,0];byGroup[g][0]+=done;byGroup[g][1]+=subs.length;
  });
  [].slice.call(document.querySelectorAll('.divider')).forEach(function(d){var g=(d.className.match(/\bt[0-4]\b/)||[])[0];var v=byGroup[g];if(!v)return;
    var p=d.querySelector('.dprog');if(!p){p=el('span','dprog');d.querySelector('.dt').appendChild(p);}
    p.innerHTML='<span class="mbar"><span style="width:'+(v[1]?v[0]/v[1]*100:0)+'%"></span></span><span class="mtxt">'+(v[0]===0?'Sin empezar':(v[0]===v[1]?'¡Completado!':v[0]+' de '+v[1]+' hechos'))+'</span>';});
}
paintProgress();

/* ===== 10. Panel "Mis notas y progreso" ===== */
var dlg=el('dialog','panel');dlg.setAttribute('aria-label','Mis notas');
dlg.innerHTML='<div class="panel-head"><h2>Mis notas</h2><button type="button" class="x" aria-label="Cerrar">×</button></div><div class="panel-body"></div><div class="panel-foot">'+
 '<button type="button" class="btn btn-copy-notes">Copiar todas las notas</button>'+
 '<button type="button" class="btn ghost btn-export">Guardar copia de mi progreso</button>'+
 '<label class="btn ghost">Recuperar copia<input type="file" accept="application/json" hidden></label>'+
 '<p class="panel-note">Tus notas y tu progreso se guardan solo en este navegador. Si cambias de ordenador o borras el historial, usa la copia.</p></div>';
document.body.appendChild(dlg);
var sbFoot=el('div','sb-foot');var nbtn=el('button','btn notes-open');nbtn.type='button';sbFoot.appendChild(nbtn);document.querySelector('.sidebar').appendChild(sbFoot);
function paintNotes(){var n=noteCount();nbtn.innerHTML='Mis notas'+(n?' <span class="badge">'+n+'</span>':'');}
paintNotes();
function fillPanel(){
  var b=dlg.querySelector('.panel-body');var items=[];
  lvl1.concat(lvl2).forEach(function(s){var t=get('nota:'+s.id,'');if(t)items.push({s:s,t:t});});
  items.sort(function(a,b){return a.s.compareDocumentPosition(b.s)&2?1:-1;});
  if(!items.length){b.innerHTML='<p class="empty">Aún no tienes notas. Al final de cada apartado hay un botón «Añadir una nota» para apuntar dudas.</p>';return items;}
  b.innerHTML='';items.forEach(function(it){var d=el('div','pn');var a=el('a','',esc(tabOf(it.s)+secTitle(it.s)));a.href='#'+it.s.id;
    a.addEventListener('click',function(e){e.preventDefault();dlg.close();goTo(it.s);});d.appendChild(a);d.appendChild(el('p','',esc(it.t).replace(/\n/g,'<br>')));b.appendChild(d);});
  return items;
}
nbtn.addEventListener('click',function(){fillPanel();if(dlg.showModal)dlg.showModal();else dlg.setAttribute('open','');});
dlg.querySelector('.x').addEventListener('click',function(){dlg.close();});
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close();});
dlg.querySelector('.btn-copy-notes').addEventListener('click',function(e){var items=fillPanel();var txt=items.map(function(it){return'• '+tabOf(it.s)+secTitle(it.s)+'\n'+it.t;}).join('\n\n');
  var b=e.currentTarget;function ok(){var o=b.textContent;b.textContent='Copiadas';setTimeout(function(){b.textContent=o;},1400);}
  if(navigator.clipboard)navigator.clipboard.writeText(txt||'(sin notas)').then(ok);});
dlg.querySelector('.btn-export').addEventListener('click',function(){var data={};try{for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf(NS)===0)data[k]=localStorage.getItem(k);}}catch(e){}
  var a=el('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(data,null,1)],{type:'application/json'}));a.download='mi-progreso-'+guide+'.json';document.body.appendChild(a);a.click();a.remove();});
dlg.querySelector('input[type=file]').addEventListener('change',function(e){var f=e.target.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{var d=JSON.parse(r.result);Object.keys(d).forEach(function(k){if(k.indexOf(NS)===0)localStorage.setItem(k,d[k]);});location.reload();}catch(err){alert('Ese archivo no es una copia válida de la guía.');}};r.readAsText(f);});


/* ===== 9. Buscador ===== */
var head=document.querySelector('.sidebar-head');
var sw=el('div','search');sw.innerHTML='<input type="search" placeholder="Buscar (por ejemplo, varianza)" aria-label="Buscar en la guía"><kbd>/</kbd>';
head.parentNode.insertBefore(sw,head.nextSibling);
var si=sw.querySelector('input'),res=el('div','search-res');res.hidden=true;var toc=document.querySelector('.toc');toc.parentNode.insertBefore(res,toc);
var idx=null;function norm(s){return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');}
function build(){idx=[];[].slice.call(doc.querySelectorAll('h1,h2,h3,h4,p,li,td,th,.co-t')).forEach(function(e){
  if(e.closest('.sec-foot,.sol-ctl,.plan-cfg'))return;if(e.tagName==='P'&&e.closest('li'))return;
  var t=e.textContent.replace(/\s+/g,' ').trim();if(t.length<2)return;var s=e.closest('section.level2')||e.closest('section.level1');if(!s)return;
  idx.push({e:e,t:t,n:norm(t),s:s,w:/^H[1-4]$/.test(e.tagName)?10:(e.classList.contains('co-t')?4:1)});});}
function snip(t,q){var n=norm(t),i=n.indexOf(q[0]);var a=Math.max(0,i-50),b=Math.min(t.length,i+110);var s=(a>0?'…':'')+t.slice(a,b)+(b<t.length?'…':'');
  var out=esc(s),ns=norm(out);q.forEach(function(w){var r='',j=0,k;var lo=norm(out);while((k=lo.indexOf(w,j))>-1){r+=out.slice(j,k)+'<mark>'+out.slice(k,k+w.length)+'</mark>';j=k+w.length;}out=r+out.slice(j);});return out;}
function search(){var q=norm(si.value).split(/\s+/).filter(Boolean);
  if(!q.length){res.hidden=true;toc.hidden=false;return;}if(!idx)build();
  var hits=idx.filter(function(it){return q.every(function(w){return it.n.indexOf(w)>-1;});});
  hits.forEach(function(h){h.sc=h.w+(q.every(function(w){return new RegExp('(^|[^a-z0-9])'+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).test(h.n);})?6:0);});
  hits.sort(function(a,b){return b.sc-a.sc;});var seen={},out=[];
  hits.forEach(function(h){var k=h.s.id+'|'+h.t.slice(0,40);if(seen[k])return;seen[k]=1;out.push(h);});
  toc.hidden=true;res.hidden=false;
  if(!out.length){res.innerHTML='<p class="sr-empty">No hay resultados para «'+esc(si.value)+'». Prueba con otra palabra, por ejemplo «media» o «PENDIENTE».</p>';return;}
  res.innerHTML='<p class="sr-count">'+(out.length>40?'40 primeros de '+out.length:out.length)+' resultado'+(out.length===1?'':'s')+'</p>';
  out.slice(0,40).forEach(function(h){var a=el('a','sr');a.href='#'+h.s.id;var l1=h.s.closest('section.level1');var g=l1?groupKey(l1):'tx';a.classList.add(g);
    a.innerHTML='<span class="sr-t">'+esc(tabOf(h.s)+secTitle(h.s))+'</span><span class="sr-s">'+snip(h.t,q)+'</span>';
    a.addEventListener('click',function(e){e.preventDefault();goTo(h.e.closest('table')||h.e);});res.appendChild(a);});}
window.GuiaAPI={get:get,set:set,paint:paintProgress,goTo:goTo,secTitle:secTitle,tabOf:tabOf,esc:esc,el:el,paintNotes:paintNotes};
var st;si.addEventListener('input',function(){clearTimeout(st);st=setTimeout(search,120);});
si.addEventListener('keydown',function(e){if(e.key==='Escape'){si.value='';search();si.blur();}if(e.key==='Enter'){var f=res.querySelector('a.sr');if(f)f.click();}});
document.addEventListener('keydown',function(e){if(e.key==='/'&&!/INPUT|TEXTAREA/.test(document.activeElement.tagName)){e.preventDefault();if(window.innerWidth<=1020)document.querySelector('.nav-toggle').click();si.focus();}});
})();
</script>
