Feature: Login Feature Intu
    Scenario: Credenciales incorrectas
    Given estoy en la página de inicio de sesion de Intu
    When ingreso credenciales invalidas
    Then un mensaje de error aparece