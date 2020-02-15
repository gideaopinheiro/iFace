# Projeto Reavaliação

**Padrão Observer**

<!-- Veja o código [aqui](https://github.com/gideaopinheiro/fanfiction-site/commit/112eb06673ce8deb60e441a84f303884c8aec483?diff=split)
 -->

Foi implementado o padrão Observer para que todos os membros de uma determinada comunidade recebessem a mensagem postada por alguém.
Os usuários que se inscrevem são armazenados no array ``` members[] ``` pelo método ``` addMembers()```, como mostrado abaixo.

![subscribe](https://github.com/gideaopinheiro/iFace/imgs/adicionandoMembro.png)

Quando uma nova mensagem é enviada, o método ``` newMessage() ``` envia a nova mensagem para todos os membros da comunidade.

![updating](https://github.com/gideaopinheiro/iFace/imgs/atualizandoObservers.png)