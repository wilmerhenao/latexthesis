library(ggplot2)
library(reshape2) # for melt
M=melt(volcano)
head(M)

M$Var1 <- M$Var1 / 10
M$Var2 <- M$Var2 / 10
M$value <- (M$Var1)^2 + (M$Var2)^2

ggplot(M, aes(x=Var1, y=Var2, fill=value)) + geom_tile()
