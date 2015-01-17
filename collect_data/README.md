#collect_data
## 執行檔案
1. 下載 node.js
2. 利用 node.js 執行 app.js (i.e. cmd> node app.js)
3. 打開瀏覽器URL輸入 localhost:3000 (Default port) 

## Parse檔案
1. .../collect_data/data/ 下有 feature.dat 與 article.dat 兩個檔案
2. article.dat 是 parse 後的文章以 JSON 格式儲存
3. feature.dat 用來定義 feature 和 value. 格式如下:

> `#heading` [前面加#會幫你分段]  
`feature_single,value1,value2,value3` [單選]  
`*feature_multiple,value1,value2,value3` [前面加\*會變成多選]  
`feature_input` [手動輸入]  

4. 注意不要有空格不然之後整理資料會很麻煩
5. 可以自已任意增減 feature, value 和調整順序!!
6. feature.dat 內的空行會自動跳過去，所以可以自己調整檔案 display

## 其他
1. 第一行的文章資訊是必填的，所以就把 hardcode 在前端了
2. 目前是每5個 feature 會幫你換到下一行
