<script>
(function(){
if(document.body.getAttribute('data-guide')!=='alumna')return;
var A=window.GuiaAPI, D=window.GUIA_DATA||{};
if(!A)return;
var get=A.get,set=A.set,esc=A.esc,el=A.el;
var doc=document.querySelector('.doc');

/* ---------- utilidades ---------- */
function fmtNum(v){if(typeof v!=='number')return String(v);var r=Math.round(v*10000)/10000;return String(r).replace('.',',');}
function parseNum(raw){
  if(raw==null)return NaN;var s=String(raw).trim().replace(/\s|€/g,'');if(!s)return NaN;
  s=s.replace('%','');
  if(s.indexOf(',')>-1&&s.indexOf('.')>-1)s=s.replace(/\./g,'').replace(',','.');else s=s.replace(',','.');
  s=s.replace('−','-');return s===''||isNaN(+s)?NaN:+s;
}
function norm(t){return String(t).trim().toUpperCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/^=+/,'').replace(/\(.*$/,'').replace(/[ÍI]/g,'I').replace(/\s+/g,' ').trim();}
function tolOf(key,dec){return Math.max(0.5*Math.pow(10,-dec)*1.02,Math.abs(key)*0.001);}
/* devuelve {ok:bool, hint:string|null, empty:bool} */
function evaluate(q,raw){
  if(raw==null||String(raw).trim()==='')return{empty:true};
  if(q.kind==='text'){
    var v=norm(raw);var acc=(q.accept||[q.key]).map(norm);
    if(acc.indexOf(v)>-1)return{ok:true};
    for(var i=0;i<(q.alts||[]).length;i++)if(norm(q.alts[i][0])===v)return{ok:false,hint:q.alts[i][1]};
    return{ok:false,hint:'Revisa la respuesta.'};
  }
  var x=parseNum(raw);if(isNaN(x))return{ok:false,hint:'Escribe solo el número (con coma o punto decimal).'};
  var key=q.key!=null?q.key:q.ans,dec=q.dec!=null?q.dec:2,t=q.tol!=null?q.tol:tolOf(key,dec);
  var pct=q.kind==='pct'||q.type==='pct';
  function near(a,b,tt){return Math.abs(a-b)<=tt;}
  if(near(x,key,t)||(pct&&near(x/100,key,t)))return{ok:true};
  var alts=q.alts||[];
  for(var j=0;j<alts.length;j++){var av=alts[j][0],at=tolOf(av,dec);if(near(x,av,at)||(pct&&near(x/100,av,at)))return{ok:false,hint:alts[j][1]};}
  return{ok:false,hint:'Revisa el cálculo.'};
}
function copyText(t,btn){
  function ok(){var o=btn.textContent;btn.textContent='Copiado';btn.classList.add('done');setTimeout(function(){btn.textContent=o;btn.classList.remove('done');},1300);}
  if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(t).then(ok,fb);else fb();
  function fb(){var ta=el('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok();}catch(e){}ta.remove();}
}
function markDone(sec,val){
  set('done:'+sec.id,!!val);var cb=sec.querySelector(':scope > .sec-foot .done-chk input');if(cb)cb.checked=!!val;A.paint();
}

/* ---------- bloques de ejercicio (prácticas y simulacros) ---------- */
function renderBlocks(container,blocks,store,opts){
  /* opts.exam: no corrige al momento.  devuelve lista de evaluadores */
  var asks=[];var stored=get(store,{})||{};var idx=0;
  function save(k,v){stored[k]=v;set(store,stored);}
  blocks.forEach(function(b){
    if(b.t==='p'){var p=el('p',b.b?'pr-lead':'',esc(b.text));container.appendChild(p);}
    else if(b.t==='h'){container.appendChild(el('h4','pr-h',esc(b.text)));}
    else if(b.t==='hint'){container.appendChild(el('p','pr-hint',esc(b.text.replace('Escribe en la fila de pistas lo que pondrías en la primera fila. ','La fila «Pista» te dice qué fórmula poner en la primera fila de cada columna en tu Excel. '))));}
    else if(b.t==='datos'){
      var w=el('div','pr-data');var tb='<table class="pr-grid"><tbody>';
      for(var i=0;i<b.values.length;i+=10){tb+='<tr>'+b.values.slice(i,i+10).map(function(v){return'<td>'+fmtNum(v)+'</td>';}).join('')+'</tr>';}
      w.innerHTML=tb+'</tbody></table>';
      var cb=el('button','btn ghost btn-sm','Copiar datos (en columna)');cb.type='button';
      cb.addEventListener('click',function(){copyText(b.values.map(fmtNum).join('\n'),cb);});
      w.appendChild(cb);container.appendChild(w);
    }
    else if(b.t==='tabla'){
      var w2=el('div','tw');var h='<table><thead><tr>'+b.headers.map(function(x){return'<th>'+esc(String(x))+'</th>';}).join('')+'</tr></thead><tbody>';
      b.rows.forEach(function(r){h+='<tr>'+r.map(function(v){return'<td>'+(v==null?'':esc(fmtNum(v)))+'</td>';}).join('')+'</tr>';});
      w2.innerHTML=h+'</tbody></table>';container.appendChild(w2);
      var cb2=el('button','btn ghost btn-sm','Copiar tabla para Excel');cb2.type='button';
      cb2.addEventListener('click',function(){copyText([b.headers.join('\t')].concat(b.rows.map(function(r){return r.map(function(v){return v==null?'':fmtNum(v);}).join('\t');})).join('\n'),cb2);});
      container.appendChild(cb2);
    }
    else if(b.t==='trabajo'){
      var ng=b.given[0].length;var w3=el('div','tw');var t=el('table','pr-work');container.appendChild(el('p','pr-note','Haz la tabla en tu Excel y escribe aquí los resultados (con 4 decimales basta). Cada casilla se pone verde o roja.'));
      var thead='<thead><tr>'+b.headers.map(function(x){return'<th>'+esc(String(x))+'</th>';}).join('')+'</tr>';
      if(b.hints)thead+='<tr class="pr-hintrow">'+'<td colspan="'+ng+'">Pista</td>'+b.hints.map(function(x){return'<td>'+esc(x)+'</td>';}).join('')+'</tr>';
      t.innerHTML=thead+'</thead>';var tbody=el('tbody');
      b.given.forEach(function(g,ri){
        var tr=el('tr');g.forEach(function(v){tr.appendChild(el('td','given',v==null?'':esc(fmtNum(v))));});
        b.keys[ri].forEach(function(k,ci){
          var td=el('td','cell');var inp=el('input');inp.type='text';inp.inputMode='decimal';inp.setAttribute('aria-label',b.headers[ng+ci]+' fila '+(ri+1));
          var key='w'+idx+'_'+ri+'_'+ci;var q={key:k,dec:b.dec[ci],kind:'num'};
          function chk(){var r=evaluate(q,inp.value);td.classList.toggle('ok',!!r.ok);td.classList.toggle('bad',!r.empty&&!r.ok);}
          inp.value=stored[key]||'';if(inp.value&&!opts.exam)chk();
          inp.addEventListener('change',function(){save(key,inp.value);if(!opts.exam)chk();});
          td.appendChild(inp);tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      t.appendChild(tbody);w3.appendChild(t);container.appendChild(w3);idx++;
    }
    else if(b.t==='ask'){
      var row=el('div','ask');var id='a'+idx;idx++;
      row.innerHTML='<label class="ask-l" for="'+store+id+'">'+esc(b.label)+'</label><div class="ask-r"><input id="'+store+id+'" type="text" '+(b.kind==='text'?'':'inputmode="decimal"')+' autocomplete="off"><span class="ask-fb" aria-live="polite"></span></div>';
      var inp2=row.querySelector('input'),fb=row.querySelector('.ask-fb');var fails=stored[id+'_f']||0;
      var item={q:b,row:row,inp:inp2,fb:fb,res:null};
      function show(r,final){
        row.classList.toggle('ok',!!r.ok);row.classList.toggle('bad',!r.empty&&!r.ok);
        if(r.empty){fb.innerHTML='';return;}
        if(r.ok){fb.innerHTML='✔ Bien';return;}
        var html='✘ '+esc(r.hint||'Revisa el cálculo.');
        if(fails>=2&&!opts.exam||final)html+=' <button type="button" class="link-btn reveal">Ver la respuesta</button>';
        fb.innerHTML=html;var rv=fb.querySelector('.reveal');
        if(rv)rv.addEventListener('click',function(){fb.innerHTML='✘ La respuesta es <b>'+esc(b.kind==='text'?String(b.key):fmtNum(Math.round(b.key*Math.pow(10,b.dec))/Math.pow(10,b.dec)))+'</b>'+(b.kind==='pct'?' (en decimal)':'')+'.';});
      }
      item.check=function(final){var r=evaluate(b,inp2.value);item.res=r;show(r,final);return r;};
      inp2.value=stored[id]||'';
      if(inp2.value&&!opts.exam)item.check();
      inp2.addEventListener('change',function(){save(id,inp2.value);if(opts.exam)return;var r=item.check();if(!r.ok&&!r.empty){fails++;save(id+'_f',fails);item.check();}if(opts.onChange)opts.onChange();});
      inp2.addEventListener('keydown',function(e){if(e.key==='Enter'){inp2.blur();}});
      asks.push(item);container.appendChild(row);
    }
  });
  return asks;
}

/* Hoja de cálculo para prácticas (Handsontable + HyperFormula en español) */
function colName(c){var s='';c++;while(c>0){var m=(c-1)%26;s=String.fromCharCode(65+m)+s;c=Math.floor((c-1)/26);}return s;}
function renderSheet(panel,sh,store,onUpd){
  var stored=get(store,{})||{};
  var blocks=sh.blocks;var firstP=true;
  /* --- instrucciones arriba --- */
  var steps=[];var hintRows=[];
  blocks.forEach(function(b){
    if(b.t==='p'&&firstP){panel.appendChild(el('p','pr-lead',esc(b.text)));firstP=false;}
    else if(b.t==='hint')steps.push('<li class="st-hint">'+esc(b.text.replace('Escribe en la fila de pistas lo que pondrías en la primera fila. ',''))+'</li>');
    else if(b.t==='trabajo'&&b.hints){var ng=b.given[0].length;hintRows.push(b.hints.map(function(h,i){return'<span><b>'+esc(String(b.headers[ng+i]))+'</b> <code>'+esc(h)+'</code></span>';}).join(''));}
  });
  var how=el('div','sh-how');
  how.innerHTML='<p><b>Hazlo aquí mismo, como en Excel.</b> Escribe las fórmulas en las casillas blancas de la tabla y en las amarillas de «Resultados». Arrastra el cuadradito azul de la esquina para copiar una fórmula hacia abajo. <b>F4</b> pone los <code>$</code>. Cada casilla se pone verde o roja al momento.</p>'+(steps.length?'<ul>'+steps.join('')+'</ul>':'')+(hintRows.length?'<div class="sh-fx"><span class="sh-fx-t">Fórmula de la primera fila:</span>'+hintRows.join('')+'</div>':'');
  panel.appendChild(how);
  /* --- maquetación --- */
  var cells={};/* "r,c" -> {v,ro,cls} */
  function put(r,c,v,cls,ro){cells[r+','+c]={v:v,cls:cls||'',ro:ro!==false};}
  var tc=0,hasData=false,dataLen=0;
  blocks.forEach(function(b){if(b.t==='datos'){hasData=true;dataLen=b.values.length;put(0,0,'Datos','sh-head');b.values.forEach(function(v,i){put(i+1,0,v,'sh-given');});}});
  if(hasData)tc=2;
  var r=0,maxW=0,work=[],pend=null,seenFirst=false,tmerges=[];
  blocks.forEach(function(b){
    if(b.t==='p'){if(!seenFirst){seenFirst=true;return;}pend=b.text;return;}
    if(b.t!=='tabla'&&b.t!=='trabajo')return;
    var lastAskBefore=false;
    if(pend&&b.t!=='ask'){put(r,tc,pend,'sh-title');tmerges.push({row:r,col:tc,rowspan:1,colspan:Math.max(b.headers.length,2)});r++;pend=null;}
    var hd=b.headers;hd.forEach(function(h,i){put(r,tc+i,String(h),'sh-head');});maxW=Math.max(maxW,hd.length);r++;
    if(b.t==='tabla'){b.rows.forEach(function(row){row.forEach(function(v,i){put(r,tc+i,v==null?'':v,'sh-given');});r++;});}
    else{var ng=b.given[0].length;b.given.forEach(function(g,ri){g.forEach(function(v,i){put(r,tc+i,v==null?'':v,'sh-given');});
        b.keys[ri].forEach(function(k,ci){put(r,tc+ng+ci,'','sh-in',false);work.push({r:r,c:tc+ng+ci,q:{key:k,dec:b.dec[ci],kind:'num'},col:String(hd[ng+ci]),first:ri===0});});r++;});}
    r++;
  });
  var span=Math.max(2,Math.min(maxW-1,4)),ac=tc,ar=r,merges=tmerges;
  function title(rr,t){put(rr,ac,t,'sh-title');merges.push({row:rr,col:ac,rowspan:1,colspan:span+1});}
  put(ar,ac,'Resultados','sh-head');merges.push({row:ar,col:ac,rowspan:1,colspan:span});put(ar,ac+span,'Tu fórmula','sh-head');ar++;
  var asks=[];pend=null;var startedAsks=false;
  blocks.forEach(function(b,i){
    if(b.t==='ask'){startedAsks=true;if(pend){title(ar,pend);ar++;pend=null;}put(ar,ac,b.label,'sh-label');merges.push({row:ar,col:ac,rowspan:1,colspan:span});for(var k=1;k<span;k++)put(ar,ac+k,'','sh-label');put(ar,ac+span,'','sh-ans',false);asks.push({q:b,r:ar,c:ac+span,res:null});ar++;}
    else if(b.t==='p'&&startedAsks){var nx=blocks[i+1];if(!nx||(nx.t!=='tabla'&&nx.t!=='trabajo'))pend=b.text;}
  });
  var nRows=Math.max(r,ar,hasData?dataLen+1:0)+3,nCols=Math.max(tc+maxW,ac+span+1)+2;
  var data=[];for(var i=0;i<nRows;i++){var row=[];for(var j=0;j<nCols;j++){var x=cells[i+','+j];row.push(x?x.v:'');}data.push(row);}
  Object.keys(stored).forEach(function(k){var p=k.split(',');if(data[+p[0]]&&cells[k]&&!cells[k].ro)data[+p[0]][+p[1]]=stored[k];});
  /* --- barra de fórmulas + hoja --- */
  var wrap=el('div','sh-wrap');var bar=el('div','sh-bar','<span class="sh-name">A1</span><span class="sh-fxl">fx</span>');var fx=el('input','sh-fxin');fx.type='text';fx.setAttribute('aria-label','Barra de fórmulas');bar.appendChild(fx);
  var gridEl=el('div','sh-grid');wrap.appendChild(bar);wrap.appendChild(gridEl);panel.appendChild(wrap);
  var hf=HyperFormula.buildEmpty({licenseKey:'internal-use-in-handsontable',language:'esES',functionArgSeparator:';',decimalSeparator:',',thousandSeparator:' ',undoLimit:200});
  var widths=[];for(var c2=0;c2<nCols;c2++){widths.push(hasData&&c2===0?70:(c2===1&&hasData?28:(c2===ac+span?110:96)));}
  function rend(inst,td,row,col,prop,val){Handsontable.renderers.TextRenderer.apply(this,arguments);
    var m=cells[row+','+col];td.className=(m?m.cls:'')+(td.className.indexOf('current')>-1?' current':'');
    var num=typeof val==='number'||(typeof val==='string'&&/^-?\d+(,\d+)?%?$/.test(val.trim()));
    if(typeof val==='number')td.textContent=String(Math.round(val*1e6)/1e6).replace('.',',');
    if(num)td.style.textAlign='right';
    var st=state[row+','+col];if(st)td.classList.add(st);}
  var state={};
  var hot=new Handsontable(gridEl,{data:data,rowHeaders:true,colHeaders:true,colWidths:widths,height:Math.min(nRows*24+34,520),width:'100%',licenseKey:'non-commercial-and-evaluation',
    formulas:{engine:hf,sheetName:'Hoja1'},mergeCells:merges,fillHandle:true,undo:true,outsideClickDeselects:false,autoWrapRow:false,autoWrapCol:false,wordWrap:true,enterMoves:{row:1,col:0},
    cells:function(row,col){var m=cells[row+','+col];return{readOnly:!!(m&&m.ro),renderer:rend};},
    afterSelectionEnd:function(row,col){bar.querySelector('.sh-name').textContent=colName(col)+(row+1);var s=hot.getSourceDataAtCell(row,col);fx.value=s==null?'':s;fx.readOnly=!!(cells[row+','+col]&&cells[row+','+col].ro);},
    afterChange:function(ch,src){if(!ch||src==='loadData')return;var dirty=false;ch.forEach(function(x){var k=x[0]+','+x[1];if(cells[k]&&cells[k].ro)return;stored[k]=x[3];dirty=true;
        asks.forEach(function(a){if(a.r===x[0]&&a.c===x[1])a.touched=true;});});
      if(dirty)set(store,stored);setTimeout(evalAll,0);}
  });
  if(hasData){try{hf.addNamedExpression('datos','=Hoja1!$A$2:$A$'+(dataLen+1));}catch(e){}}
  fx.addEventListener('keydown',function(e){if(e.key==='Enter'){var s=hot.getSelectedLast();if(s&&!fx.readOnly){hot.setDataAtCell(s[0],s[1],fx.value);hot.selectCell(Math.min(s[0]+1,nRows-1),s[1]);}e.preventDefault();}});
  panel._hot=hot;panel._asks=asks;panel._work=work;panel._st=function(){return state;};
  /* --- resultados --- */
  var list=el('div','sh-res');panel.appendChild(list);
  var fails=get(store+':f',{})||{};
  function valOf(rr,cc){var v=hot.getDataAtCell(rr,cc);return v==null?'':v;}
  function evalAll(){
    state={};var colBad={};
    work.forEach(function(w){var v=valOf(w.r,w.c);var res=evaluate(w.q,typeof v==='number'?String(v):v);if(res.empty)return;state[w.r+','+w.c]=res.ok?'ok':'bad';if(!res.ok)colBad[w.col]=w;});
    var html='';
    asks.forEach(function(a,i){var v=valOf(a.r,a.c);var res=evaluate(a.q,typeof v==='number'?String(v):v);a.res=res;
      if(!res.empty){state[a.r+','+a.c]=res.ok?'ok':'bad';if(!res.ok&&a.touched){fails[i]=(fails[i]||0)+1;a.touched=false;set(store+':f',fails);}}
      var ref=colName(a.c)+(a.r+1);
      html+='<li class="'+(res.empty?'empty':(res.ok?'ok':'bad'))+'"><span class="sr-l">'+esc(a.q.label)+' <span class="sr-ref">('+ref+')</span></span><span class="sr-fb">'+
        (res.empty?'':(res.ok?'✔ Bien':'✘ '+esc(res.hint||'Revisa el cálculo.')+((fails[i]||0)>=2?' <button type="button" class="link-btn reveal" data-i="'+i+'">Ver la respuesta</button>':'')))+'</span></li>';});
    var dol='';Object.keys(colBad).forEach(function(k){var w=colBad[k];var f=String(hot.getSourceDataAtCell(w.r,w.c)||'');
      if(/(^|[^$])\b[A-Z]{1,2}\d+:[A-Z]{1,2}\d+/.test(f)&&f.indexOf('$')<0)dol+='<p class="sh-dol">En la columna <b>'+esc(k)+'</b>, ¿has fijado el rango con <code>$</code>? Al arrastrar, el rango se ha movido. Ponte encima del rango en la fórmula y pulsa F4.</p>';});
    list.innerHTML=dol+'<ul>'+html+'</ul>';
    [].forEach.call(list.querySelectorAll('.reveal'),function(b){b.addEventListener('click',function(){var a=asks[+b.getAttribute('data-i')];b.parentNode.innerHTML='La respuesta es <b>'+(a.q.kind==='text'?esc(String(a.q.key)):fmtNum(Math.round(a.q.key*Math.pow(10,a.q.dec))/Math.pow(10,a.q.dec)))+'</b>.';});});
    hot.render();onUpd();
  }
  evalAll();
  return asks;
}
/* F4 en el editor de celdas y en la barra de fórmulas: ciclo A1 → $A$1 → A$1 → $A1 */
document.addEventListener('keydown',function(e){
  if(e.key!=='F4')return;var t=e.target;if(!t||!(t.classList.contains('handsontableInput')||t.classList.contains('sh-fxin')))return;
  e.preventDefault();e.stopPropagation();var s=t.value,p=t.selectionStart;var re=/\$?[A-Z]{1,2}\$?\d+/g,m;
  while((m=re.exec(s))){if(p>=m.index&&p<=m.index+m[0].length){var raw=m[0].replace(/\$/g,''),L=raw.match(/[A-Z]+/)[0],N=raw.match(/\d+/)[0];
    var cur=m[0],nx=cur===raw?'$'+L+'$'+N:(cur==='$'+L+'$'+N?L+'$'+N:(cur===L+'$'+N?'$'+L+N:raw));
    t.value=s.slice(0,m.index)+nx+s.slice(m.index+m[0].length);var np=m.index+nx.length;t.setSelectionRange(np,np);return;}}
},true);

/* ---------- 1. Prácticas ---------- */
var PR={};(D.practicas||[]).forEach(function(s){PR[s.id]=s;});
var NIV=['Nivel 1 · Con guía','Nivel 2 · Solo columnas','Nivel 3 · Como en el examen'];
var pendingLevel={};
[].slice.call(doc.querySelectorAll('.practica')).forEach(function(box){
  var tipo=box.getAttribute('data-tipo'),sec=box.closest('section');
  var tabs=el('div','lvl-tabs');tabs.setAttribute('role','tablist');var panel=el('div','lvl-panel');
  box.appendChild(tabs);box.appendChild(panel);
  var cur=get('pr-lvl:'+tipo,1);
  function lvlDone(l){return !!get('pr-done:'+tipo+':'+l,false);}
  function drawTabs(){tabs.innerHTML='';[1,2,3].forEach(function(l){
    var b=el('button','lvl-tab'+(l===cur?' on':'')+(lvlDone(l)?' done':''),'<span>'+NIV[l-1]+'</span>');b.type='button';b.setAttribute('role','tab');b.setAttribute('aria-selected',l===cur);
    b.addEventListener('click',function(){cur=l;set('pr-lvl:'+tipo,l);draw();});tabs.appendChild(b);});}
  function draw(){
    drawTabs();if(panel._hot){try{panel._hot.destroy();}catch(e){}panel._hot=null;}panel.innerHTML='';var sh=PR[tipo+'_N'+cur];if(!sh)return;
    var score=el('p','pr-score');panel.appendChild(score);
    var useSheet=cur<3&&window.Handsontable&&window.HyperFormula;
    if(cur===3)panel.appendChild(el('p','pr-note','Como en el examen: hazlo en tu Excel y escribe aquí los resultados.'));
    var asks=useSheet?renderSheet(panel,sh,'hoja:'+tipo+':'+cur,function(){if(asks)upd();}):renderBlocks(panel,sh.blocks,'pr:'+tipo+':'+cur,{onChange:upd});
    function upd(){var ok=asks.filter(function(a){return a.res&&a.res.ok;}).length;
      score.innerHTML='Aciertos: <b>'+ok+' de '+asks.length+'</b>'+(ok===asks.length?' · ¡Nivel completado!':'');
      if(ok===asks.length&&!lvlDone(cur)){set('pr-done:'+tipo+':'+cur,true);drawTabs();if(cur===3)markDone(sec,true);}
      if(ok===asks.length&&cur<3&&!panel.querySelector('.next-lvl')){var n=el('button','btn next-lvl','Pasar al '+NIV[cur].split(' · ')[0].toLowerCase());n.type='button';n.addEventListener('click',function(){cur=cur+1;set('pr-lvl:'+tipo,cur);draw();A.goTo(box);});panel.appendChild(n);}
    }
    asks.forEach(function(a){if(!a.res&&a.check&&a.inp.value)a.check();});upd();
    var rs=el('button','link-btn pr-reset','Borrar mis respuestas de este nivel');rs.type='button';
    rs.addEventListener('click',function(){if(confirm('¿Borrar tus respuestas de este nivel?')){set('pr:'+tipo+':'+cur,null);set('hoja:'+tipo+':'+cur,null);set('hoja:'+tipo+':'+cur+':f',null);set('pr-done:'+tipo+':'+cur,null);draw();}});
    panel.appendChild(rs);
  }
  /* la hoja se monta solo cuando la práctica se ve por primera vez */
  var drawn=false;function withLib(f){if(window.loadSheetLib)window.loadSheetLib(f);else f();}
  function first(){if(drawn)return;drawn=true;panel.innerHTML='<p class="pr-note">Cargando la hoja de cálculo…</p>';withLib(draw);}
  box._setLevel=function(l){cur=l;set('pr-lvl:'+tipo,l);drawn=true;withLib(draw);};
  drawTabs();
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){if(es.some(function(e){return e.isIntersecting;})){io.disconnect();first();}},{rootMargin:'300px'});io.observe(box);}else first();
});

/* ---------- 2. Simulacros ---------- */
var SIM={};(D.simulacros||[]).forEach(function(s){SIM[s.id]=s;});
var REC={S1:[1,2,4,5,8],S2:[1,2,3,5,7],S3:[1,2,4,6,7]};
var PRNAME={1:'Variable discreta',2:'Datos en intervalos',3:'Grupos y cambios de escala',4:'Tabla de doble entrada',5:'Regresión con datos',6:'Regresión a partir de resúmenes',7:'Índices y tasas',8:'Laspeyres, Paasche y deflactar'};
[].slice.call(doc.querySelectorAll('.simulacro')).forEach(function(box){
  var sid=box.getAttribute('data-sim'),sec=box.closest('section');
  var parts=[1,2,3,4,5].map(function(i){return SIM[sid+'_P'+i];}).filter(Boolean);
  function draw(){
    box.innerHTML='';var start=get('sim-start:'+sid,null),result=get('sim-res:'+sid,null);
    if(!start&&!result){
      var paper=parts[0]&&parts[0].paper;var intro=el('div','sim-intro','<p><b>5 preguntas · 2 puntos cada una · 90 minutos.</b> '+(paper?'Solo papel, boli y calculadora: el Excel cerrado.':'Ten abiertos tu Excel, tus prácticas de clase y tu solucionario.')+'</p>');
      var go=el('button','btn','Empezar el simulacro');go.type='button';
      go.addEventListener('click',function(){set('sim-start:'+sid,Date.now());draw();A.goTo(box);});
      intro.appendChild(go);box.appendChild(intro);return;
    }
    var bar=el('div','sim-bar');box.appendChild(bar);
    var all=[];var per=[];
    parts.forEach(function(sh,i){
      var q=el('div','sim-q');q.innerHTML='<h4>Pregunta '+(i+1)+' <span class="sim-pts"></span></h4>'+(sh.subtitle?'<p class="pr-sub">'+esc(sh.subtitle)+'</p>':'');
      var asks=renderBlocks(q,sh.blocks,'sim:'+sid+':'+i,{exam:true});per.push({asks:asks,box:q});all=all.concat(asks);box.appendChild(q);
    });
    var foot=el('div','sim-foot');box.appendChild(foot);
    function grade(){
      var total=0,weak=[];
      per.forEach(function(p,i){var ok=p.asks.filter(function(a){return a.check(true).ok;}).length;var pts=Math.round(ok/p.asks.length*2*100)/100;total+=pts;
        p.box.querySelector('.sim-pts').textContent='· '+String(pts).replace('.',',')+' de 2 puntos';if(ok/p.asks.length<0.7)weak.push(REC[sid][i]);});
      total=Math.round(total*10)/10;return{nota:total,weak:weak};
    }
    if(result){
      var g=grade();bar.innerHTML='<span>Simulacro entregado</span>';
      var msg=g.nota>=7?'Vas bien. Repasa solo las preguntas en rojo.':(g.nota>=5?'Aprobado. Repasa las preguntas en rojo y repite en nivel 3 las prácticas que se indican abajo.':'Para eso está el simulacro. Vuelve a las prácticas que se indican abajo, empezando por el nivel 2, y repite el simulacro otro día.');
      var rec=g.weak.length?'<p>Te conviene repetir: '+g.weak.filter(function(v,i,a){return a.indexOf(v)===i;}).map(function(n){return'<a href="#" class="prac-link" data-pr="'+n+'" data-lvl="'+(g.nota>=5?3:2)+'">Práctica '+n+' ('+PRNAME[n]+')</a>';}).join(', ')+'.</p>':'';
      foot.innerHTML='<div class="sim-grade"><span class="nota">'+String(g.nota).replace('.',',')+'</span><span class="de">sobre 10</span></div><p>'+msg+'</p>'+rec;
      var again=el('button','btn ghost','Volver a hacerlo desde cero');again.type='button';
      again.addEventListener('click',function(){if(confirm('Se borrarán tus respuestas de este simulacro. ¿Seguir?')){set('sim-res:'+sid,null);set('sim-start:'+sid,null);for(var i=0;i<5;i++)set('sim:'+sid+':'+i,null);draw();}});
      foot.appendChild(again);
      if(g.nota>=5)markDone(sec,true);
      return;
    }
    var timerEl=el('span','sim-timer');bar.appendChild(el('span','','Tiempo restante'));bar.appendChild(timerEl);
    var sub=el('button','btn','Entregar');sub.type='button';bar.appendChild(sub);
    function tick(){if(!document.body.contains(timerEl))return;var left=90*60-Math.floor((Date.now()-start)/1000);
      if(left<=0){timerEl.textContent='0:00 · tiempo terminado';timerEl.classList.add('over');return;}
      timerEl.textContent=Math.floor(left/60)+':'+String(left%60).padStart(2,'0');setTimeout(tick,1000);}
    tick();
    sub.addEventListener('click',function(){
      var empty=all.filter(function(a){return !a.inp.value.trim();}).length;
      if(empty&&!confirm('Te quedan '+empty+' casillas sin responder. ¿Entregar igualmente?'))return;
      set('sim-res:'+sid,{at:Date.now()});draw();A.goTo(box);
    });
    var fsub=el('button','btn','Entregar el simulacro');fsub.type='button';fsub.addEventListener('click',function(){sub.click();});foot.appendChild(fsub);
  }
  draw();
});

/* ---------- 2b. Vídeos ---------- */
var VID={t1:['qFxCvatJA7s','Tema 1. Una variable','35 min'],b12:['rRuCQaWuUSg','Boletín de los Temas 1 y 2','28 min'],t2:['bZ2RDTQ483I','Tema 2. Dos variables','9 min'],t3:['HULRqZML5gU','Tema 3. Regresión y correlación','12 min'],b3:['XRN-ahfALUc','Boletín del Tema 3','10 min'],t4:['25iXVSxnfoU','Tema 4. Números índices','12 min'],b4:['Evhy1CFN7HU','Boletín del Tema 4','11 min']};
var webOK=/^https?:$/.test(location.protocol);
[].slice.call(doc.querySelectorAll('.video')).forEach(function(box){
  var vk=box.getAttribute('data-v'),v=VID[vk];if(!v)return;var id=v[0],url='https://youtu.be/'+id;if(!document.getElementById('video-'+vk))box.id='video-'+vk;
  var seen=get('vid:'+id,false);
  box.innerHTML='<button type="button" class="vid-card"><span class="vid-th"><img loading="lazy" alt="" src="https://i.ytimg.com/vi/'+id+'/mqdefault.jpg" onerror="this.remove()"><span class="vid-play" aria-hidden="true"></span></span><span class="vid-tx"><span class="vid-k">Vídeo del '+(/^b/.test(vk)?'boletín':'tema')+' · '+v[2]+(seen?' · visto ✔':'')+'</span><span class="vid-t">'+esc(v[1])+'</span><span class="vid-m">Con voz, subtítulos y animaciones. Buen punto de partida antes de leer.</span></span></button><p class="vid-alt"><a href="'+url+'" target="_blank" rel="noopener">Abrir en YouTube</a></p>';
  box.querySelector('.vid-card').addEventListener('click',function(){
    set('vid:'+id,true);
    if(!webOK){window.open(url,'_blank','noopener');return;}
    var f=el('div','vid-frame');f.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0&vq=hd1080" title="'+esc(v[1])+'" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>';
    box.replaceChild(f,box.querySelector('.vid-card'));
  });
});

/* ---------- 2c. Simulacro tipo test (formato de la profesora) ---------- */
var TS=D.tests||{};
[].slice.call(doc.querySelectorAll('.testsim')).forEach(function(box){
  var sid=box.getAttribute('data-sim'),S=TS[sid],sec=box.closest('section');if(!S)return;
  var L='ABCD',key='ts:'+sid;
  function st(){var x=get(key,null);return x&&x.mc?x:{mc:{},sh:{},self:{}};}
  function draw(){
    box.innerHTML='';var start=get('ts-start:'+sid,null),res=get('ts-res:'+sid,null),a=st();
    if(!start&&!res){
      var intro=el('div','sim-intro','<p><b>30 preguntas tipo test + 10 de respuesta corta · 90 minutos.</b> Como el modelo de la profesora: solo papel, boli y calculadora. Cada pregunta vale lo mismo (0,25 puntos) y las falladas no restan.</p>');
      var go=el('button','btn','Empezar el simulacro');go.type='button';go.addEventListener('click',function(){set('ts-start:'+sid,Date.now());draw();A.goTo(box);});
      intro.appendChild(go);box.appendChild(intro);return;}
    var done=!!res;var bar=el('div','sim-bar');box.appendChild(bar);
    function save(){set(key,a);}
    var temaOk={1:[0,0],2:[0,0],3:[0,0],4:[0,0]};var nOk=0,nShort=0;
    box.appendChild(el('h4','ts-h','Parte 1 · Tipo test'));
    S.tests.forEach(function(q,i){
      var w=el('div','ts-q');w.innerHTML='<p class="ts-qq"><b>'+(i+1)+'.</b> '+esc(q.q)+'</p>'+(q.q_es?'<p class="ts-es" lang="es">'+esc(q.q_es)+'</p>':'');var ops=el('div','ts-ops');
      var mine=a.mc[i];
      q.opts.forEach(function(o,k){var b=el('button','ts-op'+(mine===k?' sel':''),'<span class="ts-l">'+L[k]+'</span><span>'+esc(o)+'</span>');b.type='button';
        if(done){b.disabled=true;if(k===q.ok)b.classList.add('right');else if(mine===k)b.classList.add('wrong');}
        else b.addEventListener('click',function(){a.mc[i]=k;save();[].forEach.call(ops.children,function(x){x.classList.remove('sel');});b.classList.add('sel');upd();});
        ops.appendChild(b);});
      w.appendChild(ops);
      if(done){var ok=mine===q.ok;temaOk[q.tema][1]++;if(ok){temaOk[q.tema][0]++;nOk++;}
        w.classList.add(ok?'ok':'bad');w.appendChild(el('p','ts-exp',(ok?'✔ ':'✘ '+(mine==null?'Sin responder. ':'Has marcado la '+L[mine]+'. '))+'La correcta es la <b>'+L[q.ok]+'</b>. '+esc(q.exp)+' <span class="ts-where">Repásalo en el apartado '+esc(q.where)+'.</span>'));}
      box.appendChild(w);
    });
    box.appendChild(el('h4','ts-h','Parte 2 · Respuesta corta'));
    S.cortas.forEach(function(q,i){
      var w=el('div','ts-q');w.innerHTML='<p class="ts-qq"><b>P'+(i+1)+'.</b> '+esc(q.q)+'</p>'+(q.q_es?'<p class="ts-es" lang="es">'+esc(q.q_es)+'</p>':'');
      var inp=q.kind==='open'?el('textarea','ts-ta'):el('input','ts-in');if(q.kind!=='open'){inp.type='text';if(q.kind!=='text')inp.inputMode='decimal';}
      inp.value=a.sh[i]||'';inp.setAttribute('aria-label','Respuesta P'+(i+1));
      if(done)inp.readOnly=true;else inp.addEventListener('input',function(){a.sh[i]=inp.value;save();upd();});
      w.appendChild(inp);
      if(done){
        if(q.kind==='open'){
          var m=el('div','ts-model','<p><b>Respuesta modelo:</b> '+esc(q.model)+'</p>'+(q.model_es?'<p lang="es"><b>En español:</b> '+esc(q.model_es)+'</p>':'')+'<p class="ts-self-q">Compárala con la tuya. ¿La tenías bien?</p>');
          var sv=a.self[i];var y=el('button','btn btn-sm'+(sv===true?'':' ghost'),'Sí, la tenía bien'),n=el('button','btn btn-sm'+(sv===false?'':' ghost'),'No');y.type=n.type='button';
          y.addEventListener('click',function(){a.self[i]=true;save();draw();});n.addEventListener('click',function(){a.self[i]=false;save();draw();});
          m.appendChild(y);m.appendChild(n);w.appendChild(m);if(sv===true){nShort++;w.classList.add('ok');}else if(sv===false)w.classList.add('bad');
        }else{
          var r=evaluate(q,inp.value);if(r.ok){nShort++;w.classList.add('ok');}else w.classList.add('bad');
          w.appendChild(el('p','ts-exp',(r.ok?'✔ Bien. ':'✘ '+(r.empty?'Sin responder. ':esc(r.hint||'')+' '))+'<b>Solución:</b> '+esc(q.explain)+' <span class="ts-where">Apartado '+esc(q.where)+'.</span>'));
        }
      }
      box.appendChild(w);
    });
    var foot=el('div','sim-foot');box.appendChild(foot);
    function upd(){if(done)return;var n=Object.keys(a.mc).length+Object.keys(a.sh).filter(function(k){return String(a.sh[k]).trim();}).length;cnt.textContent=n+' de 40 respondidas';}
    if(done){
      var nota=Math.round((nOk+nShort)*0.25*100)/100;bar.innerHTML='<span>Simulacro entregado</span>';
      var weak=[1,2,3,4].filter(function(t){return temaOk[t][1]&&temaOk[t][0]/temaOk[t][1]<0.7;});
      var pend=S.cortas.filter(function(q,i){return q.kind==='open'&&a.self[i]==null;}).length;
      foot.innerHTML='<div class="sim-grade"><span class="nota">'+String(nota).replace('.',',')+'</span><span class="de">sobre 10</span></div>'+
        '<p>Tipo test: <b>'+nOk+' de 30</b> · Respuesta corta: <b>'+nShort+' de 10</b>'+(pend?' (te falta corregir '+pend+' abierta: compárala con la respuesta modelo)':'')+'.</p>'+
        '<p>Por temas: '+[1,2,3,4].map(function(t){return'Tema '+t+' <b>'+temaOk[t][0]+'/'+temaOk[t][1]+'</b>';}).join(' · ')+'.</p>'+
        (weak.length?'<p>Repasa '+(function(l){return l.length>1?l.slice(0,-1).join(', ')+' y '+l[l.length-1]:l[0];})(weak.map(function(t){return'el <a href="#" class="tema-link" data-t="'+t+'">Tema '+t+'</a>';}))+' (menos del 70 % de aciertos) y vuelve a leer el examen modelo.</p>':'<p>Más del 70 % en todos los temas. ¡Bien!</p>');
      [].forEach.call(foot.querySelectorAll('.tema-link'),function(x){x.addEventListener('click',function(e){e.preventDefault();var h=doc.querySelector('section.level1 > h1.t'+x.getAttribute('data-t'));if(h)A.goTo(h.parentNode);});});
      var again=el('button','btn ghost','Volver a hacerlo desde cero');again.type='button';
      again.addEventListener('click',function(){if(confirm('Se borrarán tus respuestas de este simulacro. ¿Seguir?')){set(key,null);set('ts-res:'+sid,null);set('ts-start:'+sid,null);draw();}});
      foot.appendChild(again);if(nota>=5)markDone(sec,true);return;}
    var timerEl=el('span','sim-timer'),cnt=el('span','ts-cnt');bar.appendChild(cnt);bar.appendChild(timerEl);
    var sub=el('button','btn','Entregar');sub.type='button';bar.appendChild(sub);
    (function tick(){if(!document.body.contains(timerEl))return;var left=90*60-Math.floor((Date.now()-start)/1000);
      if(left<=0){timerEl.textContent='0:00 · tiempo terminado';timerEl.classList.add('over');return;}
      timerEl.textContent=Math.floor(left/60)+':'+String(left%60).padStart(2,'0');setTimeout(tick,1000);})();
    sub.addEventListener('click',function(){var n=40-(Object.keys(a.mc).length+Object.keys(a.sh).filter(function(k){return String(a.sh[k]).trim();}).length);
      if(n>0&&!confirm('Te quedan '+n+' preguntas sin responder. ¿Entregar igualmente?'))return;set('ts-res:'+sid,{at:Date.now()});draw();A.goTo(box);});
    var fsub=el('button','btn','Entregar el simulacro');fsub.type='button';fsub.addEventListener('click',function(){sub.click();});foot.appendChild(fsub);upd();
  }
  draw();
});

/* ---------- 2d. Zonas del índice y enlaces de la portada ---------- */
[['tema-1.-análisis-descriptivo-de-una-variable','Aprender'],['repaso-exprés-el-examen-en-pocos-días','Examen'],['chuleta-de-fórmulas','Herramientas'],['por-si-el-examen-fuera-con-ordenador','Por si acaso']].forEach(function(z){
  var a=document.querySelector('.toc a[href="#'+z[0]+'"]');if(!a)return;var li=a.closest('li');var lab=el('li','zone',z[1]);lab.setAttribute('aria-hidden','true');li.parentNode.insertBefore(lab,li);if(z[1]==='Por si acaso')li.classList.add('psa');});
(function(){var on=false;[].forEach.call(document.querySelectorAll('.toc > ul > li'),function(li){if(li.classList.contains('zone')){on=/Examen|Herramientas/.test(li.textContent);return;}if(on)li.classList.add('notab');});})();
[].forEach.call(document.querySelectorAll('.hero a[href^="#"]'),function(a){a.addEventListener('click',function(e){var t=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));if(!t)return;e.preventDefault();A.goTo(t);});});

/* ---------- 3. Comprobaciones de cada apartado ---------- */
var CH=D.checks||{};
Object.keys(CH).forEach(function(id){
  var sec=document.getElementById(id);if(!sec)return;var qs=CH[id];
  var box=el('div','check');box.innerHTML='<p class="check-t">Comprueba que lo has entendido</p>';
  var foot=sec.querySelector(':scope > .sec-foot');sec.insertBefore(box,foot);
  var lastData=null,state=get('chk:'+id,{})||{};var items=[];
  function save(){set('chk:'+id,state);}
  qs.forEach(function(q,i){
    if(q.data&&q.data!==lastData){box.appendChild(el('p','check-data',esc(q.data)));lastData=q.data;}
    var w=el('div','cq');w.appendChild(el('p','cq-q',esc(q.q)));var fb=el('p','cq-fb');fb.setAttribute('aria-live','polite');
    var st=state[i]||{};var it={ok:!!st.ok};items.push(it);
    function done(){it.ok=true;st.ok=true;state[i]=st;save();w.classList.add('ok');fb.innerHTML='✔ '+(q.explain?esc(q.explain):'Bien.');allDone();}
    function wrong(h){st.f=(st.f||0)+1;state[i]=st;save();w.classList.remove('ok');
      fb.innerHTML='✘ '+esc(h||'No es correcto. Vuelve a leer el apartado e inténtalo otra vez.')+(st.f>=2?' <button type="button" class="link-btn reveal">Ver la respuesta</button>':'');
      var rv=fb.querySelector('.reveal');if(rv)rv.addEventListener('click',function(){fb.innerHTML='La respuesta es <b>'+(q.type==='mc'?esc(q.opts[q.ok]):fmtNum(q.ans))+'</b>. '+esc(q.explain||'');});}
    if(q.type==='mc'){
      var ops=el('div','cq-ops');q.opts.forEach(function(o,k){var b=el('button','cq-op',esc(o));b.type='button';
        b.addEventListener('click',function(){[].forEach.call(ops.children,function(x){x.classList.remove('sel-ok','sel-bad');});
          if(k===q.ok){b.classList.add('sel-ok');done();}else{b.classList.add('sel-bad');wrong(q.why&&q.why[String(k)]);}});
        ops.appendChild(b);if(st.ok&&k===q.ok)b.classList.add('sel-ok');});
      w.appendChild(ops);
    }else{
      var r=el('div','cq-in');var inp=el('input');inp.type='text';inp.inputMode='decimal';inp.setAttribute('aria-label',q.q);
      var b=el('button','btn btn-sm','Comprobar');b.type='button';r.appendChild(inp);r.appendChild(b);w.appendChild(r);
      if(st.v)inp.value=st.v;
      function go(){st.v=inp.value;var res=evaluate({key:q.ans,dec:q.dec,tol:q.tol,kind:q.type==='pct'?'pct':'num',alts:q.alts},inp.value);if(res.empty)return;if(res.ok)done();else wrong(res.hint);}
      b.addEventListener('click',go);inp.addEventListener('keydown',function(e){if(e.key==='Enter')go();});
    }
    w.appendChild(fb);box.appendChild(w);
    if(st.ok){w.classList.add('ok');fb.innerHTML='✔ '+(q.explain?esc(q.explain):'Bien.');}
  });
  var end=el('p','check-end');box.appendChild(end);
  function allDone(){if(items.every(function(x){return x.ok;})){end.innerHTML='Apartado completado.';box.classList.add('all');if(!get('done:'+id,false))markDone(sec,true);}}
  allDone();
});

/* ---------- 4. Siguiente apartado ---------- */
var seq=[].slice.call(doc.querySelectorAll('section.level2')).filter(function(s){var l1=s.closest('section.level1');return l1&&l1.querySelector(':scope > h1 .tab');});
seq.forEach(function(s,i){var nx=seq[i+1];var foot=s.querySelector(':scope > .sec-foot');if(!foot||!nx)return;
  var a=el('a','next-link','Siguiente: '+esc(A.tabOf(nx)+A.secTitle(nx))+' →');a.href='#'+nx.id;
  a.addEventListener('click',function(e){e.preventDefault();A.goTo(nx);});foot.appendChild(a);});

/* ---------- 5. Continuar donde lo dejé ---------- */
var tmr;window.addEventListener('scroll',function(){clearTimeout(tmr);tmr=setTimeout(function(){
  var cur=null;for(var i=0;i<seq.length;i++){if(seq[i].offsetParent===null)continue;if(seq[i].getBoundingClientRect().top<=120)cur=seq[i];else break;}
  if(cur)set('last',cur.id);},400);},{passive:true});
var hero=document.querySelector('.hero');var last=get('last',null);
if(hero&&last&&document.getElementById(last)){
  var ls=document.getElementById(last);
  var lc=hero.querySelector('.n-learn');if(lc){lc.href='#'+last;lc.querySelector('b').textContent='Seguir donde lo dejaste';lc.querySelector('.n-d').textContent=A.tabOf(ls)+A.secTitle(ls);lc.querySelector('.n-go').textContent='Continuar →';}
}

/* ---------- 6. Enlaces del plan a prácticas y simulacros ---------- */
var prSec={};[].slice.call(doc.querySelectorAll('.practica')).forEach(function(b){prSec[b.getAttribute('data-tipo').split('_')[0]]=b;});
var simSec={};[].slice.call(doc.querySelectorAll('.simulacro')).forEach(function(b){simSec[b.getAttribute('data-sim').slice(1)]=b;});
function linkify(root){[].slice.call(root.querySelectorAll('td')).forEach(function(td){
  td.innerHTML=td.innerHTML.replace(/Práctica\s+(\d)(\s+nivel(?:es)?\s+\d(?:\s+y\s+\d)?|\s+\(los\s+3\s+niveles\))?/g,function(m,n,rest){var lv=rest&&!/los/.test(rest)?rest.match(/\d/):null;return'<a href="#" class="prac-link" data-pr="'+n+'" data-lvl="'+(lv?lv[0]:'')+'">'+m+'</a>';})
    .replace(/Simulacro\s+(\d)/g,function(m,n){return'<a href="#" class="sim-link" data-sim="'+n+'">'+m+'</a>';});});}

document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a.prac-link,a.sim-link');if(!a)return;e.preventDefault();
  if(a.classList.contains('prac-link')){var b=prSec[a.getAttribute('data-pr')];if(!b)return;var l=+a.getAttribute('data-lvl');if(l&&b._setLevel)b._setLevel(l);A.goTo(b.closest('section'));}
  else{var s=simSec[a.getAttribute('data-sim')];if(s)A.goTo(s.closest('section'));}
});
/* ---------- 7. Descargas ---------- */
var FS=D.fsize||{};
[].slice.call(doc.querySelectorAll('.descarga')).forEach(function(box){
  var name=box.getAttribute('data-file'),kb=FS[name];if(kb==null)return;
  var btn=el('a','btn dl-btn','Descargar <span class="dl-meta">'+esc(name)+' · '+kb+' KB</span>');btn.href='assets/'+encodeURIComponent(name);btn.setAttribute('download',name);
  box.appendChild(btn);
});
A.paint();
})();
</script>
