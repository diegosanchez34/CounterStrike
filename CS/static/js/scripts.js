// -----------------------------------------------------------------------
// --------------------------- sonido de fondo ---------------------------
// -----------------------------------------------------------------------

const soundButton = document.getElementById('corneta');
const icon1 = document.getElementById('icono1');
const icon2 = document.getElementById('icono2');
const audioElement = document.getElementById('myAudio');

let isPlaying = false; // Track playback state

soundButton.addEventListener('click', () => {
  if (isPlaying) {
    audioElement.pause();
    icon2.style.display = 'inline-block';
    icon1.style.display = 'none';
  } else {
    audioElement.play();
    icon2.style.display = 'none';
    icon1.style.display = 'inline-block';
  }

  isPlaying = !isPlaying; // Toggle playback state
});


// -----------------------------------------------------------------------
// ---------------------------- sonidos menu -----------------------------
// -----------------------------------------------------------------------

const menuItems = document.querySelectorAll('ul.menu li');
const hoverSound = document.getElementById('hoverSound');

menuItems.forEach(menuItem => {
  menuItem.addEventListener('mouseover', () => {
    hoverSound.play();
  });
});

// -----------------------------------------------------------------------
// ------------------------------- modal 1 -------------------------------
// -----------------------------------------------------------------------

const botonAbrir = document.getElementById('abrirModal');
const modal = document.getElementById('miModal');

botonAbrir.addEventListener('click', () => {
  modal.style.display = 'block';
});

const botonCerrar = document.getElementById('cerrarModal');

botonCerrar.addEventListener('click', () => {
  modal.style.display = 'none';
});


// -----------------------------------------------------------------------
// ------------------------------- modal 1 -------------------------------
// -----------------------------------------------------------------------

const botonAbrir2 = document.getElementById('abrirModal2');
const modal2 = document.getElementById('miModal2');

botonAbrir2.addEventListener('click', () => {
  modal2.style.display = 'block';
});

const botonCerrar2 = document.getElementById('cerrarModal2');

botonCerrar2.addEventListener('click', () => {
  modal2.style.display = 'none';
});