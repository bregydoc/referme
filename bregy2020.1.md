---
abstract: |
  Este artículo revisa tres modelos o paradigmas de computación, además
  de algunas implementaciones físicas de dichos modelos,
  específicamente: computación con autómatas celulares (Cellular
  Automata Computation), computación neuromórfica (Neuromorphic
  Computation) y computación basada en vida (Living Computation).
  Encontraremos relación entre estos modelos y veremos lo importante que
  es buscar el entendimiento de la computación y su naturaleza
  fundamental. La finalidad del artículo es conseguir que el lector
  adquiera un modesto panorama de algunas de las diferentes vías que
  tenemos para seguir el modelamiento y el desarrollo de nuestros
  dispositivos de cómputo y cálculo, que cumplen un rol fundamental en
  el desarrollo tecnológico de nuestra especie.
author:
- 
bibliography:
- ./bibliography/IEEEabrv.bib
- ./bibliography/references.bib
title: Modelos no tradicionales de computación y algunas de sus
  implementaciones hardware
---

# Introducción

Los dispositivos de computación pueden ser vistos como una consecuencia
de la necesidad de nuestra especie por interactuar con su medio, una
forma de entender la tecnología humana es como la externalización que
realiza el hombre de su memoria en su medio, es decir, una forma de
extender sus capacidades perdurando información en medios externos
(normalmente inorgánicos). El hardware computable se puede entender como
una plataforma para el procesamiento de información. El procesamiento de
dicha información puede llevarse a cabo por medios físicos (mecánicos,
eléctricos, magnéticos, etc)
[@duchesneau2014computing][@piccinini2010computation]. La naturaleza
física de varios procesos computables nos permiten aprovechar dicha
computación para poder robustecer el desarrollo y la usabilidad de
nuestra tecnología. En este artículo se hará una revisión del desarrollo
de hardware computable que se ha llevado a cabo en los últimos años, se
partirá de los tiempos modernos y no se hará enfasis en la historia
analógica del hardware para computación, teniendo como punto de
referencia el año 1936, en el que A. Turing publicó su paper con un
formalismo para computadora universal
[@turing1936a][@dodig2011significance][@eberbach2004turing] que dio paso
a la teoría de la computación moderna.

## ¿Qué es computación?

La definición de \"computación\" es bastante general, cuenta con muchos
enfoques y tiene múltiples interpretaciones [@turing2009computing]. Sin
embargo, para tener un punto de partida razonable podemos aceptar la
veracidad de la tesis Church-Turing, donde todo modelo de computación
posible y físicamente realizable no es más poderoso que una Máquina de
Turing [@Ben-amram06thechurch-turing][@eberbach2004turing]. Si esto es
así, entonces, aunque tengamos muchas formas de expresar las cosas, en
última instancia, podemos reducir cada \"computación\" a una Máquina de
Turing, obteniendo la definición de computación cómo \"todo aquello que
podamos reducir a una Máquina de Turing\". Si bien esta definición nos
deja con más preguntas por responder, nos sirve para tener un marco
formal desde donde partir ya que el modelo de Maquina de Turing es un
modelo lógico que ha sido consolidado con el paso del tiempo
[@arora2009computational].

## Sobre hardware para computación

El hardware para computación se puede enteder como un medio para el
procesamiento/transformación de información. En un amplio sentido, la
mayoría de herramientas que el humano construye sirven en la realización
de la transformación de dicha información. A lo largo de la historia del
hombre, dichas herramientas se han ido sofisticando hasta llegar a donde
nos encontramos actualmente. Hemos sabido aprovechar la naturaleza de
nuestro medio y así hemos conseguido sintetizar \"la computación\" en
diferentes herramientas (piezas de tecnología) que nos sirven para
seguir destilando nuestra tecnología. El alcance de este artículo se
limita a describir los últimos modelos de hardware para computación
digital.

## Computación digital

La computación digital fue definida G. Stibitz como aquella computación,
en donde la señal, como un voltaje en el tiempo, no es usada
directamente para representar un valor, si no, para codificarlo
[@dennhardt2014]. Las bases matemáticas de la computación digital se
apoyan en el álgebra booleana [@shannon1938]. Los modelos de computación
y hardware para computación que revisaremos en este artículo hacen uso
de este tipo de computación (digital).

# Modelos estándar

Es importante hablar de un modelo que ha sido el que ha dirigido el
desarrollo de hardware para computación en los últimos años: La
arquitectura de Von Neumann [@poznanovic2006].

## La arquitectura Von Neumann

La arquitectura de computación digital de Von Neumann es una
arquitectura de máquina de computación que se caracteriza por tener dos
etapas bien definidas y delimitadas: la unidad de proceso y control, y
la unidad de memoria, ambas partes conectadas por un bus de datos, que
además, tiene la capacidad de almacenar las instrucciones en su unidad
de memoria [@poznanovic2006] [@neumann1945]. Este concepto ya había sido
descrito por A. Turing en su modelo de Máquina Universal de Turing que
plantea una máquina capaz de simular cualquier otra Máquina de Turing
arbitraria con una entrada arbitraria
[@turing2009computing][@eberbach2004turing] [@aspray1990john]. Para
conseguir esto, la máquina universal almacena en su memoria la
descripción de la máquina a simular. Este modelo, ha sido una gran
influencia en la línea que ha seguido el desarrollo de hardware para
computación, pero también existen otros modelos que no siguen esta línea
de desarrollo, y que son de los que se habla en este artículo.

# Cellular Automata Computation

Un automata celular es un modelo computacional que puede ser descrito
como un sistema digital con una red de autómatas finitos. El concepto de
autómata celular ofrece un elegante modelo computacional concurrente de
interacción local, en el que la tarea de computación es realizada a
traves de la evolución de su estado global [@dascalu2016cellular]. Esta
característica concurrente y distribuida es totalmente diferente en
estructura a los modelos clásicos, secuenciales y centralizados que han
tenido mayor popularidad en los anteriores años [@poznanovic2006]. Von
Neumann fue, de manera sorpresiva, uno de los pioneros de la computación
y realizó un trabajo sobre máquinas auto-replicantes que inspiró muchos
trabajos alrededor de estos mecanismos (auto-replicantes)
[@poznanovic2006] [@chou1998self] [@aspray1990john], estos trabajos
promovieron el desarrollo de diversos modelos de autómatas celulares
[@poznanovic2006]. Varios estudios teóricos fueron realizados por S.
Wolfram, que propuso, entre otras cosas, una clasificación
fenomenológica a los distintos modelos de automatas celulares
[@wolfram2018].

## Hardware para un autómata celular general

La versión de hardware de un autómata celular debería de consistir en
una red de máquinas de estado finito con un número máximo predefinido de
estados, y un circuito lógico programable con un número de entradas que
depende de la topología de interconexión [@poznanovic2006]. La
construcción de un hardware que permita la operación de un autómata
celular general debería tener las siguientes características
[@poznanovic2006]:

-   Ser capaz de implementar cualquier regla local.

-   Poder implementar topologías no-homogéneas teniendo vecindades
    no-homogéneas y reglas locales no-homogéneas.

-   Poder definir diferentes condiciones para el perímetro (en el modelo
    teórico es infinito).

La utilidad de este hardware yace en la capacidad de poner a prueba
distintos modelos de autómata celular y así evaluar distintas
aplicaciones en este modelo de computación. Un ejemplo de este trabajo
es The BioWall, un hardware para autómata celular general que fue
implementado teniendo en cuenta principios de generación embrionaria
[@tempesti2002biowall]. Este proyecto dejó un framework sobre el que se
pueden implementar distintos modelos de autómata celular cómo
self-replicating loops [@tempesti2012], constructores de Von Neumann
[@chou1998self], Turing Neural Networks [@poznanovic2006], entre otros.

## Algunas aplicaciones específicas del hardware para autómata celular

Las diferentes implementaciones reportadas en la literatura científica
se encuentran como soluciones de hardware dedicadas a aplicaciones
específicas y no como máquinas de cómputo general. Muchas de estas
implementaciones son también realizadas en hardware reconfigurable como
FPGAs [@poznanovic2006]. Entre las aplicaciones más resaltantes se
encuentran los modelos físicos como autómatas celulares de
Greenberg-Hastings [@tamayohartman1995] o modelos de reacción-difusión
[@adamatzky2005reaction]. Uno de los trabajos más recientes en las
aplicaciones de autómatas celulares es un modelo que hibrida redes
neuronales y autómatas celulares en un modelo diferenciable de
morfogénesis [@mordvintsev2020growing]. Este trabajo es prometedor, ya
que abre las puertas a una generalización en las aplicaciones autómatas
celulares, y que además impactaría directamente en las aplicaciones de
hardware para computar este tipo de modelos (autómatas celulares)
dotándolos de aplicaciones para computación general.

# Neuromorphic Computation

Computación Neuromórfica es un concepto creado por C. Med a finales de
los años 80 [@chen2018neuromorphic] y que describe el uso de sistemas
VLSI que contienen componentes analógicos que emulan arquitecturas
neuro-biológicas presentes en nuestro sistema nervioso
[@chen2018neuromorphic]. Este tipo de computación tiene como mayor
cualidad el procesamiento paralelo y distribuido, esto se consigue al
emular el comportamiento biológico de las neuronas. Específicamente, se
busca distribuir el procesamiento y la memoria a través de diferentes
unidades de cómputo usando un mecanismo llamado \"neuronal signaling\",
este mecanismo requiere de que las unidades de procesamiento también
tengan la capacidad de perdurar información, es decir que la unidad
combinen procesamiento y memoria al mismo tiempo.

## Los Memristores

Los memristores son dispositivos electrónicos de memoria no volátil que
fueron teorizados en 1971 por L. Chua como uno de los cuatro elementos
electrónicos fundamentales de dos terminales después del resistor, el
capacitor y el inductor [@chua1984nonlinear]. La mayor característica de
estos dispositivos es su propiedad de alterar su resistencia modificando
su voltaje y que este nuevo estado sea almacenado incluso perdiendo la
alimentación eléctrica [@upadhyay2019emerging] [@jeong2016memristors].
Una de las limitantes actuales con estos dispositivos electrónicos es su
implementabilidad física; aunque se han logrado avances
[@jeong2016memristors], aún tenemos límites para poder llevar esta
tecnología a una escala de provecho. Como ya se dijo anteriormente, una
de las necesidades de la computación neuromórfica es que cada unidad de
procesamiento (símil de neurona) tenga la capacidad, también, de
perdurar un estado determinado (peso sináptico), es aquí en donde entran
a tallar los memristores. Los memristores tienen características que lo
convierten en un buen modelo de las sinapsis en el cerebro humano, ambos
comparten la misma característica de conmutación: el ser capaz de
modificar la eficiencia de la transferencia de las señales usando la
influencia de la misma transferencia
[@jeong2016memristors][@sung2018perspective]. Recientemente, se ha
desarrollado un nuevo dispositivo memristivo a base de capas de
di-sulfuro de molibdeno e iones de litio entre ellos
[@zhulilianglu2018ionic]. Dicho dispositivo tiene la capacidad de
cambiar el ordenamiento de sus átomos de molibdeno en presencia o
ausencia de átomos de litio [@zhulilianglu2018ionic]. Este dispositivo
emula adecuadamente el comportamiento competitivo y cooperativo presente
en las conexiones neuronales, esto lo hace un buen análogo de las
sinapsis neuronales biológicas.

# Living Computation

Living Computation es un concepto/paradigma de computación que busca
entender a los organismos vivos como sistemas de computación de los
cuales podemos extraer distintos mecanismos para conseguir una
revolución en nuestros modelos computacionales [@aguilar2014thepast] En
última instancia, se propone que la computación intrínseca en distintos
organismos vivos es la que debería guiar nuestro desarrollo
computacional y así conseguir reducir el gap entre el software y el
hardware [@aguilar2014thepast]. Según D. Ackley, las formas en que la
vida debería guiar nuestro diseño de computación son las siguientes:

-   Entender a la computación como un proceso consecuencia de la
    interacción. Este es un enfoque totalmente distinto a la idea
    tradicional de computación algorítmica y procedural [@lynn1998what]
    [@wegner1997interaction].

-   Entender a los programas (de computadora) como entidades físicas,
    estos ocupan actualmente un espacio físico, en la memoria RAM, el
    disco, o en cualquier otro dispositivo físico (media). Mientras un
    programa ocupa un determinado lugar físico, ningún otro puede
    existir en aquel medio físico, además cuando un programa está en
    ejecución, este consume a través de el CPU, es decir, como
    consecuencia de la instancia de programa. \[ref. needed\]

En mi opinión, la vida opera bajo el mismo marco de computabilidad que
opera cualquier otro sistema físico, en ese sentido, los organismos
vivos son análogos directos a nuestras computadoras. La idea de asimilar
a la computación como un fundamento de la naturaleza nos obliga a
entender a todos los procesos computables como equivalentes. Esto último
también lo sostiene S. Wolfram con su principio de equivalencia
computacional [@wolfram2002new] [@flake1998computational].

# Conclusiones

Hemos revisado tres enfoques sobre computación no clásicos. Dichos
modelos de computación, y sus respectivas implementaciones físicas,
guardan una relación estrecha en que se promueve un cambio de paradigma
en la idea de cómo concebimos la naturaleza de la computación. La
finalidad de comprender a la computación y su naturaleza es conseguir
interactuar de manera más profunda con nuestra realidad. El hombre está
cada vez más cerca de crear su propia realidad y uno de los posibles
requisitos para hacerlo es comprender el fundamento que subyace en
nuestra actual, y ya existente, realidad, aquella realidad en la que
estamos y con la que interactuamos.
