from behave import given, when, then
from selenium import webdriver
from pages.intu_login_page import IntuLogin
import time

@given('estoy en la pagina de inicio de sesion de Intu')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_page = IntuLogin(context.driver)

@when('ingreso credenciales invalidas')
def step_when_intu_login(context):
    context.login_page.login("invalid_user", "invalid_password")

@then('un mensaje de error aparece')
def step_then_intu_login(context):
    print(context.login_page.isElementPresent())
    assert "Acceso inválido. Por favor, inténtelo otra vez.".equals(context.login_page.isElementPresent())
    #assert "Acceso inválido. Por favor, inténtelo otra vez." == context.login_page.isElementPresent()