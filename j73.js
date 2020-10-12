var db;
var request = indexedDB.open("MyTestDatabase", 5);

request.onerror = function (event) {
    console.log('onerror')
    alert("Why didn't you allow my web app to use IndexedDB?!");
};

request.onsuccess = function (event) {
    console.log('onsuccess');
    db = event.target.result;
};

request.onupgradeneeded = function (event) {
    console.log('onupgradeneeded');
    // 保存 IDBDataBase 接口
    var db = event.target.result;
    db.onversionchange = function (e) {
        console.log('onversionchange');
    }
    // 为该数据库创建一个对象仓库
    var objectStore = db.createObjectStore("name", { keyPath: "myKey5" });
};