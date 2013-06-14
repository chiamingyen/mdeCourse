/*
 * =====================================================================================
 *
 *       Filename:  functions.c
 *
 *    Description:  benchmark functions for optimization
 *
 *        Version:  1.0
 *        Created:  05/03/2010 02:51:47 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Nicholas Mancuso (nam), nick.mancuso@gmail.com
 *        Company:  GSU Computer Science Dept
 *
 * =====================================================================================
 */
#include "functions.h"

void 
print_functions(void)
{
	printf("Available functions are: ");
	printf("yang\nakley\nschwefel\nrosenbrock\nmichalewicz");
	printf("easom\ndejung\n");
};

obj_func
get_function(const char *fname)
{
    obj_func func = NULL;
    if (strcmp(fname, "yang") == 0)
    {
        func = &yang;
    }
    else if (strcmp(fname, "akley") == 0)
    {
        func = &akley;
    }
    else if (strcmp(fname, "schwefel") == 0)
    {
        func = &schwefel;
    }
    else if (strcmp(fname, "rosenbrock") ==0)
    {
        func= &rosenbrock;
    }
    else if (strcmp(fname, "michalewicz") == 0)
    {
        func = &michalewicz;
    }
    else if (strcmp(fname, "easom") == 0)
    {
        func = &easom;
    }
    else if (strcmp(fname, "dejung") == 0)
    {
        func = &dejung;
    }
    return func;
};

double
yang(const ffly *fly, const size_t nparams)
{
    double x, y, z;

    x = fly->params[0];
    y = fly->params[1];

    z = exp(-((x - 4) * (x - 4)) - ((y - 4) * (y - 4))) +
        exp(-((x + 4) * (x + 4)) - ((y - 4) * (y - 4))) +
        (2 * (exp(-(x*x) - (y * y)) + exp(-(x*x) - ((y+4) * (y+4)) )));

    return -z;
};

// firefly.exe -n 100 -g 100 -d 2 -m 0.01 -x 10.0
// min 為 1/volume 約為 0.01452, volume 約為 68.853
double
volume(const ffly *fly, const size_t nparams)
{
    double x, y, z;
    double SURFACE=80.0, volume;
    x = fly->params[0];
    y = fly->params[1];

    z =(SURFACE - x*y)/(2.*(x+y));
    volume=x*y*z;
    // 因為 x, y 均不可為 0 因此可以直接將 volume 放至分母?
    return 1/(volume);
};

double
akley(const ffly *fly, const size_t nparams)
{
    unsigned int i = 0;
    double exp1, exp2, frac;
    double sumsq = 0.0, sumcos = 0.0;

    for (i = 0; i < nparams; i++)
    {
        sumsq += pow(fly->params[i], 2.0);
        sumcos += cos(2 * PI * fly->params[i]);
    }
    frac = 1.0 / ((double) nparams);
    exp1 = exp(-0.2 * sqrt(frac * sumsq));
    exp2 = exp(frac * sumcos);

    return (-20 * exp1 - exp2 + 20 + E);
};

double
schwefel(const ffly *fly, const size_t nparams)
{
    unsigned int i = 0;
    const double a = 418.9829;
    double sum = 0.0;

    for (i = 0; i < nparams; i++)
    {
        sum +=  -fly->params[i] * sin(sqrt(fabs(fly->params[i])));
    }

    return (a * ((double)nparams)) + sum;
};
double
rosenbrock(const ffly *fly, const size_t nparams)
{
    unsigned int i = 0;
    double sum = 0.0;
    double part = 0.0;
    double x;
    for (i=0; i < nparams-1; i++)
    {
        x = fly->params[i];

        part = (fly->params[i+1] - (x * x));
        part *= part;
        sum += (100 * part) + ( (1 - x) * (1 - x) );
    }
    return sum;
};

double
michalewicz(const ffly *fly, const size_t nparams)
{
    size_t i = 0;
    const size_t m = 10;
    double x_i = 0.0;
    double sum = 0.0;
    double partial = 0.0;

    for (i = 0; i < nparams; i++)
    {
        x_i = fly->params[i];
        partial = sin((i * (x_i * x_i)) / PI);

        sum += sin(x_i) * pow(partial, 2 * m);
    }
    return -sum;
};

double
easom(const ffly *fly, const size_t nparams)
{

    double x1 = fly->params[0];
    double x2 = fly->params[1];

    double p1 = (x1-PI) * (x1-PI);
    double p2 = (x2-PI) * (x2-PI);

    return -cos(x1) * cos(x2) * exp(-p1 - p2);
};

double
dejung(const ffly *fly, const size_t nparams)
{
    size_t i = 0;
    double sum = 0.0;

    for (i = 0; i < nparams; i++)
    {
        sum += pow(fly->params[i], 2.0);
    }
    return sum;
};

