# Separar-pg-PDFs
Esse código é um aplicativo em Python que usa a biblioteca tkinter para criar uma interface gráfica de usuário (GUI) para dividir um arquivo PDF em páginas individuais. Ele usa a biblioteca PyPDF2 para ler e escrever arquivos PDF.

Este código é um programa simples para dividir um arquivo PDF em várias páginas PDF individuais. Ele utiliza as bibliotecas Tkinter para criar uma interface gráfica e PyPDF2 para manipular arquivos PDF.

A interface gráfica tem dois campos para entrada de dados: um para selecionar o arquivo PDF a ser dividido e outro para selecionar a pasta onde as páginas individuais serão salvas. Existem botões "Selecionar" ao lado de cada campo para facilitar a seleção do arquivo e da pasta. Há também um botão "Enter" para iniciar o processo de divisão do PDF.

Quando o botão "Enter" é pressionado, a função split_pdf() é chamada. Ela obtém o caminho do arquivo PDF a ser dividido e a pasta onde as páginas individuais serão salvas. Em seguida, ela abre o arquivo PDF e usa a biblioteca PyPDF2 para contar o número de páginas no arquivo. Depois, ela itera sobre todas as páginas e salva cada página individual em um arquivo separado na pasta selecionada.

Após a divisão do PDF, uma mensagem de sucesso é exibida em uma caixa de diálogo usando o tk.messagebox.showinfo().

Em resumo, este código é um programa simples para dividir um arquivo PDF em várias páginas PDF individuais, utilizando uma interface gráfica fácil de usar.
