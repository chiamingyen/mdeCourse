//@+leo-ver=5-thin
//@+node:kmolII_lite.20130614201704.2983: * @file c1/w10/nx3/nxvol.c
//@@language c
//@+<< include >>
//@+node:kmolII_lite.20130614201704.2984: ** << include >>
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
// 所轉出的零件 stl 位於 啟動 start_nx3.bat 的目錄下, 檔案名稱為 mystl.txt
#define STL_FILENAME "mystl"
//@-<< include >>
//@+others
//@+node:kmolII_lite.20130614201704.2985: ** functions
char* int2str(unsigned long num);

extern void ufusr(char *param, int *retcod, int param_len)
{
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
    
    UF_initialize();
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
        uc1601(str,1);
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

    ifail = UF_STD_close_stl_file (file_handle);
    free(str);
    UF_terminate();
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
