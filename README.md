# pyPageScreenshot

**Install**  
virtualenv --distribute --setuptools pythonLib  
source pythonLib/bin/activate  
pip install -r requirements.txt  
cp chromedriver /usr/bin/  
apt-get install Xvfb  
chmod +x server.py  

**UP Server**  
./server.py

**Usage**  
<pre><code>http://127.0.0.1:4000/mandala/{mandala-query-string}</code></pre>  
<pre><code>http://127.0.0.1:4000/convert/{product-code}/{mandala-query-string}</code></pre>
<pre><code>http://127.0.0.1:3000/image/{product-code}</code></pre>
  
**Example**  
***Mandala renderizando com base na querie string***  
<pre><code>http://127.0.0.1:3000/mandala/SOL=303.384&LUA=182.086&MERCURIO=290.891&VENUS=268.581&MARTE=281.003&JUPITER=163.691&SATURNO=308.554&URANO=285.055&NETUNO=287.093&PLUTAO=232.661&ASCENDENTE=221.226&MEIODOCEU=120.64&DESCENDENTE=41.2263&FUNDODOCEU=300.64&CASA1=221.226&CASA2=250.374&CASA3=275.512&CASA4=300.64&CASA5=329.206&CASA6=3.48749&CASA7=41.2263&CASA8=70.3743&CASA9=95.5116&CASA10=120.64&CASA11=149.206&CASA12=183.487&AspectoP1=SOL&AspectoS1=LUA&TipoAspecto1=TRIGONO&AspectoP2=SOL&AspectoS2=SATURNO&TipoAspecto2=CONJUNCAO&AspectoP3=LUA&AspectoS3=VENUS&TipoAspecto3=QUADRATURA&AspectoP4=LUA&AspectoS4=SATURNO&TipoAspecto4=TRIGONO&AspectoP5=MERCURIO&AspectoS5=MARTE&TipoAspecto5=CONJUNCAO&AspectoP6=MERCURIO&AspectoS6=URANO&TipoAspecto6=CONJUNCAO&AspectoP7=MERCURIO&AspectoS7=NETUNO&TipoAspecto7=CONJUNCAO&AspectoP8=MERCURIO&AspectoS8=PLUTAO&TipoAspecto8=SEXTIL&AspectoP9=MARTE&AspectoS9=JUPITER&TipoAspecto9=TRIGONO&AspectoP10=MARTE&AspectoS10=URANO&TipoAspecto10=CONJUNCAO&AspectoP11=MARTE&AspectoS11=NETUNO&TipoAspecto11=CONJUNCAO&AspectoP12=JUPITER&AspectoS12=URANO&TipoAspecto12=TRIGONO&AspectoP13=JUPITER&AspectoS13=NETUNO&TipoAspecto13=TRIGONO&AspectoP14=URANO&AspectoS14=NETUNO&TipoAspecto14=CONJUNCAO&NUMASP=14&</code></pre>  

***Renderizando mandala e tirando um print***  
<pre><code>http://127.0.0.1:3000/convert/mjxdx_nXCmp-9OPTPyOz2QSA6Il1493OxBPmbQ-HYR8/SOL=303.384&LUA=182.086&MERCURIO=290.891&VENUS=268.581&MARTE=281.003&JUPITER=163.691&SATURNO=308.554&URANO=285.055&NETUNO=287.093&PLUTAO=232.661&ASCENDENTE=221.226&MEIODOCEU=120.64&DESCENDENTE=41.2263&FUNDODOCEU=300.64&CASA1=221.226&CASA2=250.374&CASA3=275.512&CASA4=300.64&CASA5=329.206&CASA6=3.48749&CASA7=41.2263&CASA8=70.3743&CASA9=95.5116&CASA10=120.64&CASA11=149.206&CASA12=183.487&AspectoP1=SOL&AspectoS1=LUA&TipoAspecto1=TRIGONO&AspectoP2=SOL&AspectoS2=SATURNO&TipoAspecto2=CONJUNCAO&AspectoP3=LUA&AspectoS3=VENUS&TipoAspecto3=QUADRATURA&AspectoP4=LUA&AspectoS4=SATURNO&TipoAspecto4=TRIGONO&AspectoP5=MERCURIO&AspectoS5=MARTE&TipoAspecto5=CONJUNCAO&AspectoP6=MERCURIO&AspectoS6=URANO&TipoAspecto6=CONJUNCAO&AspectoP7=MERCURIO&AspectoS7=NETUNO&TipoAspecto7=CONJUNCAO&AspectoP8=MERCURIO&AspectoS8=PLUTAO&TipoAspecto8=SEXTIL&AspectoP9=MARTE&AspectoS9=JUPITER&TipoAspecto9=TRIGONO&AspectoP10=MARTE&AspectoS10=URANO&TipoAspecto10=CONJUNCAO&AspectoP11=MARTE&AspectoS11=NETUNO&TipoAspecto11=CONJUNCAO&AspectoP12=JUPITER&AspectoS12=URANO&TipoAspecto12=TRIGONO&AspectoP13=JUPITER&AspectoS13=NETUNO&TipoAspecto13=TRIGONO&AspectoP14=URANO&AspectoS14=NETUNO&TipoAspecto14=CONJUNCAO&NUMASP=14&</code></pre>  
  
***Acessando imagem do print da mandala***  
<pre><code>http://127.0.0.1:3000/image/mjxdx_nXCmp-9OPTPyOz2QSA6Il1493OxBPmbQ-HYR8</code></pre>  
