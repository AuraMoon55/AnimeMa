const gototop = document.getElementById("gotop");



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
