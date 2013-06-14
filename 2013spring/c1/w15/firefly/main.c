/*
	 Author: Nicholas Mancuso
	 Implementation of the FireFly Algorithm to search for
	 the optimal solution in an n-variable function.
	 Date: 2/4/10
 */

#include <unistd.h>
#include "functions.h"
#include <stdlib.h> // 使用 srand()

#define POP_COUNT 50
#define MAX_GEN 50


void init_params(int argc, char **argv, size_t *npop, size_t *ngen, size_t *ndim, double *min, double *max);
void print_usage(void);

int
main(int argc, char **argv)
{
    double *mins;
    double *maxs;
    double out;
    double min=0.0, max=0.0;
    size_t pop_count = POP_COUNT, max_gen = MAX_GEN;
    size_t i = 0, dimension = 2;
    size_t nffa = 0, nffasa = 0;

    init_params(argc, argv, &pop_count, &max_gen, &dimension, &min, &max);

    //this should change to be some parameter soon...
    //obj_func func = &dejung;
    obj_func func = &volume;

    mins = (double*)calloc(dimension, sizeof(double));
    maxs = (double*)calloc(dimension, sizeof(double));

    for (i=0; i < dimension; i++)
    {
        mins[i] = min;
        maxs[i] = max;
    }

    //initialize our PRNG
    srand(time(NULL));
    
    nffa = test_ffa(pop_count, dimension, mins, maxs, func, &out);
    printf("FF Algo did %ld evaluations, min = %.5lf\n", nffa, out);

    nffasa = test_ffasa(pop_count, dimension, mins, maxs, func, &out);
    printf("Hybrid FF Algo did %ld evaluations, min = %.5lf\n", nffasa, out);

    free(mins);
    free(maxs);

    return EXIT_SUCCESS;
};

void
init_params(int argc, char **argv, size_t *npop, size_t *ngen, size_t *ndim, double *min, double *max)
{
    char c;

    
    while ( (c = getopt(argc, argv, "n:g:d:m:x:h")) != -1)
    {
        switch (c)
        {
        case 'n':
            *npop = atoi(optarg);
            break;
        case 'g':
            *ngen = atoi(optarg);
            break;
        case 'd':
            *ndim = atoi(optarg);
            break;
        case 'm':
            *min = atof(optarg);
            break;
        case 'x':
            *max = atof(optarg);
            break;
	case 'h':
		print_usage();
		print_functions();
        case '?':
            print_usage();
			break;
        default:
			print_usage();
            break;
        }
    }

    if (argc < 8)
    {
		exit(EXIT_FAILURE);
    }
};

void
print_usage(void)
{
   	printf("FFlies usage: -n NumberOfFlies [-g NumberOfGenerations] -d NumberOfDimension -m Min -x Max\n");
}

