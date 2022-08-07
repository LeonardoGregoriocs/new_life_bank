#Meu container vai ser baseado em Python
FROM python 

#Pasta raiz do meu container 
WORKDIR /app

#Copiando arquivo para dentro do docker
COPY requirements.txt ./

#RUN vai dizer que será rodado um comando dentro container
#Comando -r para ler o documento e instalar as dependencias
RUN pip install -r requirements.txt
    
#Pegando tudo que está no projeto e importanto para pasta raiz do container 
COPY . /app

#Exposa = Expor a porta que queremos que o comando rode. Ex: 8003
EXPOSE 8003

#RODANDO O PROGRAMA
CMD ["python", "app/main.py"]