window.addEventListener('DOMContentLoaded', function() {
  const loader = document.getElementById('loader');
  loader.style.display = 'block';

  setTimeout(function() {
    loader.style.display = 'none';
  }, 1200); 
});
