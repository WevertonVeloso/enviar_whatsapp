# enviar_whatsapp
Este é um script Python automatizado que utiliza as bibliotecas pywhatkit, os e random para enviar mensagens no WhatsApp. A principal funcionalidade do código é selecionar mensagens românticas e inspiradoras de forma aleatória e enviá-las periodicamente para um destinatário especificado.

# Enviar Mensagens Automáticas no WhatsApp

Este projeto é um script em Python que utiliza a biblioteca `pywhatkit` para enviar mensagens automáticas pelo WhatsApp. As mensagens são enviadas em horários aleatórios definidos pelo script, ideal para automatizar o envio de mensagens personalizadas.

## Funcionalidades

- Envio automático de mensagens para um número de telefone definido.
- Mensagens personalizadas selecionadas aleatoriamente de uma lista predefinida.
- Controle de horário para envio das mensagens.
- Requisição para que o WhatsApp esteja logado no navegador Firefox.

## Pré-requisitos

1. Python 3.11 ou superior.
2. Biblioteca `pywhatkit` instalada.
3. Biblioteca `xvfb` instalada para executar o script em servidores sem interface gráfica.
4. Navegador Firefox configurado e logado no WhatsApp.

## Configuração

1. Clone este repositório ou copie o código do script.
2. Certifique-se de ter as bibliotecas necessárias instaladas:
   ```bash
   pip install pywhatkit
   sudo apt-get install xvfb
   ```
3. Adicione o número do destinatário no formato internacional na variavel de ambiente:
   ```
   NUMERO=+5531999999999
   
   ```
4. Certifique-se de que o WhatsApp Web está logado no navegador Firefox. O script foi desenvolvido utilizando o Firefox, e utiliza o comando `os.system("kill -9 $(pidof firefox-esr)")` para gerenciar o navegador. Caso deseje usar outro navegador, será necessário modificar este comando.

## Uso

Execute o script com o seguinte comando:
```bash
xvfb-run ~/faz-script/bin/python3 enviar_whatsapp.py
```

## Funcionamento do Script

1. O script seleciona aleatoriamente uma mensagem da lista predefinida.
2. Define um horário aleatório entre 08:10 e 17:30 para o envio.
3. Utiliza a função `kit.sendwhatmsg()` para enviar a mensagem pelo WhatsApp Web.
4. Após o envio, o script pausa por 5 minutos antes de reiniciar o ciclo.
5. O Firefox é encerrado após cada iteração para evitar acúmulo de processos.

## Observação

Caso deseje utilizar outro navegador, será necessário modificar a seguinte linha do código:
```python
os.system("kill -9 $(pidof firefox-esr)")
```
Substitua `firefox-esr` pelo nome do processo do navegador desejado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é de uso livre e aberto para modificações pessoais.

