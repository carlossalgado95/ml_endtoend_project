'''Este código cria um sistema personalizado para tratamento de exceções, proporcionando mensagens de erro 
mais detalhadas, úteis especialmente para depuração, pois elas incluem o nome do arquivo e a linha do código 
onde o erro ocorreu.'''



#O módulo sys é utilizado para obter informações sobre exceções (como onde e por que elas ocorreram).

import sys
import logging
from src.logger import logging

#custom exception handling
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # Obtém informações sobre a exceção
    file_name=exc_tb.tb_frame.f_code.co_filename # Nome do arquivo onde ocorreu o erro
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) # Formata a mensagem de erro

    return error_message # Retorna a mensagem de erro detalhada


#  Define uma exceção personalizada chamada CustomException que herda da classe base Exception. 
# Isso permite criar exceções que exibem informações mais detalhadas sobre o erro.
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # Chama o construtor da classe pai (Exception)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message # Retorna a mensagem de erro personalizada

