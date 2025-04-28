Feature: Search Feature Mercado
    Scenario: Busqueda iPhone 13
    Given estoy en la página de inicio de Mercadolibre
    When ingreso "iPhone 13" en la barra de busqueda y presiono el boton para buscar
    Then aparecen resultados que contienen el texto "iPhone"