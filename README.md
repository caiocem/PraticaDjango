# Exercício

## Instruções iniciais para se fazer o exercício:

Nesta fase, o exercício tem o objetivo de avaliar: a capacidade do candidato a aprender dada uma demanda, de apresentar resultados satisfatórios dado o conteúdo aprendido mesmo quando falta detalhamento da especificação, a capacidade de escrever bons textos e comentários, da capacidade de escrever um código legível, da capacidade de se organizar e da capacidade de deixar um trabalho continuável por outros, sem que seja necessário uma explicação síncrona entre as pessoas.

Apesar de não termos controle sobre o que o candidato já sabe, o processo foi desenvolvido de forma que não é esperado que o candidato tenha o conhecimento dos assuntos tratados abaixo. O tempo usado para entregar os resultados não serão utilizado como critério de avaliação, desde que não ultrapasse a data final estipulada. Faz parte do trabalho pesquisar sobre o assunto tratado de forma isolada na internet e/ou livros, sem a ajuda de terceiros. Na fase da apresentação dos resultados haverá perguntas com o objetivo de identificar fraudes.

Mesmo que você não seja selecionado para seguir conosco neste momento, o conhecimento aqui escolhido para ser estudado será útil para sua vida profissional e você terá um feedback gratuito da sua submissão. 

Como este é um processo de estágio legal, não poderemos tirar dúvidas técnicas no decorrer do processo, mas incentivamos que haja perguntas, pois a qualidade das interações também fazem parte do critério de seleção. Qualquer falta de informação técnica, assuma alguma direção e continue o trabalho de acordo com o que acredita que faça sentido, explicando suas decisões tomadas no arquivo README.md que estarão junto ao código fonte submetido.

Será dado o prazo de duas semanas para entrega dos resultados a partir do recebimento do email que dispara essas informações. Entendemos que todos tem suas obrigações, mas cremos que no espaço de duas semanas seja possível alocar horas suficientes para a realização do trabalho. 

Quando houver um trabalho submetido mais de uma vez, somente o último será considerado. Na falta de trabalhos submetidos completos, avaliaremos trabalhos submetidos parcialmente, seguindo os mesmos critérios acima. 

O exercício será desenvolvimento em computador próprio, que deverá ter espaço suficiente para executar o código e uma máquina virtual nova.

## Contexto 

O código disponível neste exercício faz parte de um sistema inacabado de apropriação remota de horas de trabalho desenvolvido por nós, utilizando python 3 e django 2, e está disponível publicamente sob licenciamento GNU PUBLIC LICENSE V2 para quem quiser usar.

Este código foi escolhido para o exercício devido ao fato de conhecermos o código fonte e sabermos mensurar o esforço de trabalho do que está sendo pedido. 

O trabalho está propositalmente pouco especificado, dando liberdade do candidato desenvolver a solução como achar melhor, desde que siga os objetivos gerais.

O trabalho desenvolvido somente será utilizado para fins de avaliação e não será incorporado ao código original nem utilizado em produção.



O conjunto de máquina virtual e distribuição descrita no roteiro será a oficial para avaliação das submissões, mas o projeto pode ser desenvolvido no ambiente que o candidato quiser.

## Casos de uso chave

1. Uma vez terminado a atividade de um projeto, o colaborador loga no sistema de apropriação, seleciona o projeto e informa quantas horas trabalho foram realizadas e a descrição da atividade.

   ( Por motivos de simplificação, não usaremos a interface do colaborador para este exercício. Toda a população do banco de dados deverá ser feita pelo admin utilizando a interface de administrador. )

2. O administrador loga no sistema de apropriação e em uma tela específica, vê o somatório de horas mensais de horas por projeto por colaborador.

## Objetivo do exercício

Desenvolver o item 2 dos casos de uso chave.

Avaliaremos como foi desenvolvido a solução tecnicamente. Por motivos de simplificação e redução do tempo dedicado ao exercício, aspectos relativos a UX e Design não serão considerados na avaliação.

## Exercício:



1. Baixar a iso do ubuntu 18.04 server aqui https://ubuntu.com/download/server/thank-you?country=BR&version=18.04.4&architecture=amd64

2. Instalar o VirtualBox 6.1  https://www.virtualbox.org/wiki/Downloads para o seu sistema operacional.

3. Criar uma nova máquina virtual Ubuntu dentro do VirtualBox, utilizando a iso recentemente baixada, configurando o redirecionamento da porta 8000 da máquina virtual para a 8000 local. Para o restante use as opção padrão na instalação.

4. Logue na máquina virtual e clone o repositório do exercício:
   `git clone https://gitlab.com/miningmath/sistema_apropriacao.git`

5. Prepare o projeto para execução:

   ```bash
   cd sistema_apropriacao
   sudo apt-get install python3-venv
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   python manage.py makemigrations
   pythom manage.py migrate
   python manage.py createsuperuser
   ```

   e siga os passos para criar uma senha de administrador

6. Rode a aplicação

   `python manage.py runserver 0.0.0.0:8000`

7. Do seu computador acesse o http://localhost:8000/admin e acesse a aplicação para conhecer a interface do admin.

8. No item apropriação, popule pelo menos 3 registros para pelo menos 3 colaboradores diferentes.

9. Desenvolva a tela de relatório conforme o objetivo.

## Submissão dos trabalhos

A submissão dos trabalhos será feita pelo comando git send-mail, para o endereço fabricio.ceolin@miningmath.com. 



# Notas do candidato

As notas do candidato devem começar aqui...
