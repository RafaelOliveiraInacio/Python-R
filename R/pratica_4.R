##Trabalhando com importação de arquivos

##Instalando pacote excel
install.packages('xlsx', dependencies = T)
install.packages('rJava', dependencies = T)
install.packages('readxl')

##Carregando pacote
library(readxl)

##importando arquivo cvs

x = read.csv(file.choose(), header = TRUE, sep = ",") ##comando read.csv realiza a leitura do arquivo em csv juntamente 
                                                      ##com o file.choose para o pop-up para escolher o arquivo
x

summary(x)

##importando arquivo xlsx

dados = read_xlsx(file.choose(), sheet = 1) ##Tambem transforma em data frame

dados
