var btMenu = document.getElementById("menu-mobile");
var menu = document.getElementById("menu");

btMenu.addEventListener('click', function(e) {
    if (menu.style.display == 'flex') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'flex';
    }
    e.preventDefault();
});

