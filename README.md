# Projeto Reavaliação

**Padrão Observer**

Foi implementado o padrão Observer para que todos os membros de uma determinada comunidade recebessem a mensagem postada por alguém.
Os usuários que se inscrevem são armazenados no array ``` members[] ``` pelo método ``` addMembers()```, como mostrado abaixo.

![adicionandoMembro](https://github.com/gideaopinheiro/iFace/blob/master/imgs/adicionandoMembro.png)

Quando uma nova mensagem é enviada, o método ``` newMessage() ``` envia a nova mensagem para todos os membros da comunidade.

![atualizandoObservers](https://github.com/gideaopinheiro/iFace/blob/master/imgs/atualizandoObservers.png)


**Padrão Template Method**

Foi implementado o padrão Template Method para definir o "esqueleto" do método ```setProfile()``` para que as subclasses possam implementá-lo fazendo as alterações necessárias.

![templateMethod](https://github.com/gideaopinheiro/iFace/blob/master/imgs/templateMethod.png)

Abaixo segue a implementação destes métodos.

![métodos](https://github.com/gideaopinheiro/iFace/blob/master/imgs/implementando.png)