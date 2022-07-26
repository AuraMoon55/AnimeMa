const gototop = document.getElementById("gotop");
const scri = document.getElementById("trans")
const ua = navigator.userAgent


setTimeout(function() {
  document.querySelectorAll('.succ-rem').forEach(but => {
    but.remove();
  });
}, 5000);

setTimeout(function () {
  document.querySelectorAll('.err-rem').forEach(but => {
     but.remove();
    });
}, 5000);



gototop.addEventListener(
  "click", (e) => {
    window.scrollTo(
      {
        top: 0,
        behavior: 'smooth'
      }
    )
  }
)


window.onload = function(e){
  if (/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)){
    return scri.setAttribute("href", "{{url_for('static',filename='light.css')}}");
  } else {
    return;
  }
}
