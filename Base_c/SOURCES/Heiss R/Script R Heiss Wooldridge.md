R Scripts
# 1. Scripts Used in Chapter 01
## Script 1.1: R-as-a-Calculator.R
1+1
5*(4-1)^2
sqrt( log(10) )
## Script 1.2: Install-Packages.R
'# This R Script downloads and installs all packages used at some point.
'# It needs to be run once for each computer/user only
install.packages( c("AER", "car", "censReg", "dplyr", "dummies", "dynlm",
"effects", "ggplot2", "lmtest", "maps", "mfx", "orcutt", "plm",
"quantmod", "sandwich", "quantreg", "rio", "rmarkdown", "sampleSelection",
"stargazer", "survival", "systemfit", "truncreg", "tseries", "urca",
"xtable", "vars", "WDI", "wooldridge", "xts", "zoo") )
## Script 1.3: Objects.R
'# <font color="#00b0f0">generate object x (no output):</font>
x <- 5
'# <font color="#00b0f0">display x & x^2:</font>
x
x^2
'# <font color="#00b0f0">generate objects y&z with immediate display using ():</font>
(y <- 3)
(z <- y^x)
## Script 1.4: Vectors.R
'# <font color="#00b0f0">Define a with immediate output through parantheses:</font>
(a <- c(1,2,3,4,5,6))
(b <- a+1)
(c <- a+b)
(d <- b*c)
sqrt(d)
## Script 1.5: Vector-Functions.R
'# <font color="#00b0f0">Define vector</font>
(a <- c(7,2,6,9,4,1,3))
'#<font color="#00b0f0"> Basic functions:</font>
sort(a)
length(a)
min(a)
max(a)
sum(a)
prod(a)
'# <font color="#00b0f0">Creating special vectors:</font>
numeric(20)
rep(1,20)
seq(50)
5:15
seq(4,20,2)
## Script 1.6: Logical.R
'# <font color="#00b0f0">Basic comparisons:</font>
0 == 1
0 < 1
'#<font color="#00b0f0"> Logical vectors:</font>
( a <- c(7,2,6,9,4,1,3) )
( b <- a<3 | a>=6 )
## Script 1.7: Factors.R
'# <font color="#00b0f0">Original ratings:</font>
x <- c(3,2,2,3,1,2,3,2,1,2)
xf <- factor(x, labels=c("bad","okay","good"))
x
xf
## Script 1.8: Vector-Indices.R
<font color="#00b0f0">'# Create a vector "avgs":</font>
avgs <- c(.366, .358, .356, .349, .346)
<font color="#00b0f0">'# Create a string vector of names:</font>
players <- c("Cobb","Hornsby","Jackson","O’Doul","Delahanty")
<font color="#00b0f0">'# Assign names to vector and display vector:</font>
names(avgs) <- players
avgs
<font color="#00b0f0">'# Indices by number:</font>
avgs[2]
avgs[1:4]
<font color="#00b0f0">'# Indices by name:</font>
avgs["Jackson"]
<font color="#00b0f0">'# Logical indices:</font>
avgs[ avgs>=0.35 ]
## Script 1.9: Matrices.R
'# <font color="#00b0f0">Generating matrix A from one vector with all values:</font>
v <- c(2,-4,-1,5,7,0)
( A <- matrix(v,nrow=2) )
'# <font color="#00b0f0">Generating matrix A from two vectors corresponding to rows:</font>
row1 <- c(2,-1,7); row2 <- c(-4,5,0)
( A <- rbind(row1, row2) )
'# <font color="#00b0f0">Generating matrix A from three vectors corresponding to columns:</font>
col1 <- c(2,-4); col2 <- c(-1,5); col3 <- c(7,0)
( A <- cbind(col1, col2, col3) )
'# <font color="#00b0f0">Giving names to rows and columns:</font>
colnames(A) <- c("Alpha","Beta","Gamma")
rownames(A) <- c("Aleph","Bet")
A
'# <font color="#00b0f0">Diaginal and identity matrices:</font>
diag( c(4,2,6) )
diag( 3 )
'#<font color="#00b0f0"> Indexing for extracting elements (still using A from above):</font>
A[2,1]
A[,2]
A[,c(1,3)]
## Script 1.10: Matrix-Operators.R
A <- matrix( c(2,-4,-1,5,7,0), nrow=2)
B <- matrix( c(2,1,0,3,-1,5), nrow=2)
A B A
*B
'# <font color="#00b0f0">Transpose:</font>
(C <- t(B) )
'# <font color="#00b0f0">Matrix multiplication:</font>
(D <- A %*%
C )
'# <font color="#00b0f0">Inverse:</font>
solve(D)
## Script 1.11: Lists.R
'#<font color="#00b0f0"> Generate a list object:</font>
mylist <- list( A=seq(8,36,4), this="that", idm = diag(3))
'#<font color="#00b0f0"> Print whole list:</font>
mylist
'# <font color="#00b0f0">Vector of names:</font>
names(mylist)
'# <font color="#00b0f0">Print component "A":</font>
mylist$A
## Script 1.12: Data-frames.R
'# <font color="#00b0f0">Define one x vector for all:</font>
year<- c(2008,2009,2010,2011,2012,2013)
'# <font color="#00b0f0">Define a matrix of y values:</font>
product1<-c(0,3,6,9,7,8); product2<-c(1,2,3,5,9,6); product3<-c(2,4,4,2,3,2)
sales_mat <- cbind(product1,product2,product3)
rownames(sales_mat) <- year
'# <font color="#00b0f0">The matrix looks like this:</font>
sales_mat
'# <font color="#00b0f0">Create a data frame and display it:</font>
sales <- as.data.frame(sales_mat)
sales
## Script 1.13: Data-frames-vars.R
'# <font color="#00b0f0">Accessing a single variable:</font>
sales$product2
'# <font color="#00b0f0">Generating a new variable in the data frame:</font>
sales $ totalv1 <- sales$ product1 + sales$ product2 + sales$ product3
'# <font color="#00b0f0">The same but using "with":</font>
sales$totalv2 <- with(sales, product1+product2+product3)
'# <font color="#00b0f0">The same but using "attach":</font>
attach(sales)
sales$totalv3 <- product1+product2+product3
detach(sales)
'# <font color="#00b0f0">Result:</font>
sales
## Script 1.14: Data-frames-subsets.R
'# <font color="#00b0f0">Full data frame (from Data-frames.R, has to be run first)</font>
sales
'# <font color="#00b0f0">Subset: all years in which sales of product 3 were >=3</font>
subset(sales, product3>=3)
## Script 1.15: RData-Example.R
'# <font color="#00b0f0">Note: "sales" is defined in Data-frames.R, so it has to be run first!</font>
'# <font color="#00b0f0">save data frame as RData file (in the current working directory)</font>
save(sales, file = "oursalesdata.RData")
'# <font color="#00b0f0">remove data frame "sales" from memory</font>
rm(sales)
'# <font color="#00b0f0">Does variable "sales" exist?</font>
exists("sales")
'# <font color="#00b0f0">Load data set (in the current working directory):</font>
load("oursalesdata.RData")
'#<font color="#00b0f0"> Does variable "sales" exist?</font>
exists("sales")
sales
'# <font color="#00b0f0">averages of the variables:</font>
colMeans(sales)
## Script 1.16: Example-Data.R
'# <font color="#00b0f0">The data set is stored on the local computer in ~/Documents/R/data/wooldridge/affairs.dta</font>
'# <font color="#00b0f0">Version 1: from package. make sure to install.packages(wooldridge)</font>
data(affairs, package=’wooldridge’)
'# <font color="#00b0f0">Version 2: Adjust path</font>
affairs2 <- rio::import("~/Documents/R/data/wooldridge/affairs.dta")
'# <font color="#00b0f0">Version 3: Change working directory</font>
setwd("~/Documents/R/data/wooldridge/")
'# <font color="#00b0f0">import </font>
affairs3 <- rio::import("affairs.dta")
'# <font color="#00b0f0">Version 4: directly load from internet</font>
affairs4 <- rio::import("http://fmwww.bc.edu/ec-p/data/wooldridge/affairs.dta")
'# <font color="#00b0f0">Compare, e.g. avg. value of naffairs:</font>
mean(affairs$naffairs)
mean(affairs2$naffairs)
mean(affairs3$naffairs)
mean(affairs4$naffairs)
## Script 1.17: Plot-Overlays.R
plot(x,y, main="Example for an Outlier")
points(8,1)
abline(a=0.31,b=0.97,lty=2,lwd=2)
text(7,2,"outlier",pos=3)
arrows(7,2,8,1,length=0.15)
## Script 1.18: Plot-Matplot.R
'# Define one x vector for all:
year
<- c(2008,2009,2010,2011,2012,2013)
'# Define a matrix of y values:
product1 <- c(0,3,6,9,7,8)
product2 <- c(1,2,3,5,9,6)
product3 <- c(2,4,4,2,3,2)
sales <- cbind(product1,product2,product3)
'# plot
matplot(year,sales, type="b", lwd=c(1,2,3), col="black" )
## Script 1.19: Plot-Legend.R
curve( dnorm(x,0,1), -10, 10, lwd=1, lty=1)
curve( dnorm(x,0,2),add=TRUE, lwd=2, lty=2)
curve( dnorm(x,0,3),add=TRUE, lwd=3, lty=3)
'# Add the legend
legend("topright",c("sigma=1","sigma=2","sigma=3"), lwd=1:3, lty=1:3)
## Script 1.20: Plot-Legend2.R
curve( dnorm(x,0,1), -10, 10, lwd=1, lty=1)
curve( dnorm(x,0,2),add=TRUE, lwd=2, lty=2)
curve( dnorm(x,0,3),add=TRUE, lwd=3, lty=3)
'# Add the legend with greek sigma
legend("topleft",expression(sigma==1,sigma==2,sigma==3),lwd=1:3,lty=1:3)
'# Add the text with the formula, centered at x=6 and y=0.3
text(6,.3,
expression(f(x)==frac(1,sqrt(2*pi)*sigma)*e^{-frac(x^2,2*sigma^2)}))
## Script 1.21: mpg-data.R
'# load package
library(ggplot2)
'# First rows of data of data set mpg:
head(mpg)

310
R Scripts
## Script 1.22: mpg-scatter.R
'# load package
library(ggplot2)
'# Generate ggplot2 graph:
ggplot() + geom_point( data=mpg, mapping=aes(x=displ, y=hwy) )
## Script 1.23: mpg-regr.R
ggplot(mpg, aes(displ, hwy)) +
geom_point() +
geom_smooth()
## Script 1.24: mpg-color1.R
ggplot(mpg, aes(displ, hwy)) +
geom_point(color=gray(0.5)) +
geom_smooth(color="black")
## Script 1.25: mpg-color2.R
ggplot(mpg, aes(displ, hwy)) +
geom_point( aes(color=class) ) +
geom_smooth(color="black") +
scale_color_grey()
## Script 1.26: mpg-color3.R
ggplot(mpg, aes(displ, hwy)) +
geom_point( aes(color=class, shape=class) ) +
geom_smooth(color="black") +
scale_color_grey() +
scale_shape_manual(values=1:7)
## Script 1.27: mpg-color4.R
ggplot(mpg, aes(displ, hwy, color=class, shape=class)) +
geom_point() +
geom_smooth(se=FALSE) +
scale_color_grey() +
scale_shape_manual(values=1:7)
## Script 1.28: mpg-advanced.R
ggplot(mpg, aes(displ, hwy, color=class, shape=class)) +
geom_point() +
geom_smooth(se=FALSE) +
scale_color_grey() +
scale_shape_manual(values=1:7) +
theme_light() +
labs(title="Displacement vs. Mileage",
subtitle="Model years 1988 - 2008",
caption="Source: EPA through the ggplot2 package",
x = "Displacement [liters]",
y = "Miles/Gallon (Highway)",
color="Car type",
shape="Car type"
) +
coord_cartesian(xlim=c(0,7), ylim=c(0,45)) +
theme(legend.position = c(0.15, 0.3))
ggsave("my_ggplot.png", width = 7, height = 5)

1. Scripts Used in Chapter 01
311
## Script 1.29: wdi-data.R
'# packages: WDI for raw data, dplyr for manipulation
library(WDI);
wdi_raw <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014)
head(wdi_raw)
tail(wdi_raw)
## Script 1.30: wdi-manipulation.R
library(dplyr)
'# filter: only US data
ourdata <- filter(wdi_raw, iso2c=="US")
'# rename lifeexpectancy variable
ourdata <- rename(ourdata, LE_fem=SP.DYN.LE00.FE.IN)
'# select relevant variables
ourdata <- select(ourdata, year, LE_fem)
'# order by year (increasing)
ourdata <- arrange(ourdata, year)
'# Head and tail of data
head(ourdata)
tail(ourdata)
'# Graph
library(ggplot2)
ggplot(ourdata, aes(year, LE_fem)) +
geom_line() +
theme_light() +
labs(title="Life expectancy of females in the US",
subtitle="World Bank: World Development Indicators",
x = "Year",
y = "Life expectancy [years]"
)
## Script 1.31: wdi-pipes.R
library(dplyr)
'# All manipulations with pipes:
ourdata <- wdi_raw %>%
filter(iso2c=="US") %>%
rename(LE_fem=SP.DYN.LE00.FE.IN) %>%
select(year, LE_fem) %>%
arrange(year)
## Script 1.32: wdi-ctryinfo.R
library(WDI); library(dplyr)
'# Download raw life expectency data
le_data <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014) %>%
rename(LE = SP.DYN.LE00.FE.IN)
tail(le_data)
'# Country-data on income classification
ctryinfo <- as.data.frame(WDI_data$country, stringsAsFactors = FALSE) %>%
select(country, income)

filter(income != "Aggregates") %>%     '# remove rows for aggregates filter(income != "Not 
classified") %>%   '# remove unclassified ctries group_by(income, year) %>%         '# group by 
income classification summarize(LE_avg = mean(LE, na.rm=TRUE)) %>% '# average by group
ungroup()                '# remove grouping
'# First 6 rows: tail(avgdata)
'# plot
geom_line(size=1) +             '# thicker lines
scale_color_grey() +             '# gray scale scale_x_continuous(breaks=seq(1960,2015,10)) +  '# 
adjust x axis breaks
theme_light() +               '# light theme (white background,...) labs(title="Life expectancy of 
women",
subtitle="Average by country classification", x="Year", y="Life expectancy [Years]",
312
R Scripts
tail(ctryinfo)
'# Join:
alldata <- left_join(le_data, ctryinfo)
tail(alldata)
## Script 1.33: wdi-ctryavg.R
'# Note: run wdi-ctryinfo.R first to define "alldata"!
'# Summarize by country and year
avgdata <- alldata %>%
ggplot(avgdata, aes(year, LE_avg, color=income)) +
geom_line() +
scale_color_grey()
## Script 1.34: wdi-ctryavg-beautify.R
'# Note: run wdi-ctryavg.R first to define "avgdata"!
'# Order the levels meaningfully
avgdata$income <- factor( avgdata$income,
levels = c("High income",
"Upper middle income",
"Lower middle income",
"Low income") )
'# Plot
ggplot(avgdata, aes(year, LE_avg, color=income)) +
color="Income level",
caption="Source: World Bank, WDI")
## Script 1.35: Descr-Tables.R
'# load data set
data(affairs, package=’wooldridge’)
'# Generate "Factors" to attach labels
haskids <- factor(affairs$kids,labels=c("no","yes"))
mlab <- c("very unhappy","unhappy","average","happy", "very happy")
marriage <- factor(affairs$ratemarr, labels=mlab)

1. Scripts Used in Chapter 01
313
'# Frequencies for having kids:
table(haskids)
'# Marriage ratings (share):
prop.table(table(marriage))
'# Contigency table: counts (display & store in var.)
(countstab <- table(marriage,haskids))
'# Share within "marriage" (i.e. within a row):
prop.table(countstab, margin=1)
'# Share within "haskids"
(i.e. within a column):
prop.table(countstab, margin=2)
## Script 1.36: Histogram.R
'# Load data
data(ceosal1, package=’wooldridge’)
'# Extract ROE to single vector
ROE <- ceosal1$roe
'# Subfigure (a): histogram (counts)
hist(ROE)
'# Subfigure (b): histogram (densities, explicit breaks)
hist(ROE, breaks=c(0,5,10,20,30,60) )
## Script 1.37: KDensity.R
'# Subfigure (c): kernel density estimate
plot( density(ROE) )
'# Subfigure (d): overlay
hist(ROE, freq=FALSE, ylim=c(0,.07))
lines( density(ROE), lwd=3 )
## Script 1.38: Descr-Stats.R
data(ceosal1, package=’wooldridge’)
'# sample average:
mean(ceosal1$salary)
'# sample median:
median(ceosal1$salary)
'#standard deviation:
sd(ceosal1$salary)
'# summary information:
summary(ceosal1$salary)
'# correlation with ROE:
cor(ceosal1$salary, ceosal1$roe)
## Script 1.39: PMF-example.R
'# Values for x: all between 0 and 10
x <- seq(0,10)
'# pmf for all these values

314
R Scripts
fx <- dbinom(x, 10, 0.2)
'# Table(matrix) of values:
cbind(x, fx)
'# Plot
plot(x, fx, type="h")
## Script 1.40: Random-Numbers.R
'# Sample from a standard normal RV with sample size n=5:
rnorm(5)
'# A different sample from the same distribution:
rnorm(5)
'# Set the seed of the random number generator and take two samples:
set.seed(6254137)
rnorm(5)
rnorm(5)
'# Reset the seed to the same value to get the same samples again:
set.seed(6254137)
rnorm(5)
rnorm(5)
## Script 1.41: Example-C-2.R
'# Manually enter raw data from Wooldridge, Table C.3:
SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,
5.03,8,9,18,.28,7,3.97)
SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,
4,7,19,.2,5,3.83)
'# Calculate Change (the parentheses just display the results):
(Change <- SR88 - SR87)
'# Ingredients to CI formula
(avgCh<- mean(Change))
(n
<- length(Change))
(sdCh <- sd(Change))
(se
<- sdCh/sqrt(n))
(c
<- qt(.975, n-1))
'# Confidence interval:
c( avgCh - c*se, avgCh + c*se
)
## Script 1.42: Example-C-3.R
data(audit, package=’wooldridge’)
'# Ingredients to CI formula
(avgy<- mean(audit$y))
(n
<- length(audit$y))
(sdy <- sd(audit$y))
(se
<- sdy/sqrt(n))
(c
<- qnorm(.975))
'# 95% Confidence interval:
avgy + c
*
c(-se,+se)
'# 99% Confidence interval:
avgy + qnorm(.995)
*
c(-se,+se)

1. Scripts Used in Chapter 01
315
## Script 1.43: Critical-Values-t.R
'# degrees of freedom = n-1:
df <- 19
'# significance levels:
alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
alpha.two.tailed = alpha.one.tailed
*
2
'# critical values & table:
CV <- qt(1 - alpha.one.tailed, df)
cbind(alpha.one.tailed, alpha.two.tailed, CV)
## Script 1.44: Example-C-5.R
'# Note: we reuse variables from Example-C-3.R. It has to be run first!
'# t statistic for H0: mu=0:
(t <- avgy/se)
'# Critical values for t distribution with n-1=240 d.f.:
alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
CV <- qt(1 - alpha.one.tailed, n-1)
cbind(alpha.one.tailed, CV)
## Script 1.45: Example-C-6.R
'# Note: we reuse variables from Example-C-2.R. It has to be run first!
'# t statistic for H0: mu=0:
(t <- avgCh/se)
'# p value
(p <- pt(t,n-1))
## Script 1.46: Example-C-7.R
'# t statistic for H0: mu=0:
t <-
-4.276816
'# p value
(p <- pt(t,240))
## Script 1.47: Examples-C2-C6.R
'# data for the scrap rates examples:
SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,5.03,8,9,18,.28,
7,3.97)
SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,4,7,19,.2,5,3.83)
Change <- SR88 - SR87
'# Example C.2: two-sided CI
t.test(Change)
'# Example C.6: 1-sided test:
t.test(Change, alternative="less")
## Script 1.48: Examples-C3-C5-C7.R
data(audit, package=’wooldridge’)
'# Example C.3: two-sided CI
t.test(audit$y)
'# Examples C.5 & C.7: 1-sided test:
t.test(audit$y, alternative="less")

316
R Scripts
## Script 1.49: Test-Results-List.R
data(audit, package=’wooldridge’)
'# store test results as a list "testres"
testres <- t.test(audit$y)
'# print results:
testres
'# component names: which results can be accessed?
names(testres)
'# p-value
testres$p.value
## Script 1.50: Simulate-Estimate.R
'# Set the random seed
set.seed(123456)
'# Draw a sample given the population parameters
sample <- rnorm(100,10,2)
'# Estimate the population mean with the sample average
mean(sample)
'# Draw a different sample and estimate again:
sample <- rnorm(100,10,2)
mean(sample)
'# Draw a third sample and estimate again:
sample <- rnorm(100,10,2)
mean(sample)
## Script 1.51: Simulation-Repeated.R
'# Set the random seed
set.seed(123456)
'# initialize ybar to a vector of length r=10000 to later store results:
r <- 10000
ybar <- numeric(r)
'# repeat r times:
for(j in 1:r) {
'# Draw a sample and store the sample mean in pos. j=1,2,... of ybar:
sample <- rnorm(100,10,2)
ybar[j] <- mean(sample)
}
## Script 1.52: Simulation-Repeated-Results.R
'# The first 20 of 10000 estimates:
ybar[1:20]
'# Simulated mean:
mean(ybar)
'# Simulated variance:

# 2. Scripts Used in Chapter 02
317
var(ybar)
'# Simulated density:
plot(density(ybar))
curve( dnorm(x,10,sqrt(.04)), add=TRUE,lty=2)
## Script 1.53: Simulation-Inference.R
'# Set the random seed
set.seed(123456)
'# initialize vectors to later store results:
r <- 10000
CIlower <- numeric(r); CIupper <- numeric(r)
pvalue1 <- numeric(r); pvalue2 <- numeric(r)
'# repeat r times:
for(j in 1:r) {
'# Draw a sample
sample <- rnorm(100,10,2)
'# test the (correct) null hypothesis mu=10:
testres1 <- t.test(sample,mu=10)
'# store CI & p value:
CIlower[j] <- testres1$conf.int[1]
CIupper[j] <- testres1$conf.int[2]
pvalue1[j] <- testres1$p.value
'# test the (incorrect) null hypothesis mu=9.5 & store the p value:
pvalue2[j] <- t.test(sample,mu=9.5)$p.value
}
'# Test results as logical value
reject1<-pvalue1<=0.05;
reject2<-pvalue2<=0.05
table(reject1)
table(reject2)
## Script 1.54: Simulation-Inference-Figure.R
'# Needs Simulation-Inference.R to be run first
'# color vector:
color <- rep(gray(.5),100)
color[reject1[1:100]] <- "black"
'# Prepare empty plot with correct axis limits & labels:
plot(0, xlim=c(9,11), ylim=c(1,100),
ylab="Sample No.", xlab="", main="Correct H0")
'# Vertical line at 10:
abline(v=10, lty=2)
'# Add the 100 first CIs (y is equal to j for both points):
for(j in 1:100) {
lines(c(CIlower[j],CIupper[j]),c(j,j),col=color[j],lwd=2)
}
2. Scripts Used in Chapter 02
## Script 2.1: Example-2-3.R
data(ceosal1, package=’wooldridge’)
attach(ceosal1)

318
R Scripts
'# ingredients to the OLS formulas
cov(roe,salary)
var(roe)
mean(salary)
mean(roe)
'# manual calculation of OLS coefficients
( b1hat <- cov(roe,salary)/var(roe) )
( b0hat <- mean(salary) - b1hat*mean(roe)
)
'# "detach" the data frame
detach(ceosal1)
## Script 2.2: Example-2-3-2.R
data(ceosal1, package=’wooldridge’)
'# OLS regression
lm( salary ~ roe, data=ceosal1 )
## Script 2.3: Example-2-3-3.R
data(ceosal1, package=’wooldridge’)
'# OLS regression
CEOregres <- lm( salary ~ roe, data=ceosal1 )
'# Scatter plot (restrict y axis limits)
with(ceosal1, plot(roe, salary, ylim=c(0,4000)))
'# Add OLS regression line
abline(CEOregres)
## Script 2.4: Example-2-4.R
data(wage1, package=’wooldridge’)
'# OLS regression:
lm(wage ~ educ, data=wage1)
## Script 2.5: Example-2-5.R
data(vote1, package=’wooldridge’)
'# OLS regression (parentheses for immediate output):
( VOTEres <- lm(voteA ~ shareA, data=vote1) )
'# scatter plot with regression line:
with(vote1, plot(shareA, voteA))
abline(VOTEres)
## Script 2.6: Example-2-6.R
data(ceosal1, package=’wooldridge’)
'# extract variables as vectors:
sal <- ceosal1$salary
roe <- ceosal1$roe
'# regression with vectors:

2. Scripts Used in Chapter 02
319
CEOregres <- lm( sal ~ roe
)
'# obtain predicted values and residuals
sal.hat <- fitted(CEOregres)
u.hat <- resid(CEOregres)
'# Wooldridge, Table 2.2:
cbind(roe, sal, sal.hat, u.hat)[1:15,]
## Script 2.7: Example-2-7.R
data(wage1, package=’wooldridge’)
WAGEregres <- lm(wage ~ educ, data=wage1)
'# obtain coefficients, predicted values and residuals
b.hat <- coef(WAGEregres)
wage.hat <- fitted(WAGEregres)
u.hat <- resid(WAGEregres)
'# Confirm property (1):
mean(u.hat)
'# Confirm property (2):
cor(wage1$educ , u.hat)
'# Confirm property (3):
mean(wage1$wage)
b.hat[1] + b.hat[2]
*
mean(wage1$educ)
## Script 2.8: Example-2-8.R
data(ceosal1, package=’wooldridge’)
CEOregres <- lm( salary ~ roe, data=ceosal1 )
'# Calculate predicted values & residuals:
sal.hat <- fitted(CEOregres)
u.hat <- resid(CEOregres)
'# Calculate R^2 in three different ways:
sal <- ceosal1$salary
var(sal.hat) / var(sal)
1 - var(u.hat) / var(sal)
cor(sal, sal.hat)^2
## Script 2.9: Example-2-9.R
data(vote1, package=’wooldridge’)
VOTEres <- lm(voteA ~ shareA, data=vote1)
'# Summary of the regression results
summary(VOTEres)
'# Calculate R^2 manually:
var( fitted(VOTEres) ) / var( vote1$voteA )

320
R Scripts
## Script 2.10: Example-2-10.R
data(wage1, package=’wooldridge’)
'# Estimate log-level model
lm( log(wage) ~ educ, data=wage1 )
## Script 2.11: Example-2-11.R
data(ceosal1, package=’wooldridge’)
'# Estimate log-log model
lm( log(salary) ~ log(sales), data=ceosal1 )
## Script 2.12: SLR-Origin-Const.R
data(ceosal1, package=’wooldridge’)
'# Usual OLS regression:
(reg1 <- lm( salary ~ roe, data=ceosal1))
'# Regression without intercept (through origin):
(reg2 <- lm( salary ~ 0 + roe, data=ceosal1))
'# Regression without slope (on a constant):
(reg3 <- lm( salary ~ 1 , data=ceosal1))
'# average y:
mean(ceosal1$salary)
'# Scatter Plot with all 3 regression lines
plot(ceosal1$roe, ceosal1$salary, ylim=c(0,4000))
abline(reg1, lwd=2, lty=1)
abline(reg2, lwd=2, lty=2)
abline(reg3, lwd=2, lty=3)
legend("topleft",c("full","through origin","const only"),lwd=2,lty=1:3)
## Script 2.13: Example-2-12.R
data(meap93, package=’wooldridge’)
'# Estimate the model and save the results as "results"
results <- lm(math10 ~ lnchprg, data=meap93)
'# Number of obs.
( n <- nobs(results) )
'# SER:
(SER <- sd(resid(results))
*
sqrt((n-1)/(n-2)) )
'# SE of b0hat & b1hat, respectively:
SER / sd(meap93$lnchprg) / sqrt(n-1)
*
sqrt(mean(meap93$lnchprg^2))
SER / sd(meap93$lnchprg) / sqrt(n-1)
'# Automatic calculations:
summary(results)
## Script 2.14: SLR-Sim-Sample.R
'# Set the random seed
set.seed(1234567)
'# set sample size
n<-1000

2. Scripts Used in Chapter 02
321
'# set true parameters: betas and sd of u
b0<-1; b1<-0.5; su<-2
'# Draw a sample of size n:
x <- rnorm(n,4,1)
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
'# estimate parameters by OLS
(olsres <- lm(y~x))
'# features of the sample for the variance formula:
mean(x^2)
sum((x-mean(x))^2)
'# Graph
plot(x, y, col="gray", xlim=c(0,8) )
abline(b0,b1,lwd=2)
abline(olsres,col="gray",lwd=2)
legend("topleft",c("pop. regr. fct.","OLS regr. fct."),
lwd=2,col=c("black","gray"))
## Script 2.15: SLR-Sim-Model.R
'# Set the random seed
set.seed(1234567)
'# set sample size and number of simulations
n<-1000; r<-10000
'# set true parameters: betas and sd of u
b0<-1; b1<-0.5; su<-2
'# initialize b0hat and b1hat to store results later:
b0hat <- numeric(r)
b1hat <- numeric(r)
'# repeat r times:
for(j in 1:r) {
'# Draw a sample of size n:
x <- rnorm(n,4,1)
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
'# estimate parameters by OLS and store them in the vectors
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.16: SLR-Sim-Model-Condx.R
'# Set the random seed
set.seed(1234567)
'# set sample size and number of simulations
n<-1000; r<-10000
'# set true parameters: betas and sd of u

322
R Scripts
b0<-1; b1<-0.5; su<-2
'# initialize b0hat and b1hat to store results later:
b0hat <- numeric(r)
b1hat <- numeric(r)
'# Draw a sample of x, fixed over replications:
x <- rnorm(n,4,1)
'# repeat r times:
for(j in 1:r) {
'# Draw a sample of y:
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
'# estimate parameters by OLS and store them in the vectors
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.17: SLR-Sim-Results.R
'# MC estimate of the expected values:
mean(b0hat)
mean(b1hat)
'# MC estimate of the variances:
var(b0hat)
var(b1hat)
'# Initialize empty plot
plot( NULL, xlim=c(0,8), ylim=c(0,6), xlab="x", ylab="y")
'# add OLS regression lines
for (j in 1:10) abline(b0hat[j],b1hat[j],col="gray")
'# add population regression line
abline(b0,b1,lwd=2)
'# add legend
legend("topleft",c("Population","OLS regressions"),
lwd=c(2,1),col=c("black","gray"))
## Script 2.18: SLR-Sim-ViolSLR4.R
'# Set the random seed
set.seed(1234567)
'# set sample size and number of simulations
n<-1000; r<-10000
'# set true parameters: betas and sd of u
b0<-1; b1<-0.5; su<-2
'# initialize b0hat and b1hat to store results later:
b0hat <- numeric(r)
b1hat <- numeric(r)
'# Draw a sample of x, fixed over replications:
x <- rnorm(n,4,1)
'# repeat r times:

2. Scripts Used in Chapter 02
323
for(j in 1:r) {
'# Draw a sample of y:
u <- rnorm(n, (x-4)/5, su)
y <- b0 + b1*x
+ u
'# estimate parameters by OLS and store them in the vectors
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.19: SLR-Sim-Results-ViolSLR4.R
'# MC estimate of the expected values:
mean(b0hat)
mean(b1hat)
'# MC estimate of the variances:
var(b0hat)
var(b1hat)
## Script 2.20: SLR-Sim-ViolSLR5.R
'# Set the random seed
set.seed(1234567)
'# set sample size and number of simulations
n<-1000; r<-10000
'# set true parameters: betas and sd of u
b0<-1; b1<-0.5; su<-2
'# initialize b0hat and b1hat to store results later:
b0hat <- numeric(r)
b1hat <- numeric(r)
'# Draw a sample of x, fixed over replications:
x <- rnorm(n,4,1)
'# repeat r times:
for(j in 1:r) {
'# Draw a sample of y:
varu <- 4/exp(4.5)
*
exp(x)
u <- rnorm(n, 0, sqrt(varu) )
y <- b0 + b1*x
+ u
'# estimate parameters by OLS and store them in the vectors
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.21: SLR-Sim-Results-ViolSLR5.R
'# MC estimate of the expected values:
mean(b0hat)
mean(b1hat)
'# MC estimate of the variances:
var(b0hat)
var(b1hat)

324
R Scripts
# 3. Scripts Used in Chapter 03
## Script 3.1: Example-3-1.R
data(gpa1, package=’wooldridge’)
'# Just obtain parameter estimates:
lm(colGPA ~ hsGPA+ACT, data=gpa1)
'# Store results under "GPAres" and display full table:
GPAres <- lm(colGPA ~ hsGPA+ACT, data=gpa1)
summary(GPAres)
## Script 3.2: Example-3-2.R
data(wage1, package=’wooldridge’)
'# OLS regression:
summary( lm(log(wage) ~ educ+exper+tenure, data=wage1) )
## Script 3.3: Example-3-3.R
data(k401k, package=’wooldridge’)
'# OLS regression:
summary( lm(prate ~ mrate+age, data=k401k) )
## Script 3.4: Example-3-5.R
data(crime1, package=’wooldridge’)
'# Model without avgsen:
summary( lm(narr86 ~ pcnv+ptime86+qemp86, data=crime1) )
'# Model with avgsen:
summary( lm(narr86 ~ pcnv+avgsen+ptime86+qemp86, data=crime1) )
## Script 3.5: Example-3-6.R
data(wage1, package=’wooldridge’)
'# OLS regression:
summary( lm(log(wage) ~ educ, data=wage1) )
## Script 3.6: OLS-Matrices.R
data(gpa1, package=’wooldridge’)
'# Determine sample size & no. of regressors:
n <- nrow(gpa1); k<-2
'# extract y
y <- gpa1$colGPA
'# extract X & add a column of ones
X <- cbind(1, gpa1$hsGPA, gpa1$ACT)
'# Display first rows of X:
head(X)
'# Parameter estimates:
( bhat <- solve( t(X)%*%X ) %*% t(X)%*%y
)

( R2.hsGPA <- summary( lm(hsGPA~ACT, data=gpa1) )$r.squared ) ( VIF.hsGPA <- 1/(1-R2.hsGPA) )
'# manual calculation of SE of hsGPA coefficient:
n <- nobs(res)
sdx <- sd(gpa1$hsGPA) * sqrt((n-1)/n) '# (Note: sd() uses the (n-1) version) ( SE.hsGPA <- 1/sqrt(n) 
* SER/sdx * sqrt(VIF.hsGPA) )
3. Scripts Used in Chapter 03
325
'# Residuals, estimated variance of u and SER:
uhat <- y - X %*%
bhat
sigsqhat <- as.numeric( t(uhat) %*%
uhat / (n-k-1) )
( SER <- sqrt(sigsqhat) )
'# Estimated variance of the parameter estimators and SE:
Vbetahat <- sigsqhat
*
solve( t(X)%*%X
)
( se <- sqrt( diag(Vbetahat) ) )
## Script 3.7: Omitted-Vars.R
data(gpa1, package=’wooldridge’)
'# Parameter estimates for full and simple model:
beta.hat <- coef( lm(colGPA ~ ACT+hsGPA, data=gpa1) )
beta.hat
'# Relation between regressors:
delta.tilde <- coef( lm(hsGPA ~ ACT, data=gpa1) )
delta.tilde
'# Omitted variables formula for beta1.tilde:
beta.hat["ACT"] + beta.hat["hsGPA"]*delta.tilde["ACT"]
'# Actual regression with hsGPA omitted:
lm(colGPA ~ ACT, data=gpa1)
## Script 3.8: MLR-SE.R
data(gpa1, package=’wooldridge’)
'# Full estimation results including automatic SE :
res <- lm(colGPA ~ hsGPA+ACT, data=gpa1)
summary(res)
'# Extract SER (instead of calculation via residuals)
( SER <- summary(res)$sigma )
'# regressing hsGPA on ACT for calculation of R2 & VIF
## Script 3.9: MLR-VIF.R
data(wage1, package=’wooldridge’)
'# OLS regression:
lmres <- lm(log(wage) ~ educ+exper+tenure, data=wage1)
'# Regression output:
summary(lmres)
'# Load package "car" (has to be installed):
library(car)

326
R Scripts
'# Automatically calculate VIF :
vif(lmres)
# 4. Scripts Used in Chapter 04
## Script 4.1: Example-4-3.R
data(gpa1, package=’wooldridge’)
'# Store results under "sumres" and display full table:
( sumres <- summary( lm(colGPA ~ hsGPA+ACT+skipped, data=gpa1) ) )
'# Manually confirm the formulas: Extract coefficients and SE
regtable <- sumres$coefficients
bhat <- regtable[,1]
se
<- regtable[,2]
'# Reproduce t statistic
( tstat <- bhat / se )
'# Reproduce p value
( pval
<- 2*pt(-abs(tstat),137)
)
## Script 4.2: Example-4-1.R
data(wage1, package=’wooldridge’)
'# OLS regression:
summary( lm(log(wage) ~ educ+exper+tenure, data=wage1) )
## Script 4.3: Example-4-8.R
data(rdchem, package=’wooldridge’)
'# OLS regression:
myres <- lm(log(rd) ~ log(sales)+profmarg, data=rdchem)
'# Regression output:
summary(myres)
'# 95% CI:
confint(myres)
'# 99% CI:
confint(myres, level=0.99)
## Script 4.4: F-Test-MLB.R
data(mlb1, package=’wooldridge’)
'# Unrestricted OLS regression:
res.ur <- lm(log(salary) ~ years+gamesyr+bavg+hrunsyr+rbisyr, data=mlb1)
'# Restricted OLS regression:
res.r <- lm(log(salary) ~ years+gamesyr, data=mlb1)
'# R2:
( r2.ur <- summary(res.ur)$r.squared )
( r2.r <- summary(res.r)$r.squared )

# 5. Scripts Used in Chapter 05
327
'# F statistic:
( F <- (r2.ur-r2.r) / (1-r2.ur)
*
347/3 )
'# p value = 1-cdf of the appropriate F distribution:
1-pf(F, 3,347)
## Script 4.5: F-Test-MLB-auto.R
data(mlb1, package=’wooldridge’)
'# Unrestricted OLS regression:
res.ur <- lm(log(salary) ~ years+gamesyr+bavg+hrunsyr+rbisyr, data=mlb1)
'# Load package "car" (which has to be installed on the computer)
library(car)
'# F test
myH0 <- c("bavg","hrunsyr","rbisyr")
linearHypothesis(res.ur, myH0)
## Script 4.6: F-Test-MLB-auto2.R
'# F test (F-Test-MLB-auto.R has to be run first!)
myH0 <- c("bavg", "hrunsyr=2*rbisyr")
linearHypothesis(res.ur, myH0)
## Script 4.7: F-Test-MLB-auto3.R
'# Note: ## Script "F-Test-MLB-auto.R" has to be run first to create res.ur.
'# Which variables used in res.ur contain "yr" in their names?
myH0 <- matchCoefs(res.ur,"yr")
myH0
'# F test (F-Test-MLB-auto.R has to be run first!)
linearHypothesis(res.ur, myH0)
## Script 4.8: Example-4-10.R
data(meap93, package=’wooldridge’)
'# define new variable within data frame
meap93$b_s <- meap93$benefits / meap93$salary
'# Estimate three different models
model1<- lm(log(salary) ~ b_s
, data=meap93)
model2<- lm(log(salary) ~ b_s+log(enroll)+log(staff), data=meap93)
model3<- lm(log(salary) ~ b_s+log(enroll)+log(staff)+droprate+gradrate
, data=meap93)
'# Load package and display table of results
library(stargazer)
stargazer(list(model1,model2,model3),type="text",keep.stat=c("n","rsq"))
5. Scripts Used in Chapter 05
## Script 5.1: Sim-Asy-OLS-norm.R
'# Note: We’ll have to set the sample size first, e.g. by uncommenting:
'# n <- 100
'# Set the random seed

328
R Scripts
set.seed(1234567)
'# set true parameters: intercept & slope
b0 <- 1; b1 <- 0.5
'# initialize b1hat to store 10000 results:
b1hat <- numeric(10000)
'# Draw a sample of x, fixed over replications:
x <- rnorm(n,4,1)
'# repeat r times:
for(j in 1:10000) {
'# Draw a sample of u (std. normal):
u <- rnorm(n)
'# Draw a sample of y:
y <- b0 + b1*x
+ u
'# regress y on x and store slope estimate at position j
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.2: Sim-Asy-OLS-chisq.R
'# Note: We’ll have to set the sample size first, e.g. by uncommenting:
'# n <- 100
'# Set the random seed
set.seed(1234567)
'# set true parameters: intercept & slope
b0<-1; b1<-0.5
'# initialize b1hat to store 10000 results:
b1hat <- numeric(10000)
'# Draw a sample of x, fixed over replications:
x <- rnorm(n,4,1)
'# repeat r times:
for(j in 1:10000) {
'# Draw a sample of u (standardized chi-squared[1]):
u <- ( rchisq(n,1)-1 ) / sqrt(2)
'# Draw a sample of y:
y <- b0 + b1*x
+ u
'# regress y on x and store slope estimate at position j
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.3: Sim-Asy-OLS-uncond.R
'# Note: We’ll have to set the sample size first, e.g. by uncommenting:
'# n <- 100
'# Set the random seed
set.seed(1234567)
'# set true parameters: intercept & slope
b0<-1; b1<-0.5
'# initialize b1hat to store 10000 results:
b1hat <- numeric(10000)
'# repeat r times:
for(j in 1:10000) {
'# Draw a sample of x, varying over replications:
x <- rnorm(n,4,1)
'# Draw a sample of u (std. normal):
u <- rnorm(n)

# 6. Scripts Used in Chapter 06
329
'# Draw a sample of y:
y <- b0 + b1*x
+ u
'# regress y on x and store slope estimate at position j
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.4: Example-5-3.R
data(crime1, package=’wooldridge’)
'# 1. Estimate restricted model:
restr <- lm(narr86 ~ pcnv+ptime86+qemp86, data=crime1)
'# 2. Regression of residuals from restricted model:
utilde <- resid(restr)
LMreg <- lm(utilde ~ pcnv+ptime86+qemp86+avgsen+tottime, data=crime1)
'# R-squared:
(r2 <- summary(LMreg)$r.squared )
'# 3. Calculation of LM test statistic:
LM <- r2
*
nobs(LMreg)
LM
'# 4. Critical value from chi-squared distribution, alpha=10%:
qchisq(1-0.10, 2)
'# Alternative to critical value: p value
1-pchisq(LM, 2)
'# Alternative: automatic F test (see above)
library(car)
unrestr <- lm(narr86 ~ pcnv+ptime86+qemp86+avgsen+tottime, data=crime1)
linearHypothesis(unrestr, c("avgsen=0","tottime=0"))
6. Scripts Used in Chapter 06
## Script 6.1: Data-Scaling.R
data(bwght, package=’wooldridge’)
'# Basic model:
lm( bwght ~ cigs+faminc, data=bwght)
'# Weight in pounds, manual way:
bwght$bwghtlbs <- bwght$bwght/16
lm( bwghtlbs ~ cigs+faminc, data=bwght)
'# Weight in pounds, direct way:
lm( I(bwght/16) ~ cigs+faminc, data=bwght)
'# Packs of cigarettes:
lm( bwght ~ I(cigs/20) +faminc, data=bwght)
## Script 6.2: Example-6-1.R
data(hprice2, package=’wooldridge’)

330
R Scripts
'# Estimate model with standardized variables:
lm(scale(price) ~ 0+scale(nox)+scale(crime)+scale(rooms)+
scale(dist)+scale(stratio), data=hprice2)
## Script 6.3: Formula-Logarithm.R
data(hprice2, package=’wooldridge’)
'# Estimate model with logs:
lm(log(price)~log(nox)+rooms, data=hprice2)
## Script 6.4: Example-6-2.R
data(hprice2, package=’wooldridge’)
res <- lm(log(price)~log(nox)+log(dist)+rooms+I(rooms^2)+
stratio,data=hprice2)
summary(res)
'# Using poly(...):
res <- lm(log(price)~log(nox)+log(dist)+poly(rooms,2,raw=TRUE)+
stratio,data=hprice2)
summary(res)
## Script 6.5: Example-6-2-Anova.R
library(car)
data(hprice2, package=’wooldridge’)
res <- lm(log(price)~log(nox)+log(dist)+poly(rooms,2,raw=TRUE)+
stratio,data=hprice2)
'# Manual F test for rooms:
linearHypothesis(res, matchCoefs(res,"rooms"))
'# ANOVA (type 2) table:
Anova(res)
## Script 6.6: Example-6-3.R
data(attend, package=’wooldridge’)
'# Estimate model with interaction effect:
(myres<-lm(stndfnl~atndrte*priGPA+ACT+I(priGPA^2)+I(ACT^2),
data=attend))
'# Estimate for partial effect at priGPA=2.59:
b <- coef(myres)
b["atndrte"] + 2.59*b["atndrte:priGPA"]
'# Test partial effect for priGPA=2.59:
library(car)
linearHypothesis(myres,c("atndrte+2.59*atndrte:priGPA"))
## Script 6.7: Example-6-5.R
data(gpa2, package=’wooldridge’)
'# Regress and report coefficients
reg <- lm(colgpa~sat+hsperc+hsize+I(hsize^2),data=gpa2)
reg

6. Scripts Used in Chapter 06
331
'# Generate data set containing the regressor values for predictions
cvalues <- data.frame(sat=1200, hsperc=30, hsize=5)
'# Point estimate of prediction
predict(reg, cvalues)
'# Point estimate and 95% confidence interval
predict(reg, cvalues, interval = "confidence")
'# Define three sets of regressor variables
cvalues <- data.frame(sat=c(1200,900,1400), hsperc=c(30,20,5),
hsize=c(5,3,1))
cvalues
'# Point estimates and 99% confidence intervals for these
predict(reg, cvalues, interval = "confidence", level=0.99)
## Script 6.8: Example-6-6.R
data(gpa2, package=’wooldridge’)
'# Regress (as before)
reg <- lm(colgpa~sat+hsperc+hsize+I(hsize^2),data=gpa2)
'# Define three sets of regressor variables (as before)
cvalues <- data.frame(sat=c(1200,900,1400), hsperc=c(30,20,5),
hsize=c(5,3,1))
'# Point estimates and 95% prediction intervals for these
predict(reg, cvalues, interval = "prediction")
## Script 6.9: Effects-Manual.R
'# Repeating the regression from Example 6.2:
data(hprice2, package=’wooldridge’)
res <- lm( log(price) ~ log(nox)+log(dist)+rooms+I(rooms^2)+stratio,
data=hprice2)
'# Predictions: Values of the regressors:
'# rooms = 4-8, all others at the sample mean:
X <- data.frame(rooms=seq(4,8),nox=5.5498,dist=3.7958,stratio=18.4593)
'# Calculate predictions and confidence interval:
pred <- predict(res, X, interval = "confidence")
'# Table of regressor values, predictions and CI:
cbind(X,pred)
'# Plot
matplot(X$rooms, pred, type="l", lty=c(1,2,2))
## Script 6.10: Effects-Automatic.R
'# Repeating the regression from Example 6.2:
data(hprice2, package=’wooldridge’)
res <- lm( log(price) ~ log(nox)+log(dist)+rooms+I(rooms^2)+stratio,
data=hprice2)

332
R Scripts
'# Automatic effects plot using the package "effects"
library(effects)
plot( effect("rooms",res) )
# 7. Scripts Used in Chapter 07
## Script 7.1: Example-7-1.R
data(wage1, package=’wooldridge’)
lm(wage ~ female+educ+exper+tenure, data=wage1)
## Script 7.2: Example-7-6.R
data(wage1, package=’wooldridge’)
lm(log(wage)~married*female+educ+exper+I(exper^2)+tenure+I(tenure^2),
data=wage1)
## Script 7.3: Example-7-1-logical.R
data(wage1, package=’wooldridge’)
'# replace "female" with logical variable
wage1$female <- as.logical(wage1$female)
table(wage1$female)
'# regression with logical variable
lm(wage ~ female+educ+exper+tenure, data=wage1)
## Script 7.4: Regr-Factors.R
data(CPS1985,package="AER")
'# Table of categories and frequencies for two factor variables:
table(CPS1985$gender)
table(CPS1985$occupation)
'# Directly using factor variables in regression formula:
lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
'# Manually redefine the
reference category:
CPS1985$gender <- relevel(CPS1985$gender,"female")
CPS1985$occupation <- relevel(CPS1985$occupation,"management")
'# Rerun regression:
lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
## Script 7.5: Regr-Factors-Anova.R
data(CPS1985,package="AER")
'# Regression
res <- lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
'# ANOVA table
car::Anova(res)

# 8. Scripts Used in Chapter 08
333
## Script 7.6: Example-7-8.R
data(lawsch85, package=’wooldridge’)
'# Define cut points for the rank
cutpts <- c(0,10,25,40,60,100,175)
'# Create factor variable containing ranges for the rank
lawsch85$rankcat <- cut(lawsch85$rank, cutpts)
'# Display frequencies
table(lawsch85$rankcat)
'# Choose reference category
lawsch85$rankcat <- relevel(lawsch85$rankcat,"(100,175]")
'# Run regression
(res <- lm(log(salary)~rankcat+LSAT+GPA+log(libvol)+log(cost), data=lawsch85))
'# ANOVA table
car::Anova(res)
## Script 7.7: Dummy-Interact.R
data(gpa3, package=’wooldridge’)
'# Model with full interactions with female dummy (only for spring data)
reg<-lm(cumgpa~female*(sat+hsperc+tothrs),
data=gpa3, subset=(spring==1))
summary(reg)
'# F-Test from package "car". H0: the interaction coefficients are zero
'# matchCoefs(...) selects all coeffs with names containing "female"
library(car)
linearHypothesis(reg, matchCoefs(reg, "female"))
## Script 7.8: Dummy-Interact-Sep.R
data(gpa3, package=’wooldridge’)
'# Estimate model for males (& spring data)
lm(cumgpa~sat+hsperc+tothrs, data=gpa3, subset=(spring==1&female==0))
'# Estimate model for females (& spring data)
lm(cumgpa~sat+hsperc+tothrs, data=gpa3, subset=(spring==1&female==1))
8. Scripts Used in Chapter 08
## Script 8.1: Example-8-2.R
data(gpa3, package=’wooldridge’)
'# load packages (which need to be installed!)
library(lmtest); library(car)
'# Estimate model (only for spring data)
reg <- lm(cumgpa~sat+hsperc+tothrs+female+black+white,
data=gpa3, subset=(spring==1))
'# Usual SE:
coeftest(reg)

334
R Scripts
'# Refined White heteroscedasticity-robust SE:
coeftest(reg, vcov=hccm)
## Script 8.2: Example-8-2-cont.R
'# F-Tests using different variance-covariance formulas:
myH0 <- c("black","white")
'# Ususal VCOV
linearHypothesis(reg, myH0)
'# Refined White VCOV
linearHypothesis(reg, myH0, vcov=hccm)
'# Classical White VCOV
linearHypothesis(reg, myH0, vcov=hccm(reg,type="hc0"))
## Script 8.3: Example-8-4.R
data(hprice1, package=’wooldridge’)
'# Estimate model
reg <- lm(price~lotsize+sqrft+bdrms, data=hprice1)
reg
'# Automatic BP test
library(lmtest)
bptest(reg)
'# Manual regression of squared residuals
summary(lm( resid(reg)^2 ~ lotsize+sqrft+bdrms, data=hprice1))
## Script 8.4: Example-8-5.R
data(hprice1, package=’wooldridge’)
'# Estimate model
reg <- lm(log(price)~log(lotsize)+log(sqrft)+bdrms, data=hprice1)
reg
'# BP test
library(lmtest)
bptest(reg)
'# White test
bptest(reg, ~ fitted(reg) + I(fitted(reg)^2) )
## Script 8.5: Example-8-6.R
data(k401ksubs, package=’wooldridge’)
'# OLS (only for singles: fsize==1)
lm(nettfa ~ inc + I((age-25)^2) + male + e401k,
data=k401ksubs, subset=(fsize==1))
'# WLS
lm(nettfa ~ inc + I((age-25)^2) + male + e401k, weight=1/inc,
data=k401ksubs, subset=(fsize==1))
## Script 8.6: WLS-Robust.R
data(k401ksubs, package=’wooldridge’)
'# WLS

# 9. Scripts Used in Chapter 09
335
wlsreg <- lm(nettfa ~ inc + I((age-25)^2) + male + e401k,
weight=1/inc, data=k401ksubs, subset=(fsize==1))
'# non-robust results
library(lmtest); library(car)
coeftest(wlsreg)
'# robust results (Refined White SE:)
coeftest(wlsreg,hccm)
## Script 8.7: Example-8-7.R
data(smoke, package=’wooldridge’)
'# OLS
olsreg<-lm(cigs~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
data=smoke)
olsreg
'# BP test
library(lmtest)
bptest(olsreg)
'# FGLS: estimation of the variance function
logu2 <- log(resid(olsreg)^2)
varreg<-lm(logu2~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
data=smoke)
'# FGLS: WLS
w <- 1/exp(fitted(varreg))
lm(cigs~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
weight=w ,data=smoke)
9. Scripts Used in Chapter 09
## Script 9.1: Example-9-2-manual.R
data(hprice1, package=’wooldridge’)
'# original linear regression
orig <- lm(price ~ lotsize+sqrft+bdrms, data=hprice1)
'# regression for RESET test
RESETreg <- lm(price ~ lotsize+sqrft+bdrms+I(fitted(orig)^2)+
I(fitted(orig)^3), data=hprice1)
RESETreg
'# RESET test. H0: all coeffs including "fitted" are=0
library(car)
linearHypothesis(RESETreg, matchCoefs(RESETreg,"fitted"))
## Script 9.2: Example-9-2-automatic.R
data(hprice1, package=’wooldridge’)
'# original linear regression
orig <- lm(price ~ lotsize+sqrft+bdrms, data=hprice1)

336
R Scripts
'# RESET test
library(lmtest)
resettest(orig)
## Script 9.3: Nonnested-Test.R
data(hprice1, package=’wooldridge’)
'# two alternative models
model1 <- lm(price ~
lotsize
+
sqrft
+ bdrms, data=hprice1)
model2 <- lm(price ~ log(lotsize) + log(sqrft) + bdrms, data=hprice1)
'# Test against comprehensive model
library(lmtest)
encomptest(model1,model2, data=hprice1)
## Script 9.4: Sim-ME-Dep.R
'# Set the random seed
set.seed(1234567)
'# set true parameters: intercept & slope
b0<-1; b1<-0.5
'# initialize b1hat to store 10000 results:
b1hat <- numeric(10000)
b1hat.me <- numeric(10000)
'# Draw a sample of x, fixed over replications:
x <- rnorm(1000,4,1)
'# repeat r times:
for(j in 1:10000) {
'# Draw a sample of u
u <- rnorm(1000)
'# Draw a sample of ystar:
ystar <- b0 + b1*x
+ u
'# regress ystar on x and store slope estimate at position j
bhat <- coef( lm(ystar~x) )
b1hat[j] <- bhat["x"]
'# Measurement error and mismeasured y:
e0 <- rnorm(1000)
y <- ystar+e0
'# regress y on x and store slope estimate at position j
bhat.me <- coef( lm(y~x) )
b1hat.me[j] <- bhat.me["x"]
}
'# Mean with and without ME
c( mean(b1hat), mean(b1hat.me) )
'# Variance with and without ME
c( var(b1hat), var(b1hat.me) )
## Script 9.5: Sim-ME-Explan.R
'# Set the random seed
set.seed(1234567)
'# set true parameters: intercept & slope
b0<-1; b1<-0.5
'# initialize b1hat to store 10000 results:
b1hat <- numeric(10000)
b1hat.me <- numeric(10000)

9. Scripts Used in Chapter 09
337
'# Draw a sample of x, fixed over replications:
xstar <- rnorm(1000,4,1)
'# repeat r times:
for(j in 1:10000) {
'# Draw a sample of u
u <- rnorm(1000)
'# Draw a sample of ystar:
y <- b0 + b1*xstar
+ u
'# regress y on xstar and store slope estimate at position j
bhat <- coef( lm(y~xstar) )
b1hat[j] <- bhat["xstar"]
'# Measurement error and mismeasured y:
e1 <- rnorm(1000)
x <- xstar+e1
'# regress y on x and store slope estimate at position j
bhat.me <- coef( lm(y~x) )
b1hat.me[j] <- bhat.me["x"]
}
'# Mean with and without ME
c( mean(b1hat), mean(b1hat.me) )
'# Variance with and without ME
c( var(b1hat), var(b1hat.me) )
## Script 9.6: NA-NaN-Inf.R
x <- c(-1,0,1,NA,NaN,-Inf,Inf)
logx <- log(x)
invx <- 1/x
ncdf <- pnorm(x)
isna <- is.na(x)
data.frame(x,logx,invx,ncdf,isna)
## Script 9.7: Missings.R
data(lawsch85, package=’wooldridge’)
'# extract LSAT
lsat <- lawsch85$LSAT
'# Create logical indicator for missings
missLSAT <- is.na(lawsch85$LSAT)
'# LSAT and indicator for Schools No. 120-129:
rbind(lsat,missLSAT)[,120:129]
'# Frequencies of indicator
table(missLSAT)
'# Missings for all variables in data frame (counts)
colSums(is.na(lawsch85))
'# Indicator for complete cases
compl <- complete.cases(lawsch85)
table(compl)

338
R Scripts
## Script 9.8: Missings-Analyses.R
data(lawsch85, package=’wooldridge’)
'# Mean of a variable with missings:
mean(lawsch85$LSAT)
mean(lawsch85$LSAT,na.rm=TRUE)
'# Regression with missings
summary(lm(log(salary)~LSAT+cost+age, data=lawsch85))
## Script 9.9: Outliers.R
data(rdchem, package=’wooldridge’)
'# Regression
reg <- lm(rdintens~sales+profmarg, data=rdchem)
'# Studentized residuals for all observations:
studres <- rstudent(reg)
'# Display extreme values:
min(studres)
max(studres)
'# Histogram (and overlayed density plot):
hist(studres, freq=FALSE)
lines(density(studres), lwd=2)
## Script 9.10: LAD.R
data(rdchem, package=’wooldridge’)
'# OLS Regression
ols <- lm(rdintens ~ I(sales/1000) +profmarg, data=rdchem)
'# LAD Regression
library(quantreg)
lad <- rq(rdintens ~ I(sales/1000) +profmarg, data=rdchem)
'# regression table
library(stargazer)
stargazer(ols,lad,
type = "text")
# 10. Scripts Used in Chapter 10
## Script 10.1: Example-10-2.R
data(intdef, package=’wooldridge’)
'# Linear regression of static model:
summary( lm(i3~inf+def,data=intdef)
)
## Script 10.2: Example-Barium.R
data(barium, package=’wooldridge’)
'# Imports from China: Variable "chnimp" from data frame "data"
'# Monthly time series starting Feb. 1978
impts <- ts(barium$chnimp, start=c(1978,2), frequency=12)

10. Scripts Used in Chapter 10
339
'# plot time series
plot(impts)
## Script 10.3: Example-zoo.R
data(intdef, package=’wooldridge’)
'# Variable "year" as the time measure:
intdef$year
'# define "zoo" object containing all data, time measure=year:
library(zoo)
zoodata <- zoo(intdef, order.by=intdef$year)
'# Time series plot of inflation
plot(zoodata$i3)
## Script 10.4: Example-quantmod.R
library(quantmod)
'# Which Yahoo Finance symbols?
'# See http://finance.yahoo.com/lookup:
'# "F" = Ford Motor Company
'# Download data
getSymbols("F", auto.assign=TRUE)
'# first and last 6 rows of resulting data frame:
head(F)
tail(F)
'# Time series plot of adjusted closing prices:
plot(F$F.Adjusted, las=2)
## Script 10.5: Example-10-4.R
'# Libraries for dynamic lm, regression table and F tests
library(dynlm);library(lmtest);library(car)
data(fertil3, package=’wooldridge’)
'# Define Yearly time series beginning in 1913
tsdata <- ts(fertil3, start=1913)
'# Linear regression of model with lags:
res <- dynlm(gfr ~ pe + L(pe) + L(pe,2) + ww2 + pill, data=tsdata)
coeftest(res)
'# F test. H0: all pe coefficients are=0
linearHypothesis(res, matchCoefs(res,"pe"))
## Script 10.6: Example-10-4-contd.R
'# Calculating the LRP
b<-coef(res)
b["pe"]+b["L(pe)"]+b["L(pe, 2)"]
'# F test. H0: LRP=0
linearHypothesis(res,"pe + L(pe) + L(pe, 2) = 0")

reg1 <- dynlm(return~L(return)           , data=tsdata) reg2 <- dynlm(return~L(return)+L(return,2)  
    , data=tsdata)
340
R Scripts
## Script 10.7: Example-10-7.R
library(dynlm);library(stargazer)
data(hseinv, package=’wooldridge’)
'# Define Yearly time series beginning in 1947
tsdata <- ts(hseinv, start=1947)
'# Linear regression of model with lags:
res1 <- dynlm(log(invpc) ~ log(price)
, data=tsdata)
res2 <- dynlm(log(invpc) ~ log(price) + trend(tsdata), data=tsdata)
'# Pretty regression table
stargazer(res1,res2, type="text")
## Script 10.8: Example-10-11.R
library(dynlm);library(lmtest)
data(barium, package=’wooldridge’)
'# Define monthly time series beginning in Feb. 1978
tsdata <- ts(barium, start=c(1978,2), frequency=12)
res <- dynlm(log(chnimp) ~ log(chempi)+log(gas)+log(rtwex)+befile6+
affile6+afdec6+ season(tsdata) , data=tsdata )
coeftest(res)
# 11. Scripts Used in Chapter 11
## Script 11.1: Example-11-4.R
library(dynlm);library(stargazer)
data(nyse, package=’wooldridge’)
'# Define time series (numbered 1,...,n)
tsdata <- ts(nyse)
'# Linear regression of models with lags:
reg3 <- dynlm(return~L(return)+L(return,2)+L(return,3), data=tsdata)
'# Pretty regression table
stargazer(reg1, reg2, reg3, type="text",
keep.stat=c("n","rsq","adj.rsq","f"))
## Script 11.2: Example-EffMkts.R
library(zoo);library(quantmod);library(dynlm);library(stargazer)
'# Download data using the quantmod package:
getSymbols("AAPL", auto.assign = TRUE)
'# Calculate return as the log difference
ret <- diff( log(AAPL$AAPL.Adjusted) )
'# Subset 2008-2016 by special xts indexing:
ret <- ret["2008/2016"]
'# Plot returns

11. Scripts Used in Chapter 11
341
plot(ret)
'# Linear regression of models with lags:
ret <- as.zoo(ret)
'# dynlm cannot handle xts objects
reg1 <- dynlm(ret~L(ret) )
reg2 <- dynlm(ret~L(ret)+L(ret,2) )
reg3 <- dynlm(ret~L(ret)+L(ret,2)+L(ret,3) )
'# Pretty regression table
stargazer(reg1, reg2, reg3, type="text",
keep.stat=c("n","rsq","adj.rsq","f"))
## Script 11.3: Simulate-RandomWalk.R
'# Initialize Random Number Generator
set.seed(348546)
'# initial graph
plot(c(0,50),c(0,0),type="l",lwd=2,ylim=c(-18,18))
'# loop over draws:
for(r in 1:30) {
'# i.i.d. standard normal shock
e <- rnorm(50)
'# Random walk as cumulative sum of shocks
y <- ts(cumsum(e))
'# Add line to graph
lines(y, col=gray(.6))
}
## Script 11.4: Simulate-RandomWalkDrift.R
'# Initialize Random Number Generator
set.seed(348546)
'# initial empty graph with expected value
plot(c(0,50),c(0,100),type="l",lwd=2)
'# loop over draws:
for(r in 1:30) {
'# i.i.d. standard normal shock
e <- rnorm(50)
'# Random walk as cumulative sum of shocks
y <- ts(cumsum(2+e))
'# Add line to graph
lines(y, col=gray(.6))
}
## Script 11.5: Simulate-RandomWalkDrift-Diff.R
'# Initialize Random Number Generator
set.seed(348546)
'# initial empty graph with expected value
plot(c(0,50),c(2,2),type="l",lwd=2,ylim=c(-1,5))
'# loop over draws:
for(r in 1:30) {
'# i.i.d. standard normal shock
e <- rnorm(50)
'# Random walk as cumulative sum of shocks
y <- ts(cumsum(2+e))
'# First difference

342
R Scripts
Dy <- diff(y)
'# Add line to graph
lines(Dy, col=gray(.6))
}
## Script 11.6: Example-11-6.R
'# Libraries for dynamic lm and "stargazer" regression table
library(dynlm);library(stargazer)
data(fertil3, package=’wooldridge’)
'# Define Yearly time series beginning in 1913
tsdata <- ts(fertil3, start=1913)
'# Linear regression of model with first differences:
res1 <- dynlm( d(gfr) ~ d(pe), data=tsdata)
'# Linear regression of model with lagged differences:
res2 <- dynlm( d(gfr) ~ d(pe) + L(d(pe)) + L(d(pe),2), data=tsdata)
'# Pretty regression table
stargazer(res1,res2,type="text")
# 12. Scripts Used in Chapter 12
## Script 12.1: Example-12-2.R
library(dynlm);library(lmtest)
data(phillips, package=’wooldridge’)
'# Define Yearly time series beginning in 1948
tsdata <- ts(phillips, start=1948)
'# Estimation of static Phillips curve:
reg.s <- dynlm( inf ~ unem, data=tsdata, end=1996)
'# residuals and AR(1) test:
residual.s <- resid(reg.s)
coeftest( dynlm(residual.s ~ L(residual.s)) )
'# Same with expectations-augmented Phillips curve:
reg.ea <- dynlm( d(inf) ~ unem, data=tsdata, end=1996)
residual.ea <- resid(reg.ea)
coeftest( dynlm(residual.ea ~ L(residual.ea)) )
## Script 12.2: Example-12-4.R
library(dynlm);library(car);library(lmtest)
data(barium, package=’wooldridge’)
tsdata <- ts(barium, start=c(1978,2), frequency=12)
reg <- dynlm(log(chnimp)~log(chempi)+log(gas)+log(rtwex)+
befile6+affile6+afdec6, data=tsdata )
'# Pedestrian test:
residual <- resid(reg)
resreg <- dynlm(residual ~ L(residual)+L(residual,2)+L(residual,3)+
log(chempi)+log(gas)+log(rtwex)+befile6+

12. Scripts Used in Chapter 12
343
affile6+afdec6, data=tsdata )
linearHypothesis(resreg,
c("L(residual)","L(residual, 2)","L(residual, 3)"))
'# Automatic test:
bgtest(reg, order=3, type="F")
## Script 12.3: Example-DWtest.R
library(dynlm);library(lmtest)
data(phillips, package=’wooldridge’)
tsdata <- ts(phillips, start=1948)
'# Estimation of both Phillips curve models:
reg.s <- dynlm( inf ~ unem, data=tsdata, end=1996)
reg.ea <- dynlm( d(inf) ~ unem, data=tsdata, end=1996)
'# DW tests
dwtest(reg.s)
dwtest(reg.ea)
## Script 12.4: Example-12-5.R
library(dynlm);library(car);library(orcutt)
data(barium, package=’wooldridge’)
tsdata <- ts(barium, start=c(1978,2), frequency=12)
'# OLS estimation
olsres <- dynlm(log(chnimp)~log(chempi)+log(gas)+log(rtwex)+
befile6+affile6+afdec6, data=tsdata)
'# Cochrane-Orcutt estimation
cochrane.orcutt(olsres)
## Script 12.5: Example-12-1.R
library(dynlm);library(lmtest);library(sandwich)
data(prminwge, package=’wooldridge’)
tsdata <- ts(prminwge, start=1950)
'# OLS regression
reg<-dynlm(log(prepop)~log(mincov)+log(prgnp)+log(usgnp)+trend(tsdata),
data=tsdata )
'# results with usual SE
coeftest(reg)
'# results with HAC SE
coeftest(reg, vcovHAC)
## Script 12.6: Example-12-9.R
library(dynlm);library(lmtest)
data(nyse, package=’wooldridge’)
tsdata <- ts(nyse)
'# Linear regression of model:
reg <- dynlm(return ~ L(return), data=tsdata)

344
R Scripts
'# squared residual
residual.sq <- resid(reg)^2
'# Model for squared residual:
ARCHreg <- dynlm(residual.sq ~ L(residual.sq))
coeftest(ARCHreg)
## Script 12.7: Example-ARCH.R
library(zoo);library(quantmod);library(dynlm);library(stargazer)
'# Download data using the quantmod package:
getSymbols("AAPL", auto.assign = TRUE)
'# Calculate return as the log difference
ret <- diff( log(AAPL$AAPL.Adjusted) )
'# Subset 2008-2016 by special xts indexing:
ret <- ret["2008/2016"]
'# AR(1) model for returns
ret <- as.zoo(ret)
reg <- dynlm( ret ~ L(ret) )
'# squared residual
residual.sq <- resid(reg)^2
'# Model for squared residual:
ARCHreg <- dynlm(residual.sq ~ L(residual.sq))
summary(ARCHreg)
# 13. Scripts Used in Chapter 13
## Script 13.1: Example-13-2.R
data(cps78_85, package=’wooldridge’)
'# Detailed OLS results including interaction terms
summary( lm(lwage ~ y85*(educ+female)
+exper+ I((exper^2)/100) + union,
data=cps78_85) )
## Script 13.2: Example-13-3-1.R
data(kielmc, package=’wooldridge’)
'# Separate regressions for 1978 and 1981: report coeeficients only
coef( lm(rprice~nearinc, data=kielmc, subset=(year==1978)) )
coef( lm(rprice~nearinc, data=kielmc, subset=(year==1981)) )
'# Joint regression including an interaction term
library(lmtest)
coeftest( lm(rprice~nearinc*y81,
data=kielmc) )
## Script 13.3: Example-13-3-2.R
DiD
<- lm(log(rprice)~nearinc*y81
, data=kielmc)
DiDcontr <- lm(log(rprice)~nearinc*y81+age+I(age^2)+log(intst)+
log(land)+log(area)+rooms+baths, data=kielmc)
library(stargazer)
stargazer(DiD,DiDcontr,type="text")

13. Scripts Used in Chapter 13
345
## Script 13.4: PDataFrame.R
library(plm)
data(crime2, package=’wooldridge’)
'# Define panel data frame
crime2.p <- pdata.frame(crime2, index=46 )
'# Panel dimensions:
pdim(crime2.p)
'# Observation 1-6: new "id" and "time" and some other variables:
crime2.p[1:6,c("id","time","year","pop","crimes","crmrte","unem")]
## Script 13.5: Example-PLM-Calcs.R
library(plm)
data(crime4, package=’wooldridge’)
'# Generate pdata.frame:
crime4.p <- pdata.frame(crime4, index=c("county","year") )
'# Calculations within the pdata.frame:
crime4.p$cr.l <- lag(crime4.p$crmrte)
crime4.p$cr.d <- diff(crime4.p$crmrte)
crime4.p$cr.B <- Between(crime4.p$crmrte)
crime4.p$cr.W <- Within(crime4.p$crmrte)
'# Display selected variables for observations 1-16:
crime4.p[1:16,c("county","year","crmrte","cr.l","cr.d","cr.B","cr.W")]
## Script 13.6: Example-FD.R
library(plm); library(lmtest)
data(crime2, package=’wooldridge’)
crime2.p <- pdata.frame(crime2, index=46 )
'# manually calculate first differences:
crime2.p$dyear
<- diff(crime2.p$year)
crime2.p$dcrmrte <- diff(crime2.p$crmrte)
crime2.p$dunem
<- diff(crime2.p$unem)
'# Display selected variables for observations 1-6:
crime2.p[1:6,c("id","time","year","dyear","crmrte","dcrmrte","unem","dunem")]
'# Estimate FD model with lm on differenced data:
coeftest( lm(dcrmrte~dunem, data=crime2.p) )
'# Estimate FD model with plm on original data:
coeftest( plm(crmrte~unem, data=crime2.p, model="fd") )
## Script 13.7: Example-13-9.R
library(plm);library(lmtest)
data(crime4, package=’wooldridge’)
crime4.p <- pdata.frame(crime4, index=c("county","year") )
pdim(crime4.p)
'# manually calculate first differences of crime rate:

346
R Scripts
crime4.p$dcrmrte <- diff(crime4.p$crmrte)
'# Display selected variables for observations 1-9:
crime4.p[1:9, c("county","year","crmrte","dcrmrte")]
'# Estimate FD model:
coeftest( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+
lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
# 14. Scripts Used in Chapter 14
## Script 14.1: Example-14-2.R
library(plm)
data(wagepan, package=’wooldridge’)
'# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
pdim(wagepan.p)
'# Estimate FE model
summary( plm(lwage~married+union+factor(year)*educ,
data=wagepan.p, model="within") )
## Script 14.2: Example-14-4-1.R
library(plm);library(stargazer)
data(wagepan, package=’wooldridge’)
'# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
pdim(wagepan.p)
'# Check variation of variables within individuals
pvar(wagepan.p)
## Script 14.3: Example-14-4-2.R
'# Estimate different models
wagepan.p$yr<-factor(wagepan.p$year)
reg.ols<- (plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
data=wagepan.p, model="pooling") )
reg.re <- (plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
data=wagepan.p, model="random") )
reg.fe <- (plm(lwage~
I(exper^2)+married+union+yr,
data=wagepan.p, model="within") )
'# Pretty table of selected results (not reporting year dummies)
stargazer(reg.ols,reg.re,reg.fe, type="text",
column.labels=c("OLS","RE","FE"),keep.stat=c("n","rsq"),
keep=c("ed","bl","hi","exp","mar","un"))

14. Scripts Used in Chapter 14
347
## Script 14.4: Example-HausmTest.R
'# Note that the estimates "reg.fe" and "reg.re" are calculated in
'# Example 14.4. The scripts have to be run first.
'# Hausman test of RE vs. FE:
phtest(reg.fe, reg.re)
## Script 14.5: Example-Dummy-CRE-1.R
library(plm);library(stargazer)
data(wagepan, package=’wooldridge’)
'# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
'# Estimate FE parameter in 3 different ways:
wagepan.p$yr<-factor(wagepan.p$year)
reg.fe <-(plm(lwage~married+union+year*educ,data=wagepan.p,
model="within"))
reg.dum<-( lm(lwage~married+union+year*educ+factor(nr),
data=wagepan.p))
reg.re <-(plm(lwage~married+union+year*educ,data=wagepan.p,
model="random"))
reg.cre<-(plm(lwage~married+union+year*educ+Between(married)+Between(union)
,data=wagepan.p, model="random"))
## Script 14.6: Example-Dummy-CRE-2.R
stargazer(reg.fe,reg.dum,reg.cre,reg.re,type="text",model.names=FALSE,
keep=c("married","union",":educ"),keep.stat=c("n","rsq"),
column.labels=c("Within","Dummies","CRE","RE"))
## Script 14.7: Example-CRE-test-RE.R
'# Note that the estimates "reg.cre" are calculated in
# ## Script "Example-Dummy-CRE-1.R" which has to be run first.
'# RE test as an F test on the "Between" coefficients
library(car)
linearHypothesis(reg.cre, matchCoefs(reg.cre,"Between"))
## Script 14.8: Example-CRE2.R
library(plm)
data(wagepan, package=’wooldridge’)
'# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
'# Estimate CRE parameters
wagepan.p$yr<-factor(wagepan.p$year)
summary(plm(lwage~married+union+educ+black+hisp+Between(married)+
Between(union), data=wagepan.p, model="random"))
## Script 14.9: Example-13-9-ClSE.R
library(plm);library(lmtest)
data(crime4, package=’wooldridge’)
'# Generate pdata.frame:
crime4.p <- pdata.frame(crime4, index=c("county","year") )
'# Estimate FD model:
reg <- ( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+

348
R Scripts
lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
'# Regression table with standard SE
coeftest(reg)
'# Regression table with "clustered" SE (default type HC0):
coeftest(reg, vcovHC)
'# Regression table with "clustered" SE (small-sample correction)
'# This is the default version used by Stata and reported by Wooldridge:
coeftest(reg, vcovHC(reg, type="sss"))
# 15. Scripts Used in Chapter 15
## Script 15.1: Example-15-1.R
library(AER);library(stargazer)
data(mroz, package=’wooldridge’)
'# restrict to non-missing wage observations
oursample <- subset(mroz, !is.na(wage))
'# OLS slope parameter manually
with(oursample, cov(log(wage),educ) / var(educ) )
'# IV slope parameter manually
with(oursample, cov(log(wage),fatheduc) / cov(educ,fatheduc) )
'# OLS automatically
reg.ols <-
lm(log(wage) ~ educ, data=oursample)
'# IV automatically
reg.iv <- ivreg(log(wage) ~ educ | fatheduc, data=oursample)
'# Pretty regression table
stargazer(reg.ols,reg.iv, type="text")
## Script 15.2: Example-15-4.R
library(AER);library(stargazer)
data(card, package=’wooldridge’)
'# Checking for relevance: reduced form
redf<-lm(educ ~ nearc4+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
'# OLS
ols<-lm(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
'# IV estimation
iv <-ivreg(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+
reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
| nearc4+exper+I(exper^2)+black+smsa+south+smsa66+
reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
, data=card)
'# Pretty regression table of selected coefficients
stargazer(redf,ols,iv,type="text",
keep=c("ed","near","exp","bl"),keep.stat=c("n","rsq"))

15. Scripts Used in Chapter 15
349
## Script 15.3: Example-15-5.R
library(AER);library(stargazer)
data(mroz, package=’wooldridge’)
'# restrict to non-missing wage observations
oursample <- subset(mroz, !is.na(wage))
'# 1st stage: reduced form
stage1 <- lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
'# 2nd stage
man.2SLS<-lm(log(wage)~fitted(stage1)+exper+I(exper^2), data=oursample)
'# Automatic 2SLS estimation
aut.2SLS<-ivreg(log(wage)~educ+exper+I(exper^2)
| motheduc+fatheduc+exper+I(exper^2) , data=oursample)
'# Pretty regression table
stargazer(stage1,man.2SLS,aut.2SLS,type="text",keep.stat=c("n","rsq"))
## Script 15.4: Example-15-7.R
library(AER);library(lmtest)
data(mroz, package=’wooldridge’)
'# restrict to non-missing wage observations
oursample <- subset(mroz, !is.na(wage))
'# 1st stage: reduced form
stage1<-lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
'# 2nd stage
stage2<-lm(log(wage)~educ+exper+I(exper^2)+resid(stage1),data=oursample)
'# results including t tests
coeftest(stage2)
## Script 15.5: Example-15-8.R
library(AER)
data(mroz, package=’wooldridge’)
'# restrict to non-missing wage observations
oursample <- subset(mroz, !is.na(wage))
'# IV regression
summary( res.2sls <- ivreg(log(wage) ~ educ+exper+I(exper^2)
| exper+I(exper^2)+motheduc+fatheduc,data=oursample) )
'# Auxiliary regression
res.aux <-
lm(resid(res.2sls) ~ exper+I(exper^2)+motheduc+fatheduc
, data=oursample)
'# Calculations for test
( r2 <- summary(res.aux)$r.squared )
( n <- nobs(res.aux) )
( teststat <- n*r2
)
( pval <- 1-pchisq(teststat,1) )

eq.hrs  <- hours  ~ log(wage)+educ+age+kidslt6+nwifeinc eq.wage <- log(wage)~ hours  
+educ+exper+I(exper^2) eq.system<- list(eq.hrs, eq.wage)
instrum <- ~educ+age+kidslt6+nwifeinc+exper+I(exper^2)
350
R Scripts
## Script 15.6: Example-15-10.R
library(plm)
data(jtrain, package=’wooldridge’)
'# Define panel data (for 1987 and 1988 only)
jtrain.87.88 <- subset(jtrain,year<=1988)
jtrain.p<-pdata.frame(jtrain.87.88, index=c("fcode","year"))
'# IV FD regression
summary( plm(log(scrap)~hrsemp|grant, model="fd",data=jtrain.p) )
# 16. Scripts Used in Chapter 16
## Script 16.1: Example-16-5-ivreg.R
library(AER)
data(mroz, package=’wooldridge’)
oursample <- subset(mroz,!is.na(wage))
'# 2SLS regressions
summary( ivreg(hours~log(wage)+educ+age+kidslt6+nwifeinc
|educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
summary( ivreg(log(wage)~hours+educ+exper+I(exper^2)
|educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
## Script 16.2: Example-16-5-systemfit-prep.R
library(systemfit)
data(mroz, package=’wooldridge’)
oursample <- subset(mroz,!is.na(wage))
'# Define system of equations and instruments
## Script 16.3: Example-16-5-systemfit.R
'# 2SLS of whole system (run Example-16-5-systemfit-prep.R first!)
summary(systemfit(eq.system,inst=instrum,data=oursample,method="2SLS"))
## Script 16.4: Example-16-5-3sls.R
'# 3SLS of whole system (run Example-16-5-systemfit-prep.R first!)
summary(systemfit(eq.system,inst=instrum,data=oursample,method="3SLS"))
# 17. Scripts Used in Chapter 17
## Script 17.1: Example-17-1-1.R
library(car); library(lmtest)
'# for robust SE
data(mroz, package=’wooldridge’)
'# Estimate linear probability model
linprob <- lm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,data=mroz)
'# Regression table with heteroscedasticity-robust SE and t tests:
coeftest(linprob,vcov=hccm)

17. Scripts Used in Chapter 17
351
## Script 17.2: Example-17-1-2.R
'# predictions for two "extreme" women (run Example-17-1-1.R first!):
xpred <- list(nwifeinc=c(100,0),educ=c(5,17),exper=c(0,30),
age=c(20,52),kidslt6=c(2,0),kidsge6=c(0,0))
predict(linprob,xpred)
## Script 17.3: Example-17-1-3.R
data(mroz, package=’wooldridge’)
'# Estimate logit model
logitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
family=binomial(link=logit),data=mroz)
'# Summary of results:
summary(logitres)
'# Log likelihood value:
logLik(logitres)
'# McFadden’s pseudo R2:
1 - logitres$deviance/logitres$null.deviance
## Script 17.4: Example-17-1-4.R
data(mroz, package=’wooldridge’)
'# Estimate probit model
probitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
family=binomial(link=probit),data=mroz)
'# Summary of results:
summary(probitres)
'# Log likelihood value:
logLik(probitres)
'# McFadden’s pseudo R2:
1 - probitres$deviance/probitres$null.deviance
## Script 17.5: Example-17-1-5.R
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# Test of overall significance:
'# Manual calculation of the LR test statistic:
probitres$null.deviance - probitres$deviance
'# Automatic calculations including p-values,...:
library(lmtest)
lrtest(probitres)
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# Test of H0: experience and age are irrelevant
restr <- glm(inlf~nwifeinc+educ+ kidslt6+kidsge6,
family=binomial(link=probit),data=mroz)
lrtest(restr,probitres)
## Script 17.6: Example-17-1-6.R
'# Predictions from linear probability, probit and logit model:
'# (run 17-1-1.R through 17-1-4.R first to define the variables!)
predict(linprob,
xpred,type = "response")
predict(logitres, xpred,type = "response")
predict(probitres,xpred,type = "response")

352
R Scripts
## Script 17.7: Binary-Predictions.R
'# Simulated data
set.seed(8237445)
y <- rbinom(100,1,0.5)
x <- rnorm(100) + 2*y
'# Estimation
linpr.res <-
lm(y~x)
logit.res <- glm(y~x,family=binomial(link=logit))
probit.res<- glm(y~x,family=binomial(link=probit))
'# Prediction for regular grid of x values
xp <- seq(from=min(x),to=max(x),length=50)
linpr.p <- predict( linpr.res, list(x=xp), type="response" )
logit.p <- predict( logit.res, list(x=xp), type="response" )
probit.p<- predict( probit.res,list(x=xp), type="response" )
'# Graph
plot(x,y)
lines(xp,linpr.p, lwd=2,lty=1)
lines(xp,logit.p, lwd=2,lty=2)
lines(xp,probit.p,lwd=1,lty=1)
legend("topleft",c("linear prob.","logit","probit"),
lwd=c(2,2,1),lty=c(1,2,1))
## Script 17.8: Binary-Margeff.R
'# Calculate partial effects
linpr.eff <- coef(linpr.res)["x"]
*
rep(1,100)
logit.eff <- coef(logit.res)["x"]
*
dlogis(predict(logit.res))
probit.eff <- coef(probit.res)["x"]
*
dnorm(predict(probit.res))
'# Graph
plot(
x,linpr.eff, pch=1,ylim=c(0,.7),ylab="partial effect")
points(x,logit.eff, pch=3)
points(x,probit.eff,pch=18)
legend("topright",c("linear prob.","logit","probit"),pch=c(1,3,18))
## Script 17.9: Example-17-1-7.R
'# APEs (run 17-1-1.R through 17-1-4.R first to define the variables!)
'# Calculation of linear index at individual values:
xb.log <- predict(logitres)
xb.prob<- predict(probitres)
'# APE factors = average(g(xb))
factor.log <- mean( dlogis(xb.log) )
factor.prob<- mean( dnorm(xb.prob) )
cbind(factor.log,factor.prob)
'# average partial effects = beta*factor:
APE.lin <- coef(linprob)
*
1
APE.log <- coef(logitres)
*
factor.log
APE.prob<- coef(probitres)
*
factor.prob
'# Table of APEs
cbind(APE.lin, APE.log, APE.prob)

lines(x,Ey  , lty=1,lwd=2)
abline(h=0,lty=3)   '# horizontal line at 0
x    <- sort(rnorm(100)+4)
xb   <- -4 + 1*x
ystar  <- xb + rnorm(100)
y    <- ystar
17. Scripts Used in Chapter 17
353
## Script 17.10: Example-17-1-8.R
'# Automatic APE calculations with package mfx
library(mfx)
logitmfx(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
data=mroz, atmean=FALSE)
## Script 17.11: Example-17-3-1.R
data(crime1, package=’wooldridge’)
'# Estimate linear model
lm.res
<-
lm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1)
'# Estimate Poisson model
Poisson.res <- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1, family=poisson)
'# Quasi-Poisson model
QPoisson.res<- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1, family=quasipoisson)
## Script 17.12: Example-17-3-2.R
'# Example 17.3: Regression table (run Example-17-3-1.R first!)
library(stargazer) '# package for regression output
stargazer(lm.res,Poisson.res,QPoisson.res,type="text",keep.stat="n")
## Script 17.13: Tobit-CondMean.R
'# Simulated data
set.seed(93876553)
y[ystar<0]<- 0
'# Conditional means
Eystar <- xb
Ey <- pnorm(xb/1)*xb+1*dnorm(xb/1)
'# Graph
plot(x,ystar,ylab="y", pch=3)
points(x,y, pch=1)
lines(x,Eystar, lty=2,lwd=2)
legend("topleft",c(expression(y^"*"),"y",expression(E(y^"*")),"E(y)"),
lty=c(NA,NA,2,1),pch=c(3,1,NA,NA),lwd=c(1,1,2,2))
## Script 17.14: Example-17-2.R
data(mroz, package=’wooldridge’)
'# Estimate Tobit model using censReg:
library(censReg)
TobitRes <- censReg(hours~nwifeinc+educ+exper+I(exper^2)+
age+kidslt6+kidsge6, data=mroz )
summary(TobitRes)
'# Partial Effects at the average x:
margEff(TobitRes)

pred.OLS  <- predict(   lm(y~x, data=sample) ) pred.trunc <- predict( truncreg(y~x, data=sample) )
'# Graph
plot(  compl$x, compl$y, pch= 1,xlab="x",ylab="y") points(sample$x,sample$y, pch=16)
lines( sample$x,pred.OLS, lty=2,lwd=2) lines( sample$x,pred.trunc,lty=1,lwd=2)
abline(h=0,lty=3)   '# horizontal line at 0
354
R Scripts
## Script 17.15: Example-17-2-survreg.R
'# Estimate Tobit model using survreg:
library(survival)
res <- survreg(Surv(hours, hours>0, type="left") ~ nwifeinc+educ+exper+
I(exper^2)+age+kidslt6+kidsge6, data=mroz, dist="gaussian")
summary(res)
## Script 17.16: Example-17-4.R
library(survival)
data(recid, package=’wooldridge’)
'# Define Dummy for UNcensored observations
recid$ uncensored <- recid$ cens== 0
'# Estimate censored regression model:
res<-survreg(Surv(log(durat),uncensored, type="right") ~ workprg+priors+
tserved+felon+alcohol+drugs+black+married+educ+age,
data=recid, dist="gaussian")
'# Output:
summary(res)
## Script 17.17: TruncReg-Simulation.R
library(truncreg)
'# Simulated data
set.seed(93876553)
x
<- sort(rnorm(100)+4)
y
<- -4 + 1*x
+ rnorm(100)
'# complete observations and observed sample:
compl <- data.frame(x,y)
sample <- subset(compl, y>0)
'# Predictions
legend("topleft", c("all points","observed points","OLS fit",
"truncated regression"),
lty=c(NA,NA,2,1),pch=c(1,16,NA,NA),lwd=c(1,1,2,2))
## Script 17.18: Example-17-5.R
library(sampleSelection)
data(mroz, package=’wooldridge’)
'# Estimate Heckman selection model (2 step version)
res<-selection(inlf~educ+exper+I(exper^2)+nwifeinc+age+kidslt6+kidsge6,
log(wage)~educ+exper+I(exper^2), data=mroz, method="2step" )
'# Summary of results:
summary(res)

# 18. Scripts Used in Chapter 18
355
19. Scripts Used in Chapter 18
## Script 18.1: Example-18-1.R
library(dynlm); library(stargazer)
data(hseinv, package=’wooldridge’)
'# detrended variable: residual from a regression on the obs. index:
trendreg <- dynlm( log(invpc) ~ trend(hseinv), data=hseinv )
hseinv$linv.detr <-
resid( trendreg )
'# ts data:
hseinv.ts <- ts(hseinv)
'# Koyck geometric d.l.:
gDL<-dynlm(linv.detr~gprice + L(linv.detr)
,data=hseinv.ts)
'# rational d.l.:
rDL<-dynlm(linv.detr~gprice + L(linv.detr) + L(gprice),data=hseinv.ts)
stargazer(gDL,rDL, type="text", keep.stat=c("n","adj.rsq"))
'# LRP geometric DL:
b <- coef(gDL)
b["gprice"]
/ (1-b["L(linv.detr)"])
'# LRP rationalDL:
b <- coef(rDL)
(b["gprice"]+b["L(gprice)"]) / (1-b["L(linv.detr)"])
## Script 18.2: Example-18-4.R
library(dynlm)
data(inven, package=’wooldridge’)
'# variable to test: y=log(gdp)
inven$y <- log(inven$gdp)
inven.ts<- ts(inven)
'# summary output of ADF regression:
summary(dynlm( d(y) ~ L(y) + L(d(y)) + trend(inven.ts), data=inven.ts))
'# automated ADF test using tseries:
library(tseries)
adf.test(inven$y, k=1)
## Script 18.3: Example-18-4-urca.R
library(urca)
data(inven, package=’wooldridge’)
'# automated ADF test using urca:
summary( ur.df(log(inven$gdp) , type = c("trend"), lags = 1) )
## Script 18.4: Simulate-Spurious-Regression-1.R
'# Initialize Random Number Generator
set.seed(29846)
'# i.i.d. N(0,1) innovations
n <- 50
e <- rnorm(n)
a <- rnorm(n)
'# independent random walks

356
R Scripts
x <- cumsum(a)
y <- cumsum(e)
'# plot
plot(x,type="l",lty=1,lwd=1)
lines(y
,lty=2,lwd=2)
legend("topright",c("x","y"), lty=c(1,2), lwd=c(1,2))
'# Regression of y on x
summary( lm(y~x) )
## Script 18.5: Simulate-Spurious-Regression-2.R
'# Initialize Random Number Generator
set.seed(29846)
'# generate 10,000 independent random walks
'# and store the p val of the t test
pvals <- numeric(10000)
for (r in 1:10000) {
'# i.i.d. N(0,1) innovations
n <- 50
a <- rnorm(n)
e <- rnorm(n)
'# independent random walks
x <- cumsum(a)
y <- cumsum(e)
'# regression summary
regsum <- summary(lm(y~x))
'# p value: 2nd row, 4th column of regression table
pvals[r] <- regsum$coef[2,4]
}
'# How often is p<5% ?
table(pvals<=0.05)
## Script 18.6: Example-18-8.R
'# load updataed data from URfIE Website since online file is incomplete
library(dynlm); library(stargazer)
data(phillips, package=’wooldridge’)
tsdat=ts(phillips, start=1948)
'# Estimate models and display results
res1 <- dynlm(unem ~ unem_1
, data=tsdat, end=1996)
res2 <- dynlm(unem ~ unem_1+inf_1, data=tsdat, end=1996)
stargazer(res1, res2 ,type="text", keep.stat=c("n","adj.rsq","ser"))
'# Predictions for 1997-2003 including 95% forecast intervals:
predict(res1, newdata=window(tsdat,start=1997), interval="prediction")
predict(res2, newdata=window(tsdat,start=1997), interval="prediction")
## Script 18.7: Example-18-9.R
'# Note: run Example-18-8.R first to generate the results res1 and res2
'# Actual unemployment and forecasts:
y
<- window(tsdat,start=1997)[,"unem"]
f1 <- predict( res1, newdata=window(tsdat,start=1997) )

source("data.R"    ,echo=TRUE,max=1000) '# Data import and cleaning 
source("descriptives.R",echo=TRUE,max=1000) '# Descriptive statistics source("estimation.R" 
,echo=TRUE,max=1000) '# Estimation of model source("results.R"   ,echo=TRUE,max=1000) '# Tables and 
Figures
# 19. Scripts Used in Chapter 19
357
f2 <- predict( res2, newdata=window(tsdat,start=1997) )
'# Plot unemployment and forecasts:
matplot(time(y), cbind(y,f1,f2), type="l",
col="black",lwd=2,lty=1:3)
legend("topleft",c("Unempl.","Forecast 1","Forecast 2"),lwd=2,lty=1:3)
'# Forecast errors:
e1<- y - f1
e2<- y - f2
'# RMSE:
sqrt(mean(e1^2))
sqrt(mean(e2^2))
'# MAE:
mean(abs(e1))
mean(abs(e2))
19. Scripts Used in Chapter 19
## Script 19.1: ultimate-calcs.R
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# Project X:
'# "The Ultimate Question of Life, the Universe, and Everything"
'# Project Collaborators: Mr. X, Mrs. Y
'#
'# R ## Script "ultimate-calcs"
'# by: F Heiss
'# Date of this version: February 08, 2016
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# The main calculation using the method "square root"
'# (http://mathworld.wolfram.com/SquareRoot.html)
sqrt(1764)
## Script 19.2: projecty-master.R
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# Bachelor Thesis Mr. Z
'# "Best Practice in Using R Scripts"
'#
'# R ## Script "master"
'# Date of this version: 2020-08-13
'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#
'# Some preparations:
setwd(~/bscthesis/r)
rm(list = ls())
'# Call R scripts

res1 <- lm(colGPA ~ hsGPA   , data=gpa1) res2 <- lm(colGPA ~    ACT, data=gpa1)
358
R Scripts
## Script 19.3: LaTeXwithR.R
library(stargazer);library(xtable)
data(gpa1, package=’wooldridge’)
'# Number of obs.
sink("numb-n.txt"); cat(nrow(gpa1)); sink()
'# generate frequency table in file "tab-gender.txt"
gender <- factor(gpa1$male,labels=c("female","male"))
sink("tab-gender.txt")
xtable( table(gender) )
sink()
'# calculate OLS results
res3 <- lm(colGPA ~ hsGPA + ACT, data=gpa1)
'# write regression table to file "tab-regr.txt"
sink("tab-regr.txt")
stargazer(res1,res2,res3, keep.stat=c("n","rsq"),
type="latex",title="Regression Results",label="t:reg")
sink()
'# b1 hat
sink("numb-b1.txt"); cat(round(coef(res1)[2],3)); sink()
'# Generate graph as PDF file
pdf(file = "regr-graph.pdf", width = 3, height = 2)
par(mar=c(2,2,1,1))
plot(gpa1$hsGPA, gpa1$colGPA)
abline(res1)
dev.off()
