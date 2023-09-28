Supongamos que tenemos al estado de inicio 𝑖𝑛𝑖 y tenemos al estado 𝑚𝑒𝑡𝑎, porque se los hemos
pedido al usuario de nuestro programa. Entonces la distancia en línea recta entre cualquier estado 𝐴 y 𝐵
es:
𝑑𝑙𝑟[𝑒𝑑𝑜, 𝑚𝑒𝑡𝑎]
Luego supongamos que hemos decidido que nuestra función de costo es para llegar a un estado 𝑒𝑑𝑜𝑘
desde un estado 𝑒𝑑𝑜𝑘−1 es:
𝑔(𝑒𝑑𝑜𝑘) = 𝑑𝑙𝑟[𝑒𝑑𝑜𝑘−1, 𝑒𝑑𝑜𝑘] + 𝑔(𝑒𝑑𝑜𝑘−1)
Naturalmente que 𝑔(𝑖𝑛𝑖) = 𝑑𝑙𝑟[𝑖𝑛𝑖, 𝑖𝑛𝑖] = 0. Además, también hemos decidido que usaremos cono
función de valor heurístico a esta misma tabla de distancias en línea recta. Por ejemplo. El valor
heurístico de cualquier estado 𝑒𝑑𝑜 es su distancia en línea recta hacia la 𝑚𝑒𝑡𝑎:
ℎ(𝑒𝑑𝑜) = 𝑑𝑙𝑟[𝑒𝑑𝑜, 𝑚𝑒𝑡𝑎]
Así que todo lo que necesitamos para implementar cualquier técnica de búsqueda informada lo tenemos
ya en la tabla anterior. Así las cosas, implementemos usando el lenguaje de nuestra preferencia las
siguientes técnicas de búsqueda informada:
1. Búsqueda primero por lo mejor
2. Búsqueda avara
3. Búsqueda A*
Presentemos nuestros resultados en un reporte en formato PDF que incluya una breve descripción del
problema, una breve descripción de nuestra implementación, el código del script o programa que hemos
usado para implementar la solución, así como una captura de como el programa pide la información de
entrada (estados de inicio y meta) y como nos reporta el camino u orden de visita para llegar del estado
de inicio al meta.