R Scripts
# 1. Scripts Used in Chapter 01
## Script 1.1: R-as-a-Calculator.R
1+1
5*(4-1)^2
sqrt( log(10) )
## Script 1.2: Install-Packages.R
<span style="color: #1E90FF;">'&#35; This R Script downloads and installs all packages used at some point.</span>
<span style="color: #1E90FF;">'&#35; It needs to be run once for each computer/user only</span>
install.packages( c("AER", "car", "censReg", "dplyr", "dummies", "dynlm",
"effects", "ggplot2", "lmtest", "maps", "mfx", "orcutt", "plm",
"quantmod", "sandwich", "quantreg", "rio", "rmarkdown", "sampleSelection",
"stargazer", "survival", "systemfit", "truncreg", "tseries", "urca",
"xtable", "vars", "WDI", "wooldridge", "xts", "zoo") )
## Script 1.3: Objects.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">generate object x (no output):</font></span>
x <- 5
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">display x & x^2:</font></span>
x
x^2
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">generate objects y&z with immediate display using ():</font></span>
(y <- 3)
(z <- y^x)
## Script 1.4: Vectors.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Define a with immediate output through parantheses:</font></span>
(a <- c(1,2,3,4,5,6))
(b <- a+1)
(c <- a+b)
(d <- b*c)
sqrt(d)
## Script 1.5: Vector-Functions.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Define vector</font></span>
(a <- c(7,2,6,9,4,1,3))
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Basic functions:</font></span>
sort(a)
length(a)
min(a)
max(a)
sum(a)
prod(a)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Creating special vectors:</font></span>
numeric(20)
rep(1,20)
seq(50)
5:15
seq(4,20,2)
## Script 1.6: Logical.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Basic comparisons:</font></span>
0 ==  1
0 < 1
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Logical vectors:</font></span>
( a <- c(7,2,6,9,4,1,3) )
( b <- a<3 | a>=6 )
## Script 1.7: Factors.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Original ratings:</font></span>
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
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Generating matrix A from one vector with all values:</font></span>
v <- c(2,-4,-1,5,7,0)
( A <- matrix(v,nrow=2) )
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Generating matrix A from two vectors corresponding to rows:</font></span>
row1 <- c(2,-1,7); row2 <- c(-4,5,0)
( A <- rbind(row1, row2) )
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Generating matrix A from three vectors corresponding to columns:</font></span>
col1 <- c(2,-4); col2 <- c(-1,5); col3 <- c(7,0)
( A <- cbind(col1, col2, col3) )
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Giving names to rows and columns:</font></span>
colnames(A) <- c("Alpha","Beta","Gamma")
rownames(A) <- c("Aleph","Bet")
A
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Diaginal and identity matrices:</font></span>
diag( c(4,2,6) )
diag( 3 )
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Indexing for extracting elements (still using A from above):</font></span>
A[2,1]
A[,2]
A[,c(1,3)]
## Script 1.10: Matrix-Operators.R
A <- matrix( c(2,-4,-1,5,7,0), nrow=2)
B <- matrix( c(2,1,0,3,-1,5), nrow=2)
A B A
*B
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Transpose:</font></span>
(C <- t(B) )
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Matrix multiplication:</font></span>
(D <- A %*%
C )
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Inverse:</font></span>
solve(D)
## Script 1.11: Lists.R
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Generate a list object:</font></span>
mylist <- list( A=seq(8,36,4), this="that", idm = diag(3))
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Print whole list:</font></span>
mylist
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Vector of names:</font></span>
names(mylist)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Print component "A":</font></span>
mylist$A
## Script 1.12: Data-frames.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Define one x vector for all:</font></span>
year<- c(2008,2009,2010,2011,2012,2013)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Define a matrix of y values:</font></span>
product1<-c(0,3,6,9,7,8); product2<-c(1,2,3,5,9,6); product3<-c(2,4,4,2,3,2)
sales_mat <- cbind(product1,product2,product3)
rownames(sales_mat) <- year
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">The matrix looks like this:</font></span>
sales_mat
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Create a data frame and display it:</font></span>
sales <- as.data.frame(sales_mat)
sales
## Script 1.13: Data-frames-vars.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Accessing a single variable:</font></span>
sales$product2
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Generating a new variable in the data frame:</font></span>
sales $ totalv1 <- sales$ product1 + sales$ product2 + sales$ product3
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">The same but using "with":</font></span>
sales$totalv2 <- with(sales, product1+product2+product3)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">The same but using "attach":</font></span>
attach(sales)
sales$totalv3 <- product1+product2+product3
detach(sales)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Result:</font></span>
sales
## Script 1.14: Data-frames-subsets.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Full data frame (from Data-frames.R, has to be run first)</font></span>
sales
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Subset: all years in which sales of product 3 were >=3</font></span>
subset(sales, product3>=3)
## Script 1.15: RData-Example.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Note: "sales" is defined in Data-frames.R, so it has to be run first!</font></span>
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">save data frame as RData file (in the current working directory)</font></span>
save(sales, file = "oursalesdata.RData")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">remove data frame "sales" from memory</font></span>
rm(sales)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Does variable "sales" exist?</font></span>
exists("sales")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Load data set (in the current working directory):</font></span>
load("oursalesdata.RData")
<span style="color: #1E90FF;">'&#35;<font color="#00b0f0"> Does variable "sales" exist?</font></span>
exists("sales")
sales
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">averages of the variables:</font></span>
colMeans(sales)
## Script 1.16: Example-Data.R
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">The data set is stored on the local computer in ~/Documents/R/data/wooldridge/affairs.dta</font></span>
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Version 1: from package. make sure to install.packages(wooldridge)</font></span>
data(affairs, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Version 2: Adjust path</font></span>
affairs2 <- rio::import("~/Documents/R/data/wooldridge/affairs.dta")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Version 3: Change working directory</font></span>
setwd("~/Documents/R/data/wooldridge/")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">import </font></span>
affairs3 <- rio::import("affairs.dta")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Version 4: directly load from internet</font></span>
affairs4 <- rio::import("http://fmwww.bc.edu/ec-p/data/wooldridge/affairs.dta")
<span style="color: #1E90FF;">'&#35; <font color="#00b0f0">Compare, e.g. avg. value of naffairs:</font></span>
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
<span style="color: #1E90FF;">'&#35; Define one x vector for all:</span>
year
<- c(2008,2009,2010,2011,2012,2013)
<span style="color: #1E90FF;">'&#35; Define a matrix of y values:</span>
product1 <- c(0,3,6,9,7,8)
product2 <- c(1,2,3,5,9,6)
product3 <- c(2,4,4,2,3,2)
sales <- cbind(product1,product2,product3)
<span style="color: #1E90FF;">'&#35; plot</span>
matplot(year,sales, type="b", lwd=c(1,2,3), col="black" )
## Script 1.19: Plot-Legend.R
curve( dnorm(x,0,1), -10, 10, lwd=1, lty=1)
curve( dnorm(x,0,2),add=TRUE, lwd=2, lty=2)
curve( dnorm(x,0,3),add=TRUE, lwd=3, lty=3)
<span style="color: #1E90FF;">'&#35; Add the legend</span>
legend("topright",c("sigma=1","sigma=2","sigma=3"), lwd=1:3, lty=1:3)
## Script 1.20: Plot-Legend2.R
curve( dnorm(x,0,1), -10, 10, lwd=1, lty=1)
curve( dnorm(x,0,2),add=TRUE, lwd=2, lty=2)
curve( dnorm(x,0,3),add=TRUE, lwd=3, lty=3)
<span style="color: #1E90FF;">'&#35; Add the legend with greek sigma</span>
legend("topleft",expression(sigma==  1,sigma==  2,sigma==  3),lwd=1:3,lty=1:3)
<span style="color: #1E90FF;">'&#35; Add the text with the formula, centered at x=6 and y=0.3</span>
text(6,.3,
expression(f(x)== frac(1,sqrt(2*pi)*sigma)*e^{-frac(x^2,2*sigma^2)}))
## Script 1.21: mpg-data.R
<span style="color: #1E90FF;">'&#35; load package</span>
library(ggplot2)
<span style="color: #1E90FF;">'&#35; First rows of data of data set mpg:</span>
head(mpg)

310
R Scripts
## Script 1.22: mpg-scatter.R
<span style="color: #1E90FF;">'&#35; load package</span>
library(ggplot2)
<span style="color: #1E90FF;">'&#35; Generate ggplot2 graph:</span>
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
<span style="color: #1E90FF;">'&#35; packages: WDI for raw data, dplyr for manipulation</span>
library(WDI);
wdi_raw <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014)
head(wdi_raw)
tail(wdi_raw)
## Script 1.30: wdi-manipulation.R
library(dplyr)
<span style="color: #1E90FF;">'&#35; filter: only US data</span>
ourdata <- filter(wdi_raw, iso2c== "US")
<span style="color: #1E90FF;">'&#35; rename lifeexpectancy variable</span>
ourdata <- rename(ourdata, LE_fem=SP.DYN.LE00.FE.IN)
<span style="color: #1E90FF;">'&#35; select relevant variables</span>
ourdata <- select(ourdata, year, LE_fem)
<span style="color: #1E90FF;">'&#35; order by year (increasing)</span>
ourdata <- arrange(ourdata, year)
<span style="color: #1E90FF;">'&#35; Head and tail of data</span>
head(ourdata)
tail(ourdata)
<span style="color: #1E90FF;">'&#35; Graph</span>
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
<span style="color: #1E90FF;">'&#35; All manipulations with pipes:</span>
ourdata <- wdi_raw %>%
filter(iso2c== "US") %>%
rename(LE_fem=SP.DYN.LE00.FE.IN) %>%
select(year, LE_fem) %>%
arrange(year)
## Script 1.32: wdi-ctryinfo.R
library(WDI); library(dplyr)
<span style="color: #1E90FF;">'&#35; Download raw life expectency data</span>
le_data <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014) %>%
rename(LE = SP.DYN.LE00.FE.IN)
tail(le_data)
<span style="color: #1E90FF;">'&#35; Country-data on income classification</span>
ctryinfo <- as.data.frame(WDI_data$country, stringsAsFactors = FALSE) %>%
select(country, income)

filter(income != "Aggregates") %>%     '# remove rows for aggregates filter(income != "Not 
classified") %>%   '# remove unclassified ctries group_by(income, year) %>%         '# group by 
income classification summarize(LE_avg = mean(LE, na.rm=TRUE)) %>% '# average by group
ungroup()                '# remove grouping
<span style="color: #1E90FF;">'&#35; First 6 rows: tail(avgdata)</span>
<span style="color: #1E90FF;">'&#35; plot</span>
geom_line(size=1) +             '# thicker lines
scale_color_grey() +             '# gray scale scale_x_continuous(breaks=seq(1960,2015,10)) +  '# 
adjust x axis breaks
theme_light() +               '# light theme (white background,...) labs(title="Life expectancy of 
women",
subtitle="Average by country classification", x="Year", y="Life expectancy [Years]",
312
R Scripts
tail(ctryinfo)
<span style="color: #1E90FF;">'&#35; Join:</span>
alldata <- left_join(le_data, ctryinfo)
tail(alldata)
## Script 1.33: wdi-ctryavg.R
<span style="color: #1E90FF;">'&#35; Note: run wdi-ctryinfo.R first to define "alldata"!</span>
<span style="color: #1E90FF;">'&#35; Summarize by country and year</span>
avgdata <- alldata %>%
ggplot(avgdata, aes(year, LE_avg, color=income)) +
geom_line() +
scale_color_grey()
## Script 1.34: wdi-ctryavg-beautify.R
<span style="color: #1E90FF;">'&#35; Note: run wdi-ctryavg.R first to define "avgdata"!</span>
<span style="color: #1E90FF;">'&#35; Order the levels meaningfully</span>
avgdata$income <- factor( avgdata$income,
levels = c("High income",
"Upper middle income",
"Lower middle income",
"Low income") )
<span style="color: #1E90FF;">'&#35; Plot</span>
ggplot(avgdata, aes(year, LE_avg, color=income)) +
color="Income level",
caption="Source: World Bank, WDI")
## Script 1.35: Descr-Tables.R
<span style="color: #1E90FF;">'&#35; load data set</span>
data(affairs, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate "Factors" to attach labels</span>
haskids <- factor(affairs$kids,labels=c("no","yes"))
mlab <- c("very unhappy","unhappy","average","happy", "very happy")
marriage <- factor(affairs$ratemarr, labels=mlab)

1. Scripts Used in Chapter 01
313
<span style="color: #1E90FF;">'&#35; Frequencies for having kids:</span>
table(haskids)
<span style="color: #1E90FF;">'&#35; Marriage ratings (share):</span>
prop.table(table(marriage))
<span style="color: #1E90FF;">'&#35; Contigency table: counts (display & store in var.)</span>
(countstab <- table(marriage,haskids))
<span style="color: #1E90FF;">'&#35; Share within "marriage" (i.e. within a row):</span>
prop.table(countstab, margin=1)
<span style="color: #1E90FF;">'&#35; Share within "haskids"</span>
(i.e. within a column):
prop.table(countstab, margin=2)
## Script 1.36: Histogram.R
<span style="color: #1E90FF;">'&#35; Load data</span>
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Extract ROE to single vector</span>
ROE <- ceosal1$roe
<span style="color: #1E90FF;">'&#35; Subfigure (a): histogram (counts)</span>
hist(ROE)
<span style="color: #1E90FF;">'&#35; Subfigure (b): histogram (densities, explicit breaks)</span>
hist(ROE, breaks=c(0,5,10,20,30,60) )
## Script 1.37: KDensity.R
<span style="color: #1E90FF;">'&#35; Subfigure (c): kernel density estimate</span>
plot( density(ROE) )
<span style="color: #1E90FF;">'&#35; Subfigure (d): overlay</span>
hist(ROE, freq=FALSE, ylim=c(0,.07))
lines( density(ROE), lwd=3 )
## Script 1.38: Descr-Stats.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; sample average:</span>
mean(ceosal1$salary)
<span style="color: #1E90FF;">'&#35; sample median:</span>
median(ceosal1$salary)
<span style="color: #1E90FF;">'&#35;standard deviation:</span>
sd(ceosal1$salary)
<span style="color: #1E90FF;">'&#35; summary information:</span>
summary(ceosal1$salary)
<span style="color: #1E90FF;">'&#35; correlation with ROE:</span>
cor(ceosal1$salary, ceosal1$roe)
## Script 1.39: PMF-example.R
<span style="color: #1E90FF;">'&#35; Values for x: all between 0 and 10</span>
x <- seq(0,10)
<span style="color: #1E90FF;">'&#35; pmf for all these values</span>

314
R Scripts
fx <- dbinom(x, 10, 0.2)
<span style="color: #1E90FF;">'&#35; Table(matrix) of values:</span>
cbind(x, fx)
<span style="color: #1E90FF;">'&#35; Plot</span>
plot(x, fx, type="h")
## Script 1.40: Random-Numbers.R
<span style="color: #1E90FF;">'&#35; Sample from a standard normal RV with sample size n=5:</span>
rnorm(5)
<span style="color: #1E90FF;">'&#35; A different sample from the same distribution:</span>
rnorm(5)
<span style="color: #1E90FF;">'&#35; Set the seed of the random number generator and take two samples:</span>
set.seed(6254137)
rnorm(5)
rnorm(5)
<span style="color: #1E90FF;">'&#35; Reset the seed to the same value to get the same samples again:</span>
set.seed(6254137)
rnorm(5)
rnorm(5)
## Script 1.41: Example-C-2.R
<span style="color: #1E90FF;">'&#35; Manually enter raw data from Wooldridge, Table C.3:</span>
SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,
5.03,8,9,18,.28,7,3.97)
SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,
4,7,19,.2,5,3.83)
<span style="color: #1E90FF;">'&#35; Calculate Change (the parentheses just display the results):</span>
(Change <- SR88 - SR87)
<span style="color: #1E90FF;">'&#35; Ingredients to CI formula</span>
(avgCh<- mean(Change))
(n
<- length(Change))
(sdCh <- sd(Change))
(se
<- sdCh/sqrt(n))
(c
<- qt(.975, n-1))
<span style="color: #1E90FF;">'&#35; Confidence interval:</span>
c( avgCh - c*se, avgCh + c*se
)
## Script 1.42: Example-C-3.R
data(audit, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Ingredients to CI formula</span>
(avgy<- mean(audit$y))
(n
<- length(audit$y))
(sdy <- sd(audit$y))
(se
<- sdy/sqrt(n))
(c
<- qnorm(.975))
<span style="color: #1E90FF;">'&#35; 95% Confidence interval:</span>
avgy + c
*
c(-se,+se)
<span style="color: #1E90FF;">'&#35; 99% Confidence interval:</span>
avgy + qnorm(.995)
*
c(-se,+se)

1. Scripts Used in Chapter 01
315
## Script 1.43: Critical-Values-t.R
<span style="color: #1E90FF;">'&#35; degrees of freedom = n-1:</span>
df <- 19
<span style="color: #1E90FF;">'&#35; significance levels:</span>
alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
alpha.two.tailed = alpha.one.tailed
*
2
<span style="color: #1E90FF;">'&#35; critical values & table:</span>
CV <- qt(1 - alpha.one.tailed, df)
cbind(alpha.one.tailed, alpha.two.tailed, CV)
## Script 1.44: Example-C-5.R
<span style="color: #1E90FF;">'&#35; Note: we reuse variables from Example-C-3.R. It has to be run first!</span>
<span style="color: #1E90FF;">'&#35; t statistic for H0: mu=0:</span>
(t <- avgy/se)
<span style="color: #1E90FF;">'&#35; Critical values for t distribution with n-1=240 d.f.:</span>
alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
CV <- qt(1 - alpha.one.tailed, n-1)
cbind(alpha.one.tailed, CV)
## Script 1.45: Example-C-6.R
<span style="color: #1E90FF;">'&#35; Note: we reuse variables from Example-C-2.R. It has to be run first!</span>
<span style="color: #1E90FF;">'&#35; t statistic for H0: mu=0:</span>
(t <- avgCh/se)
<span style="color: #1E90FF;">'&#35; p value</span>
(p <- pt(t,n-1))
## Script 1.46: Example-C-7.R
<span style="color: #1E90FF;">'&#35; t statistic for H0: mu=0:</span>
t <-
-4.276816
<span style="color: #1E90FF;">'&#35; p value</span>
(p <- pt(t,240))
## Script 1.47: Examples-C2-C6.R
<span style="color: #1E90FF;">'&#35; data for the scrap rates examples:</span>
SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,5.03,8,9,18,.28,
7,3.97)
SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,4,7,19,.2,5,3.83)
Change <- SR88 - SR87
<span style="color: #1E90FF;">'&#35; Example C.2: two-sided CI</span>
t.test(Change)
<span style="color: #1E90FF;">'&#35; Example C.6: 1-sided test:</span>
t.test(Change, alternative="less")
## Script 1.48: Examples-C3-C5-C7.R
data(audit, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Example C.3: two-sided CI</span>
t.test(audit$y)
<span style="color: #1E90FF;">'&#35; Examples C.5 & C.7: 1-sided test:</span>
t.test(audit$y, alternative="less")

316
R Scripts
## Script 1.49: Test-Results-List.R
data(audit, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; store test results as a list "testres"</span>
testres <- t.test(audit$y)
<span style="color: #1E90FF;">'&#35; print results:</span>
testres
<span style="color: #1E90FF;">'&#35; component names: which results can be accessed?</span>
names(testres)
<span style="color: #1E90FF;">'&#35; p-value</span>
testres$p.value
## Script 1.50: Simulate-Estimate.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(123456)
<span style="color: #1E90FF;">'&#35; Draw a sample given the population parameters</span>
sample <- rnorm(100,10,2)
<span style="color: #1E90FF;">'&#35; Estimate the population mean with the sample average</span>
mean(sample)
<span style="color: #1E90FF;">'&#35; Draw a different sample and estimate again:</span>
sample <- rnorm(100,10,2)
mean(sample)
<span style="color: #1E90FF;">'&#35; Draw a third sample and estimate again:</span>
sample <- rnorm(100,10,2)
mean(sample)
## Script 1.51: Simulation-Repeated.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(123456)
<span style="color: #1E90FF;">'&#35; initialize ybar to a vector of length r=10000 to later store results:</span>
r <- 10000
ybar <- numeric(r)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample and store the sample mean in pos. j=1,2,... of ybar:</span>
sample <- rnorm(100,10,2)
ybar[j] <- mean(sample)
}
## Script 1.52: Simulation-Repeated-Results.R
<span style="color: #1E90FF;">'&#35; The first 20 of 10000 estimates:</span>
ybar[1:20]
<span style="color: #1E90FF;">'&#35; Simulated mean:</span>
mean(ybar)
<span style="color: #1E90FF;">'&#35; Simulated variance:</span>

# 2. Scripts Used in Chapter 02
317
var(ybar)
<span style="color: #1E90FF;">'&#35; Simulated density:</span>
plot(density(ybar))
curve( dnorm(x,10,sqrt(.04)), add=TRUE,lty=2)
## Script 1.53: Simulation-Inference.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(123456)
<span style="color: #1E90FF;">'&#35; initialize vectors to later store results:</span>
r <- 10000
CIlower <- numeric(r); CIupper <- numeric(r)
pvalue1 <- numeric(r); pvalue2 <- numeric(r)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample</span>
sample <- rnorm(100,10,2)
<span style="color: #1E90FF;">'&#35; test the (correct) null hypothesis mu=10:</span>
testres1 <- t.test(sample,mu=10)
<span style="color: #1E90FF;">'&#35; store CI & p value:</span>
CIlower[j] <- testres1$conf.int[1]
CIupper[j] <- testres1$conf.int[2]
pvalue1[j] <- testres1$p.value
<span style="color: #1E90FF;">'&#35; test the (incorrect) null hypothesis mu=9.5 & store the p value:</span>
pvalue2[j] <- t.test(sample,mu=9.5)$p.value
}
<span style="color: #1E90FF;">'&#35; Test results as logical value</span>
reject1<-pvalue1<=0.05;
reject2<-pvalue2<=0.05
table(reject1)
table(reject2)
## Script 1.54: Simulation-Inference-Figure.R
<span style="color: #1E90FF;">'&#35; Needs Simulation-Inference.R to be run first</span>
<span style="color: #1E90FF;">'&#35; color vector:</span>
color <- rep(gray(.5),100)
color[reject1[1:100]] <- "black"
<span style="color: #1E90FF;">'&#35; Prepare empty plot with correct axis limits & labels:</span>
plot(0, xlim=c(9,11), ylim=c(1,100),
ylab="Sample No.", xlab="", main="Correct H0")
<span style="color: #1E90FF;">'&#35; Vertical line at 10:</span>
abline(v=10, lty=2)
<span style="color: #1E90FF;">'&#35; Add the 100 first CIs (y is equal to j for both points):</span>
for(j in 1:100) {
lines(c(CIlower[j],CIupper[j]),c(j,j),col=color[j],lwd=2)
}
2. Scripts Used in Chapter 02
## Script 2.1: Example-2-3.R
data(ceosal1, package=’wooldridge’)
attach(ceosal1)

318
R Scripts
<span style="color: #1E90FF;">'&#35; ingredients to the OLS formulas</span>
cov(roe,salary)
var(roe)
mean(salary)
mean(roe)
<span style="color: #1E90FF;">'&#35; manual calculation of OLS coefficients</span>
( b1hat <- cov(roe,salary)/var(roe) )‰
( b0hat <- mean(salary) - b1hat*mean(roe)
)
<span style="color: #1E90FF;">'&#35; "detach" the data frame</span>
detach(ceosal1)
## Script 2.2: Example-2-3-2.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression</span>
lm( salary ~ roe, data=ceosal1 )
## Script 2.3: Example-2-3-3.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression</span>
CEOregres <- lm( salary ~ roe, data=ceosal1 )
<span style="color: #1E90FF;">'&#35; Scatter plot (restrict y axis limits)</span>
with(ceosal1, plot(roe, salary, ylim=c(0,4000)))
<span style="color: #1E90FF;">'&#35; Add OLS regression line</span>
abline(CEOregres)
## Script 2.4: Example-2-4.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
lm(wage ~ educ, data=wage1)
## Script 2.5: Example-2-5.R
data(vote1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression (parentheses for immediate output):</span>
( VOTEres <- lm(voteA ~ shareA, data=vote1) )
<span style="color: #1E90FF;">'&#35; scatter plot with regression line:</span>
with(vote1, plot(shareA, voteA))
abline(VOTEres)
## Script 2.6: Example-2-6.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; extract variables as vectors:</span>
sal <- ceosal1$salary
roe <- ceosal1$roe
<span style="color: #1E90FF;">'&#35; regression with vectors:</span>

2. Scripts Used in Chapter 02
319
CEOregres <- lm( sal ~ roe
)
<span style="color: #1E90FF;">'&#35; obtain predicted values and residuals</span>
sal.hat <- fitted(CEOregres)
u.hat <- resid(CEOregres)
<span style="color: #1E90FF;">'&#35; Wooldridge, Table 2.2:</span>
cbind(roe, sal, sal.hat, u.hat)[1:15,]
## Script 2.7: Example-2-7.R
data(wage1, package=’wooldridge’)
WAGEregres <- lm(wage ~ educ, data=wage1)
<span style="color: #1E90FF;">'&#35; obtain coefficients, predicted values and residuals</span>
b.hat <- coef(WAGEregres)
wage.hat <- fitted(WAGEregres)
u.hat <- resid(WAGEregres)
<span style="color: #1E90FF;">'&#35; Confirm property (1):</span>
mean(u.hat)
<span style="color: #1E90FF;">'&#35; Confirm property (2):</span>
cor(wage1$educ , u.hat)
<span style="color: #1E90FF;">'&#35; Confirm property (3):</span>
mean(wage1$wage)
b.hat[1] + b.hat[2]
*
mean(wage1$educ)
## Script 2.8: Example-2-8.R
data(ceosal1, package=’wooldridge’)
CEOregres <- lm( salary ~ roe, data=ceosal1 )
<span style="color: #1E90FF;">'&#35; Calculate predicted values & residuals:</span>
sal.hat <- fitted(CEOregres)
u.hat <- resid(CEOregres)
<span style="color: #1E90FF;">'&#35; Calculate R^2 in three different ways:</span>
sal <- ceosal1$salary
var(sal.hat) / var(sal)
1 - var(u.hat) / var(sal)
cor(sal, sal.hat)^2
## Script 2.9: Example-2-9.R
data(vote1, package=’wooldridge’)
VOTEres <- lm(voteA ~ shareA, data=vote1)
<span style="color: #1E90FF;">'&#35; Summary of the regression results</span>
summary(VOTEres)
<span style="color: #1E90FF;">'&#35; Calculate R^2 manually:</span>
var( fitted(VOTEres) ) / var( vote1$voteA )

320
R Scripts
## Script 2.10: Example-2-10.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate log-level model</span>
lm( log(wage) ~ educ, data=wage1 )
## Script 2.11: Example-2-11.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate log-log model</span>
lm( log(salary) ~ log(sales), data=ceosal1 )
## Script 2.12: SLR-Origin-Const.R
data(ceosal1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Usual OLS regression:</span>
(reg1 <- lm( salary ~ roe, data=ceosal1))
<span style="color: #1E90FF;">'&#35; Regression without intercept (through origin):</span>
(reg2 <- lm( salary ~ 0 + roe, data=ceosal1))
<span style="color: #1E90FF;">'&#35; Regression without slope (on a constant):</span>
(reg3 <- lm( salary ~ 1 , data=ceosal1))
<span style="color: #1E90FF;">'&#35; average y:</span>
mean(ceosal1$salary)
<span style="color: #1E90FF;">'&#35; Scatter Plot with all 3 regression lines</span>
plot(ceosal1$roe, ceosal1$salary, ylim=c(0,4000))
abline(reg1, lwd=2, lty=1)
abline(reg2, lwd=2, lty=2)
abline(reg3, lwd=2, lty=3)
legend("topleft",c("full","through origin","const only"),lwd=2,lty=1:3)
## Script 2.13: Example-2-12.R
data(meap93, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate the model and save the results as "results"</span>
results <- lm(math10 ~ lnchprg, data=meap93)
<span style="color: #1E90FF;">'&#35; Number of obs.</span>
( n <- nobs(results) )
<span style="color: #1E90FF;">'&#35; SER:</span>
(SER <- sd(resid(results))
*
sqrt((n-1)/(n-2)) )
<span style="color: #1E90FF;">'&#35; SE of b0hat & b1hat, respectively:</span>
SER / sd(meap93$lnchprg) / sqrt(n-1)
*
sqrt(mean(meap93$lnchprg^2))
SER / sd(meap93$lnchprg) / sqrt(n-1)
<span style="color: #1E90FF;">'&#35; Automatic calculations:</span>
summary(results)
## Script 2.14: SLR-Sim-Sample.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set sample size</span>
n<-1000

2. Scripts Used in Chapter 02
321
<span style="color: #1E90FF;">'&#35; set true parameters: betas and sd of u</span>
b0<-1; b1<-0.5; su<-2
<span style="color: #1E90FF;">'&#35; Draw a sample of size n:</span>
x <- rnorm(n,4,1)
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; estimate parameters by OLS</span>
(olsres <- lm(y~x))
<span style="color: #1E90FF;">'&#35; features of the sample for the variance formula:</span>
mean(x^2)
sum((x-mean(x))^2)
<span style="color: #1E90FF;">'&#35; Graph</span>
plot(x, y, col="gray", xlim=c(0,8) )
abline(b0,b1,lwd=2)
abline(olsres,col="gray",lwd=2)
legend("topleft",c("pop. regr. fct.","OLS regr. fct."),
lwd=2,col=c("black","gray"))
## Script 2.15: SLR-Sim-Model.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set sample size and number of simulations</span>
n<-1000; r<-10000
<span style="color: #1E90FF;">'&#35; set true parameters: betas and sd of u</span>
b0<-1; b1<-0.5; su<-2
<span style="color: #1E90FF;">'&#35; initialize b0hat and b1hat to store results later:</span>
b0hat <- numeric(r)
b1hat <- numeric(r)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample of size n:</span>
x <- rnorm(n,4,1)
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; estimate parameters by OLS and store them in the vectors</span>
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.16: SLR-Sim-Model-Condx.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set sample size and number of simulations</span>
n<-1000; r<-10000
<span style="color: #1E90FF;">'&#35; set true parameters: betas and sd of u</span>

322
R Scripts
b0<-1; b1<-0.5; su<-2
<span style="color: #1E90FF;">'&#35; initialize b0hat and b1hat to store results later:</span>
b0hat <- numeric(r)
b1hat <- numeric(r)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
u <- rnorm(n,0,su)
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; estimate parameters by OLS and store them in the vectors</span>
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.17: SLR-Sim-Results.R
<span style="color: #1E90FF;">'&#35; MC estimate of the expected values:</span>
mean(b0hat)
mean(b1hat)
<span style="color: #1E90FF;">'&#35; MC estimate of the variances:</span>
var(b0hat)
var(b1hat)
<span style="color: #1E90FF;">'&#35; Initialize empty plot</span>
plot( NULL, xlim=c(0,8), ylim=c(0,6), xlab="x", ylab="y")
<span style="color: #1E90FF;">'&#35; add OLS regression lines</span>
for (j in 1:10) abline(b0hat[j],b1hat[j],col="gray")
<span style="color: #1E90FF;">'&#35; add population regression line</span>
abline(b0,b1,lwd=2)
<span style="color: #1E90FF;">'&#35; add legend</span>
legend("topleft",c("Population","OLS regressions"),
lwd=c(2,1),col=c("black","gray"))
## Script 2.18: SLR-Sim-ViolSLR4.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set sample size and number of simulations</span>
n<-1000; r<-10000
<span style="color: #1E90FF;">'&#35; set true parameters: betas and sd of u</span>
b0<-1; b1<-0.5; su<-2
<span style="color: #1E90FF;">'&#35; initialize b0hat and b1hat to store results later:</span>
b0hat <- numeric(r)
b1hat <- numeric(r)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>

2. Scripts Used in Chapter 02
323
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
u <- rnorm(n, (x-4)/5, su)
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; estimate parameters by OLS and store them in the vectors</span>
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.19: SLR-Sim-Results-ViolSLR4.R
<span style="color: #1E90FF;">'&#35; MC estimate of the expected values:</span>
mean(b0hat)
mean(b1hat)
<span style="color: #1E90FF;">'&#35; MC estimate of the variances:</span>
var(b0hat)
var(b1hat)
## Script 2.20: SLR-Sim-ViolSLR5.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set sample size and number of simulations</span>
n<-1000; r<-10000
<span style="color: #1E90FF;">'&#35; set true parameters: betas and sd of u</span>
b0<-1; b1<-0.5; su<-2
<span style="color: #1E90FF;">'&#35; initialize b0hat and b1hat to store results later:</span>
b0hat <- numeric(r)
b1hat <- numeric(r)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:r) {
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
varu <- 4/exp(4.5)
*
exp(x)
u <- rnorm(n, 0, sqrt(varu) )
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; estimate parameters by OLS and store them in the vectors</span>
bhat <- coefficients( lm(y~x) )
b0hat[j] <- bhat["(Intercept)"]
b1hat[j] <- bhat["x"]
}
## Script 2.21: SLR-Sim-Results-ViolSLR5.R
<span style="color: #1E90FF;">'&#35; MC estimate of the expected values:</span>
mean(b0hat)
mean(b1hat)
<span style="color: #1E90FF;">'&#35; MC estimate of the variances:</span>
var(b0hat)
var(b1hat)

324
R Scripts
# 3. Scripts Used in Chapter 03
## Script 3.1: Example-3-1.R
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Just obtain parameter estimates:</span>
lm(colGPA ~ hsGPA+ACT, data=gpa1)
<span style="color: #1E90FF;">'&#35; Store results under "GPAres" and display full table:</span>
GPAres <- lm(colGPA ~ hsGPA+ACT, data=gpa1)
summary(GPAres)
## Script 3.2: Example-3-2.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
summary( lm(log(wage) ~ educ+exper+tenure, data=wage1) )
## Script 3.3: Example-3-3.R
data(k401k, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
summary( lm(prate ~ mrate+age, data=k401k) )
## Script 3.4: Example-3-5.R
data(crime1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Model without avgsen:</span>
summary( lm(narr86 ~ pcnv+ptime86+qemp86, data=crime1) )
<span style="color: #1E90FF;">'&#35; Model with avgsen:</span>
summary( lm(narr86 ~ pcnv+avgsen+ptime86+qemp86, data=crime1) )
## Script 3.5: Example-3-6.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
summary( lm(log(wage) ~ educ, data=wage1) )
## Script 3.6: OLS-Matrices.R
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Determine sample size & no. of regressors:</span>
n <- nrow(gpa1); k<-2
<span style="color: #1E90FF;">'&#35; extract y</span>
y <- gpa1$colGPA
<span style="color: #1E90FF;">'&#35; extract X & add a column of ones</span>
X <- cbind(1, gpa1$hsGPA, gpa1$ACT)
<span style="color: #1E90FF;">'&#35; Display first rows of X:</span>
head(X)
<span style="color: #1E90FF;">'&#35; Parameter estimates:</span>
( bhat <- solve( t(X)%*%X ) %*% t(X)%*%y
)

( R2.hsGPA <- summary( lm(hsGPA~ACT, data=gpa1) )$r.squared ) ( VIF.hsGPA <- 1/(1-R2.hsGPA) )
<span style="color: #1E90FF;">'&#35; manual calculation of SE of hsGPA coefficient:</span>
n <- nobs(res)
sdx <- sd(gpa1$hsGPA) * sqrt((n-1)/n) '# (Note: sd() uses the (n-1) version) ( SE.hsGPA <- 1/sqrt(n) 
* SER/sdx * sqrt(VIF.hsGPA) )
3. Scripts Used in Chapter 03
325
<span style="color: #1E90FF;">'&#35; Residuals, estimated variance of u and SER:</span>
uhat <- y - X %*%
bhat
sigsqhat <- as.numeric( t(uhat) %*%
uhat / (n-k-1) )
( SER <- sqrt(sigsqhat) )
<span style="color: #1E90FF;">'&#35; Estimated variance of the parameter estimators and SE:</span>
Vbetahat <- sigsqhat
*
solve( t(X)%*%X
)
( se <- sqrt( diag(Vbetahat) ) )
## Script 3.7: Omitted-Vars.R
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Parameter estimates for full and simple model:</span>
beta.hat <- coef( lm(colGPA ~ ACT+hsGPA, data=gpa1) )
beta.hat
<span style="color: #1E90FF;">'&#35; Relation between regressors:</span>
delta.tilde <- coef( lm(hsGPA ~ ACT, data=gpa1) )
delta.tilde
<span style="color: #1E90FF;">'&#35; Omitted variables formula for beta1.tilde:</span>
beta.hat["ACT"] + beta.hat["hsGPA"]*delta.tilde["ACT"]
<span style="color: #1E90FF;">'&#35; Actual regression with hsGPA omitted:</span>
lm(colGPA ~ ACT, data=gpa1)
## Script 3.8: MLR-SE.R
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Full estimation results including automatic SE :</span>
res <- lm(colGPA ~ hsGPA+ACT, data=gpa1)
summary(res)
<span style="color: #1E90FF;">'&#35; Extract SER (instead of calculation via residuals)</span>
( SER <- summary(res)$sigma )
<span style="color: #1E90FF;">'&#35; regressing hsGPA on ACT for calculation of R2 & VIF</span>
## Script 3.9: MLR-VIF.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
lmres <- lm(log(wage) ~ educ+exper+tenure, data=wage1)
<span style="color: #1E90FF;">'&#35; Regression output:</span>
summary(lmres)
<span style="color: #1E90FF;">'&#35; Load package "car" (has to be installed):</span>
library(car)

326
R Scripts
<span style="color: #1E90FF;">'&#35; Automatically calculate VIF :</span>
vif(lmres)
# 4. Scripts Used in Chapter 04
## Script 4.1: Example-4-3.R
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Store results under "sumres" and display full table:</span>
( sumres <- summary( lm(colGPA ~ hsGPA+ACT+skipped, data=gpa1) ) )
<span style="color: #1E90FF;">'&#35; Manually confirm the formulas: Extract coefficients and SE</span>
regtable <- sumres$coefficients
bhat <- regtable[,1]
se
<- regtable[,2]
<span style="color: #1E90FF;">'&#35; Reproduce t statistic</span>
( tstat <- bhat / se )
<span style="color: #1E90FF;">'&#35; Reproduce p value</span>
( pval
<- 2*pt(-abs(tstat),137)
)
## Script 4.2: Example-4-1.R
data(wage1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
summary( lm(log(wage) ~ educ+exper+tenure, data=wage1) )
## Script 4.3: Example-4-8.R
data(rdchem, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS regression:</span>
myres <- lm(log(rd) ~ log(sales)+profmarg, data=rdchem)
<span style="color: #1E90FF;">'&#35; Regression output:</span>
summary(myres)
<span style="color: #1E90FF;">'&#35; 95% CI:</span>
confint(myres)
<span style="color: #1E90FF;">'&#35; 99% CI:</span>
confint(myres, level=0.99)
## Script 4.4: F-Test-MLB.R
data(mlb1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Unrestricted OLS regression:</span>
res.ur <- lm(log(salary) ~ years+gamesyr+bavg+hrunsyr+rbisyr, data=mlb1)
<span style="color: #1E90FF;">'&#35; Restricted OLS regression:</span>
res.r <- lm(log(salary) ~ years+gamesyr, data=mlb1)
<span style="color: #1E90FF;">'&#35; R2:</span>
( r2.ur <- summary(res.ur)$r.squared )
( r2.r <- summary(res.r)$r.squared )

# 5. Scripts Used in Chapter 05
327
<span style="color: #1E90FF;">'&#35; F statistic:</span>
( F <- (r2.ur-r2.r) / (1-r2.ur)
*
347/3 )
<span style="color: #1E90FF;">'&#35; p value = 1-cdf of the appropriate F distribution:</span>
1-pf(F, 3,347)
## Script 4.5: F-Test-MLB-auto.R
data(mlb1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Unrestricted OLS regression:</span>
res.ur <- lm(log(salary) ~ years+gamesyr+bavg+hrunsyr+rbisyr, data=mlb1)
<span style="color: #1E90FF;">'&#35; Load package "car" (which has to be installed on the computer)</span>
library(car)
<span style="color: #1E90FF;">'&#35; F test</span>
myH0 <- c("bavg","hrunsyr","rbisyr")
linearHypothesis(res.ur, myH0)
## Script 4.6: F-Test-MLB-auto2.R
<span style="color: #1E90FF;">'&#35; F test (F-Test-MLB-auto.R has to be run first!)</span>
myH0 <- c("bavg", "hrunsyr=2*rbisyr")
linearHypothesis(res.ur, myH0)
## Script 4.7: F-Test-MLB-auto3.R
<span style="color: #1E90FF;">'&#35; Note: ## Script "F-Test-MLB-auto.R" has to be run first to create res.ur.</span>
<span style="color: #1E90FF;">'&#35; Which variables used in res.ur contain "yr" in their names?</span>
myH0 <- matchCoefs(res.ur,"yr")
myH0
<span style="color: #1E90FF;">'&#35; F test (F-Test-MLB-auto.R has to be run first!)</span>
linearHypothesis(res.ur, myH0)
## Script 4.8: Example-4-10.R
data(meap93, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; define new variable within data frame</span>
meap93$b_s <- meap93$benefits / meap93$salary
<span style="color: #1E90FF;">'&#35; Estimate three different models</span>
model1<- lm(log(salary) ~ b_s
, data=meap93)
model2<- lm(log(salary) ~ b_s+log(enroll)+log(staff), data=meap93)
model3<- lm(log(salary) ~ b_s+log(enroll)+log(staff)+droprate+gradrate
, data=meap93)
<span style="color: #1E90FF;">'&#35; Load package and display table of results</span>
library(stargazer)
stargazer(list(model1,model2,model3),type="text",keep.stat=c("n","rsq"))
5. Scripts Used in Chapter 05
## Script 5.1: Sim-Asy-OLS-norm.R
<span style="color: #1E90FF;">'&#35; Note: We’ll have to set the sample size first, e.g. by uncommenting:</span>
<span style="color: #1E90FF;">'&#35; n <- 100</span>
<span style="color: #1E90FF;">'&#35; Set the random seed</span>

328
R Scripts
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set true parameters: intercept & slope</span>
b0 <- 1; b1 <- 0.5
<span style="color: #1E90FF;">'&#35; initialize b1hat to store 10000 results:</span>
b1hat <- numeric(10000)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:10000) {
<span style="color: #1E90FF;">'&#35; Draw a sample of u (std. normal):</span>
u <- rnorm(n)
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; regress y on x and store slope estimate at position j</span>
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.2: Sim-Asy-OLS-chisq.R
<span style="color: #1E90FF;">'&#35; Note: We’ll have to set the sample size first, e.g. by uncommenting:</span>
<span style="color: #1E90FF;">'&#35; n <- 100</span>
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set true parameters: intercept & slope</span>
b0<-1; b1<-0.5
<span style="color: #1E90FF;">'&#35; initialize b1hat to store 10000 results:</span>
b1hat <- numeric(10000)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:10000) {
<span style="color: #1E90FF;">'&#35; Draw a sample of u (standardized chi-squared[1]):</span>
u <- ( rchisq(n,1)-1 ) / sqrt(2)
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; regress y on x and store slope estimate at position j</span>
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.3: Sim-Asy-OLS-uncond.R
<span style="color: #1E90FF;">'&#35; Note: We’ll have to set the sample size first, e.g. by uncommenting:</span>
<span style="color: #1E90FF;">'&#35; n <- 100</span>
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set true parameters: intercept & slope</span>
b0<-1; b1<-0.5
<span style="color: #1E90FF;">'&#35; initialize b1hat to store 10000 results:</span>
b1hat <- numeric(10000)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:10000) {
<span style="color: #1E90FF;">'&#35; Draw a sample of x, varying over replications:</span>
x <- rnorm(n,4,1)
<span style="color: #1E90FF;">'&#35; Draw a sample of u (std. normal):</span>
u <- rnorm(n)

# 6. Scripts Used in Chapter 06
329
<span style="color: #1E90FF;">'&#35; Draw a sample of y:</span>
y <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; regress y on x and store slope estimate at position j</span>
bhat <- coef( lm(y~x) )
b1hat[j] <- bhat["x"]
}
## Script 5.4: Example-5-3.R
data(crime1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; 1. Estimate restricted model:</span>
restr <- lm(narr86 ~ pcnv+ptime86+qemp86, data=crime1)
<span style="color: #1E90FF;">'&#35; 2. Regression of residuals from restricted model:</span>
utilde <- resid(restr)
LMreg <- lm(utilde ~ pcnv+ptime86+qemp86+avgsen+tottime, data=crime1)
<span style="color: #1E90FF;">'&#35; R-squared:</span>
(r2 <- summary(LMreg)$r.squared )
<span style="color: #1E90FF;">'&#35; 3. Calculation of LM test statistic:</span>
LM <- r2
*
nobs(LMreg)
LM
<span style="color: #1E90FF;">'&#35; 4. Critical value from chi-squared distribution, alpha=10%:</span>
qchisq(1-0.10, 2)
<span style="color: #1E90FF;">'&#35; Alternative to critical value: p value</span>
1-pchisq(LM, 2)
<span style="color: #1E90FF;">'&#35; Alternative: automatic F test (see above)</span>
library(car)
unrestr <- lm(narr86 ~ pcnv+ptime86+qemp86+avgsen+tottime, data=crime1)
linearHypothesis(unrestr, c("avgsen=0","tottime=0"))
6. Scripts Used in Chapter 06
## Script 6.1: Data-Scaling.R
data(bwght, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Basic model:</span>
lm( bwght ~ cigs+faminc, data=bwght)
<span style="color: #1E90FF;">'&#35; Weight in pounds, manual way:</span>
bwght$bwghtlbs <- bwght$bwght/16
lm( bwghtlbs ~ cigs+faminc, data=bwght)
<span style="color: #1E90FF;">'&#35; Weight in pounds, direct way:</span>
lm( I(bwght/16) ~ cigs+faminc, data=bwght)
<span style="color: #1E90FF;">'&#35; Packs of cigarettes:</span>
lm( bwght ~ I(cigs/20) +faminc, data=bwght)
## Script 6.2: Example-6-1.R
data(hprice2, package=’wooldridge’)

330
R Scripts
<span style="color: #1E90FF;">'&#35; Estimate model with standardized variables:</span>
lm(scale(price) ~ 0+scale(nox)+scale(crime)+scale(rooms)+
scale(dist)+scale(stratio), data=hprice2)
## Script 6.3: Formula-Logarithm.R
data(hprice2, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate model with logs:</span>
lm(log(price)~log(nox)+rooms, data=hprice2)
## Script 6.4: Example-6-2.R
data(hprice2, package=’wooldridge’)
res <- lm(log(price)~log(nox)+log(dist)+rooms+I(rooms^2)+
stratio,data=hprice2)
summary(res)
<span style="color: #1E90FF;">'&#35; Using poly(...):</span>
res <- lm(log(price)~log(nox)+log(dist)+poly(rooms,2,raw=TRUE)+
stratio,data=hprice2)
summary(res)
## Script 6.5: Example-6-2-Anova.R
library(car)
data(hprice2, package=’wooldridge’)
res <- lm(log(price)~log(nox)+log(dist)+poly(rooms,2,raw=TRUE)+
stratio,data=hprice2)
<span style="color: #1E90FF;">'&#35; Manual F test for rooms:</span>
linearHypothesis(res, matchCoefs(res,"rooms"))
<span style="color: #1E90FF;">'&#35; ANOVA (type 2) table:</span>
Anova(res)
## Script 6.6: Example-6-3.R
data(attend, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate model with interaction effect:</span>
(myres<-lm(stndfnl~atndrte*priGPA+ACT+I(priGPA^2)+I(ACT^2),
data=attend))
<span style="color: #1E90FF;">'&#35; Estimate for partial effect at priGPA=2.59:</span>
b <- coef(myres)
b["atndrte"] + 2.59*b["atndrte:priGPA"]
<span style="color: #1E90FF;">'&#35; Test partial effect for priGPA=2.59:</span>
library(car)
linearHypothesis(myres,c("atndrte+2.59*atndrte:priGPA"))
## Script 6.7: Example-6-5.R
data(gpa2, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Regress and report coefficients</span>
reg <- lm(colgpa~sat+hsperc+hsize+I(hsize^2),data=gpa2)
reg

6. Scripts Used in Chapter 06
331
<span style="color: #1E90FF;">'&#35; Generate data set containing the regressor values for predictions</span>
cvalues <- data.frame(sat=1200, hsperc=30, hsize=5)
<span style="color: #1E90FF;">'&#35; Point estimate of prediction</span>
predict(reg, cvalues)
<span style="color: #1E90FF;">'&#35; Point estimate and 95% confidence interval</span>
predict(reg, cvalues, interval = "confidence")
<span style="color: #1E90FF;">'&#35; Define three sets of regressor variables</span>
cvalues <- data.frame(sat=c(1200,900,1400), hsperc=c(30,20,5),
hsize=c(5,3,1))
cvalues
<span style="color: #1E90FF;">'&#35; Point estimates and 99% confidence intervals for these</span>
predict(reg, cvalues, interval = "confidence", level=0.99)
## Script 6.8: Example-6-6.R
data(gpa2, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Regress (as before)</span>
reg <- lm(colgpa~sat+hsperc+hsize+I(hsize^2),data=gpa2)
<span style="color: #1E90FF;">'&#35; Define three sets of regressor variables (as before)</span>
cvalues <- data.frame(sat=c(1200,900,1400), hsperc=c(30,20,5),
hsize=c(5,3,1))
<span style="color: #1E90FF;">'&#35; Point estimates and 95% prediction intervals for these</span>
predict(reg, cvalues, interval = "prediction")
## Script 6.9: Effects-Manual.R
<span style="color: #1E90FF;">'&#35; Repeating the regression from Example 6.2:</span>
data(hprice2, package=’wooldridge’)
res <- lm( log(price) ~ log(nox)+log(dist)+rooms+I(rooms^2)+stratio,
data=hprice2)
<span style="color: #1E90FF;">'&#35; Predictions: Values of the regressors:</span>
<span style="color: #1E90FF;">'&#35; rooms = 4-8, all others at the sample mean:</span>
X <- data.frame(rooms=seq(4,8),nox=5.5498,dist=3.7958,stratio=18.4593)
<span style="color: #1E90FF;">'&#35; Calculate predictions and confidence interval:</span>
pred <- predict(res, X, interval = "confidence")
<span style="color: #1E90FF;">'&#35; Table of regressor values, predictions and CI:</span>
cbind(X,pred)
<span style="color: #1E90FF;">'&#35; Plot</span>
matplot(X$rooms, pred, type="l", lty=c(1,2,2))
## Script 6.10: Effects-Automatic.R
<span style="color: #1E90FF;">'&#35; Repeating the regression from Example 6.2:</span>
data(hprice2, package=’wooldridge’)
res <- lm( log(price) ~ log(nox)+log(dist)+rooms+I(rooms^2)+stratio,
data=hprice2)

332
R Scripts
<span style="color: #1E90FF;">'&#35; Automatic effects plot using the package "effects"</span>
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
<span style="color: #1E90FF;">'&#35; replace "female" with logical variable</span>
wage1$female <- as.logical(wage1$female)
table(wage1$female)
<span style="color: #1E90FF;">'&#35; regression with logical variable</span>
lm(wage ~ female+educ+exper+tenure, data=wage1)
## Script 7.4: Regr-Factors.R
data(CPS1985,package="AER")
<span style="color: #1E90FF;">'&#35; Table of categories and frequencies for two factor variables:</span>
table(CPS1985$gender)
table(CPS1985$occupation)
<span style="color: #1E90FF;">'&#35; Directly using factor variables in regression formula:</span>
lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
<span style="color: #1E90FF;">'&#35; Manually redefine the</span>
reference category:
CPS1985$gender <- relevel(CPS1985$gender,"female")
CPS1985$occupation <- relevel(CPS1985$occupation,"management")
<span style="color: #1E90FF;">'&#35; Rerun regression:</span>
lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
## Script 7.5: Regr-Factors-Anova.R
data(CPS1985,package="AER")
<span style="color: #1E90FF;">'&#35; Regression</span>
res <- lm(log(wage) ~ education+experience+gender+occupation, data=CPS1985)
<span style="color: #1E90FF;">'&#35; ANOVA table</span>
car::Anova(res)

# 8. Scripts Used in Chapter 08
333
## Script 7.6: Example-7-8.R
data(lawsch85, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define cut points for the rank</span>
cutpts <- c(0,10,25,40,60,100,175)
<span style="color: #1E90FF;">'&#35; Create factor variable containing ranges for the rank</span>
lawsch85$rankcat <- cut(lawsch85$rank, cutpts)
<span style="color: #1E90FF;">'&#35; Display frequencies</span>
table(lawsch85$rankcat)
<span style="color: #1E90FF;">'&#35; Choose reference category</span>
lawsch85$rankcat <- relevel(lawsch85$rankcat,"(100,175]")
<span style="color: #1E90FF;">'&#35; Run regression</span>
(res <- lm(log(salary)~rankcat+LSAT+GPA+log(libvol)+log(cost), data=lawsch85))
<span style="color: #1E90FF;">'&#35; ANOVA table</span>
car::Anova(res)
## Script 7.7: Dummy-Interact.R
data(gpa3, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Model with full interactions with female dummy (only for spring data)</span>
reg<-lm(cumgpa~female*(sat+hsperc+tothrs),
data=gpa3, subset=(spring== 1))
summary(reg)
<span style="color: #1E90FF;">'&#35; F-Test from package "car". H0: the interaction coefficients are zero</span>
<span style="color: #1E90FF;">'&#35; matchCoefs(...) selects all coeffs with names containing "female"</span>
library(car)
linearHypothesis(reg, matchCoefs(reg, "female"))
## Script 7.8: Dummy-Interact-Sep.R
data(gpa3, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate model for males (& spring data)</span>
lm(cumgpa~sat+hsperc+tothrs, data=gpa3, subset=(spring== 1&female== 0))
<span style="color: #1E90FF;">'&#35; Estimate model for females (& spring data)</span>
lm(cumgpa~sat+hsperc+tothrs, data=gpa3, subset=(spring== 1&female== 1))
8. Scripts Used in Chapter 08
## Script 8.1: Example-8-2.R
data(gpa3, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; load packages (which need to be installed!)</span>
library(lmtest); library(car)
<span style="color: #1E90FF;">'&#35; Estimate model (only for spring data)</span>
reg <- lm(cumgpa~sat+hsperc+tothrs+female+black+white,
data=gpa3, subset=(spring== 1))
<span style="color: #1E90FF;">'&#35; Usual SE:</span>
coeftest(reg)

334
R Scripts
<span style="color: #1E90FF;">'&#35; Refined White heteroscedasticity-robust SE:</span>
coeftest(reg, vcov=hccm)
## Script 8.2: Example-8-2-cont.R
<span style="color: #1E90FF;">'&#35; F-Tests using different variance-covariance formulas:</span>
myH0 <- c("black","white")
<span style="color: #1E90FF;">'&#35; Ususal VCOV</span>
linearHypothesis(reg, myH0)
<span style="color: #1E90FF;">'&#35; Refined White VCOV</span>
linearHypothesis(reg, myH0, vcov=hccm)
<span style="color: #1E90FF;">'&#35; Classical White VCOV</span>
linearHypothesis(reg, myH0, vcov=hccm(reg,type="hc0"))
## Script 8.3: Example-8-4.R
data(hprice1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate model</span>
reg <- lm(price~lotsize+sqrft+bdrms, data=hprice1)
reg
<span style="color: #1E90FF;">'&#35; Automatic BP test</span>
library(lmtest)
bptest(reg)
<span style="color: #1E90FF;">'&#35; Manual regression of squared residuals</span>
summary(lm( resid(reg)^2 ~ lotsize+sqrft+bdrms, data=hprice1))
## Script 8.4: Example-8-5.R
data(hprice1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate model</span>
reg <- lm(log(price)~log(lotsize)+log(sqrft)+bdrms, data=hprice1)
reg
<span style="color: #1E90FF;">'&#35; BP test</span>
library(lmtest)
bptest(reg)
<span style="color: #1E90FF;">'&#35; White test</span>
bptest(reg, ~ fitted(reg) + I(fitted(reg)^2) )
## Script 8.5: Example-8-6.R
data(k401ksubs, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS (only for singles: fsize== 1)</span>
lm(nettfa ~ inc + I((age-25)^2) + male + e401k,
data=k401ksubs, subset=(fsize== 1))
<span style="color: #1E90FF;">'&#35; WLS</span>
lm(nettfa ~ inc + I((age-25)^2) + male + e401k, weight=1/inc,
data=k401ksubs, subset=(fsize== 1))
## Script 8.6: WLS-Robust.R
data(k401ksubs, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; WLS</span>

# 9. Scripts Used in Chapter 09
335
wlsreg <- lm(nettfa ~ inc + I((age-25)^2) + male + e401k,
weight=1/inc, data=k401ksubs, subset=(fsize== 1))
<span style="color: #1E90FF;">'&#35; non-robust results</span>
library(lmtest); library(car)
coeftest(wlsreg)
<span style="color: #1E90FF;">'&#35; robust results (Refined White SE:)</span>
coeftest(wlsreg,hccm)
## Script 8.7: Example-8-7.R
data(smoke, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS</span>
olsreg<-lm(cigs~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
data=smoke)
olsreg
<span style="color: #1E90FF;">'&#35; BP test</span>
library(lmtest)
bptest(olsreg)
<span style="color: #1E90FF;">'&#35; FGLS: estimation of the variance function</span>
logu2 <- log(resid(olsreg)^2)
varreg<-lm(logu2~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
data=smoke)
<span style="color: #1E90FF;">'&#35; FGLS: WLS</span>
w <- 1/exp(fitted(varreg))
lm(cigs~log(income)+log(cigpric)+educ+age+I(age^2)+restaurn,
weight=w ,data=smoke)
9. Scripts Used in Chapter 09
## Script 9.1: Example-9-2-manual.R
data(hprice1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; original linear regression</span>
orig <- lm(price ~ lotsize+sqrft+bdrms, data=hprice1)
<span style="color: #1E90FF;">'&#35; regression for RESET test</span>
RESETreg <- lm(price ~ lotsize+sqrft+bdrms+I(fitted(orig)^2)+
I(fitted(orig)^3), data=hprice1)
RESETreg
<span style="color: #1E90FF;">'&#35; RESET test. H0: all coeffs including "fitted" are=0</span>
library(car)
linearHypothesis(RESETreg, matchCoefs(RESETreg,"fitted"))
## Script 9.2: Example-9-2-automatic.R
data(hprice1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; original linear regression</span>
orig <- lm(price ~ lotsize+sqrft+bdrms, data=hprice1)

336
R Scripts
<span style="color: #1E90FF;">'&#35; RESET test</span>
library(lmtest)
resettest(orig)
## Script 9.3: Nonnested-Test.R
data(hprice1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; two alternative models</span>
model1 <- lm(price ~
lotsize
+
sqrft
+ bdrms, data=hprice1)
model2 <- lm(price ~ log(lotsize) + log(sqrft) + bdrms, data=hprice1)
<span style="color: #1E90FF;">'&#35; Test against comprehensive model</span>
library(lmtest)
encomptest(model1,model2, data=hprice1)
## Script 9.4: Sim-ME-Dep.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set true parameters: intercept & slope</span>
b0<-1; b1<-0.5
<span style="color: #1E90FF;">'&#35; initialize b1hat to store 10000 results:</span>
b1hat <- numeric(10000)
b1hat.me <- numeric(10000)
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
x <- rnorm(1000,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:10000) {
<span style="color: #1E90FF;">'&#35; Draw a sample of u</span>
u <- rnorm(1000)
<span style="color: #1E90FF;">'&#35; Draw a sample of ystar:</span>
ystar <- b0 + b1*x
+ u
<span style="color: #1E90FF;">'&#35; regress ystar on x and store slope estimate at position j</span>
bhat <- coef( lm(ystar~x) )
b1hat[j] <- bhat["x"]
<span style="color: #1E90FF;">'&#35; Measurement error and mismeasured y:</span>
e0 <- rnorm(1000)
y <- ystar+e0
<span style="color: #1E90FF;">'&#35; regress y on x and store slope estimate at position j</span>
bhat.me <- coef( lm(y~x) )
b1hat.me[j] <- bhat.me["x"]
}
<span style="color: #1E90FF;">'&#35; Mean with and without ME</span>
c( mean(b1hat), mean(b1hat.me) )
<span style="color: #1E90FF;">'&#35; Variance with and without ME</span>
c( var(b1hat), var(b1hat.me) )
## Script 9.5: Sim-ME-Explan.R
<span style="color: #1E90FF;">'&#35; Set the random seed</span>
set.seed(1234567)
<span style="color: #1E90FF;">'&#35; set true parameters: intercept & slope</span>
b0<-1; b1<-0.5
<span style="color: #1E90FF;">'&#35; initialize b1hat to store 10000 results:</span>
b1hat <- numeric(10000)
b1hat.me <- numeric(10000)

9. Scripts Used in Chapter 09
337
<span style="color: #1E90FF;">'&#35; Draw a sample of x, fixed over replications:</span>
xstar <- rnorm(1000,4,1)
<span style="color: #1E90FF;">'&#35; repeat r times:</span>
for(j in 1:10000) {
<span style="color: #1E90FF;">'&#35; Draw a sample of u</span>
u <- rnorm(1000)
<span style="color: #1E90FF;">'&#35; Draw a sample of ystar:</span>
y <- b0 + b1*xstar
+ u
<span style="color: #1E90FF;">'&#35; regress y on xstar and store slope estimate at position j</span>
bhat <- coef( lm(y~xstar) )
b1hat[j] <- bhat["xstar"]
<span style="color: #1E90FF;">'&#35; Measurement error and mismeasured y:</span>
e1 <- rnorm(1000)
x <- xstar+e1
<span style="color: #1E90FF;">'&#35; regress y on x and store slope estimate at position j</span>
bhat.me <- coef( lm(y~x) )
b1hat.me[j] <- bhat.me["x"]
}
<span style="color: #1E90FF;">'&#35; Mean with and without ME</span>
c( mean(b1hat), mean(b1hat.me) )
<span style="color: #1E90FF;">'&#35; Variance with and without ME</span>
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
<span style="color: #1E90FF;">'&#35; extract LSAT</span>
lsat <- lawsch85$LSAT
<span style="color: #1E90FF;">'&#35; Create logical indicator for missings</span>
missLSAT <- is.na(lawsch85$LSAT)
<span style="color: #1E90FF;">'&#35; LSAT and indicator for Schools No. 120-129:</span>
rbind(lsat,missLSAT)[,120:129]
<span style="color: #1E90FF;">'&#35; Frequencies of indicator</span>
table(missLSAT)
<span style="color: #1E90FF;">'&#35; Missings for all variables in data frame (counts)</span>
colSums(is.na(lawsch85))
<span style="color: #1E90FF;">'&#35; Indicator for complete cases</span>
compl <- complete.cases(lawsch85)
table(compl)

338
R Scripts
## Script 9.8: Missings-Analyses.R
data(lawsch85, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Mean of a variable with missings:</span>
mean(lawsch85$LSAT)
mean(lawsch85$LSAT,na.rm=TRUE)
<span style="color: #1E90FF;">'&#35; Regression with missings</span>
summary(lm(log(salary)~LSAT+cost+age, data=lawsch85))
## Script 9.9: Outliers.R
data(rdchem, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Regression</span>
reg <- lm(rdintens~sales+profmarg, data=rdchem)
<span style="color: #1E90FF;">'&#35; Studentized residuals for all observations:</span>
studres <- rstudent(reg)
<span style="color: #1E90FF;">'&#35; Display extreme values:</span>
min(studres)
max(studres)
<span style="color: #1E90FF;">'&#35; Histogram (and overlayed density plot):</span>
hist(studres, freq=FALSE)
lines(density(studres), lwd=2)
## Script 9.10: LAD.R
data(rdchem, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; OLS Regression</span>
ols <- lm(rdintens ~ I(sales/1000) +profmarg, data=rdchem)
<span style="color: #1E90FF;">'&#35; LAD Regression</span>
library(quantreg)
lad <- rq(rdintens ~ I(sales/1000) +profmarg, data=rdchem)
<span style="color: #1E90FF;">'&#35; regression table</span>
library(stargazer)
stargazer(ols,lad,
type = "text")
# 10. Scripts Used in Chapter 10
## Script 10.1: Example-10-2.R
data(intdef, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Linear regression of static model:</span>
summary( lm(i3~inf+def,data=intdef)
)
## Script 10.2: Example-Barium.R
data(barium, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Imports from China: Variable "chnimp" from data frame "data"</span>
<span style="color: #1E90FF;">'&#35; Monthly time series starting Feb. 1978</span>
impts <- ts(barium$chnimp, start=c(1978,2), frequency=12)

10. Scripts Used in Chapter 10
339
<span style="color: #1E90FF;">'&#35; plot time series</span>
plot(impts)
## Script 10.3: Example-zoo.R
data(intdef, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Variable "year" as the time measure:</span>
intdef$year
<span style="color: #1E90FF;">'&#35; define "zoo" object containing all data, time measure=year:</span>
library(zoo)
zoodata <- zoo(intdef, order.by=intdef$year)
<span style="color: #1E90FF;">'&#35; Time series plot of inflation</span>
plot(zoodata$i3)
## Script 10.4: Example-quantmod.R
library(quantmod)
<span style="color: #1E90FF;">'&#35; Which Yahoo Finance symbols?</span>
<span style="color: #1E90FF;">'&#35; See http://finance.yahoo.com/lookup:</span>
<span style="color: #1E90FF;">'&#35; "F" = Ford Motor Company</span>
<span style="color: #1E90FF;">'&#35; Download data</span>
getSymbols("F", auto.assign=TRUE)
<span style="color: #1E90FF;">'&#35; first and last 6 rows of resulting data frame:</span>
head(F)
tail(F)
<span style="color: #1E90FF;">'&#35; Time series plot of adjusted closing prices:</span>
plot(F$F.Adjusted, las=2)
## Script 10.5: Example-10-4.R
<span style="color: #1E90FF;">'&#35; Libraries for dynamic lm, regression table and F tests</span>
library(dynlm);library(lmtest);library(car)
data(fertil3, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define Yearly time series beginning in 1913</span>
tsdata <- ts(fertil3, start=1913)
<span style="color: #1E90FF;">'&#35; Linear regression of model with lags:</span>
res <- dynlm(gfr ~ pe + L(pe) + L(pe,2) + ww2 + pill, data=tsdata)
coeftest(res)
<span style="color: #1E90FF;">'&#35; F test. H0: all pe coefficients are=0</span>
linearHypothesis(res, matchCoefs(res,"pe"))
## Script 10.6: Example-10-4-contd.R
<span style="color: #1E90FF;">'&#35; Calculating the LRP</span>
b<-coef(res)
b["pe"]+b["L(pe)"]+b["L(pe, 2)"]
<span style="color: #1E90FF;">'&#35; F test. H0: LRP=0</span>
linearHypothesis(res,"pe + L(pe) + L(pe, 2) = 0")

reg1 <- dynlm(return~L(return)           , data=tsdata) reg2 <- dynlm(return~L(return)+L(return,2)  
    , data=tsdata)
340
R Scripts
## Script 10.7: Example-10-7.R
library(dynlm);library(stargazer)
data(hseinv, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define Yearly time series beginning in 1947</span>
tsdata <- ts(hseinv, start=1947)
<span style="color: #1E90FF;">'&#35; Linear regression of model with lags:</span>
res1 <- dynlm(log(invpc) ~ log(price)
, data=tsdata)
res2 <- dynlm(log(invpc) ~ log(price) + trend(tsdata), data=tsdata)
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(res1,res2, type="text")
## Script 10.8: Example-10-11.R
library(dynlm);library(lmtest)
data(barium, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define monthly time series beginning in Feb. 1978</span>
tsdata <- ts(barium, start=c(1978,2), frequency=12)
res <- dynlm(log(chnimp) ~ log(chempi)+log(gas)+log(rtwex)+befile6+
affile6+afdec6+ season(tsdata) , data=tsdata )
coeftest(res)
# 11. Scripts Used in Chapter 11
## Script 11.1: Example-11-4.R
library(dynlm);library(stargazer)
data(nyse, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define time series (numbered 1,...,n)</span>
tsdata <- ts(nyse)
<span style="color: #1E90FF;">'&#35; Linear regression of models with lags:</span>
reg3 <- dynlm(return~L(return)+L(return,2)+L(return,3), data=tsdata)
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(reg1, reg2, reg3, type="text",
keep.stat=c("n","rsq","adj.rsq","f"))
## Script 11.2: Example-EffMkts.R
library(zoo);library(quantmod);library(dynlm);library(stargazer)
<span style="color: #1E90FF;">'&#35; Download data using the quantmod package:</span>
getSymbols("AAPL", auto.assign = TRUE)
<span style="color: #1E90FF;">'&#35; Calculate return as the log difference</span>
ret <- diff( log(AAPL$AAPL.Adjusted) )
<span style="color: #1E90FF;">'&#35; Subset 2008-2016 by special xts indexing:</span>
ret <- ret["2008/2016"]
<span style="color: #1E90FF;">'&#35; Plot returns</span>

11. Scripts Used in Chapter 11
341
plot(ret)
<span style="color: #1E90FF;">'&#35; Linear regression of models with lags:</span>
ret <- as.zoo(ret)
<span style="color: #1E90FF;">'&#35; dynlm cannot handle xts objects</span>
reg1 <- dynlm(ret~L(ret) )
reg2 <- dynlm(ret~L(ret)+L(ret,2) )
reg3 <- dynlm(ret~L(ret)+L(ret,2)+L(ret,3) )
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(reg1, reg2, reg3, type="text",
keep.stat=c("n","rsq","adj.rsq","f"))
## Script 11.3: Simulate-RandomWalk.R
<span style="color: #1E90FF;">'&#35; Initialize Random Number Generator</span>
set.seed(348546)
<span style="color: #1E90FF;">'&#35; initial graph</span>
plot(c(0,50),c(0,0),type="l",lwd=2,ylim=c(-18,18))
<span style="color: #1E90FF;">'&#35; loop over draws:</span>
for(r in 1:30) {
<span style="color: #1E90FF;">'&#35; i.i.d. standard normal shock</span>
e <- rnorm(50)
<span style="color: #1E90FF;">'&#35; Random walk as cumulative sum of shocks</span>
y <- ts(cumsum(e))
<span style="color: #1E90FF;">'&#35; Add line to graph</span>
lines(y, col=gray(.6))
}
## Script 11.4: Simulate-RandomWalkDrift.R
<span style="color: #1E90FF;">'&#35; Initialize Random Number Generator</span>
set.seed(348546)
<span style="color: #1E90FF;">'&#35; initial empty graph with expected value</span>
plot(c(0,50),c(0,100),type="l",lwd=2)
<span style="color: #1E90FF;">'&#35; loop over draws:</span>
for(r in 1:30) {
<span style="color: #1E90FF;">'&#35; i.i.d. standard normal shock</span>
e <- rnorm(50)
<span style="color: #1E90FF;">'&#35; Random walk as cumulative sum of shocks</span>
y <- ts(cumsum(2+e))
<span style="color: #1E90FF;">'&#35; Add line to graph</span>
lines(y, col=gray(.6))
}
## Script 11.5: Simulate-RandomWalkDrift-Diff.R
<span style="color: #1E90FF;">'&#35; Initialize Random Number Generator</span>
set.seed(348546)
<span style="color: #1E90FF;">'&#35; initial empty graph with expected value</span>
plot(c(0,50),c(2,2),type="l",lwd=2,ylim=c(-1,5))
<span style="color: #1E90FF;">'&#35; loop over draws:</span>
for(r in 1:30) {
<span style="color: #1E90FF;">'&#35; i.i.d. standard normal shock</span>
e <- rnorm(50)
<span style="color: #1E90FF;">'&#35; Random walk as cumulative sum of shocks</span>
y <- ts(cumsum(2+e))
<span style="color: #1E90FF;">'&#35; First difference</span>

342
R Scripts
Dy <- diff(y)
<span style="color: #1E90FF;">'&#35; Add line to graph</span>
lines(Dy, col=gray(.6))
}
## Script 11.6: Example-11-6.R
<span style="color: #1E90FF;">'&#35; Libraries for dynamic lm and "stargazer" regression table</span>
library(dynlm);library(stargazer)
data(fertil3, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define Yearly time series beginning in 1913</span>
tsdata <- ts(fertil3, start=1913)
<span style="color: #1E90FF;">'&#35; Linear regression of model with first differences:</span>
res1 <- dynlm( d(gfr) ~ d(pe), data=tsdata)
<span style="color: #1E90FF;">'&#35; Linear regression of model with lagged differences:</span>
res2 <- dynlm( d(gfr) ~ d(pe) + L(d(pe)) + L(d(pe),2), data=tsdata)
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(res1,res2,type="text")
# 12. Scripts Used in Chapter 12
## Script 12.1: Example-12-2.R
library(dynlm);library(lmtest)
data(phillips, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define Yearly time series beginning in 1948</span>
tsdata <- ts(phillips, start=1948)
<span style="color: #1E90FF;">'&#35; Estimation of static Phillips curve:</span>
reg.s <- dynlm( inf ~ unem, data=tsdata, end=1996)
<span style="color: #1E90FF;">'&#35; residuals and AR(1) test:</span>
residual.s <- resid(reg.s)
coeftest( dynlm(residual.s ~ L(residual.s)) )
<span style="color: #1E90FF;">'&#35; Same with expectations-augmented Phillips curve:</span>
reg.ea <- dynlm( d(inf) ~ unem, data=tsdata, end=1996)
residual.ea <- resid(reg.ea)
coeftest( dynlm(residual.ea ~ L(residual.ea)) )
## Script 12.2: Example-12-4.R
library(dynlm);library(car);library(lmtest)
data(barium, package=’wooldridge’)
tsdata <- ts(barium, start=c(1978,2), frequency=12)
reg <- dynlm(log(chnimp)~log(chempi)+log(gas)+log(rtwex)+
befile6+affile6+afdec6, data=tsdata )
<span style="color: #1E90FF;">'&#35; Pedestrian test:</span>
residual <- resid(reg)
resreg <- dynlm(residual ~ L(residual)+L(residual,2)+L(residual,3)+
log(chempi)+log(gas)+log(rtwex)+befile6+

12. Scripts Used in Chapter 12
343
affile6+afdec6, data=tsdata )
linearHypothesis(resreg,
c("L(residual)","L(residual, 2)","L(residual, 3)"))
<span style="color: #1E90FF;">'&#35; Automatic test:</span>
bgtest(reg, order=3, type="F")
## Script 12.3: Example-DWtest.R
library(dynlm);library(lmtest)
data(phillips, package=’wooldridge’)
tsdata <- ts(phillips, start=1948)
<span style="color: #1E90FF;">'&#35; Estimation of both Phillips curve models:</span>
reg.s <- dynlm( inf ~ unem, data=tsdata, end=1996)
reg.ea <- dynlm( d(inf) ~ unem, data=tsdata, end=1996)
<span style="color: #1E90FF;">'&#35; DW tests</span>
dwtest(reg.s)
dwtest(reg.ea)
## Script 12.4: Example-12-5.R
library(dynlm);library(car);library(orcutt)
data(barium, package=’wooldridge’)
tsdata <- ts(barium, start=c(1978,2), frequency=12)
<span style="color: #1E90FF;">'&#35; OLS estimation</span>
olsres <- dynlm(log(chnimp)~log(chempi)+log(gas)+log(rtwex)+
befile6+affile6+afdec6, data=tsdata)
<span style="color: #1E90FF;">'&#35; Cochrane-Orcutt estimation</span>
cochrane.orcutt(olsres)
## Script 12.5: Example-12-1.R
library(dynlm);library(lmtest);library(sandwich)
data(prminwge, package=’wooldridge’)
tsdata <- ts(prminwge, start=1950)
<span style="color: #1E90FF;">'&#35; OLS regression</span>
reg<-dynlm(log(prepop)~log(mincov)+log(prgnp)+log(usgnp)+trend(tsdata),
data=tsdata )
<span style="color: #1E90FF;">'&#35; results with usual SE</span>
coeftest(reg)
<span style="color: #1E90FF;">'&#35; results with HAC SE</span>
coeftest(reg, vcovHAC)
## Script 12.6: Example-12-9.R
library(dynlm);library(lmtest)
data(nyse, package=’wooldridge’)
tsdata <- ts(nyse)
<span style="color: #1E90FF;">'&#35; Linear regression of model:</span>
reg <- dynlm(return ~ L(return), data=tsdata)

344
R Scripts
<span style="color: #1E90FF;">'&#35; squared residual</span>
residual.sq <- resid(reg)^2
<span style="color: #1E90FF;">'&#35; Model for squared residual:</span>
ARCHreg <- dynlm(residual.sq ~ L(residual.sq))
coeftest(ARCHreg)
## Script 12.7: Example-ARCH.R
library(zoo);library(quantmod);library(dynlm);library(stargazer)
<span style="color: #1E90FF;">'&#35; Download data using the quantmod package:</span>
getSymbols("AAPL", auto.assign = TRUE)
<span style="color: #1E90FF;">'&#35; Calculate return as the log difference</span>
ret <- diff( log(AAPL$AAPL.Adjusted) )
<span style="color: #1E90FF;">'&#35; Subset 2008-2016 by special xts indexing:</span>
ret <- ret["2008/2016"]
<span style="color: #1E90FF;">'&#35; AR(1) model for returns</span>
ret <- as.zoo(ret)
reg <- dynlm( ret ~ L(ret) )
<span style="color: #1E90FF;">'&#35; squared residual</span>
residual.sq <- resid(reg)^2
<span style="color: #1E90FF;">'&#35; Model for squared residual:</span>
ARCHreg <- dynlm(residual.sq ~ L(residual.sq))
summary(ARCHreg)
# 13. Scripts Used in Chapter 13
## Script 13.1: Example-13-2.R
data(cps78_85, package=’wooldridge’) # ==alternative : charger wooldridge puis apper cps 78_85==
<span style="color: #1E90FF;">'&#35; Detailed OLS results including interaction terms</span>
summary( lm(lwage ~ y85*(educ+female)
+exper+ I((exper^2)/100) + union,
data=cps78_85) )
## Script 13.2: Example-13-3-1.R
data(kielmc, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Separate regressions for 1978 and 1981: report coeeficients only</span>
coef( lm(rprice~nearinc, data=kielmc, subset=(year== 1978)) )
coef( lm(rprice~nearinc, data=kielmc, subset=(year== 1981)) )
<span style="color: #1E90FF;">'&#35; Joint regression including an interaction term</span>
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
<span style="color: #1E90FF;">'&#35; Define panel data frame</span>
crime2.p <- pdata.frame(crime2, index=46 )
<span style="color: #1E90FF;">'&#35; Panel dimensions:</span>
pdim(crime2.p)
<span style="color: #1E90FF;">'&#35; Observation 1-6: new "id" and "time" and some other variables:</span>
crime2.p[1:6,c("id","time","year","pop","crimes","crmrte","unem")]
## Script 13.5: Example-PLM-Calcs.R
library(plm)
data(crime4, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
crime4.p <- pdata.frame(crime4, index=c("county","year") )
<span style="color: #1E90FF;">'&#35; Calculations within the pdata.frame:</span>
crime4.p$cr.l <- lag(crime4.p$crmrte)
crime4.p$cr.d <- diff(crime4.p$crmrte)
crime4.p$cr.B <- Between(crime4.p$crmrte)
crime4.p$cr.W <- Within(crime4.p$crmrte)
<span style="color: #1E90FF;">'&#35; Display selected variables for observations 1-16:</span>
crime4.p[1:16,c("county","year","crmrte","cr.l","cr.d","cr.B","cr.W")]
## Script 13.6: Example-FD.R
library(plm); library(lmtest)
data(crime2, package=’wooldridge’)
crime2.p <- pdata.frame(crime2, index=46 )
<span style="color: #1E90FF;">'&#35; manually calculate first differences:</span>
crime2.p$dyear
<- diff(crime2.p$year)
crime2.p$dcrmrte <- diff(crime2.p$crmrte)
crime2.p$dunem
<- diff(crime2.p$unem)
<span style="color: #1E90FF;">'&#35; Display selected variables for observations 1-6:</span>
crime2.p[1:6,c("id","time","year","dyear","crmrte","dcrmrte","unem","dunem")]
<span style="color: #1E90FF;">'&#35; Estimate FD model with lm on differenced data:</span>
coeftest( lm(dcrmrte~dunem, data=crime2.p) )
<span style="color: #1E90FF;">'&#35; Estimate FD model with plm on original data:</span>
coeftest( plm(crmrte~unem, data=crime2.p, model="fd") )
## Script 13.7: Example-13-9.R
library(plm);library(lmtest)
data(crime4, package=’wooldridge’)
crime4.p <- pdata.frame(crime4, index=c("county","year") )
pdim(crime4.p)
<span style="color: #1E90FF;">'&#35; manually calculate first differences of crime rate:</span>

346
R Scripts
crime4.p$dcrmrte <- diff(crime4.p$crmrte)
<span style="color: #1E90FF;">'&#35; Display selected variables for observations 1-9:</span>
crime4.p[1:9, c("county","year","crmrte","dcrmrte")]
<span style="color: #1E90FF;">'&#35; Estimate FD model:</span>
coeftest( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+
lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
# 14. Scripts Used in Chapter 14
## Script 14.1: Example-14-2.R
library(plm)
data(wagepan, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
pdim(wagepan.p)
<span style="color: #1E90FF;">'&#35; Estimate FE model</span>
summary( plm(lwage~married+union+factor(year)*educ,
data=wagepan.p, model="within") )
## Script 14.2: Example-14-4-1.R
library(plm);library(stargazer)
data(wagepan, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
pdim(wagepan.p)
<span style="color: #1E90FF;">'&#35; Check variation of variables within individuals</span>
pvar(wagepan.p)
## Script 14.3: Example-14-4-2.R
<span style="color: #1E90FF;">'&#35; Estimate different models</span>
wagepan.p$yr<-factor(wagepan.p$year)
reg.ols<- (plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
data=wagepan.p, model="pooling") )
reg.re <- (plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
data=wagepan.p, model="random") )
reg.fe <- (plm(lwage~
I(exper^2)+married+union+yr,
data=wagepan.p, model="within") )
<span style="color: #1E90FF;">'&#35; Pretty table of selected results (not reporting year dummies)</span>
stargazer(reg.ols,reg.re,reg.fe, type="text",
column.labels=c("OLS","RE","FE"),keep.stat=c("n","rsq"),
keep=c("ed","bl","hi","exp","mar","un"))

14. Scripts Used in Chapter 14
347
## Script 14.4: Example-HausmTest.R
<span style="color: #1E90FF;">'&#35; Note that the estimates "reg.fe" and "reg.re" are calculated in</span>
<span style="color: #1E90FF;">'&#35; Example 14.4. The scripts have to be run first.</span>
<span style="color: #1E90FF;">'&#35; Hausman test of RE vs. FE:</span>
phtest(reg.fe, reg.re)
## Script 14.5: Example-Dummy-CRE-1.R
library(plm);library(stargazer)
data(wagepan, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
<span style="color: #1E90FF;">'&#35; Estimate FE parameter in 3 different ways:</span>
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
<span style="color: #1E90FF;">'&#35; Note that the estimates "reg.cre" are calculated in</span>
# ## Script "Example-Dummy-CRE-1.R" which has to be run first.
<span style="color: #1E90FF;">'&#35; RE test as an F test on the "Between" coefficients</span>
library(car)
linearHypothesis(reg.cre, matchCoefs(reg.cre,"Between"))
## Script 14.8: Example-CRE2.R
library(plm)
data(wagepan, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
<span style="color: #1E90FF;">'&#35; Estimate CRE parameters</span>
wagepan.p$yr<-factor(wagepan.p$year)
summary(plm(lwage~married+union+educ+black+hisp+Between(married)+
Between(union), data=wagepan.p, model="random"))
## Script 14.9: Example-13-9-ClSE.R
library(plm);library(lmtest)
data(crime4, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Generate pdata.frame:</span>
crime4.p <- pdata.frame(crime4, index=c("county","year") )
<span style="color: #1E90FF;">'&#35; Estimate FD model:</span>
reg <- ( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+

348
R Scripts
lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
<span style="color: #1E90FF;">'&#35; Regression table with standard SE</span>
coeftest(reg)
<span style="color: #1E90FF;">'&#35; Regression table with "clustered" SE (default type HC0):</span>
coeftest(reg, vcovHC)
<span style="color: #1E90FF;">'&#35; Regression table with "clustered" SE (small-sample correction)</span>
<span style="color: #1E90FF;">'&#35; This is the default version used by Stata and reported by Wooldridge:</span>
coeftest(reg, vcovHC(reg, type="sss"))
# 15. Scripts Used in Chapter 15
## Script 15.1: Example-15-1.R
library(AER);library(stargazer)
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; restrict to non-missing wage observations</span>
oursample <- subset(mroz, !is.na(wage))
<span style="color: #1E90FF;">'&#35; OLS slope parameter manually</span>
with(oursample, cov(log(wage),educ) / var(educ) )
<span style="color: #1E90FF;">'&#35; IV slope parameter manually</span>
with(oursample, cov(log(wage),fatheduc) / cov(educ,fatheduc) )
<span style="color: #1E90FF;">'&#35; OLS automatically</span>
reg.ols <-
lm(log(wage) ~ educ, data=oursample)
<span style="color: #1E90FF;">'&#35; IV automatically</span>
reg.iv <- ivreg(log(wage) ~ educ | fatheduc, data=oursample)
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(reg.ols,reg.iv, type="text")
## Script 15.2: Example-15-4.R
library(AER);library(stargazer)
data(card, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Checking for relevance: reduced form</span>
redf<-lm(educ ~ nearc4+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
<span style="color: #1E90FF;">'&#35; OLS</span>
ols<-lm(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
<span style="color: #1E90FF;">'&#35; IV estimation</span>
iv <-ivreg(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+
reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
| nearc4+exper+I(exper^2)+black+smsa+south+smsa66+
reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
, data=card)
<span style="color: #1E90FF;">'&#35; Pretty regression table of selected coefficients</span>
stargazer(redf,ols,iv,type="text",
keep=c("ed","near","exp","bl"),keep.stat=c("n","rsq"))

15. Scripts Used in Chapter 15
349
## Script 15.3: Example-15-5.R
library(AER);library(stargazer)
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; restrict to non-missing wage observations</span>
oursample <- subset(mroz, !is.na(wage))
<span style="color: #1E90FF;">'&#35; 1st stage: reduced form</span>
stage1 <- lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
<span style="color: #1E90FF;">'&#35; 2nd stage</span>
man.2SLS<-lm(log(wage)~fitted(stage1)+exper+I(exper^2), data=oursample)
<span style="color: #1E90FF;">'&#35; Automatic 2SLS estimation</span>
aut.2SLS<-ivreg(log(wage)~educ+exper+I(exper^2)
| motheduc+fatheduc+exper+I(exper^2) , data=oursample)
<span style="color: #1E90FF;">'&#35; Pretty regression table</span>
stargazer(stage1,man.2SLS,aut.2SLS,type="text",keep.stat=c("n","rsq"))
## Script 15.4: Example-15-7.R
library(AER);library(lmtest)
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; restrict to non-missing wage observations</span>
oursample <- subset(mroz, !is.na(wage))
<span style="color: #1E90FF;">'&#35; 1st stage: reduced form</span>
stage1<-lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
<span style="color: #1E90FF;">'&#35; 2nd stage</span>
stage2<-lm(log(wage)~educ+exper+I(exper^2)+resid(stage1),data=oursample)
<span style="color: #1E90FF;">'&#35; results including t tests</span>
coeftest(stage2)
## Script 15.5: Example-15-8.R
library(AER)
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; restrict to non-missing wage observations</span>
oursample <- subset(mroz, !is.na(wage))
<span style="color: #1E90FF;">'&#35; IV regression</span>
summary( res.2sls <- ivreg(log(wage) ~ educ+exper+I(exper^2)
| exper+I(exper^2)+motheduc+fatheduc,data=oursample) )
<span style="color: #1E90FF;">'&#35; Auxiliary regression</span>
res.aux <-
lm(resid(res.2sls) ~ exper+I(exper^2)+motheduc+fatheduc
, data=oursample)
<span style="color: #1E90FF;">'&#35; Calculations for test</span>
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
<span style="color: #1E90FF;">'&#35; Define panel data (for 1987 and 1988 only)</span>
jtrain.87.88 <- subset(jtrain,year<=1988)
jtrain.p<-pdata.frame(jtrain.87.88, index=c("fcode","year"))
<span style="color: #1E90FF;">'&#35; IV FD regression</span>
summary( plm(log(scrap)~hrsemp|grant, model="fd",data=jtrain.p) )
# 16. Scripts Used in Chapter 16
## Script 16.1: Example-16-5-ivreg.R
library(AER)
data(mroz, package=’wooldridge’)
oursample <- subset(mroz,!is.na(wage))
<span style="color: #1E90FF;">'&#35; 2SLS regressions</span>
summary( ivreg(hours~log(wage)+educ+age+kidslt6+nwifeinc
|educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
summary( ivreg(log(wage)~hours+educ+exper+I(exper^2)
|educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
## Script 16.2: Example-16-5-systemfit-prep.R
library(systemfit)
data(mroz, package=’wooldridge’)
oursample <- subset(mroz,!is.na(wage))
<span style="color: #1E90FF;">'&#35; Define system of equations and instruments</span>
## Script 16.3: Example-16-5-systemfit.R
<span style="color: #1E90FF;">'&#35; 2SLS of whole system (run Example-16-5-systemfit-prep.R first!)</span>
summary(systemfit(eq.system,inst=instrum,data=oursample,method="2SLS"))
## Script 16.4: Example-16-5-3sls.R
<span style="color: #1E90FF;">'&#35; 3SLS of whole system (run Example-16-5-systemfit-prep.R first!)</span>
summary(systemfit(eq.system,inst=instrum,data=oursample,method="3SLS"))
# 17. Scripts Used in Chapter 17
## Script 17.1: Example-17-1-1.R
library(car); library(lmtest)
<span style="color: #1E90FF;">'&#35; for robust SE</span>
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate linear probability model</span>
linprob <- lm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,data=mroz)
<span style="color: #1E90FF;">'&#35; Regression table with heteroscedasticity-robust SE and t tests:</span>
coeftest(linprob,vcov=hccm)

17. Scripts Used in Chapter 17
351
## Script 17.2: Example-17-1-2.R
<span style="color: #1E90FF;">'&#35; predictions for two "extreme" women (run Example-17-1-1.R first!):</span>
xpred <- list(nwifeinc=c(100,0),educ=c(5,17),exper=c(0,30),
age=c(20,52),kidslt6=c(2,0),kidsge6=c(0,0))
predict(linprob,xpred)
## Script 17.3: Example-17-1-3.R
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate logit model</span>
logitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
family=binomial(link=logit),data=mroz)
<span style="color: #1E90FF;">'&#35; Summary of results:</span>
summary(logitres)
<span style="color: #1E90FF;">'&#35; Log likelihood value:</span>
logLik(logitres)
<span style="color: #1E90FF;">'&#35; McFadden’s pseudo R2:</span>
1 - logitres$deviance/logitres$null.deviance
## Script 17.4: Example-17-1-4.R
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate probit model</span>
probitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
family=binomial(link=probit),data=mroz)
<span style="color: #1E90FF;">'&#35; Summary of results:</span>
summary(probitres)
<span style="color: #1E90FF;">'&#35; Log likelihood value:</span>
logLik(probitres)
<span style="color: #1E90FF;">'&#35; McFadden’s pseudo R2:</span>
1 - probitres$deviance/probitres$null.deviance
## Script 17.5: Example-17-1-5.R
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; Test of overall significance:</span>
<span style="color: #1E90FF;">'&#35; Manual calculation of the LR test statistic:</span>
probitres$null.deviance - probitres$deviance
<span style="color: #1E90FF;">'&#35; Automatic calculations including p-values,...:</span>
library(lmtest)
lrtest(probitres)
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; Test of H0: experience and age are irrelevant</span>
restr <- glm(inlf~nwifeinc+educ+ kidslt6+kidsge6,
family=binomial(link=probit),data=mroz)
lrtest(restr,probitres)
## Script 17.6: Example-17-1-6.R
<span style="color: #1E90FF;">'&#35; Predictions from linear probability, probit and logit model:</span>
<span style="color: #1E90FF;">'&#35; (run 17-1-1.R through 17-1-4.R first to define the variables!)</span>
predict(linprob,
xpred,type = "response")
predict(logitres, xpred,type = "response")
predict(probitres,xpred,type = "response")

352
R Scripts
## Script 17.7: Binary-Predictions.R
<span style="color: #1E90FF;">'&#35; Simulated data</span>
set.seed(8237445)
y <- rbinom(100,1,0.5)
x <- rnorm(100) + 2*y
<span style="color: #1E90FF;">'&#35; Estimation</span>
linpr.res <-
lm(y~x)
logit.res <- glm(y~x,family=binomial(link=logit))
probit.res<- glm(y~x,family=binomial(link=probit))
<span style="color: #1E90FF;">'&#35; Prediction for regular grid of x values</span>
xp <- seq(from=min(x),to=max(x),length=50)
linpr.p <- predict( linpr.res, list(x=xp), type="response" )
logit.p <- predict( logit.res, list(x=xp), type="response" )
probit.p<- predict( probit.res,list(x=xp), type="response" )
<span style="color: #1E90FF;">'&#35; Graph</span>
plot(x,y)
lines(xp,linpr.p, lwd=2,lty=1)
lines(xp,logit.p, lwd=2,lty=2)
lines(xp,probit.p,lwd=1,lty=1)
legend("topleft",c("linear prob.","logit","probit"),
lwd=c(2,2,1),lty=c(1,2,1))
## Script 17.8: Binary-Margeff.R
<span style="color: #1E90FF;">'&#35; Calculate partial effects</span>
linpr.eff <- coef(linpr.res)["x"]
*
rep(1,100)
logit.eff <- coef(logit.res)["x"]
*
dlogis(predict(logit.res))
probit.eff <- coef(probit.res)["x"]
*
dnorm(predict(probit.res))
<span style="color: #1E90FF;">'&#35; Graph</span>
plot(
x,linpr.eff, pch=1,ylim=c(0,.7),ylab="partial effect")
points(x,logit.eff, pch=3)
points(x,probit.eff,pch=18)
legend("topright",c("linear prob.","logit","probit"),pch=c(1,3,18))
## Script 17.9: Example-17-1-7.R
<span style="color: #1E90FF;">'&#35; APEs (run 17-1-1.R through 17-1-4.R first to define the variables!)</span>
<span style="color: #1E90FF;">'&#35; Calculation of linear index at individual values:</span>
xb.log <- predict(logitres)
xb.prob<- predict(probitres)
<span style="color: #1E90FF;">'&#35; APE factors = average(g(xb))</span>
factor.log <- mean( dlogis(xb.log) )
factor.prob<- mean( dnorm(xb.prob) )
cbind(factor.log,factor.prob)
<span style="color: #1E90FF;">'&#35; average partial effects = beta*factor:</span>
APE.lin <- coef(linprob)
*
1
APE.log <- coef(logitres)
*
factor.log
APE.prob<- coef(probitres)
*
factor.prob
<span style="color: #1E90FF;">'&#35; Table of APEs</span>
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
<span style="color: #1E90FF;">'&#35; Automatic APE calculations with package mfx</span>
library(mfx)
logitmfx(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
data=mroz, atmean=FALSE)
## Script 17.11: Example-17-3-1.R
data(crime1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate linear model</span>
lm.res
<-
lm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1)
<span style="color: #1E90FF;">'&#35; Estimate Poisson model</span>
Poisson.res <- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1, family=poisson)
<span style="color: #1E90FF;">'&#35; Quasi-Poisson model</span>
QPoisson.res<- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
black+hispan+born60, data=crime1, family=quasipoisson)
## Script 17.12: Example-17-3-2.R
<span style="color: #1E90FF;">'&#35; Example 17.3: Regression table (run Example-17-3-1.R first!)</span>
library(stargazer) '# package for regression output
stargazer(lm.res,Poisson.res,QPoisson.res,type="text",keep.stat="n")
## Script 17.13: Tobit-CondMean.R
<span style="color: #1E90FF;">'&#35; Simulated data</span>
set.seed(93876553)
y[ystar<0]<- 0
<span style="color: #1E90FF;">'&#35; Conditional means</span>
Eystar <- xb
Ey <- pnorm(xb/1)*xb+1*dnorm(xb/1)
<span style="color: #1E90FF;">'&#35; Graph</span>
plot(x,ystar,ylab="y", pch=3)
points(x,y, pch=1)
lines(x,Eystar, lty=2,lwd=2)
legend("topleft",c(expression(y^"*"),"y",expression(E(y^"*")),"E(y)"),
lty=c(NA,NA,2,1),pch=c(3,1,NA,NA),lwd=c(1,1,2,2))
## Script 17.14: Example-17-2.R
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate Tobit model using censReg:</span>
library(censReg)
TobitRes <- censReg(hours~nwifeinc+educ+exper+I(exper^2)+
age+kidslt6+kidsge6, data=mroz )
summary(TobitRes)
<span style="color: #1E90FF;">'&#35; Partial Effects at the average x:</span>
margEff(TobitRes)

pred.OLS  <- predict(   lm(y~x, data=sample) ) pred.trunc <- predict( truncreg(y~x, data=sample) )
<span style="color: #1E90FF;">'&#35; Graph</span>
plot(  compl$x, compl$y, pch= 1,xlab="x",ylab="y") points(sample$x,sample$y, pch=16)
lines( sample$x,pred.OLS, lty=2,lwd=2) lines( sample$x,pred.trunc,lty=1,lwd=2)
abline(h=0,lty=3)   '# horizontal line at 0
354
R Scripts
## Script 17.15: Example-17-2-survreg.R
<span style="color: #1E90FF;">'&#35; Estimate Tobit model using survreg:</span>
library(survival)
res <- survreg(Surv(hours, hours>0, type="left") ~ nwifeinc+educ+exper+
I(exper^2)+age+kidslt6+kidsge6, data=mroz, dist="gaussian")
summary(res)
## Script 17.16: Example-17-4.R
library(survival)
data(recid, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Define Dummy for UNcensored observations</span>
recid$ uncensored <- recid$ cens==  0
<span style="color: #1E90FF;">'&#35; Estimate censored regression model:</span>
res<-survreg(Surv(log(durat),uncensored, type="right") ~ workprg+priors+
tserved+felon+alcohol+drugs+black+married+educ+age,
data=recid, dist="gaussian")
<span style="color: #1E90FF;">'&#35; Output:</span>
summary(res)
## Script 17.17: TruncReg-Simulation.R
library(truncreg)
<span style="color: #1E90FF;">'&#35; Simulated data</span>
set.seed(93876553)
x
<- sort(rnorm(100)+4)
y
<- -4 + 1*x
+ rnorm(100)
<span style="color: #1E90FF;">'&#35; complete observations and observed sample:</span>
compl <- data.frame(x,y)
sample <- subset(compl, y>0)
<span style="color: #1E90FF;">'&#35; Predictions</span>
legend("topleft", c("all points","observed points","OLS fit",
"truncated regression"),
lty=c(NA,NA,2,1),pch=c(1,16,NA,NA),lwd=c(1,1,2,2))
## Script 17.18: Example-17-5.R
library(sampleSelection)
data(mroz, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Estimate Heckman selection model (2 step version)</span>
res<-selection(inlf~educ+exper+I(exper^2)+nwifeinc+age+kidslt6+kidsge6,
log(wage)~educ+exper+I(exper^2), data=mroz, method="2step" )
<span style="color: #1E90FF;">'&#35; Summary of results:</span>
summary(res)

# 18. Scripts Used in Chapter 18
355
19. Scripts Used in Chapter 18
## Script 18.1: Example-18-1.R
library(dynlm); library(stargazer)
data(hseinv, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; detrended variable: residual from a regression on the obs. index:</span>
trendreg <- dynlm( log(invpc) ~ trend(hseinv), data=hseinv )
hseinv$linv.detr <-
resid( trendreg )
<span style="color: #1E90FF;">'&#35; ts data:</span>
hseinv.ts <- ts(hseinv)
<span style="color: #1E90FF;">'&#35; Koyck geometric d.l.:</span>
gDL<-dynlm(linv.detr~gprice + L(linv.detr)
,data=hseinv.ts)
<span style="color: #1E90FF;">'&#35; rational d.l.:</span>
rDL<-dynlm(linv.detr~gprice + L(linv.detr) + L(gprice),data=hseinv.ts)
stargazer(gDL,rDL, type="text", keep.stat=c("n","adj.rsq"))
<span style="color: #1E90FF;">'&#35; LRP geometric DL:</span>
b <- coef(gDL)
b["gprice"]
/ (1-b["L(linv.detr)"])
<span style="color: #1E90FF;">'&#35; LRP rationalDL:</span>
b <- coef(rDL)
(b["gprice"]+b["L(gprice)"]) / (1-b["L(linv.detr)"])
## Script 18.2: Example-18-4.R
library(dynlm)
data(inven, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; variable to test: y=log(gdp)</span>
inven$y <- log(inven$gdp)
inven.ts<- ts(inven)
<span style="color: #1E90FF;">'&#35; summary output of ADF regression:</span>
summary(dynlm( d(y) ~ L(y) + L(d(y)) + trend(inven.ts), data=inven.ts))
<span style="color: #1E90FF;">'&#35; automated ADF test using tseries:</span>
library(tseries)
adf.test(inven$y, k=1)
## Script 18.3: Example-18-4-urca.R
library(urca)
data(inven, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; automated ADF test using urca:</span>
summary( ur.df(log(inven$gdp) , type = c("trend"), lags = 1) )
## Script 18.4: Simulate-Spurious-Regression-1.R
<span style="color: #1E90FF;">'&#35; Initialize Random Number Generator</span>
set.seed(29846)
<span style="color: #1E90FF;">'&#35; i.i.d. N(0,1) innovations</span>
n <- 50
e <- rnorm(n)
a <- rnorm(n)
<span style="color: #1E90FF;">'&#35; independent random walks</span>

356
R Scripts
x <- cumsum(a)
y <- cumsum(e)
<span style="color: #1E90FF;">'&#35; plot</span>
plot(x,type="l",lty=1,lwd=1)
lines(y
,lty=2,lwd=2)
legend("topright",c("x","y"), lty=c(1,2), lwd=c(1,2))
<span style="color: #1E90FF;">'&#35; Regression of y on x</span>
summary( lm(y~x) )
## Script 18.5: Simulate-Spurious-Regression-2.R
<span style="color: #1E90FF;">'&#35; Initialize Random Number Generator</span>
set.seed(29846)
<span style="color: #1E90FF;">'&#35; generate 10,000 independent random walks</span>
<span style="color: #1E90FF;">'&#35; and store the p val of the t test</span>
pvals <- numeric(10000)
for (r in 1:10000) {
<span style="color: #1E90FF;">'&#35; i.i.d. N(0,1) innovations</span>
n <- 50
a <- rnorm(n)
e <- rnorm(n)
<span style="color: #1E90FF;">'&#35; independent random walks</span>
x <- cumsum(a)
y <- cumsum(e)
<span style="color: #1E90FF;">'&#35; regression summary</span>
regsum <- summary(lm(y~x))
<span style="color: #1E90FF;">'&#35; p value: 2nd row, 4th column of regression table</span>
pvals[r] <- regsum$coef[2,4]
}
<span style="color: #1E90FF;">'&#35; How often is p<5% ?</span>
table(pvals<=0.05)
## Script 18.6: Example-18-8.R
<span style="color: #1E90FF;">'&#35; load updataed data from URfIE Website since online file is incomplete</span>
library(dynlm); library(stargazer)
data(phillips, package=’wooldridge’)
tsdat=ts(phillips, start=1948)
<span style="color: #1E90FF;">'&#35; Estimate models and display results</span>
res1 <- dynlm(unem ~ unem_1
, data=tsdat, end=1996)
res2 <- dynlm(unem ~ unem_1+inf_1, data=tsdat, end=1996)
stargazer(res1, res2 ,type="text", keep.stat=c("n","adj.rsq","ser"))
<span style="color: #1E90FF;">'&#35; Predictions for 1997-2003 including 95% forecast intervals:</span>
predict(res1, newdata=window(tsdat,start=1997), interval="prediction")
predict(res2, newdata=window(tsdat,start=1997), interval="prediction")
## Script 18.7: Example-18-9.R
<span style="color: #1E90FF;">'&#35; Note: run Example-18-8.R first to generate the results res1 and res2</span>
<span style="color: #1E90FF;">'&#35; Actual unemployment and forecasts:</span>
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
<span style="color: #1E90FF;">'&#35; Plot unemployment and forecasts:</span>
matplot(time(y), cbind(y,f1,f2), type="l",
col="black",lwd=2,lty=1:3)
legend("topleft",c("Unempl.","Forecast 1","Forecast 2"),lwd=2,lty=1:3)
<span style="color: #1E90FF;">'&#35; Forecast errors:</span>
e1<- y - f1
e2<- y - f2
<span style="color: #1E90FF;">'&#35; RMSE:</span>
sqrt(mean(e1^2))
sqrt(mean(e2^2))
<span style="color: #1E90FF;">'&#35; MAE:</span>
mean(abs(e1))
mean(abs(e2))
19. Scripts Used in Chapter 19
## Script 19.1: ultimate-calcs.R
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; Project X:</span>
<span style="color: #1E90FF;">'&#35; "The Ultimate Question of Life, the Universe, and Everything"</span>
<span style="color: #1E90FF;">'&#35; Project Collaborators: Mr. X, Mrs. Y</span>
<span style="color: #1E90FF;">'&#35;</span>
<span style="color: #1E90FF;">'&#35; R ## Script "ultimate-calcs"</span>
<span style="color: #1E90FF;">'&#35; by: F Heiss</span>
<span style="color: #1E90FF;">'&#35; Date of this version: February 08, 2016</span>
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; The main calculation using the method "square root"</span>
<span style="color: #1E90FF;">'&#35; (http://mathworld.wolfram.com/SquareRoot.html)</span>
sqrt(1764)
## Script 19.2: projecty-master.R
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; Bachelor Thesis Mr. Z</span>
<span style="color: #1E90FF;">'&#35; "Best Practice in Using R Scripts"</span>
<span style="color: #1E90FF;">'&#35;</span>
<span style="color: #1E90FF;">'&#35; R ## Script "master"</span>
<span style="color: #1E90FF;">'&#35; Date of this version: 2020-08-13</span>
<span style="color: #1E90FF;">'&#35;'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#'#</span>
<span style="color: #1E90FF;">'&#35; Some preparations:</span>
setwd(~/bscthesis/r)
rm(list = ls())
<span style="color: #1E90FF;">'&#35; Call R scripts</span>

res1 <- lm(colGPA ~ hsGPA   , data=gpa1) res2 <- lm(colGPA ~    ACT, data=gpa1)
358
R Scripts
## Script 19.3: LaTeXwithR.R
library(stargazer);library(xtable)
data(gpa1, package=’wooldridge’)
<span style="color: #1E90FF;">'&#35; Number of obs.</span>
sink("numb-n.txt"); cat(nrow(gpa1)); sink()
<span style="color: #1E90FF;">'&#35; generate frequency table in file "tab-gender.txt"</span>
gender <- factor(gpa1$male,labels=c("female","male"))
sink("tab-gender.txt")
xtable( table(gender) )
sink()
<span style="color: #1E90FF;">'&#35; calculate OLS results</span>
res3 <- lm(colGPA ~ hsGPA + ACT, data=gpa1)
<span style="color: #1E90FF;">'&#35; write regression table to file "tab-regr.txt"</span>
sink("tab-regr.txt")
stargazer(res1,res2,res3, keep.stat=c("n","rsq"),
type="latex",title="Regression Results",label="t:reg")
sink()
<span style="color: #1E90FF;">'&#35; b1 hat</span>
sink("numb-b1.txt"); cat(round(coef(res1)[2],3)); sink()
<span style="color: #1E90FF;">'&#35; Generate graph as PDF file</span>
pdf(file = "regr-graph.pdf", width = 3, height = 2)
par(mar=c(2,2,1,1))
plot(gpa1$hsGPA, gpa1$colGPA)
abline(res1)
dev.off()
