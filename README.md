# mail-to-students
一個可以寄信給大家的小東西。

## Usage
1. 準備好data.csv，格式如下：
   
    | student_no | student_name | score | custom1 |
    | ---------- | ------------ | ----- | ------- |
    | B10500001  | 學生1        | 87    | message |
    | B10500002  | 學生2        | 87    | message |
    | B10500003  | 學生3        | 95    | message |
    | B10500004  | 學生4        | 80    | message |
    | B10500005  | 學生5        | 80    | message |
    | B10500006  | 學生6        | 40    | message |

    **至少應有 "student_no" 及 "student_name"欄位**  
    如有score欄位可選計算排名  
    也可以自訂欄位(如custom1)作個別訊息，會自動新增在信內

2.  執行
    ```
    python3 main.py
    ```