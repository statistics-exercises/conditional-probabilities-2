# Using conditional probabilities with discrete random variables

In this distribution we are going to sample the distribution sampled by the random variable X that is given below:

![](https://render.githubusercontent.com/render/math?math=P(X=x|Y=y)=k\delta(x-0)\quad\\textrm{if}\quad\y<0\qquad\P(X=x|Y=y)=k\left(1-\frac{1}{y}\right)^{x}\frac{1}{y}\qquad\textrm{otherwise}\qquad\textrm{where}\qquad\P(Y=y)=\binom{n}{y}(1-p)^{n-y}p^y)

In these expressions ![](https://render.githubusercontent.com/render/math?math=\delta(x-0)) is the (so-called) Kronecker delta and k is a constant.  This is a function that is 1 when x=0 and is zero everywhere else.  If y<2 X is thus guaranteed to be 0.  For every other value of y X is a geometric random variable with ![](https://render.githubusercontent.com/render/math?math=p=\frac{1}{y}).  The random variable Y meanwhile is a binomial random variable.   

X has a complicated distribution that we have not studied in this course.  You can see, however, that I have constructed it using conditional probability and the simpler distributions that we have studied extensively in this course. 

Your task is to write a function to generate samples of the random variable X.  This function will be called `gen_x` and it should take two input parameters `n` and `p`.  These are the `n` and `p` values that are used to generate the Y value that appears as a parameter in the (conditional) probability mass function for X.  I would also recommend completing the function called `binomial` and using this function to generate Y values for use in `gen_x`.

As always I have added some code at the end of the exercise to plot the random variables you have generated 
