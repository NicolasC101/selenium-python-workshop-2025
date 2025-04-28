from behave import given, when, then
from selenium import webdriver
from pages.mercado_base_page import MercadoBase
from pages.mercado_search_page import MercadoSearch
import time

@given('estoy en la página de inicio de Mercadolibre')
def step_given_mercado_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co/")
    context.mercado_base_page = MercadoBase(context.driver)

@when('ingreso "iPhone 13" en la barra de busqueda y presiono el boton para buscar')
def step_when_mercado_search(context):
    context.mercado_base_page.search("iPhone 13")

@then('aparecen resultados que contienen el texto "iPhone"')
def step_then_mercado_search(context):
    context.mercado_search_page = MercadoSearch(context.driver)
    assert context.mercado_search_page.verify_results_contain_iphone(), "No se encontraron resultados con 'iPhone'"