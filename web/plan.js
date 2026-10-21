<script>
(function(){
if(document.body.getAttribute('data-guide')!=='alumna')return;
var A=window.GuiaAPI;if(!A)return;var get=A.get,set=A.set,esc=A.esc,el=A.el;
var doc=document.querySelector('.doc');var app=doc.querySelector('.plan-app');
var DIAS=['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'],DC=['L','M','X','J','V','S','D'],DCI=[1,2,3,4,5,6,0];
var MES=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
function parseD(s){if(!s)return null;var p=s.split('-');return new Date(+p[0],+p[1]-1,+p[2]);}
function iso(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function today(){var n=new Date();return new Date(n.getFullYear(),n.getMonth(),n.getDate());}
function fmt(d){return DIAS[d.getDay()].toLowerCase()+' '+d.getDate()+' '+MES[d.getMonth()];}
function words(s){return (s.textContent||'').split(/\s+/).length;}
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}

/* ---- 1. Unidades de estudio, sacadas de la propia guía ---- */
function buildUnits(){
  var groups=[],cur=null,base=[],exam=[];
  [].slice.call(doc.querySelectorAll(':scope > section.level1')).forEach(function(l1){
    var tab=l1.querySelector(':scope > h1 .tab');if(!tab)return;
    var t=tab.textContent.trim(),ht=(l1.querySelector(':scope > h1 .ht')||{}).textContent||'';
    var temas=((t+' '+ht).match(/\d+/g)||[]).map(Number);
    var kind=/^Tema/.test(t)?'teo':(/^Bolet/.test(t)?'ej':(/^Pr[aá]ct/.test(t)?'prac':(/^Parte/.test(t)?'base':(/^Examen/.test(t)?'exam':'otro'))));
    var secs=[].slice.call(l1.querySelectorAll(':scope > section.level2'));
    var us=[];
    secs.forEach(function(s){
      var title=(A.tabOf(s)+A.secTitle(s)).replace(/\s+/g,' ').trim();
      if(kind==='prac'){var box=s.querySelector('.practica');if(!box)return;var tipo=box.getAttribute('data-tipo');
        [1,2,3].forEach(function(l){us.push({id:s.id+'#'+l,sec:s,lvl:l,title:title+' · nivel '+l,min:l===1?25:20,kind:'prac',done:function(){return !!get('pr-done:'+tipo+':'+l,false);}});});return;}
      if(kind==='exam'){var sim=s.querySelector('.simulacro');
        if(sim){var sid=sim.getAttribute('data-sim');us.push({id:s.id,sec:s,title:title,min:100,kind:'sim',big:true,paper:/papel/i.test(title),done:function(){return !!get('sim-res:'+sid,null);}});}
        else if(s.querySelector('.testsim')){var tsid=s.querySelector('.testsim').getAttribute('data-sim');us.push({id:s.id,sec:s,title:title,min:100,kind:'sim',big:true,paper:true,done:function(){return !!get('ts-res:'+tsid,null);}});}
        else us.push({id:s.id,sec:s,title:title,min:25,kind:'exq',done:function(){return !!get('done:'+s.id,false);}});return;}
      var w=words(s),min=kind==='ej'?clamp(Math.round(w/22),8,30):clamp(Math.round(w/28),8,40);
      if(/^comprueba-que-sabes/.test(s.id))min=10;
      us.push({id:s.id,sec:s,title:title,min:min,kind:kind,done:function(){return !!get('done:'+s.id,false);}});
    });
    us.forEach(function(u){u.temas=temas;});
    if(kind==='base'){base=base.concat(us);return;}
    if(kind==='exam'){exam=exam.concat(us);return;}
    if(kind==='otro')return;
    if(!cur){cur={teo:[],pr:[],temas:[]};groups.push(cur);}
    if(kind==='teo')cur.teo=cur.teo.concat(us);else cur.pr=cur.pr.concat(us);
    temas.forEach(function(x){if(cur.temas.indexOf(x)<0)cur.temas.push(x);});
    if(kind==='prac')cur=null;
  });
  return{groups:groups,base:base,exam:exam};
}
var U=buildUnits();
/* ---- 1b. Plan exprés: siempre el mismo contenido; solo cambia cuánto toca cada día ---- */
var XID='repaso-exprés-el-examen-en-pocos-días';
var XP={1:{vid:35,ej:['boletín-de-ejercicios-de-los-temas-1-y-2-resuelto',[[2,15],[5,15],[14,20],[22,15],[19,10]]],mod:['tipo-test-tema-1-preguntas-1-a-10','1 a 10',40]},
  2:{vid:10,rep:20,ej:['boletín-de-ejercicios-de-los-temas-1-y-2-resuelto',[[18,20]]],mod:['tipo-test-tema-2-preguntas-11-a-15','11 a 15',20]},
  3:{vid:15,rep:30,ej:['boletín-del-tema-3-resuelto',[[1,20],[6,15],[8,10]]],mod:['tipo-test-tema-3-preguntas-16-a-23','16 a 23',30]},
  4:{vid:15,rep:30,ej:['boletín-del-tema-4-resuelto',[[1,15],[8,15],[9,20],[10,20]]],mod:['tipo-test-tema-4-preguntas-24-a-30','24 a 30',30]}};
function byId(id){return document.getElementById(id);}
function ejOf(l1id,n){var l1=byId(l1id);if(!l1)return null;return [].slice.call(l1.querySelectorAll(':scope > section.level2')).filter(function(s){return s.id.indexOf('ejercicio-'+n+'.')===0;})[0]||null;}
function canDone(s){var cs=s?s.querySelectorAll('label.can input'):[];return cs.length>0&&[].every.call(cs,function(x){return x.checked;});}
function weakS4(){
  var S=((window.GUIA_DATA||{}).tests||{}).S4;if(!S||!get('ts-res:S4',null))return null;var a=get('ts:S4',null)||{mc:{}};
  var by={},bad={};
  S.tests.forEach(function(q,i){var t=q.tema;by[t]=by[t]||[0,0];by[t][1]++;
    if(a.mc[i]===q.ok)by[t][0]++;else{bad[t]=bad[t]||[];var w=String(q.where).split(' ')[0];if(bad[t].indexOf(w)<0)bad[t].push(w);}});
  var t=Object.keys(by).sort(function(x,y){return by[x][0]/by[x][1]-by[y][0]/by[y][1];})[0];
  return{t:+t,ok:by[t][0],n:by[t][1],where:(bad[t]||[]).sort()};
}
function xpBlocks(temas){
  var R=byId(XID);if(!R)return null;
  var rs=[].slice.call(R.querySelectorAll(':scope > section.level2')).filter(function(s){return /^tema-\d/.test(s.id);});
  var out=[];
  function add(k,sec,title,min,auto){if(!sec)return;var id='xp:'+k;
    out.push({id:id,sec:sec,title:title,min:min,kind:'xp',auto:auto||null,done:function(){return !!get(id,false)||(!!auto&&auto());}});}
  function dn(s){return function(){return !!get('done:'+s.id,false);};}
  var how=byId('cómo-es-el-examen');add('how',how,'Examen modelo · Cómo es el examen',5,how&&dn(how));
  [1,2,3,4].filter(function(t){return !temas||temas.indexOf(t)>-1;}).forEach(function(t){
    var X=XP[t],r=rs[t-1],v=doc.querySelector('.video[data-v="t'+t+'"]'),T='Tema '+t+' · ';
    if(v&&!v.id)v.id='video-t'+t;
    add('v'+t,v,T+'Vídeo (puedes ponerlo a 1,25×)',X.vid);
    if(t===1&&r){var h3=r.querySelectorAll(':scope > section.level3');
      add('r1a',h3[0]||r,T+'Repaso: variables, centro y dispersión',25);
      add('r1b',h3[3]||r,T+'Repaso: cuartiles y caja, forma y grupos',20);}
    else add('r'+t,r,T+'Repaso: lo imprescindible',X.rep);
    var c=byId('comprueba-que-sabes-hacer-tema-'+t);add('c'+t,c,T+'¿Lo sé hacer? Marca lo que ya sabes',t===1?10:5,function(){return canDone(c);});
    X.ej[1].forEach(function(e){var s=ejOf(X.ej[0],e[0]);if(s)add('e'+t+'-'+e[0],s,T+A.secTitle(s).replace(/\s+/g,' ').trim(),e[1],dn(s));});
    var m=byId(X.mod[0]);add('m'+t,m,T+'Examen modelo, preguntas '+X.mod[1],X.mod[2],m&&dn(m));
  });
  var P=byId('respuesta-corta-p1-a-p10');add('p',P,'Examen modelo · Respuesta corta, P1 a P10',35,P&&dn(P));
  var Q=byId('preguntas-de-excel-sin-ordenador');add('x',Q,'Preguntas de Excel sin ordenador',30,Q&&dn(Q));
  var S=byId('simulacro-tipo-test');
  add('s',S,'Simulacro tipo test, con reloj (90 minutos de una sentada)',90,function(){return !!get('ts-res:S4',null);});
  add('sc',S,'Corrige el simulacro: lee la explicación de cada fallo',40);
  var w=weakS4();
  add('rf',w?(rs[w.t-1]||S):S,w?'Refuerzo: Tema '+w.t+' ('+w.ok+' de '+w.n+' en el simulacro)'+(w.where.length?'. Repasa '+(w.where.length>1?'los apartados ':'el apartado ')+w.where.join(', '):''):'Refuerzo del tema que peor te salga en el simulacro',30);
  return out;
}
function trapItem(key){var s=byId('las-15-trampas-del-test');if(!s)return null;var id='xp:tr:'+key;
  return{id:id,sec:s,title:'Las 15 trampas, tapando la respuesta',min:10,kind:'xp',done:function(){return !!get(id,false);}};}
/* reparte en n días seguidos, sin partir tareas ni cambiar el orden */
function xpSplit(items,n){
  var plan=[];for(var i=0;i<n;i++)plan.push([]);if(!n)return plan;
  var total=items.reduce(function(a,u){return a+u.min;},0),target=total/n,cum=0;
  items.forEach(function(u){var di=Math.min(n-1,Math.floor((cum+u.min/2)/Math.max(1,target)));plan[di].push(u);cum+=u.min;});
  return plan;
}
function hm(m){m=Math.round(m/5)*5;var h=Math.floor(m/60),r=m%60;return h?h+' h'+(r?' '+String(r).padStart(2,'0')+' min':''):r+' min';}
var ALLTEMAS=[];U.groups.forEach(function(g){g.temas.forEach(function(t){if(t>0&&ALLTEMAS.indexOf(t)<0)ALLTEMAS.push(t);});});ALLTEMAS.sort(function(a,b){return a-b;});

/* ---- 2. Configuración ---- */
function cfg(){var c=get('plan:cfg',null)||{};
  if(!c.days)c.days=[0,1,2,3,4,5,6];if(!c.temas)c.temas=ALLTEMAS.slice();if(c.base===undefined)c.base=false;return c;}
function saveCfg(c){set('plan:cfg',c);}

/* ---- 3. Reparto ---- */
function interleave(teo,pr){
  var out=[],n=teo.length,m=pr.length,j=0;
  for(var i=0;i<n;i++){out.push(teo[i]);while(j<m&&(j+1)/m<=(i+1)/n){out.push(pr[j]);j++;}}
  while(j<m){out.push(pr[j]);j++;}return out;
}
function xpSchedule(seq,days,E,S,info){
  var t0=today(),pend=seq.filter(function(u){return !u.done();});
  var res={days:[],seq:seq,pend:pend,doneN:seq.length-pend.length,E:E,S:S,repaso:null,perDay:0,extra:[],expres:true,info:info};
  if(!days.length)return res;
  var isT=+days[0]===+t0,snap=get('xp:hoy',null),fixed=[];
  if(isT&&snap&&snap.d===iso(t0))fixed=seq.filter(function(u){return snap.k.indexOf(u.id)>-1;});
  else if(isT){snap=null;}
  var rest=pend.filter(function(u){return fixed.indexOf(u)<0;}),plan;
  if(fixed.length)plan=days.length>1?[fixed].concat(xpSplit(rest,days.length-1)):[fixed.concat(rest)];
  else{plan=xpSplit(rest,days.length);if(isT){snap={d:iso(t0),k:plan[0].map(function(u){return u.id;}),tr:res.doneN>0};set('xp:hoy',snap);}}
  res.days=plan.map(function(items,i){
    var tr=(i>0||(isT&&snap&&snap.tr))&&items.length?trapItem(iso(days[i])):null;if(tr)items=[tr].concat(items);
    return{date:days[i],items:items,min:items.reduce(function(a,u){return a+u.min;},0)};});
  var left=res.days.reduce(function(a,d){return a+d.items.filter(function(u){return !u.done();}).reduce(function(b,u){return b+u.min;},0);},0);
  res.perDay=Math.round(left/days.length);
  return res;
}
function planMode(c){return c.mode||(c.full?'full':'auto');}
function schedule(){
  var c=cfg(),E=parseD(c.exam);if(!E)return null;
  var S=parseD(c.start)||today();var t0=today();if(S<t0)S=t0;
  var days=[];for(var d=new Date(S);d<E;d.setDate(d.getDate()+1)){if(c.days.indexOf(d.getDay())>-1)days.push(new Date(d));}
  var inc=function(u){return u.temas.some(function(x){return c.temas.indexOf(x)>-1;});};
  var seq=[];
  if(c.base)seq=seq.concat(U.base);
  U.groups.forEach(function(g){var teo=g.teo.filter(inc),pr=g.pr.filter(inc);seq=seq.concat(interleave(teo,pr));});
  var nTem=c.temas.length;
  U.exam.forEach(function(u){if(u.kind==='exq'||nTem>=Math.min(3,ALLTEMAS.length))seq.push(u);});
  /* el alumno elige el plan; si no ha elegido, se recomienda el exprés cuando el completo pasa de 3 h al día */
  var xs=xpBlocks(c.temas)||[],xseq=(c.base?U.base:[]).concat(xs);
  function left(q){return q.filter(function(u){return !u.done();}).reduce(function(a,u){return a+u.min;},0);}
  var info={rec:xs.length&&(!days.length||left(seq)/days.length>180)?'xp':'full',mode:planMode(c),hFull:left(seq),hXp:left(xseq)};
  var expres=xs.length>0&&(info.mode==='auto'?info.rec:info.mode)==='xp';
  if(expres)return xpSchedule(xseq,days,E,S,info);
  var pend=seq.filter(function(u){return !u.done();}),doneN=seq.length-pend.length;
  var res={days:[],seq:seq,pend:pend,doneN:doneN,E:E,S:S,repaso:null,perDay:0,extra:[],expres:false,info:info};
  if(!days.length)return res;
  if(days.length>=4&&!expres){res.repaso=days.pop();}
  var bigs=pend.filter(function(u){return u.big;}),norm=pend.filter(function(u){return !u.big;});
  bigs.sort(function(x,y){return (y.paper?1:0)-(x.paper?1:0);});
  var bigDays=Math.min(bigs.length,Math.max(days.length>=3?1:0,Math.floor(days.length/4)));res.extra=bigs.slice(bigDays);bigs=bigs.slice(0,bigDays);var nd=days.length-bigDays;
  var total=norm.reduce(function(a,u){return a+u.min;},0),target=total/Math.max(1,nd);res.perDay=Math.round(target);
  var plan=days.map(function(d){return{date:d,items:[],min:0};});
  var cum=0;norm.forEach(function(u){var mid=cum+u.min/2;var di=Math.min(nd-1,Math.floor(mid/target));plan[di].items.push(u);plan[di].min+=u.min;cum+=u.min;});
  bigs.forEach(function(u,k){var di=nd+k;plan[di].items.push(u);plan[di].min+=u.min;});
  res.days=plan;return res;
}

/* ---- 4. Pintar ---- */
function itemHtml(u){var d=u.done(),ck='';
  if(u.kind==='xp'){var au=!!(u.auto&&u.auto());ck='<label class="pl-chk" title="'+(au?'Hecho en la guía':'Márcalo cuando lo termines')+'"><input type="checkbox" data-x="'+esc(u.id)+'"'+(d?' checked':'')+(au?' disabled':'')+' aria-label="Hecho: '+esc(u.title)+'"></label>';}
  return'<li class="pl-it'+(d?' done':'')+(ck?' xp':'')+'">'+ck+'<a href="#'+u.sec.id+'" data-u="'+esc(u.id)+'">'+esc(u.title)+'</a><span class="pl-min">'+u.min+' min</span></li>';}
function allItems(r){var a=r.seq.slice();(r.days||[]).forEach(function(d){d.items.forEach(function(u){if(a.indexOf(u)<0)a.push(u);});});return a;}
function bindLinks(root,r){var all=allItems(r);function find(id){return all.filter(function(x){return x.id===id;})[0];}
  [].forEach.call(root.querySelectorAll('a[data-u]'),function(a){a.addEventListener('click',function(e){e.preventDefault();
  var u=find(a.getAttribute('data-u'));if(!u)return;
  if(u.lvl){var b=u.sec.querySelector('.practica');if(b&&b._setLevel)b._setLevel(u.lvl);}A.goTo(u.sec);});});
  [].forEach.call(root.querySelectorAll('input[data-x]'),function(x){x.addEventListener('change',function(){set(x.getAttribute('data-x'),x.checked);paint();});});}
var moreOpen=false;
function paint(){
  var c=cfg(),r=schedule();
  if(app){
    var cur=r?(r.expres?'xp':'full'):(planMode(c)==='full'?'full':'xp');
    var h='<div class="pl-cfg">'+
      '<div class="pl-q"><span class="pl-n">1</span><label class="pl-qt" for="pl-exam">¿Cuándo es tu examen?</label><div class="pl-qa"><input type="date" id="pl-exam" class="pl-exam" value="'+(c.exam||'')+'"></div></div>'+
      '<div class="pl-q"><span class="pl-n">2</span><span class="pl-qt">¿Qué días puedes estudiar?</span><div class="pl-qa chips">'+DCI.map(function(d,i){return'<button type="button" class="chip'+(c.days.indexOf(d)>-1?' on':'')+'" data-day="'+d+'" aria-pressed="'+(c.days.indexOf(d)>-1)+'" aria-label="'+DIAS[d]+'">'+DC[i]+'</button>';}).join('')+'</div></div>'+
      '<div class="pl-q"><span class="pl-n">3</span><span class="pl-qt">¿Qué plan quieres?</span><div class="pl-qa pl-pick">'+[['xp','Exprés','Lo imprescindible de cada tema: vídeo, repaso exprés, ejercicios clave y examen modelo. Al final, el simulacro.'],['full','Completo','Toda la guía: la teoría entera, todos los ejercicios del boletín, las prácticas y los simulacros.']].map(function(m){
        return'<button type="button" class="pl-opt'+(cur===m[0]?' on':'')+'" data-mode="'+m[0]+'" aria-pressed="'+(cur===m[0])+'"><b>'+m[1]+(r&&r.info.rec===m[0]?' <em>recomendado</em>':'')+'</b>'+m[2]+(r?' Te quedan unas '+hm(m[0]==='xp'?r.info.hXp:r.info.hFull)+'.':'')+'</button>';}).join('')+'</div></div>'+
      '<details class="pl-more"'+(moreOpen?' open':'')+'><summary>Más opciones</summary>'+
      '<div class="pl-row"><label>Empiezo otro día <span class="opt">(si no, hoy)</span><input type="date" class="pl-start" value="'+(c.start||'')+'"></label></div>'+
      '<div class="pl-row"><span class="pl-lab">Qué entra</span><div class="chips">'+ALLTEMAS.map(function(t){return'<button type="button" class="chip'+(c.temas.indexOf(t)>-1?' on':'')+'" data-tema="'+t+'" aria-pressed="'+(c.temas.indexOf(t)>-1)+'">Tema '+t+'</button>';}).join('')+
      '<button type="button" class="chip'+(c.base?' on':'')+'" data-base="1" aria-pressed="'+c.base+'">Repaso de números</button></div></div></details></div>';
    if(!r){h+='<p class="pl-empty">Pon el día del examen y aquí aparecerá tu plan, día a día.</p>';}
    else{
      var left=r.pend.length,tot=r.seq.length;
      h+='<div class="pl-sum"><div class="meter"><span style="width:'+(tot?Math.round(r.doneN/tot*100):0)+'%"></span></div><p>Llevas <b>'+r.doneN+' de '+tot+'</b> tareas. Faltan <b>'+Math.max(0,Math.round((r.E-today())/864e5))+'</b> días para el examen'+(r.days.length?'; te salen unos <b>'+(r.expres?hm(r.perDay):r.perDay+' minutos')+'</b> por día de estudio'+(r.expres?', sin contar los descansos.':'.'):'.')+'</p>'+
                (r.expres?(r.days.length===1?'<p class="pl-warn"><b>Solo te queda un día.</b> No da para todo con calma. Sigue el orden de la lista: cada tarea que hagas suma.</p>':(r.perDay>300?'<p class="pl-warn"><b>Son días largos.</b> Parte cada día en tres tandas (mañana, tarde y noche), con bloques de 25 minutos y un descanso largo entre tandas.</p>':'')):(r.perDay>150?'<p class="pl-warn"><b>Son muchos minutos al día.</b> Si no te da, elige el plan <b>Exprés</b>. Si prefieres seguir con el completo, añade días de estudio o marca como hecho lo que ya sepas hacer («Ya lo sé hacer»): el plan se reparte solo con lo que queda.</p>':''))+'</div>';
      if(r.extra&&r.extra.length)h+='<p class="pl-note">No caben todos los simulacros. Si te sobra tiempo, haz también: '+r.extra.map(function(u){return'<a href="#'+u.sec.id+'" data-u="'+esc(u.id)+'">'+esc(u.title.replace(/^Examen · /,''))+'</a>';}).join(', ')+'.</p>';
      if(!left)h+='<p class="pl-empty">¡Lo tienes todo hecho! Repasa la chuleta y repite el simulacro que peor te saliera.</p>';
      var t0=today();
      h+='<ol class="pl-days">'+r.days.filter(function(d){return d.items.length;}).map(function(d){var isT=+d.date===+t0;
        return'<li class="pl-day'+(isT?' is-today':'')+'"><div class="pl-dh"><span class="pl-date">'+(isT?'Hoy · ':'')+fmt(d.date)+'</span><span class="pl-m">'+(r.expres?hm(d.min):d.min+' min')+'</span></div><ul>'+d.items.map(itemHtml).join('')+'</ul></li>';}).join('')+
        (r.expres?'<li class="pl-day pl-rep"><div class="pl-dh"><span class="pl-date">'+fmt(r.E)+' · examen</span><span class="pl-m">15 min</span></div><ul><li class="pl-it"><a href="#las-15-trampas-del-test">Por la mañana, una última vuelta a las 15 trampas. Nada nuevo.</a></li></ul></li>':'')+
        (r.repaso?'<li class="pl-day pl-rep'+(+r.repaso===+t0?' is-today':'')+'"><div class="pl-dh"><span class="pl-date">'+fmt(r.repaso)+'</span><span class="pl-m">repaso</span></div><ul><li class="pl-it"><a href="#chuleta-de-fórmulas">Nada nuevo: lee la chuleta y las listas de comprobación. Duerme bien.</a></li></ul></li>':'')+'</ol>';
    }
    app.innerHTML=h;
    app.querySelector('.pl-exam').addEventListener('change',function(e){var c=cfg();c.exam=e.target.value;saveCfg(c);paint();});
    app.querySelector('.pl-start').addEventListener('change',function(e){var c=cfg();c.start=e.target.value;saveCfg(c);paint();});
    var md=app.querySelector('.pl-more');if(md)md.addEventListener('toggle',function(){moreOpen=md.open;});
    [].forEach.call(app.querySelectorAll('.chip,.pl-opt'),function(b){b.addEventListener('click',function(){var c=cfg();
      if(b.hasAttribute('data-day')){var d=+b.getAttribute('data-day'),i=c.days.indexOf(d);if(i>-1){if(c.days.length>1)c.days.splice(i,1);}else c.days.push(d);}
      else if(b.hasAttribute('data-tema')){var t=+b.getAttribute('data-tema'),j=c.temas.indexOf(t);if(j>-1){if(c.temas.length>1)c.temas.splice(j,1);}else c.temas.push(t);}
      else if(b.hasAttribute('data-mode')){c.mode=b.getAttribute('data-mode');delete c.full;}
      else c.base=!c.base;saveCfg(c);paint();});});
    if(r)bindLinks(app,r);
  }
  paintToday(r);
}
function paintToday(r){
  var box=document.querySelector('.today');if(!box)return;var h;
  if(!r){h='<p class="td-k">Tu plan de estudio</p><p class="td-t">¿Cuándo es el examen? Ponlo y la guía te dirá qué toca cada día.</p><label class="td-in">Examen el <input type="date" class="td-exam"></label>';}
  else{var t0=today(),d=r.days.filter(function(x){return +x.date===+t0&&x.items.length;})[0];
    if(r.repaso&&+r.repaso===+t0)h='<p class="td-k">Hoy, '+fmt(t0)+'</p><p class="td-t">Repaso final: nada nuevo. Lee la chuleta y las listas de comprobación.</p>';
    else if(d){var pl=d.items.filter(function(u){return !u.done();}),pend=pl.length,nd=d.items.length-pend;
      var nx=!pend&&r.expres?r.days.filter(function(x){return x.date>t0;}).map(function(x){return x.items.filter(function(u){return !u.done()&&u.kind==='xp'&&!/^xp:tr:/.test(u.id);})[0];}).filter(Boolean)[0]:null;
      h='<p class="td-k">Hoy, '+fmt(t0)+' · unos '+(r.expres?hm(d.min):d.min+' min')+'</p><p class="td-t">'+(pend?(nd?'Llevas '+nd+' de '+d.items.length+'. Sigue con:':'Te toca:'):'¡Hecho lo de hoy!'+(nx?' Si te quedan fuerzas, adelanta:':''))+'</p><ul class="td-list">'+(pend?pl.slice(0,6):(nx?[nx]:[])).map(itemHtml).join('')+'</ul>'+(pend>6?'<p class="td-more">y '+(pend-6)+' más en el plan.</p>':'')+'<a class="td-go" href="#plan-de-estudio">Ver el plan completo</a>';}
    else{var nx=r.days.filter(function(x){return x.date>t0&&x.items.length;})[0];
      h='<p class="td-k">Hoy no toca nada del plan</p><p class="td-t">'+(nx?'Lo siguiente, el '+fmt(nx.date)+': '+esc(nx.items[0].title)+'.':'Repasa lo que peor te haya salido o descansa.')+'</p><a class="td-go" href="#plan-de-estudio">Ver el plan completo</a>';}
  }
  box.innerHTML=h;box.hidden=false;
  var ei=box.querySelector('.td-exam');if(ei)ei.addEventListener('change',function(){var c=cfg();c.exam=ei.value;saveCfg(c);paint();});
  if(r)bindLinks(box,r);
  [].forEach.call(box.querySelectorAll('a.td-go'),function(a){a.addEventListener('click',function(e){var t=document.getElementById('plan-de-estudio');if(t){e.preventDefault();A.goTo(t);}});});
}
var tm;function later(){clearTimeout(tm);tm=setTimeout(paint,300);}
document.addEventListener('change',function(e){if(e.target.closest&&(e.target.closest('.done-chk')||e.target.closest('.sec-foot')||e.target.closest('label.can')))later();});
document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.testsim'))later();});
var op=A.paint;A.paint=function(){op.apply(this,arguments);later();};
window.GuiaPlan={paint:paint,schedule:schedule,units:U};
paint();
})();
</script>
