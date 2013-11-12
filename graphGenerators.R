# maple code
restart:with(VectorCalculus):with(plots):with(plottools):
 z:=(x,y)->sin(1/2*x^2-1/4*y^2+3)*cos(2*x+1-exp(y)):
 grad:=VectorCalculus[Gradient](z(x,y),[x,y]);
 plot3d(z(x,y),x=-1.2..1.2,y=-1.2..1.2,axes=normal,numpoints=1000);p3d:=%:
 contourplot(z(x,y),x=-1.2..1.2,y=-1.2..1.2,axes=normal,contours=30,numpoints=3000);cont:=%:
 start:=[-1/4,1/3];ptf[0]:=Vector(start):
 steps:=15;
 for i from 0 to steps do:
  print(ptf[i]):
  pt[i]:=Vector([convert(ptf[i],list)[],z(ptf[i][1],ptf[i][2])]):
  dir[i]:=evalf(Normalize(evalVF(grad,ptf[i])));
  par[i]:=ptf[i]+lambda*dir[i];
  lambd[i]:=fsolve(diff(z(par[i][1],par[i][2]),lambda)=0,lambda=0);
  ptf[i+1]:=eval(par[i],lambda=lambd[i]);
  od:i:='i':
 display(cont,'point(convert(ptf[i],list),color=blue)'$'i'=0..steps,'plot([par[i][1],par[i][2],lambda=0..lambd[i]])'$'i'=0..steps);
 display(p3d,'point(convert(pt[i],list),color=blue,symbol=circle,symbolsize=4)'$'i'=0..steps,'spacecurve([par[i][1],par[i][2],z(par[i][1],par[i][2])],lambda=0



install.packages("lattice")
pdf(file='Figures/steepestweird.pdf')
x <- seq(pi/4, 5 * pi, length.out = 100)
y <- seq(pi/4, 5 * pi, length.out = 100)
r <- as.vector(sqrt(outer(x^2, y^2, "+")))
grid <- expand.grid(x=x, y=y)
grid$z <- cos(r^2) * exp(-r/(pi^3))
lattice::levelplot(z~x*y, grid, cuts = 50, scales=list(log="e"), xlab="",
          ylab="", main="Weird Function", sub="with log scales",
          colorkey = FALSE, region = TRUE)
dev.off()

pdf(file='Figures/steepestdescentnice.pdf')
op = par(pty = "s", mar = c(2, 1, 2, 0), cex.axis = 0.75, cex.main = 0.85)
x2 = x1 = seq(-2 * pi, 2 * pi, 0.1)
f = function(x, y) x^2 + 3 * sin(y)
contour(x1, x2, outer(x1, x2, f), col = "red", main = "")
mtext(side = 3, expression(z == x[1]^2 + 3 * sin(x[2])))
for (i in 1:3) {
  x = unlist(locator(1))
  s = 0.05
  newx = x - s * c(2 * x1, 3 * cos(x2))
  eps = 0.001
  gap = abs(f(newx[1], newx[2]) - f(x1, x2))
  while (gap > eps) {
    arrows(x[1], x[2], newx[1], newx[2], length = 0.075, col = "blue")
    x = newx
    newx = x - s * c(2 * x1, 3 * cos(x2))
    gap = abs(f(newx[1], newx[2]) - f(x1, x2))
    Sys.sleep(gap/3)
  }
}
par(op)
dev.off()
