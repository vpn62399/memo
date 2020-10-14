var db;
var request = indexedDB.open("MyTestDatabase", 5);

request.onerror = function () {
    console.log('onerror')
}

request.onsuccess = function (event) {
    console.log('onsuccess');
    // db = event.target.result;
}

request.onupgradeneeded = function () {
    console.log('onupgradeneeded');
    // var objectStore = db.createObjectStore("name", { keyPath: "myKey" });
}



const customerData = [
    { ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" },
    { ssn: "555-55-5555", name: "Donna", age: 32, email: "donna@home.org" }
];










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