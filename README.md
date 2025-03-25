# AdaptShop - Automação de testes (Selenium)

Este repositório contém um arquivo de teste automatizado do **AdaptShop**, um sistema fictício de e-commerce especializado na venda de calçados. O teste foi desenvolvidos utilizando **Selenium** e **Python**, garantindo que as principais funcionalidades do sistema estejam operando corretamente.

---

## Pré-requisitos

Certifique-se de que seu ambiente está configurado corretamente.

### **Instalar o Python**
Faça o download e instalação do Python abaixo:
🔗 [Download Python](https://www.python.org/downloads/)

Após a instalação, verifique se o Python e o `pip` estão disponíveis:
```sh
python --version
pip --version
```

### **Instalar as dependências**
Execute o seguinte comando para instalar as bibliotecas necessárias:
```sh
pip install selenium
```

### **Baixar e Configurar o ChromeDriver**
O Selenium precisa do **ChromeDriver** para controlar o navegador.

1. Verifique a versão do Google Chrome;

2. Baixe a versão correspondente do ChromeDriver:
   🔗 [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)

3. Extraia o arquivo e:
   - Coloque o `chromedriver.exe` na mesma pasta do script, **OU**
   - Adicione o caminho do `chromedriver` ao **PATH do sistema**.

Para verificar se o WebDriver está funcionando, rode:
```sh
chromedriver --version
```

---

## Executando os Testes

### **Clonar o Repositório**
Se estiver rodando o projeto pela primeira vez, clone o repositório:
```sh
git clone https://github.com/seu-usuario/adapt-edtech-sistema-ficticio.git
```

### **Comando para executar o teste**
```sh
python test_cart.py
```
