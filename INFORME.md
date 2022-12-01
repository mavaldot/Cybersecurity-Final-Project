
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

La llave pública es conformada por los números n y e (la e representa encriptación). La llave privada es conformada por los números n y d (la d representa desencriptación), y está protegido por una contraseña que el usuario elija. Después de generar el par de llaves, se puede firmar un archivo digitalmente utilizando esas llaves. Para esto, se creo una función que toma como parámetros el archivo, la llave privada y la contraseña. Esta función crear un hash sha256 del archivo y los encripta utilizando la llave privada para obtener un archivo con la firma.

Para verificar la firma, se creó una función que toma como parámetros el archivo, la llave pública y la firma. Esta función obtiene el hash sha256 del archivo, y utiliza la llave pública para desencriptar la firma (en RSA, la llave pública puede desencriptar los archivo que han sido encriptados con la llave privada, y la llave privada puede desencriptar los archivos que han sido encriptados con la llave pública). El hash sha256 del archivo es comparada con la firma desencriptada, y si son iguales la función retorna True. De lo contrario, retorna False.
