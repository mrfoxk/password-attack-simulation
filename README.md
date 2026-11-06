# Password Attack Simulation


## :: Introdução

Este repositório conta toda minha trajetória pelo modulo **criando um ataque de brute force de senhas com medusa e kali linux** um modulo do Bootcamp de Cibersegurança da Dio.me

Abaixo vou contar minha trajetória, prints interessantes das partes mais legais da minha trajetória e o que eu aprendi sobre cada tema do curso, achei muito legal esse curso pois ele conta desde a parte explicativa, que inclusive explicou bem cada parte, quanto pela parte prática onde tive também a oportunidade de montar um laboratório de testes e realizar as simulações o que me proporcionou uma compreensão mais aprofundada de como as ferramentas funcionam na pratica.


| Ferramenta | O que eu entendi de cada assunto | 
| --- | --- |
| Hydra | Realiza ataques de força bruta, ou seja eles testam combinações ate encontrar alguma valida utilizando as chamadas "Wordlists" que sao arquivos de texto com gigas e mais gigas de senhas das quais o sistema vai automatizar o ataque de forma rápida e precisa, compatível com varios protocolos da internet como SSH, FTP, TelNET, SMB, MySQL entre outros, essa ferramenta representa um verdadeiro risco se voce usa senhas fracas, previsíveis, ou usa as mesmas senhas desde muitos anos... | 
| Ncrack | Pelos mesmos criadores do Nmap, esta ferramenta e uma versão tao poderosa quanto Hydra, enquanto o hydra e focado principalmente em ataques direcionados, o Ncrack foi concebida para realizar o ataque a uma lista de alvos, realiza um gerenciamento mais avançado da rede, por exemplo controlando a velocidade do trafego para nao travar as conexões ou derrubar o serviço, ele e capaz de encontrar senhas padrão ou fracas em SSH, FTP, RDP entre outros, ele e especialmente perigoso pelo fato de ser capaz de literalmente varrer redes inteiras em busca de servidores com senhas fracas ou vazadas ou configurações mal feitas.. | 
| John | Esta é particularmente interessante, focada especialmente em arquivos locais. O John possui diversos módulos independentes projetados para quebrar senhas em arquivos de diferentes formatos, desde PDF, ZIP, RAR, até documentos do Microsoft Office, além de diversos outros formatos. Ele também quebra hashes de formatos mais conhecidos como SHA1 e MD5, até formatos mais específicos como hashes de sistemas Windows, por exemplo. No geral, ele realiza ataques com dicionário, ataques de força bruta (onde a senha é calculada sequencialmente pelo programa, ex: AAAAAAAA, AAAAAAAB, AAAAAAAC...) e também ataques híbridos. É uma ferramenta especialmente poderosa contra arquivos protegidos por senhas fracas, algoritmos antigos, ou credenciais repetidas e vazadas. Não é porque você definiu uma senha para o arquivo que ele está totalmente seguro, por isso é importante sempre garantir a utilização de senhas fortes e proteger os arquivos importantes contra vazamentos também.
| WPScan | Esta é particularmente interessante. Ela é focada especificamente em auditoria e teste de intrusão em instalações do WordPress, realizando várias operações como, por exemplo, a enumeração de nomes de usuário e de plugins da instalação, identificando complementos mal configurados ou desatualizados. Esta ferramenta chama a atenção pelo fato de mostrar que se você tem um site em WordPress e ele possui um tema ou plugin desatualizado, ele realmente pode estar em risco. O WPScan também é capaz de realizar ataques de força bruta contra as credenciais de login dos usuários encontrados. Um dos grandes diferenciais dele é a sua integração direta com o banco de dados de vulnerabilidades mantido pela própria equipe do WPScan, o que garante que o escaneamento identifique falhas de segurança reais e atualizadas constantemente. |
| Patator | Voltada para usuários mais avançados, esta ferramenta oferece um nível de customização superior ao Hydra. O Patator permite que o atacante configure praticamente todos os aspectos do ataque, como cabeçalhos (headers) HTTP, tempos de espera, parâmetros enviados, formatos de resposta e até mesmo o comportamento exato do sistema em caso de falhas. Ele suporta múltiplos protocolos e é ideal quando o atacante precisa de um ajuste fino para contornar defesas específicas, como mecanismos anti-bruteforce ou captchas leves. É extremamente útil, por exemplo, em cenários onde o sistema de login não informa diretamente se o usuário ou a senha estão incorretos, mas apresenta tempos de resposta diferentes caso o usuário exista ou não (devido ao processamento interno do servidor). O Patator consegue identificar essas micro variações de tempo e utilizá-las para realizar a enumeração de contas válidas. |
| Medusa | Uma ferramenta voltada para ataques de força bruta em rede com foco em velocidade, estabilidade e escalabilidade. Ela suporta dezenas de protocolos populares, como SSH, FTP e SMB, entre outros. É muito utilizada quando é necessário testar listas massivas de usuários ou senhas em paralelo, graças à sua capacidade nativa de trabalhar com múltiplas conexões simultâneas (threads). Também permite utilizar parâmetros altamente personalizados, sendo uma excelente escolha para realizar testes de autenticação em serviços de rede quando o objetivo é alinhar desempenho máximo e paralelismo eficiente.

---

## :: Montando o laboratorio com Kali Linux & Metasploitable 2

- Para acompanhar o curso eu realizei o download do Metasploitable 2 através do link https://sourceforge.net/projects/metasploitable/.

- Para baixar o Kali Linux utilizei o site oficial https://www.kali.org/get-kali/#kali-platforms.

Meu laboratório então ficou:

### 🖥 Servidor: Metasploitable 2
IP: 192.168.56.101

### 💻 Kali: Kali Linux 2026.2
IP: 192.168.56.102

Utilizei ambas as maquinas com a seguinte configuração: 

![test](<images/Captura de tela 2026-11-04 214901.png>)

Desta forma ambas as maquinas poderiam se ver na mesma rede sem que nenhuma delas tivesse acesso direto a internet.


## :: Exercicio 1 . Ataque ao Servico FTP

Vou chamar de Exercícios para fins de organização, neste exercício basicamente realizamos um ataque de brute force com listas de usuários e senhas, em ambientes reais sao utilizados técnicas de enumeração para obter nomes de usuário ou simplesmente e utilizado listas de nomes comuns de usuários, mesma coisa vale para a senha, em uma organização real um atacante poderia tentar obter na internet uma lista de senhas vazadas ou então utilizar uma das wordlists publicas de senhas mais comuns, para fins didáticos criamos um arquivo de nome **users.txt** e o arquivo **pass.txt** como voce pode ver abaixo:

![test](<images/Captura de tela 2026-11-04 220202.png>)

Voce pode observar também dois arquivos, um deles foi o **fox.txt** e o outro **saida_comando_medusa.txt**, o arquivo de nome fox eu criei originalmente no Metasploitable 2 com o intuito de realizar o download dele no serviço FTP para testar como esse cliente FTP no linux funciona (Usa-se o comando get < nome_do_arquivo> para realizar o download..), ja o arquivo saida_comando_medusa.txt foi basicamente porque eu rodei o comando do ataque utilizando o parâmetro ">>" para redirecionar para um arquivo, uma boa prática uma vez que se voce limpar o terminal logo apos a exploração ira ter que rodar tudo de novo.. inclui estes arquivos neste repositório voce pode olhar se quiser..

Com os arquivos necessários ja criados chegou a hora de montar o comando, montei o comando e realizei o teste como voce pode observar na imagem abaixo:

**Comando executado:**
``` bash
medusa -h 192.168.56.101 -U users.txt -P pass.txt -M ftp -t 6
```

![test](<images/Captura de tela 2026-11-04 195930.png>)

Como podemos observar temos uma saída destacada, nela podemos ver um ACCOUNT FOUND, ou seja, sim temos uma conta onde a senha foi bem sucedida! O usuário foi o msfadmin e a senha msfadmin, então realizei o teste pra ver se era possível de fato realizar o login:

**Comando executado:**
```bash
ftp msfadmin@192.168.56.101
```

![test](<images/Captura de tela 2026-11-04 200407.png>)

Como foi observado o login foi bem sucedido, inclusive quis rodar um ls pra listar os arquivos da pasta do usuário logado, funcionou perfeitamente, conseguimos!

## :: Exercicio 2 . Ataque a um portal de login web: DVWA

DVWA ou Damn Vulnerable Web Application na sua tradução literal Aplicação Web Deliberadamente Vulnerável, este e um site web com muitas vulnerabilidades para que voce possa testar em ambiente isolado suas vulnerabilidades para fins de estudo e aprender a utilizar as ferramentas da forma correta..

Então entrei no link informado na aula que no meu caso era http://192.168.56.101/dvwa/ e pude observar a tela de login do nosso portal, uma informação interessante e que quando voce insere um usuário e uma senha ele gera uma requisição para /dvwa/login.php, a mesma e do tipo POST e contem os parametros de login "username", "password" e também um campo extra de nome "Login" que recebe como parâmetro padrão "Login" que temos que replicar.. então meu teste ficou basicamente assim:

**Comando executado:**
```bash
medusa -h 192.168.56.101 -U users.txt -P pass.txt -M http -m PAGE:'/dvwa/login.php' -m FORM:'username=^USER^&password=^PASS^&Login=Login' -m 'FAIL=Login failed' -t 6
```

![test](<images/Captura de tela 2026-11-04 200907.png>)

Um detalhe importante é que depois do login ser realizado, todas as requisições abaixo pelo fato de compartilharem o mesmo cookie de sessão no navegador foram aceitas também, porém foi configurado 6 threads, então sim, muitos falsos positivos povoaram nosso log.. Infelizmente, pesquisando sobre o problema, descobri que o motivo é basicamente o cookie de sessão do PHP, que depois de logado responde as demais requisições como logadas também.. Infelizmente não encontrei uma forma prática de corrigir isso, uma solução seria o Medusa reiniciar o cookie de sessão a cada vez que fosse realizar uma nova tentativa, porém infelizmente a ferramenta não possui essa funcionalidade.. Então, o que resta fazer a partir deste ponto é basicamente testar cada uma das informações corretas até encontrar qual delas foi bem-sucedida.

Depois de uma busca encontrei uma das requisições a qual foi bem sucedida, nome do usuário era "admin" e a senha era "password" presente no log, então sim a operação deu certo apesar do contratempo.

## :: Exercicio 3 . Ataque ao SMB: Entendendo o ataque a servidores de compartilhamento de arquivos Samba.

### Enumeração:

Esta parte foi a minha favorita, nela foi abordado basicamente duas etapas, uma delas foi a enumeração onde foi utilizado o **enum4linux** para enumerar os usuários no sistema, e o **medusa** para tentar poucas senhas para muitos usuários, uma prática que eu para falar a verdade nao conhecia ainda.. e faz completo sentido visto que o sistema de detecção provavelmente nao ira detectar isto se nao for previamente configurado para o mesmo.. então vamos começar.. eu fiz um procedimento um pouco diferente do curso nesta parte então quero deixar registrado o que eu fiz..

1. Eu joguei a saída do comando para um arquivo: basicamente eu utilizei o operador **pipe** e o comando tee para jogar a saída do comando para um arquivo.

2. Minha parte favorita, utilizei o VIM para abrir o arquivo e observei que a sessão que se referia aos usuários possuía um padrão especifico então criei um script em Python para extrair os nomes dos usuários do restante do arquivo:

Observei que o arquivo de saída possuía basicamente este padrão:

```
index: 0x1 RID: 0x3f2 acb: 0x00000011 Account: games    Name: games     Desc: (null)
```

Então pensei que se usássemos **split("Account:")[1]** cortaríamos essa string ficando apenas com:

```
' games    Name: games     Desc: (null)'
```

agora ficou simples, podemos usar **split()[0]** que tira os espaços e pega primeira divisão, dai fica assim:

```
split("Account:")[1].split()[0]
```

o operador acima pega uma linha do arquivo e transforma em uma linha modificada com apenas o nome dos usuários, agora ficou fácil.. basta abrir o arquivo com **with open** e depois usar um **laço de repetição for** para aplicar o padrão a todas as linhas, em seguida criamos um novo arquivo para salvar os nomes de usuário, o script ficou assim:

```Python
# Abre o arquivo
with open("saida_enumeracao_samba.txt", "r") as f:
  linhas = f.readlines()

usuarios = []

# Percorre as linhas aplicando o padrão
for linha in linhas:
  if "Account: " in linha:
    parte = linha.split("Account:")[1]
    usuario = parte.split()[0]
    usuarios.append(usuario)

# Salva apenas os usuarios em um novo arquivo
with open("smb_users.txt", "w") as arquivo:
    for y in usuarios:
        arquivo.write(y + "\n")
```

Agora temos um arquivo com todos os nomes de usuários de nome **smb_users.txt** que foi levado para a fase 2.

### Testando as senhas:

Para a fase dois o trabalho foi bem mais simples, apenas um comando que eu utilizei foi capaz de ler os dois arquivos e tentar todas as senhas, o ataque em questão que estamos realizando se chama Password Spraying, consiste em tentar poucas senhas para muitos usuários, veja na imagem a execução do teste:

**Comando executado:**
```bash
medusa -h 192.168.56.101 -M smbnt -U smb_users.txt -P senhas_spray.txt -t 2 -T 50
```

![test](<images/Captura de tela 2026-11-04 201145.png>)


### Como a saída foi muito grande eu tirei uma segunda print mostrando a senha correta no terminal em destaque:

![test](<images/Captura de tela 2026-11-04 201215.png>)

Vamos testar o usuário e senha encontrado para ver se esta correto:

**Comando executado:**
```bash
smbclient -L 192.168.56.101 -U msfadmin
```

![test](<images/Captura de tela 2026-11-06 123312.png>)

como no curso foi realizado o teste com uma senha incorreta resolvi trazer aqui também para observação de o que acontece:


![test](<images/Captura de tela 2026-11-06 123440.png>)


## :: Conclusão . Visão geral sobre o conteúdo e boas praticas de segurança.

A realização deste laboratório pratico me permitiu compreender nao apenas as mecânicas de execução de ferramentas apresentadas, mas principalmente o impacto que senhas previsíveis e configurações padrão causam na segurança de uma infraestrutura.

- força bruta vs. Password Sprayng: ficou clara a diferença entre atacar uma conta especifica com muitas tentativas de senhas (o que e extremamente provável de ser bloqueado em pouco tempo) e a prática de pulverizar senhas comuns contra múltiplos alvos.
- Automação e Scripting: O domínio de linguagens como python e comandos de terminal linux e essencial para tratar saídas de ferramentas e criar fluxos de trabalho personalizados.
- Desafios reais de auditoria: O cenario com o DVWA evidenciou que auditorias de segurança exigem analise critica de falsos positivos e compressão comportamental de protocolos e sessões (cookies).

### Como mitigar esses ataques? (Defesa):

1. Politicas de senhas fortes e MFA: implementar duplo fator de autenticação em todos os pontos de entradas externos e exigir senhas robustas para mitigar ataques de dicionario.
2. Rate limiting e bloqueio inteligente: ferramentas como Fail2Ban ou soluções de WAF/SIEM para identificar padrões repetidos de login e bloqueio de tentativas abusivas.
3. Hardening de serviços: desabilitar protocolos legados ou inseguros como por exemplo o FTP em texto claro e compartilhamento anonimo via smb, manter sistemas e plugins sempre atualizados.

Foi um prazer fazer esta etapa e criar esta documentação do que aprendi sobre o curso, estou ansioso para as novidades que me aguardam na continuação do Bootcamp Santander Cibersecurity.