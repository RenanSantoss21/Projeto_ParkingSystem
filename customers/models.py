from django.db import models
from django.contrib.auth.models import User

#banco de dados
class Customer(models.Model): #tabelas de bancos de dados por meio de classes 
    user = models.OneToOneField(
        User,
        on_delete = models.PROTECT, #Bloqueia a tentativa de apagar um registro de usuário ligado a um Cliente
        blank = True, 
        null = True,
        #blank e null true são usados em campos NÃO obrigatórios
        related_name= 'customers',  #relação inversa da quarry
        verbose_name = 'Usuário', #como o campo irá aparecer para o usuário
    )
    name = models.CharField(max_length=100, verbose_name = 'Nome')

    cpf = models.CharField(
        max_length=15, #não é feita validação de informação no banco de dados
        blank=True,
        null=True,
        verbose_name='CPF',
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, #campo automático da tabela
        verbose_name='Criado em ',
    )
    updated_at = models.DateTimeField( #DateTimeField - armazena data e horas
        auto_now=True,
        verbose_name='Atualizado em ',
    )

class Meta:
    verbose_name = 'Cliente' #como o campo irá aparecer para o usuário
    verbose_name_plural = 'Clientes' #como o campo irá aparecer para o usuário no plural


    def __str__(self): #representação do objeto em string
        return self.verbose_name
    


