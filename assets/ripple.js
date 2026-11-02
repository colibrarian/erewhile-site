// Hover ripple for cards and rings for buttons (see ripple.css). Desktop pointers only.
(function(){
  if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  function spawn(host,cls,css){
    var s=document.createElement('span');s.className=cls;s.setAttribute('aria-hidden','true');
    if(css)for(var k in css)s.style[k]=css[k];
    host.appendChild(s);s.addEventListener('animationend',function(){s.remove()});
  }
  document.querySelectorAll('.service-card,.bcard,.scard,.calc-card,.form-card').forEach(function(c){
    c.classList.add('rp-host');if(getComputedStyle(c).position==='static')c.style.position='relative';
    var last=0;
    c.addEventListener('pointerenter',function(e){
      var now=Date.now();if(now-last<500)return;last=now;
      var b=c.getBoundingClientRect(),x=e.clientX-b.left,y=e.clientY-b.top;
      var d=2*Math.hypot(Math.max(x,b.width-x),Math.max(y,b.height-y));
      var css={left:x+'px',top:y+'px',width:d+'px',height:d+'px'};
      spawn(c,'rp',css);spawn(c,'rp rp2',css);
    });
  });
  document.querySelectorAll('.btn').forEach(function(btn){
    btn.classList.add('rb-host');if(getComputedStyle(btn).position==='static')btn.style.position='relative';
    var last=0;
    btn.addEventListener('pointerenter',function(){
      var now=Date.now();if(now-last<700)return;last=now;
      spawn(btn,'rb');spawn(btn,'rb rb2');
    });
  });
})();
