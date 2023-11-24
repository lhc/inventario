# Inventário LHC

Este é o repositório onde armazenamos os detalhes dos equipamentos, móveis, itens, etc.
do LHC que precisamos manter um controle.

## Como adicionar um item

1. Pegar uma etiqueta com QR Code do inventário
1. Colar ela no item de maneira que ela fiquei visível facilmente
1. Verificar o número da etiqueta. Como exemplo, nos próximos passos consideramos
   que a etiqueta com número 42 foi a utilizada. Troque o número de acordo com a etiqueta
   que você pegou

Os passos a seguir são semelhantes a contribuir com código em um projeto. Caso tenha
dúvidas, peça ajuda a alguém nos grupos do LHC, com certeza alguém poderá te guiar.

1. Crie um fork do projeto na sua conta do Github e faça um clone dele
1. No seu fork, você vai encontrar o diretório `docs`
1. No diretório `docs/0042/` existe um arquivo chamado `index.html`. Edite esse arquivo
   de modo a fornecer as informações sobre o item que você colou a etiqueta. Use HTML simples
   e não se preocupe tanto com a melhor estética
1. Caso você queira adicionar fotos, esquemáticos, datasheets, etc., que auxiliem quem
   for verificar as informações do item posteriormente, adicione dentro do diretório
   `docs/0042/assets`. Você pode até referenciá-los no seu arquivo `index.html`
1. Faça o commit das suas mudanças e em seguida faça um pull requests com o repośitório
   original

Assim que seu pull request for aprovado, o conteúdo será acessível em
https://inventario.lhc.net.br/0042/ automaticamente.

**Ao ler o QR code da etiqueta, você também será redirecionado para essa página**

## Melhorias

Esse texto foi escrito como uma referência no processo. Sintam-se a vontade para ir
melhorando ele para que fique mais claro como fazer o inventário dos nossos items.