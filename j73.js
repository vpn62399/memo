var mIDBDatabase;
const mIDBOpenDBRequest = indexedDB.open("MyTestDatabase", 5);

mIDBOpenDBRequest.onerror = function () {
    console.log('onerror')
}

mIDBOpenDBRequest.onsuccess = function (event) {
    console.log('onsuccess');
    mIDBDatabase = event.target.result;
    mIDBTransaction = mIDBDatabase.transaction("t1", "readwrite");
    mIDBObjectStore = mIDBTransaction.objectStore("t1");
    add(mIDBObjectStore);

    mIDBTransaction.oncomplete = function (e) {
        console.log("mIDBTransaction.oncomplete");
    }

    mIDBTransaction.onerror = function (e) {
        console.log("mIDBTransaction.onerror");
    }
}

function add(mIDBObjectStore) {
    console.log("add(mIDBObjectStore)");
    customerData.forEach(function (e) {
        console.log(e);
        mIDBObjectStore.add(e);
    })
}

mIDBOpenDBRequest.onupgradeneeded = function (event) {
    console.log('onupgradeneeded');
    mIDBDatabase = event.target.result;
    mIDBObjectStore = mIDBDatabase.createObjectStore("t1", { keyPath: "ssn" });
    mIDBObjectStore.createIndex("name", "name", { unique: false });
    mIDBObjectStore.createIndex("email", "email", { unique: false });

    mIDBObjectStore.transaction.oncomplete = function (event) {
        console.log("oncomplete");
    }
}


const customerData = [
    { ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" },
    { ssn: "555-55-5555", name: "Donna", age: 32, email: "donna@home.org" }
];

window.onclose = function (e) {
    alert("close");
}

