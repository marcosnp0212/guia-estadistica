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
var ALLTEMAS=[];U.groups.forEach(function(g){g.temas.forEach(function(t){if(t>0&&ALLTEMAS.indexOf(t)<0)ALLTEMAS.push(t);});});ALLTEMAS.sort(function(a,b){return a-b;});

/* ---- 2. Configuración ---- */
function cfg(){var c=get('plan:cfg',null)||{};
  if(!c.days)c.days=[1,2,3,4,5,6];if(!c.temas)c.temas=ALLTEMAS.slice();if(c.base===undefined)c.base=true;return c;}
function saveCfg(c){set('plan:cfg',c);}

/* ---- 3. Reparto ---- */
function interleave(teo,pr){
  var out=[],n=teo.length,m=pr.length,j=0;
  for(var i=0;i<n;i++){out.push(teo[i]);while(j<m&&(j+1)/m<=(i+1)/n){out.push(pr[j]);j++;}}
  while(j<m){out.push(pr[j]);j++;}return out;
}
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
  var pend=seq.filter(function(u){return !u.done();}),doneN=seq.length-pend.length;
  var res={days:[],seq:seq,pend:pend,doneN:doneN,E:E,S:S,repaso:null,perDay:0,extra:[]};
  if(!days.length)return res;
  if(days.length>=4){res.repaso=days.pop();}
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
function itemHtml(u){return'<li class="pl-it'+(u.done()?' done':'')+'"><a href="#'+u.sec.id+'" data-u="'+esc(u.id)+'">'+esc(u.title)+'</a><span class="pl-min">'+u.min+' min</span></li>';}
function bindLinks(root,r){[].forEach.call(root.querySelectorAll('a[data-u]'),function(a){a.addEventListener('click',function(e){e.preventDefault();
  var u=r.seq.filter(function(x){return x.id===a.getAttribute('data-u');})[0];if(!u)return;
  if(u.lvl){var b=u.sec.querySelector('.practica');if(b&&b._setLevel)b._setLevel(u.lvl);}A.goTo(u.sec);});});}
function paint(){
  var c=cfg(),r=schedule();
  if(app){
    var h='<div class="pl-cfg"><div class="pl-row"><label>Día del examen<input type="date" class="pl-exam" value="'+(c.exam||'')+'"></label><label>Empiezo <span class="opt">(si no, hoy)</span><input type="date" class="pl-start" value="'+(c.start||'')+'"></label></div>'+
      '<div class="pl-row"><span class="pl-lab">Días que estudio</span><div class="chips">'+DCI.map(function(d,i){return'<button type="button" class="chip'+(c.days.indexOf(d)>-1?' on':'')+'" data-day="'+d+'" aria-pressed="'+(c.days.indexOf(d)>-1)+'">'+DC[i]+'</button>';}).join('')+'</div></div>'+
      '<div class="pl-row"><span class="pl-lab">Qué entra</span><div class="chips">'+ALLTEMAS.map(function(t){return'<button type="button" class="chip'+(c.temas.indexOf(t)>-1?' on':'')+'" data-tema="'+t+'" aria-pressed="'+(c.temas.indexOf(t)>-1)+'">Tema '+t+'</button>';}).join('')+
      '<button type="button" class="chip'+(c.base?' on':'')+'" data-base="1" aria-pressed="'+c.base+'">Parte 0 (base)</button></div></div></div>';
    if(!r){h+='<p class="pl-empty">Pon el día del examen y aquí aparecerá tu plan, día a día.</p>';}
    else{
      var left=r.pend.length,tot=r.seq.length;
      h+='<div class="pl-sum"><div class="meter"><span style="width:'+(tot?Math.round(r.doneN/tot*100):0)+'%"></span></div><p>Llevas <b>'+r.doneN+' de '+tot+'</b> tareas. Faltan <b>'+Math.max(0,Math.round((r.E-today())/864e5))+'</b> días para el examen'+(r.days.length?'; te salen unos <b>'+r.perDay+' minutos</b> por día de estudio.':'.')+'</p>'+
                (r.perDay>150?'<p class="pl-warn"><b>¿Poco tiempo?</b> Si el examen está muy cerca, usa el <a href="#repaso-exprés-el-examen-en-3-días">Repaso exprés</a>: lo imprescindible en unas 2 horas al día.</p><p class="pl-warn">Son muchos minutos al día. Si puedes, añade días de estudio. Si no, quita la Parte 0 si ya la dominas, y marca como hecho lo que ya sepas hacer («Ya lo sé hacer»): el plan se reparte solo con lo que queda.</p>':'')+'</div>';
      if(r.extra&&r.extra.length)h+='<p class="pl-note">No caben todos los simulacros. Si te sobra tiempo, haz también: '+r.extra.map(function(u){return'<a href="#'+u.sec.id+'" data-u="'+esc(u.id)+'">'+esc(u.title.replace(/^Examen · /,''))+'</a>';}).join(', ')+'.</p>';
      if(!left)h+='<p class="pl-empty">¡Lo tienes todo hecho! Repasa la chuleta y repite el simulacro que peor te saliera.</p>';
      var t0=today();
      h+='<ol class="pl-days">'+r.days.filter(function(d){return d.items.length;}).map(function(d){var isT=+d.date===+t0;
        return'<li class="pl-day'+(isT?' is-today':'')+'"><div class="pl-dh"><span class="pl-date">'+(isT?'Hoy · ':'')+fmt(d.date)+'</span><span class="pl-m">'+d.min+' min</span></div><ul>'+d.items.map(itemHtml).join('')+'</ul></li>';}).join('')+
        (r.repaso?'<li class="pl-day pl-rep'+(+r.repaso===+t0?' is-today':'')+'"><div class="pl-dh"><span class="pl-date">'+fmt(r.repaso)+'</span><span class="pl-m">repaso</span></div><ul><li class="pl-it"><a href="#chuleta-de-fórmulas">Nada nuevo: lee la chuleta y las listas de comprobación. Duerme bien.</a></li></ul></li>':'')+'</ol>';
    }
    app.innerHTML=h;
    app.querySelector('.pl-exam').addEventListener('change',function(e){var c=cfg();c.exam=e.target.value;saveCfg(c);paint();});
    app.querySelector('.pl-start').addEventListener('change',function(e){var c=cfg();c.start=e.target.value;saveCfg(c);paint();});
    [].forEach.call(app.querySelectorAll('.chip'),function(b){b.addEventListener('click',function(){var c=cfg();
      if(b.hasAttribute('data-day')){var d=+b.getAttribute('data-day'),i=c.days.indexOf(d);if(i>-1){if(c.days.length>1)c.days.splice(i,1);}else c.days.push(d);}
      else if(b.hasAttribute('data-tema')){var t=+b.getAttribute('data-tema'),j=c.temas.indexOf(t);if(j>-1){if(c.temas.length>1)c.temas.splice(j,1);}else c.temas.push(t);}
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
    else if(d){var pend=d.items.filter(function(u){return !u.done();}).length;
      h='<p class="td-k">Hoy, '+fmt(t0)+' · unos '+d.min+' min</p><p class="td-t">'+(pend?'Te toca:':'¡Hecho lo de hoy!')+'</p><ul class="td-list">'+d.items.filter(function(u){return !u.done();}).slice(0,6).map(itemHtml).join('')+'</ul>'+(pend>6?'<p class="td-more">y '+(pend-6)+' más en el plan.</p>':'')+'<a class="td-go" href="#plan-de-estudio">Ver el plan completo</a>';}
    else{var nx=r.days.filter(function(x){return x.date>t0&&x.items.length;})[0];
      h='<p class="td-k">Hoy no toca nada del plan</p><p class="td-t">'+(nx?'Lo siguiente, el '+fmt(nx.date)+': '+esc(nx.items[0].title)+'.':'Repasa lo que peor te haya salido o descansa.')+'</p><a class="td-go" href="#plan-de-estudio">Ver el plan completo</a>';}
  }
  box.innerHTML=h;box.hidden=false;
  var ei=box.querySelector('.td-exam');if(ei)ei.addEventListener('change',function(){var c=cfg();c.exam=ei.value;saveCfg(c);paint();});
  if(r)bindLinks(box,r);
  [].forEach.call(box.querySelectorAll('a.td-go'),function(a){a.addEventListener('click',function(e){var t=document.getElementById('plan-de-estudio');if(t){e.preventDefault();A.goTo(t);}});});
}
var tm;function later(){clearTimeout(tm);tm=setTimeout(paint,300);}
document.addEventListener('change',function(e){if(e.target.closest&&(e.target.closest('.done-chk')||e.target.closest('.sec-foot')))later();});
var op=A.paint;A.paint=function(){op.apply(this,arguments);later();};
window.GuiaPlan={paint:paint,schedule:schedule,units:U};
paint();
})();
</script>
