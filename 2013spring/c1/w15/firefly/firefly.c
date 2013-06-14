#include "firefly.h"

/*
    Static functions not to be used outside of this file
*/

static void move_fflies(ffly_population *pop, const ffly_population *pop_old, obj_func f,
                        double alpha, const double gamma, const double mins[], const double maxs[]);
static int move_fly(ffly *fly, ffly *old, const size_t nparams, double alpha, const double gamma, 
                        const double mins[], const double maxs[]);

static ffly_population* init_fflies(const size_t ncount, const size_t nparams, const double mins[],
                                    const double maxs[], const obj_func f);

static void destroy_fflies(ffly_population *pop);
static void memcpy_fflies(ffly_population *fflies_old, ffly_population *dest);
static void memcpy_ffly(ffly *fly, ffly *dest, size_t nparams);
static void output_points(ffly_population *pop, const char *fname);

static int cmp_flies(const void *fly1,const void *fly2);

static double calc_distance(const ffly *fly, const ffly *fly_old, size_t nparams);
static double std_dev(const ffly_population *pop);
static double delta_mean(const ffly_population *pop, const ffly_population *old);

double drand48(void)
{   // return a random float between 0.0 and 1.0
    return (float) rand() / (float)RAND_MAX;
}
/*
        This creates our firefly population and assigns random positions.
*/
static ffly_population*
init_fflies(const size_t ncount, const size_t nparams, const double mins[], const double maxs[], const obj_func f)
{
    size_t i = 0, j = 0;
    double range = 0.0;
    ffly_population *pop = NULL;

    //create memory chunks for values
    pop = (ffly_population*)malloc(sizeof(ffly_population));
    pop->nfflies = ncount;
    pop->nparams = nparams;
    pop->flies = (ffly*)calloc(ncount, sizeof(ffly));

    range = maxs[0] - mins[0];
    
    //init random positions and set f value
    for (i=0; i < ncount; i++)
    {            
        pop->flies[i].params = (double*)calloc(nparams, sizeof(double));
        for (j=0; j < nparams; j++)
        {
            pop->flies[i].params[j] = drand48()*(maxs[j]-mins[j]) + mins[j];
        }
        pop->flies[i].val = (*f)(&pop->flies[i], nparams);
    }
    return pop;
};

/*

        This is called to free up the population
*/
static void
destroy_fflies(ffly_population *pop)
{
    size_t i = 0;
    for (i = 0; i < pop->nfflies; i++)
    {
        free(pop->flies[i].params);
    }
    free(pop->flies);
    free(pop);

    return;
};

/*

    Use this to copy a set of fireflies to a new set
*/
static void
memcpy_fflies(ffly_population *dest, ffly_population *fflies_old)
{
    size_t i = 0;

    dest->nfflies = fflies_old->nfflies;
    dest->nparams = fflies_old->nparams;

    for (i = 0 ; i < fflies_old->nfflies; i++)
    {
        memcpy_ffly(&dest->flies[i], &fflies_old->flies[i], dest->nparams);
    }
};

static void
memcpy_ffly(ffly *dest, ffly *fly, size_t nparams)
{
    dest->val = fly->val;
    memcpy(dest->params, fly->params, sizeof(double) * nparams);
};

void
ffa(const size_t nfireflies, const size_t niteration, const size_t nparams, const double mins[], const double maxs[],
    obj_func f)
{

    size_t i = 0;
    ffly_population *fflies = NULL;
    ffly_population *fflies_old = NULL;

    const double alpha = ALPHA_ZERO;        //randomness step
    const double gamma = GAMMA / (maxs[0] - mins[0]);   //absorption coefficient

    //initialize our firefly array
    fflies = init_fflies(nfireflies, nparams, mins, maxs, f);

    //initialize our old firefly array
    fflies_old = init_fflies(nfireflies, nparams, mins, maxs, f);

    //output_points(fflies, "start_ffa.dat");
    for (i=0; i < niteration; i++)
    {
        //keep another copy for move function
        memcpy_fflies(fflies_old, fflies);

        //rank our flies
        //qsort(fflies->flies, nfireflies, sizeof(ffly), &cmp_flies);
        
        //move the flies based on attractiveness
        move_fflies(fflies, fflies_old, f, alpha, gamma, mins, maxs);
    }
    //output_points(fflies, "end_ffa.dat");

    destroy_fflies(fflies);
    destroy_fflies(fflies_old);
    return;
};

size_t
test_ffa(const size_t nfireflies, const size_t nparams, const double mins[], const double maxs[],
         obj_func f, double *out)
{
    size_t i = 0;
    ffly_population *fflies = NULL;
    ffly_population *fflies_old = NULL;

    const double alpha = ALPHA_ZERO;        //randomness step
    const double gamma = GAMMA / (maxs[0] - mins[0]);   //absorption coefficient

    //initialize our firefly array
    fflies = init_fflies(nfireflies, nparams, mins, maxs, f);

    //initialize our old firefly array
    fflies_old = init_fflies(nfireflies, nparams, mins, maxs, f);

    //output_points(fflies, "start_ffa.dat");
    do
    {        
        //keep another copy for move function
        memcpy_fflies(fflies_old, fflies);

        //rank our flies
        //qsort(fflies, nfireflies, sizeof(ffly), &cmp_flies);
        
        //move the flies based on attractiveness
        move_fflies(fflies, fflies_old, f, alpha, gamma, mins, maxs);
        i++;
    }while (delta_mean(fflies, fflies_old) > EPSILON);
    
    qsort(fflies->flies, nfireflies, sizeof(ffly), &cmp_flies);
    *out = fflies->flies[0].val;

    output_points(fflies, "end_ffa.dat");

    destroy_fflies(fflies);
    destroy_fflies(fflies_old);

    return i * nfireflies;
};

void
ffasa(const size_t nfireflies, const size_t niteration, const size_t nparams, const double mins[], const double maxs[],
      obj_func f)
{

    size_t i = 2;
    ffly_population *fflies = NULL;
    ffly_population *fflies_old = NULL;

    double alpha = 0.0;
    const double alpha0 = ALPHA_ZERO;       //intial randomness step
    const double gamma = GAMMA / (maxs[0] - mins[0]);   //absorption coefficient

    //initialize our firefly array
    fflies = init_fflies(nfireflies, nparams, mins, maxs, f);

    //initialize our old firefly array
    fflies_old = init_fflies(nfireflies, nparams, mins, maxs, f);

    //output_points(fflies, "start_ffasa.dat");
    for (i=0; i < niteration; i++)
    {
        //keep another copy for move function
        memcpy_fflies(fflies_old, fflies);

        //rank our flies
        //qsort(fflies, nfireflies, sizeof(ffly), &cmp_flies);
        
        //calculate our new alpha
        alpha = alpha0 / log(i);

        //move the flies based on attractiveness
        move_fflies(fflies, fflies_old, f, alpha, gamma, mins, maxs);
    }
    //output_points(fflies, "end_ffasa.dat");

    destroy_fflies(fflies);
    destroy_fflies(fflies_old);
    return;
};

size_t
test_ffasa(const size_t nfireflies, const size_t nparams, const double mins[], const double maxs[],
           obj_func f, double *out)
{

    size_t i = 2;
    ffly_population *fflies = NULL;
    ffly_population *fflies_old = NULL;

    double alpha = 0.0;
    const double alpha0 = ALPHA_ZERO;       //intial randomness step
    const double gamma = GAMMA / (maxs[0] - mins[0]);   //absorption coefficient

    //initialize our firefly array
    fflies = init_fflies(nfireflies, nparams, mins, maxs, f);

    //initialize our old firefly array
    fflies_old = init_fflies(nfireflies, nparams, mins, maxs, f);

    //output_points(fflies, "start_ffasa.dat");
    do
    {
        //keep another copy for move function
        memcpy_fflies(fflies_old, fflies);
        
        //rank our flies
        //qsort(fflies, nfireflies, sizeof(ffly), &cmp_flies);
        
        //calculate our new alpha
        alpha = alpha0 / log(i);

        //move the flies based on attractiveness
        move_fflies(fflies, fflies_old, f, alpha, gamma, mins, maxs);
        i++;
    } while (delta_mean(fflies, fflies_old) > EPSILON);
    //output_points(fflies, "end_ffasa.dat");
    qsort(fflies->flies, nfireflies, sizeof(ffly), &cmp_flies);
    *out = fflies->flies[0].val;

    destroy_fflies(fflies);
    destroy_fflies(fflies_old);

    return (i-2) * nfireflies;
};


/*
        This is what moves our fireflies towards the most attractive flies.
*/
static void
move_fflies(ffly_population *pop, const ffly_population *pop_old, obj_func f,
            double alpha, const double gamma, const double mins[], const double maxs[])
{
    size_t i = 0, j = 0, k = 0;
    int moved = 0;
    const size_t nflies = pop->nfflies;
    const size_t nparams = pop->nparams;

    for (i=0; i < nflies; i++)
    {   	    
        for (j = 0; j < nflies; j++)
        {
            moved |= move_fly(&pop->flies[i], &pop_old->flies[j], nparams, alpha, gamma, mins, maxs);
        }

        /* we never moved, so move a lil bit randomly*/
        if (!moved)
        {
            double val = 0.0;
            for (k = 0; k < nparams; k++)
            {
                val = pop->flies[i].params[k] + (alpha * (drand48() - 0.5));
                pop->flies[i].params[k] = (val < mins[k]) ? mins[k] : (val > maxs[k]) ? maxs[k] : val;
            }
        }
        moved = 0;
        //re-evaluate our current brightness
        pop->flies[i].val = (*f)(&pop->flies[i], nparams);
    }
};

/*
    This moves an individual fly torwards another
*/
static int 
move_fly(ffly *fly, ffly *old, const size_t nparams,
         const double alpha, const double gamma, const double mins[], const double maxs[])
{
    size_t i = 0;
    int moved = 0;
    const double beta0 = BETA_ZERO;	//base attraction

    if (fly->val > old->val)
    {
        //get the distance to the other fly
        double r = calc_distance(fly, old, nparams);

        //determine attractiveness with air density [gamma]
        double beta = beta0 * exp((-gamma) * pow(r, 2.0));
				beta = (beta < BETA_MIN) ? BETA_MIN : beta;

        //adjust position with a small random step
        for (i = 0; i < nparams; i++)
        {
            double val = fly->params[i] + (beta * (old->params[i] - fly->params[i])) + (alpha * (drand48() - 0.5));

            //keep within bounds
            fly->params[i] = (val < mins[i]) ? mins[i] : (val > maxs[i]) ? maxs[i] : val;
        }
        moved = 1;
    }
    return moved;
};


/*
    Comparison function for sorting our flies
*/
static int 
cmp_flies(const void *fly1, const void *fly2)
{
    ffly *f1 = (ffly*)fly1;
    ffly *f2 = (ffly*)fly2;
    
    return f1->val <= f2->val ? ( f1->val < f2->val ? -1 : 0 ) : 1;
};

/*
    Calculates the euclidean distance of the two vectors
*/
static double
calc_distance(const ffly *fly, const ffly *fly_old, const size_t nparams)
{
    size_t i = 0;
    double aggr = 0.0, dist = 0.0;
    for (i = 0; i < nparams; i++)
    {
        dist = fly->params[i] - fly_old->params[i];
        aggr += pow(dist, 2.0);
    }
    return sqrt(aggr);
};

/*
    writes our points out to a file
*/
static void
output_points(ffly_population *pop, const char *fname)
{

    size_t i = 0, j = 0;
    FILE *file = NULL;

    file = fopen(fname, "wt");
    if (file != NULL)
    {
        for (i = 0; i < pop->nfflies; i++)
        {
            for (j = 0; j < pop->nparams; j++)
            {
                fprintf(file, "%.5lf ", pop->flies[i].params[j]);
            }
            fprintf(file, "\n");
        }
    }
    fclose(file);
};

/*
    returns the std dev of the objective func values
*/
static double
std_dev(const ffly_population *pop)
{
    size_t i = 0;
    double mean = 0.0;
    double sumsq = 0.0;

    for (i = 0; i < pop->nfflies; i++)
    {
        mean += pop->flies[i].val;
    }

    mean /= ((double)pop->nfflies);

    for (i = 0; i < pop->nfflies; i++)
    {
        sumsq += (pop->flies[i].val - mean) * (pop->flies[i].val - mean);
    }

    sumsq /= ((double)pop->nfflies);

    return sqrt(sumsq);
};

/*
    returns the mean of all the deltas for the objective func
*/
static double
delta_mean(const ffly_population *pop, const ffly_population *old)
{
    double sumnew = 0.0;
    double sumold = 0.0;
    size_t i = 0;

    for (i = 0; i < pop->nfflies; i++)
    {
        sumnew += pop->flies[i].val;
        sumold += old->flies[i].val;
    }

    sumnew = sumnew / ((double)pop->nfflies);
    sumold = sumold / ((double)pop->nfflies);
		return fabs(sumnew - sumold);
};


