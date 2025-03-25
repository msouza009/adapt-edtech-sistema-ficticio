from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_login():
    driver.get("http://localhost:3000/login")
    
    email = driver.find_element(By.ID, "email")
    email.send_keys("usuario@teste.com")

    password = driver.find_element(By.ID, "password")
    password.send_keys("senha123")
    password.send_keys(Keys.RETURN)

    time.sleep(2)  

    assert "Bem-vindo" in driver.page_source
    print("Login realizado com sucesso!")

def test_add_to_cart():
    driver.get("http://localhost:3000/produtos")
    
    produto = driver.find_element(By.CLASS_NAME, "add-to-cart")
    produto.click()

    time.sleep(2) 

    carrinho = driver.find_element(By.ID, "cart-items").text
    assert "Tênis" in carrinho
    print("Produto adicionado ao carrinho com sucesso!")

test_login()
test_add_to_cart()

driver.quit()
