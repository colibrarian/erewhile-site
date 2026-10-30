/* Preview screens start "switched off" (see .crt-off in the page CSS).
   With a mouse they switch on by hover or focus (pure CSS). On touch screens there is no hover,
   so a card switches on while it sits in the middle band of the viewport and off when it leaves. */
(function(){
  if(!window.matchMedia||!matchMedia('(hover: none)').matches||!('IntersectionObserver' in window))return;
  var cards=document.querySelectorAll('.crt-off .bcard, .crt-off .scard, .crt-off .gallery-card');
  if(!cards.length)return;
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){e.target.classList.toggle('lit',e.isIntersecting);});
  },{rootMargin:'-30% 0px -30% 0px'});
  cards.forEach(function(c){io.observe(c);});
})();
