#include <CUnit/CUnit.h>
#include <CUnit/Basic.h>
#include "../firefly.c"
#include "../functions.h"

void test_memcpy_fly(void);
void test_akley(void);

int main()
{
   CU_pSuite pSuite = NULL;

   /* initialize the CUnit test registry */
   if (CUE_SUCCESS != CU_initialize_registry())
      return CU_get_error();

   /* add a suite to the registry */
   pSuite = CU_add_suite("Firefly tets", NULL, NULL);
   if (NULL == pSuite) {
      CU_cleanup_registry();
      return CU_get_error();
   }

   /* add the tests to the suite */
   if ((NULL == CU_add_test(pSuite, "test_memcpy_fly", test_memcpy_fly)) ||
				   ((NULL == CU_add_test(pSuite, "test_akley", test_akley)))
   {
      CU_cleanup_registry();
      return CU_get_error();
   }

   /* Run all tests using the basic interface */
   CU_basic_set_mode(CU_BRM_VERBOSE);
   CU_basic_run_tests();
   printf("\n");
   CU_basic_show_failures(CU_get_failure_list());
   printf("\n\n");

   /* Run all tests using the automated interface */
   CU_automated_run_tests();
   CU_list_tests_to_file();

   /* Clean up registry and return */
   CU_cleanup_registry();
   return CU_get_error();
};

void 
test_memcpy_fly(void)
{
    ffly f1;
    ffly f2;
    size_t i = 0;
    
    f1.params = calloc(10, sizeof(double));
    f2.params = calloc(10, sizeof(double));

    f1.val = -101.0;
    f2.val = 10.0;
    
    for (i=0; i < 10; i++)
    {
        f1.params[i] = 2.1;
        f2.params[i] = 5.5;
    }
    memcpy_ffly(&f2, &f1, 10);
    
    for (i=0; i < 10; i++)
    {
        CU_ASSERT(f2.params[i] == 2.1);
    }
    CU_ASSERT(f2.val == -101.0);

    free(f1.params);
    free(f2.params);

};

void
test_akley(void)
{
	ffly f1;
	size_t i = 0, n = 5;

	f1.params = calloc(n, sizeof(double));
	f1.val = 1.0;

	f1.val = akley(&f1, n);
	CU_ASSERT(f1.val == 0.0);
	free(f1.params);
}
