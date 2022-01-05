from flask import Flask, render_template, request,  redirect, session, flash, url_for
from models import Movie
import dao 

def createDb():
    dao.create(Movie('A.I. Inteligência Artificial', '2001', 'Em um cenário futurista, robôs passam a conviver com humanos. A empresa Cybertronics cria um robô em forma de criança, chamado David, programado para amar os pais eternamente. Na iminência de perder o único filho, que está gravemente doente, o casal Henry e Monica decide adotar David. Mas, o filho deles se recupera da doença e David passa a ser visto como uma ameaça para o garoto.'))
    dao.create(Movie('1917', '2019', 'No auge da Primeira Guerra Mundial, em 1917, no norte da França, dois soldados britânicos, Schofield e Blake, recebem uma missão aparentemente impossível: atravessar um território inimigo para alertar outro batalhão britânico sobre uma emboscada mortal. Assim, eles correm contra o tempo para impedir que mais de 1600 soldados, incluindo o irmão de Blake, caiam na armadilha.'))
    dao.create(Movie('Zodíaco', '2007', 'Durante os anos 1960 e 70, um assassino chamado Zodíaco está aterrorizando São Francisco. Enquanto isso, três cartas diferentes chegam aos jornais da cidade. Com códigos secretos, elas trazem a confissão do assassino, mas precisam ser decodificadas. A polícia e os jornalistas fazem de tudo para descobrir a identidade de Zodíaco, mas o cartunista Robert Graysmith é o único a perceber o que está por trás das cartas: uma referência ao filme “Zaroff, o Caçador de Vidas” (1932).'))
    dao.create(Movie('O Labirinto do Fauno', '2006', 'Em 1944, a Guerra Civil Espanhola já terminou, mas um grupo de guerrilheiros ainda ocupa a região de Navarra. A pequena Ofélia está indo para lá com sua mãe, que está grávida. As duas irão viver com seu padrasto, um oficial do exército responsável por combater os rebeldes. Enquanto explora o jardim de sua nova casa, Ofélia se depara com um labirinto, habitado por um fauno. Esse ser místico diz à garota que ela é, na verdade, uma princesa perdida do submundo.'))
    dao.create(Movie('Onde os Fracos Não Têm Vez', '2008', 'Enquanto caça cervos, Llewelyn Moss encontra um traficante morto no deserto do Texas. Então, ele leva consigo uma grande quantidade de dinheiro que estava com o rapaz. Em busca da quantia perdida, o impiedoso assassino Chigurh começa a perseguir Moss. No entanto, para capturá-lo, ele terá de enfrentar o xerife da cidade, que também está procurando Moss. O filme é baseado no livro homônimo de Cormac McCarthy.'))
    dao.create(Movie('Arca Russa', '2002', 'Nos dias atuais, um homem é misteriosamente enviado a uma festa no Museu Hermitage no início do século 19. Guiado por um aristocrata, chamado apenas de “europeu”, ele assiste a um baile organizado pelo Imperador Alexandre I e observa várias figuras russas dos últimos 200 anos. Cada sala do palácio apresenta um período diferente da história do país.'))
    dao.create(Movie('Amor', '2012', 'Georges e Anne são um casal de aposentados apaixonado por arte. Eles estão aprendendo a lidar com os sinais da velhice, até que Anne sofre um enfarto de repente. A doença, aos poucos, se apodera de suas capacidades físicas e mentais. A filha do casal, Eva, mora em outro país e deseja que a mãe vá para um local onde receba cuidados especializados. Mas, George deseja continuar ao lado da esposa e cuidar dela em casa.'))
    dao.create(Movie('Melancolia', '2011', 'O filme se inicia com o casamento de Justine. Mesmo sendo um dia importante, ela sente uma profunda tristeza. E, ao perceber o desinteresse de Justine, seu noivo a abandona. Apresentando sintomas graves de depressão, ela vai morar com sua irmã, Claire, e seu cunhado, John. Enquanto isso, todos recebem a notícia de que um planeta que vaga pelo espaço, chamado Melancolia, está prestes a colidir com a Terra.'))
    dao.create(Movie('Dovgille', '2003', 'Em uma pequena cidade fictícia chamada Dogville, todos vivem sob as orientações de Thomas Edison Jr., um escritor que prega sermões à comunidade. Uma misteriosa mulher, Grace, pede refúgio em Dogville, dizendo que está sendo perseguida por um gângster. O povo tem medo de acolher a forasteira, mas Tom propõe que ela preste serviços às pessoas como prova de que merece ficar. O tempo passa e os moradores exigem cada vez mais favores à Grace.'))
    dao.create(Movie('A Rede Social', '2010', 'Em 2003, após levar um fora da namorada, Mark Zuckerberg, aluno de Harvard, cria um site para comparar a beleza dela com a das outras garotas, o Facemash. O site se torna um sucesso e Zuckerberg atrai outros estudantes de computação interessados em criar uma rede social inovadora, o Facebook. Poucos anos depois, Zuckerberg se torna um dos bilionários mais jovens do mundo, mas o sucesso traz muitas complicações para sua vida pessoal.'))
    dao.create(Movie('Retrato de Uma Jovem em Chamas', '2020', 'Na França do século 18, Marianne é uma jovem pintora contratada para fazer um retrato de Héloïse, sem que ela saiba. A mãe de Héloïse pretende enviar a pintura para um pretendente da filha, oferecendo-a em casamento. Como o plano é um segredo, durante o dia Marianne se disfarça como dama de companhia de Heloïse e passa as noites pintando. Com o passar do tempo, ela se apaixona por sua modelo.'))
    dao.create(Movie('Wall-E', '2008', 'Em 2815, a Terra é um lugar tóxico e coberto por lixo, por isso a humanidade deixa o planeta para viver em uma gigantesca nave. Robôs compactadores de lixo são programados para limparem a Terra por cinco anos, até que os humanos possam regressar. Mas, 700 anos se passam e Wall-E é o último robô ainda ativo. Quando a robô Eva chega misteriosamente à Terra, Wall-E se apaixona e decide segui-la.'))
    dao.create(Movie('Mad Max: Estrada da Fúria', '2015', 'Perseguido pelas lembranças do passado, Max Rockatansky acredita que a melhor forma de sobreviver é não depender de mais ninguém. Ainda assim, ele aceita se juntar a um grupo de rebeldes que atravessa Wasteland em uma máquina de guerra, conduzida pela imperatriz Furiosa. O bando está fugindo do tirano Immortan Joe, que inicia uma perseguição implacável aos insurgentes.'))
    dao.create(Movie('Cidade de Deus', '2002', 'O filme retrata o crescimento do crime organizado na Cidade de Deus, favela do Rio de Janeiro considerada uma das mais perigosas da capital. O drama é narrado pelo personagem Buscapé, um adolescente que encontrou na fotografia uma forma de retratar o cotidiano da favela. Ao contar sua história, Buscapé apresenta os conflitos violentos entre os líderes do tráfico na Cidade de Deus: Zé Pequeno, Bené e Cenoura.'))
    dao.create(Movie('O Cavalo de Turim', '2011', 'O filme inicia narrando um relato que teria ocorrido com o filósofo alemão Friedrich Nietzsche durante uma viagem. Ao avistar um cavalo sendo chicoteado pelo dono, ele interrompe a tortura e abraça o animal. A atitude do filósofo é vista como um indício de loucura. A partir deste episódio, a obra apresenta a possível história do cavalo defendido por Nietzsche.'))