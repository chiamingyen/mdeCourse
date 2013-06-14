//@+leo-ver=5-thin
//@+node:kmolII_lite.20130614201704.3060: * @file c1/w10/stl/nxstl.c
//@@language c
//@+<< include >>
//@+node:kmolII_lite.20130614201704.3061: ** << include >>
#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_obj.h>

// for stl 資料轉出
#include <uf_std.h>
// 假設檔案中所對應的實體, 至多 100 個
#define TOTAL_NUMBER 100
// 所轉出的零件 stl 位於 try_portablenx3 目錄下, 檔案名稱為 mystl.txt
#define STL_FILENAME "mystl"

char* int2str(unsigned long num);
//@-<< include >>
//@+others
//@+node:kmolII_lite.20130614201704.3062: ** functions
//extern void ufusr(char *param, int *retcod, int param_len)
//int main(int argc, char **argv)
int main(int argc, char *argv[])
{
    // 這裡要處理 command 讀檔案與寫出處理完成後的資料輸入
        // 以下為 part 處理宣告
        tag_t body_tag = NULL_TAG;
        char *str;
        int index = 0;
        // 假設檔案中至多有 100 (TOTAL_NUMBER) 個物件
        tag_t object_id[TOTAL_NUMBER];
        // 配合設定不同物理條件的精確度
        double  acc_val[11] = {.01,0,0,0,0,0,0,0,0,0,0};
        double  massprop[47];
        double  massprop_stat[13];
        // 以下為 stl 相關變數
        UF_STD_stl_params_t     params;
        void * file_handle;
        int ifail;
        int open_type;
        tag_t open_feature, open_body_tag;
        open_type = UF_feature_type;
        int num_errors;
        UF_STD_stl_error_p_t  error_info;
        // 與所開啟的零件檔案有關
        tag_t part;
        UF_PART_load_status_t error_status;
        
       // 表示指令直接執行, 並沒有後續的開檔參數
       if(argc < 2 || argc > 3)
       {  printf("The correct format is: myfile.exe part.prt\n");
          exit(1);
       }
       UF_initialize();
       // 根據使用者所要處理的檔案, 將零件檔案打開
       ifail = UF_PART_open(argv[1],&part,&error_status);
   
    // 為 str 字串保留足夠的記憶體空間
    str = malloc(256);
    // 以下試圖將檔案中的實體轉為 stl
    // 此地必須要先確定 STL_FILENAME 在寫入 stl 資料之前為空檔案, 否則會以附加的方式置入 stl 資料
    ifail = UF_STD_open_text_stl_file (STL_FILENAME,TRUE,&file_handle);
    
    // 擷取零件中的實體 (type=70, subtype=0) 資料 
    UF_MODL_ask_object(70,0,&body_tag);
    while(body_tag !=NULL_TAG)
    {
        object_id[index] = body_tag;
        //求質量特性，
        UF_MODL_ask_mass_props_3d(&body_tag,1,1,3,1.0,1,acc_val,massprop,massprop_stat);
        sprintf(str,"massprop[%d]=%G",index, massprop[1]);
        // 針對獨立執行的程式, 也可以使用 uc1601()
        //uc1601(str,1);
        // 改採 printf 將 str 字串輸出
        printf("%s\n",str);
        index++;
        // 由 UF_MODL_ask_object 取得的 tag 確實為 body tag
        ifail = UF_STD_put_solid_in_stl_file (
        file_handle,
        NULL_TAG,
        body_tag,
        0.1,
        0.5,
        0.05,
        &num_errors,
        &error_info );
            
        UF_MODL_ask_object(70,0,&body_tag);
    }
    
    /* UF_STD_put_solid_in_stl_file 函式定義
    extern int UF_STD_put_solid_in_stl_file (
    void * file_handle,
    tag_t csys,
    tag_t body,
    double min_edge_len,
    double max_edge_len,
    double facet_toler,
    int * num_errors,
    UF_STD_stl_error_p_t * error_info );
    void * 	file_handle	Input	Handle of file
    tag_t 	csys	Input	Specifies the coordinate system with respect
    to which output data is to be made. If specified
    as NULL_TAG, the current WCS is used.
    tag_t 	body	Input	Solid body to facetize for STL
    double 	min_edge_len	Input	This argument is not used, it for future
    enhancements (Minimum facet edge length).
    double 	max_edge_len	Input	Maximum facet edge length
    double 	facet_toler	Input	Facet to surface tolerance (Interactive
    Triangle Tolerance)
    int * 	num_errors	Output	Number of errors
    UF_STD_stl_error_p_t * 	error_info	Output to be freed	Error information - NULL if there is none.
    This must be free by calling UF_free.
    */

    ifail = UF_STD_close_stl_file (file_handle);
    free(str);
    UF_PART_close (part, 0, 1);
    /* 關閉零件檔案的相關資料
    extern int UF_PART_close (
    tag_t part,
    int scope,
    int mode );
    tag_t 	part	Input	part object identifier
    int 	scope	Input	scope specifies how much of the part to close.
    0 = Only specified part
    1 = Part and all sub-assemblies
        * 
    int 	mode	Input	mode
    0 = Ask confirmation if part is modified
    (Internal only, External assumes
    "Yes, Delete" answer)
    1 = Unload part(s) even if modified
    2 = Unload part(s) only if not modified
    */
    UF_terminate();
    return 0;
}

int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}

// 此一程式目前沒有使用整數轉成字串的函式
char* int2str(unsigned long num) {
        char* retstr = calloc(12, sizeof(char));
        if (sprintf(retstr, "%ld", num) > 0) {
                return retstr;
        } else {
                return NULL;
        }
}
//@-others
//@-leo
