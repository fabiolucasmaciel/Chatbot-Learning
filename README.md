# Chatbot-Learning
Um projeto de chatbot simples, de linha de comando em python, que é ensinado a cada interação pelo usuário, e armazena informações em JSON.

# Explicação por partes da execução Chatbot
 
|  Execução | Explicação  |
|---|---|
|![ficha](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Ficha.png)|<ul> <li>No início se informaa se a intenção é criar um bot novo, depois se diz o nome do bot desejado, seja novo ou existente.</li> <li>Se o bot for novo você deve-se ensiná-lo, no exemplo o bot já existe, então fomos levados à ficha.</li> <li>Na ficha dizemos o nome e se desejamos ensinar esse bot, se for permetido.</li></ul> |
|  |  |
|![chat](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Chat.png)   | <ul> <li>Escolhemos falar com o Chatbot chamado bot, o básico.</li> <li>Logo apos o ficha o bot se apresenta com uma de suas frases gravadas e  cumprimenta o usuario, o cumprimento muda se o bot conheça usuário</li> <li>Ele responde ao oi e a pergunta do seu nome, que são as primeiras coisas que ele aprende a responder.</li> </ul>  |
| |  |
|![comandos](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Comandos.png)| <ul> <li>Existem comandos para o chatbot.</li> <li>o comando "~help" mostra uma ajuda.</li> <li>o "~learn" serve para ensinar o chatbot vom mais velocidade.</li> <li>Todos os comandos começam com ~.</li></ul>
|   |   |
|![ensinando](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Ensinando.png)| <ul> <li>O bot não entendeu a frase "Bom dia", nesse caso pode-se ensiná-lo.</li> <li>Apos confirmar o ensino, se digita as 3 frases de respostas ao "Bom dia".</li> <li>Uma dessas 3 frases será escolhida como resposta caso o bot receba "Bom dia".</li> <li>As respostas são salvas em JSONs do bot, e são escolhidas aleatóriamente.</li></ul>
|   |   |
|![teste](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Teste.png)| <ul> <li>O usuário digitou "Bom dia" depois de ensinar.</li> <li>As 2 primeiras respostas foram as frases ensinadas.</li> <li>Na terceira resposta o bot tenta mudar de assunto, percebendo a repetição.</li> <li>O bot as vezes puxa um assunto que ele gosta ou diria que o usuario está digitando a mesma coisa, isso quando a frase for a mesma sempre.</li></ul>
|   |   |
|![fim](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Fim.png)| <ul> <li>O usuário se despediu do chatbot.</li> <li>Quando o bot entendeu a intençõa, ele responde com uma frase de despedida.</li> <li>Após isso a execução termina.</li></ul>
|   |   |
|![criando](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/execu%C3%A7%C3%A3o/Criando.png)| <ul> <li>Agora, se o usuario tivesse optado por criar um novo bot.</li> <li>Ele escolhe um nome para o bot novo, o nome deve ser novo também.</li> <li>Depois ele deve ensinar todas as frases basicas desse bot.</li> <li>Ensina cumprimentos, descrição do bot, despedida, assuntos que gosta, como responder caso não entenda, e mais coisas.</li></ul>
|   |   |


# Explicação por partes do código Chatbot
## Main
 
|  Código | Explicação  |
|---|---|
|![imports](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/main/imprte_var.png)|<ul> <li>Bibliotecas necessárias e declaração de variáveis. </li></ul> |
|  |  |
|![botname](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/main/bot_nome.png)|<ul> <li>Recebe o nome do bot. </li></ul> |
|  |  |
|![botini](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/main/bot_ini.png)|<ul> <li>Inicia a classe bot com as info recebidas. </li></ul> |
|  |  |
|![loopbot](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/main/loop_bot.png)|<ul> <li>Loop de chat com bot. </li></ul> |
|  |  |

## Classe Chatbot e init
 
|  Código | Explicação  |
|---|---|
|![imports](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/imports.png)|<ul> <li>Bibliotecas necessárias. </li></ul> |
|  |  |
|![init](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/classe_init.png)|<ul> <li>classe do bot e seu init. </li></ul> |
|  |  |
|![novobot](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/novo_bot_if.png)|<ul> <li>Cria bot caso seja novo. </li></ul> |
|  |  |
|![direc](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/dir_if.png)|<ul> <li>Confere existencia de diretorios. </li></ul> |
|  |  |
|![dirfrases](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/dir_if_frases.png)|<ul> <li>Confere existencia de arquivos com frases. </li></ul> |
|  |  |
|![conheci](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/conhecidos.png)|<ul> <li>Puxa arquiva de conhecidas ou cria ele. </li></ul> |
|  |  |
|![naosabe](https://github.com/fabiolucasmaciel/Chatbot-Learning/blob/main/assets/classe%20chatbot/not_know_var_listas.png)|<ul> <li>Exemplo de como são os arquivos de frases do bot. </li></ul> |
|  |  |

## Aprendizagem
 
|  Código | Explicação  |
|---|---|
|![lib](https://github.com/paulovitornovaes/project_threads/blob/9a4c6c73fe0b4307746f37d7526cab76f47109b9/part_1/assets/library_part1.png)|<ul> <li>Bibliotecas necessárias. </li></ul> |
|  |  |

## Menu e Ficha
 
|  Código | Explicação  |
|---|---|
|![lib](https://github.com/paulovitornovaes/project_threads/blob/9a4c6c73fe0b4307746f37d7526cab76f47109b9/part_1/assets/library_part1.png)|<ul> <li>Bibliotecas necessárias. </li></ul> |
|  |  |
## Escuta, Pensa e Fala, o cérebro do chatbot
 
|  Código | Explicação  |
|---|---|
|![lib](https://github.com/paulovitornovaes/project_threads/blob/9a4c6c73fe0b4307746f37d7526cab76f47109b9/part_1/assets/library_part1.png)|<ul> <li>Bibliotecas necessárias. </li></ul> |
|  |  |

## Organizção de arquivos e Tratamentos
 
|  Código | Explicação  |
|---|---|
|![lib](https://github.com/paulovitornovaes/project_threads/blob/9a4c6c73fe0b4307746f37d7526cab76f47109b9/part_1/assets/library_part1.png)|<ul> <li>Bibliotecas necessárias. </li></ul> |
|  |  |

# Conclusão e Links
Um projeto de chatbot simples, de linha de comando em python, que é ensinado a cada interação pelo usuário, e armazena informações em JSON.
