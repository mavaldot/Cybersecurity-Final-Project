
# INFORME

## Elaboración del programa

Como lenguaje de programación, elegimos Python, puesto que es un lenguaje que permite desarrollar aplicaciones de manera fácil, rápida y eficiente. También cuenta con una amplia colección de librerias y una gran comunidad.

Para la UI, elegimos la librería Tkinter de Python, puesto que es fácil y rápida de usar. Además, tenemos experiencia previa con Tkinter. 

En cuanto al desarrollo de la aplicación, lo primero que se hizo fue generar la llave privada y la llave pública (key pair) mediante el algoritmo RSA (el algoritmo está disponible en el artículo de Wikipedia de RSA: https://en.wikipedia.org/wiki/RSA_(cryptosystem) ). 

Escoger dos números primos $p$ y $q$ 

$n = pq$

$λ = lcm(p -1, q - 1)$

Escoger un número $e$ tal que $e$ y  $λ$ son coprimos y $1 < e < λ$

$d ≡ e^{-1}(mod (λ))$
