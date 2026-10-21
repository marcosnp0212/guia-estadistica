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
  var r=0,maxW=0,work=[],pend=null,seenFirst=false;
  blocks.forEach(function(b){
    if(b.t==='p'){if(!seenFirst){seenFirst=true;return;}pend=b.text;return;}
    if(b.t!=='tabla'&&b.t!=='trabajo')return;
    var lastAskBefore=false;
    if(pend&&b.t!=='ask'){put(r,tc,pend,'sh-title');r++;pend=null;}
    var hd=b.headers;hd.forEach(function(h,i){put(r,tc+i,String(h),'sh-head');});maxW=Math.max(maxW,hd.length);r++;
    if(b.t==='tabla'){b.rows.forEach(function(row){row.forEach(function(v,i){put(r,tc+i,v==null?'':v,'sh-given');});r++;});}
    else{var ng=b.given[0].length;b.given.forEach(function(g,ri){g.forEach(function(v,i){put(r,tc+i,v==null?'':v,'sh-given');});
        b.keys[ri].forEach(function(k,ci){put(r,tc+ng+ci,'','sh-in',false);work.push({r:r,c:tc+ng+ci,q:{key:k,dec:b.dec[ci],kind:'num'},col:String(hd[ng+ci]),first:ri===0});});r++;});}
    r++;
  });
  var ac=tc+Math.max(maxW,1)+1,ar=0;put(ar,ac,'Resultados','sh-head');put(ar,ac+1,'Tu fórmula','sh-head');ar++;
  var asks=[];pend=null;var startedAsks=false;
  blocks.forEach(function(b,i){
    if(b.t==='ask'){startedAsks=true;if(pend){put(ar,ac,pend,'sh-title');ar++;pend=null;}put(ar,ac,b.label,'sh-label');put(ar,ac+1,'','sh-ans',false);asks.push({q:b,r:ar,c:ac+1,res:null});ar++;}
    else if(b.t==='p'&&startedAsks){pend=b.text;}
  });
  var nRows=Math.max(r,ar,hasData?dataLen+1:0)+3,nCols=ac+3;
  var data=[];for(var i=0;i<nRows;i++){var row=[];for(var j=0;j<nCols;j++){var x=cells[i+','+j];row.push(x?x.v:'');}data.push(row);}
  Object.keys(stored).forEach(function(k){var p=k.split(',');if(data[+p[0]]&&cells[k]&&!cells[k].ro)data[+p[0]][+p[1]]=stored[k];});
  /* --- barra de fórmulas + hoja --- */
  var wrap=el('div','sh-wrap');var bar=el('div','sh-bar','<span class="sh-name">A1</span><span class="sh-fxl">fx</span>');var fx=el('input','sh-fxin');fx.type='text';fx.setAttribute('aria-label','Barra de fórmulas');bar.appendChild(fx);
  var gridEl=el('div','sh-grid');wrap.appendChild(bar);wrap.appendChild(gridEl);panel.appendChild(wrap);
  var hf=HyperFormula.buildEmpty({licenseKey:'internal-use-in-handsontable',language:'esES',functionArgSeparator:';',decimalSeparator:',',thousandSeparator:' ',undoLimit:200});
  var widths=[];for(var c2=0;c2<nCols;c2++){widths.push(c2===ac?250:(c2===ac+1?120:(hasData&&c2===0?70:(c2===1&&hasData?28:96))));}
  function rend(inst,td,row,col,prop,val){Handsontable.renderers.TextRenderer.apply(this,arguments);
    var m=cells[row+','+col];td.className=(m?m.cls:'')+(td.className.indexOf('current')>-1?' current':'');
    var num=typeof val==='number'||(typeof val==='string'&&/^-?\d+(,\d+)?%?$/.test(val.trim()));
    if(typeof val==='number')td.textContent=String(Math.round(val*1e6)/1e6).replace('.',',');
    if(num)td.style.textAlign='right';
    var st=state[row+','+col];if(st)td.classList.add(st);}
  var state={};
  var hot=new Handsontable(gridEl,{data:data,rowHeaders:true,colHeaders:true,colWidths:widths,height:Math.min(nRows*24+34,520),width:'100%',licenseKey:'non-commercial-and-evaluation',
    formulas:{engine:hf,sheetName:'Hoja1'},fillHandle:true,undo:true,outsideClickDeselects:false,autoWrapRow:false,autoWrapCol:false,wordWrap:true,enterMoves:{row:1,col:0},
    cells:function(row,col){var m=cells[row+','+col];return{readOnly:!!(m&&m.ro),renderer:rend};},
    afterSelectionEnd:function(row,col){bar.querySelector('.sh-name').textContent=colName(col)+(row+1);var s=hot.getSourceDataAtCell(row,col);fx.value=s==null?'':s;fx.readOnly=!!(cells[row+','+col]&&cells[row+','+col].ro);},
    afterChange:function(ch,src){if(!ch||src==='loadData')return;var dirty=false;ch.forEach(function(x){var k=x[0]+','+x[1];if(cells[k]&&cells[k].ro)return;stored[k]=x[3];dirty=true;
        asks.forEach(function(a){if(a.r===x[0]&&a.c===x[1])a.touched=true;});});
      if(dirty)set(store,stored);setTimeout(evalAll,0);}
  });
  if(hasData){try{hf.addNamedExpression('datos','=Hoja1!$A$2:$A$'+(dataLen+1));}catch(e){}}
  fx.addEventListener('keydown',function(e){if(e.key==='Enter'){var s=hot.getSelectedLast();if(s&&!fx.readOnly){hot.setDataAtCell(s[0],s[1],fx.value);hot.selectCell(Math.min(s[0]+1,nRows-1),s[1]);}e.preventDefault();}});
  panel._hot=hot;
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
      html+='<li class="'+(res.empty?'':(res.ok?'ok':'bad'))+'"><span class="sr-l">'+esc(a.q.label)+' <span class="sr-ref">('+ref+')</span></span><span class="sr-fb">'+
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
