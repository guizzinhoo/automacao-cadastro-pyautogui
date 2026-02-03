# Automação de Cadastro com Python (PyAutoGUI)

Este projeto foi desenvolvido **durante uma aula prática**, como parte de um treinamento em Python, com o objetivo de aprender e aplicar conceitos de **automação de tarefas repetitivas**.

A automação simula a interação humana com um sistema web, realizando login e preenchendo formulários automaticamente a partir de dados armazenados em um arquivo CSV.

## 🧠 Contexto do projeto

O projeto foi desenvolvido em aula, com orientação da **Hashtag Treinamentos**, como exercício prático para introdução à automação de processos utilizando Python.

O foco principal foi compreender:
- como funciona a automação de interface gráfica
- integração entre Python, arquivos CSV e automação
- limitações de soluções baseadas em coordenadas de tela

## 🧩 Funcionalidades

- Abertura automática do navegador
- Acesso e login em sistema web
- Leitura de dados a partir de arquivo CSV
- Preenchimento automático de formulários
- Envio sequencial de registros
- Scroll automático da página

## 🛠️ Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- Arquivos CSV
- Automação de interface gráfica (RPA básico)

## ⚠️ Limitações conhecidas

Este projeto utiliza coordenadas fixas de tela (`x`, `y`) para realizar os cliques, o que faz com que ele:

- Não seja responsivo
- Dependa da resolução da tela
- Funcione apenas em ambientes com layout e escala semelhantes ao original

Essas limitações são conhecidas e fazem parte do processo de aprendizado do projeto.
