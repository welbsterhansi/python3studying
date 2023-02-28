Para listar as instâncias EC2 de uma conta na AWS usando o Boto3, você pode seguir os seguintes passos:

Instale o Boto3 usando o pip:

```
import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("ID da instância: ", instance['InstanceId'])
        print("Estado da instância: ", instance['State']['Name'])
```

Explicação do código:

Primeiro, importamos o módulo boto3 e criamos um cliente EC2 na região us-east-1.
Em seguida, usamos o método describe_instances() do cliente para obter informações sobre todas as instâncias na região us-east-1 que possuem a tag "Shutdown" com o valor "yes". Isso é feito usando o parâmetro Filters para definir o filtro desejado.
Depois, iteramos sobre as instâncias retornadas pelo método describe_instances(). Para cada instância, pegamos o seu ID e usamos o método stop_instances() do cliente EC2 para desligá-la.
Finalmente, imprimimos uma mensagem informando que a instância está sendo desligada.

Explicando o for:

O método describe_instances() do cliente EC2 retorna uma estrutura JSON que contém informações sobre as instâncias que correspondem ao filtro especificado. Essa estrutura JSON possui um array de objetos Reservation, que contém as informações de cada grupo de instâncias iniciadas juntas, como as instâncias lançadas em uma única solicitação de execução ou as instâncias que fazem parte de um auto-scaling group.

O primeiro loop for itera sobre todos os objetos Reservation retornados pela chamada ao método describe_instances(). Para cada objeto Reservation, iteramos sobre todas as instâncias que fazem parte dele, acessando o array de objetos Instance dentro do objeto Reservation.

Dentro do segundo loop for, podemos acessar as informações de cada instância individual, como o ID da instância (InstanceId) ou o estado atual da instância (State).

No código proposto, estamos apenas recuperando o ID de cada instância (instance['InstanceId']) e, em seguida, imprimindo uma mensagem na tela informando que a instância está sendo desligada. Em seguida, estamos chamando o método stop_instances() do cliente EC2 para desligar a instância usando o ID da instância.

Esse processo se repete para cada instância retornada pela chamada ao método describe_instances() que atenda ao filtro especificado.