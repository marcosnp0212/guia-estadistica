<script>
(function(){
  var root=document.documentElement, body=document.body;
  /* tema claro/oscuro */
  var tb=document.querySelector('.theme-toggle');
  function isDark(){var t=root.getAttribute('data-theme');if(t)return t==='dark';return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches;}
  tb&&tb.addEventListener('click',function(){var n=isDark()?'light':'dark';root.setAttribute('data-theme',n);try{localStorage.setItem('guia-tema',n);}catch(e){}});

  /* índice: colores por tema y estado abierto */
  var tocLinks=[].slice.call(document.querySelectorAll('.toc a'));
  var top=[].slice.call(document.querySelectorAll('.toc > ul > li'));
  top.forEach(function(li){
    var a=li.querySelector('a');var sec=a&&document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    if(sec){var c=(sec.className.match(/\bt[0-4x]\b/)||[])[0];if(c)li.classList.add(c);li._sec=sec;}
  });
  /* menú móvil */
  var nt=document.querySelector('.nav-toggle'),scrim=document.querySelector('.scrim');
  function setNav(o){body.classList.toggle('nav-open',o);nt&&nt.setAttribute('aria-expanded',o?'true':'false');if(scrim)scrim.hidden=!o;}
  var mqDesk=window.matchMedia('(min-width:1021px)'),root=document.documentElement;
  function syncNt(){if(nt)nt.setAttribute('aria-expanded',mqDesk.matches?(!root.classList.contains('sb-off')?'true':'false'):(body.classList.contains('nav-open')?'true':'false'));}
  nt&&nt.addEventListener('click',function(){
    if(mqDesk.matches){var off=!root.classList.contains('sb-off');root.classList.toggle('sb-off',off);try{localStorage.setItem('guia-sb',off?'0':'1');}catch(e){}syncNt();setTimeout(function(){window.dispatchEvent(new Event('resize'));},260);}
    else setNav(!body.classList.contains('nav-open'));});
  syncNt();if(mqDesk.addEventListener)mqDesk.addEventListener('change',syncNt);
  scrim&&scrim.addEventListener('click',function(){setNav(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')setNav(false);});
  tocLinks.forEach(function(a){a.addEventListener('click',function(){if(window.innerWidth<=1020)setNav(false);});});

  /* sección actual */
  var heads=[].slice.call(document.querySelectorAll('.doc section.level1, .doc section.level2'));
  var bar=document.querySelector('.progress span'),here=document.querySelector('.here');
  var lastTop=null,lastSub=null;
  function colorOf(el){return getComputedStyle(el).getPropertyValue('--c').trim();}
  function update(){
    var h=document.documentElement,sc=h.scrollTop||body.scrollTop,max=h.scrollHeight-h.clientHeight;
    if(bar)bar.style.width=(max>0?sc/max*100:0)+'%';
    var y=sc+90,cur1=null,cur2=null;
    for(var i=0;i<heads.length;i++){var s=heads[i];if(s.offsetTop<=y){if(s.classList.contains('level1')){cur1=s;cur2=null;}else cur2=s;}}
    if(cur1!==lastTop){
      top.forEach(function(li){li.classList.toggle('open',li._sec===cur1);});
      if(cur1){var col=colorOf(cur1);root.style.setProperty('--cur',col);}
      lastTop=cur1;
    }
    if(cur2!==lastSub){
      tocLinks.forEach(function(a){a.classList.remove('active');});
      if(cur2){var a=document.querySelector('.toc a[href="#'+CSS.escape(cur2.id)+'"]');if(a){a.classList.add('active');
        var toc=document.querySelector('.toc');var r=a.getBoundingClientRect(),tr=toc.getBoundingClientRect();
        if(r.top<tr.top+40||r.bottom>tr.bottom-40)toc.scrollTop+= (r.top-tr.top)-tr.height/3;}}
      lastSub=cur2;
    }
    if(here){
      var t1=cur1?cur1.querySelector('h1'):null,t2=cur2?cur2.querySelector('h2'):null;
      var tab=t1&&t1.querySelector('.tab'),ht=t1&&t1.querySelector('.ht');
      var a=tab?tab.textContent:(ht?ht.textContent:'');var b='';if(t2){var n2=t2.querySelector('.num'),h2t=t2.querySelector('.ht');b=n2?((t2.classList.contains('prac')?'Práctica ':'Ejercicio ')+n2.textContent+': '+(h2t?h2t.textContent:'')):(h2t?h2t.textContent:t2.textContent);}
      here.innerHTML=(a?'<b>'+a+'</b>':'')+(b?' &nbsp;/&nbsp; '+b:'');
    }
  }
  var ticking=false;
  window.addEventListener('scroll',function(){if(!ticking){requestAnimationFrame(function(){update();ticking=false;});ticking=true;}},{passive:true});
  window.addEventListener('resize',update);update();
})();
</script>
