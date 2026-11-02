// Cursor spotlight for cards (see spotlight.css). Desktop pointers only.
(function(){
  if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  var sel='.service-card,.bcard,.scard,.calc-card,.form-card,.step-card';
  var cards=[].slice.call(document.querySelectorAll(sel));
  if(!cards.length)return;
  cards.forEach(function(c){
    c.classList.add('spot');if(getComputedStyle(c).position==='static')c.style.position='relative';
    var r=document.createElement('span');r.className='spot-ring';r.setAttribute('aria-hidden','true');c.appendChild(r);
    if(c.parentElement)c.parentElement.classList.add('spot-zone');
  });
  var x=0,y=0,raf=0;
  function paint(){
    raf=0;
    for(var i=0;i<cards.length;i++){
      var b=cards[i].getBoundingClientRect();
      if(b.bottom<-300||b.top>innerHeight+300)continue;
      cards[i].style.setProperty('--mx',(x-b.left)+'px');
      cards[i].style.setProperty('--my',(y-b.top)+'px');
    }
  }
  addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY;if(!raf)raf=requestAnimationFrame(paint)},{passive:true});
})();
