##FAÇA VOCE MESMO 34.

##1

ana = 8L
paulo = 12L

if(ana>paulo){
  print('A menina é mais velha')
}else{
  print('O menino é mais velho')
}

ifelse(ana>paulo, 'A menina é mais velha','O menino é mais velho')

##2

x = BOD
class(x)

##3

x = c(1,2,3,4,5,6,7,8,9,10)

for(i in x)
    if(i%%2==0){
      print(i)
    }

##4

tail(women,10)

##5
install.packages('e1071', dependencies = T)
install.packages('ggplot2')
library(e1071)
library(ggplot2)



x = iris['Sepal.Width']
x[50:100,0]
