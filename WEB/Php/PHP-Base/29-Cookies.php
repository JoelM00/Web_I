<?php
//Cookie

setcookie('user','Joel Martins',time()+3600);
setcookie('email','jsmartins2000@homtimail.com',time()+3600);
setcookie('ultima_pesquisa','tenis adidas',time()+3600);

echo $_COOKIE['ultima_pesquisa'];
