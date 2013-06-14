/*
 * =====================================================================================
 *
 *       Filename:  functions.h
 *
 *    Description:  benchmark functions for optmization
 *
 *        Version:  1.0
 *        Created:  05/03/2010 02:52:28 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Nicholas Mancuso (nam), nick.mancuso@gmail.com
 *        Company:  GSU Computer Science Dept
 *
 * =====================================================================================
 */


#include "firefly.h"

#define PI 3.14159265
#define E 2.71828183


/*
 * Prints the available functions
 */
void print_functions(void);

/*  
 	Use function name to get pointer to the function
*/
obj_func get_function(const char *fname);

/*
    Our objective function declarations
*/
double yang(const ffly *fly, const size_t nparams);
double akley(const ffly *fly, const size_t nparams);
double schwefel(const ffly *fly, const size_t nparams);
double rosenbrock(const ffly *fly, const size_t nparams);
double michalewicz(const ffly *fly, const size_t nparams);
double easom(const ffly *fly, const size_t nparams);
double dejung(const ffly *fly, const size_t nparams);
double volume(const ffly *fly, const size_t nparams);

