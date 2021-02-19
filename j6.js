///https://www.takarakuji-official.jp/ec/loto6/
//ランダム取得
var ms = [];
var size = 0;
var item2;
var items;
var but;
var LMax3743 = 43;

var xx = function () {
    var url = 'https://www.takarakuji-official.jp/ec/loto6/';
    if (location.href != url) {
        // window.open(url);
        alert("URL Error");
        return;
    }
    item2 = document.getElementsByClassName('m_lotteryNumContainer_item2');
    items = item2[0].getElementsByClassName('m_lotteryNumInputNum_btn is_random');
    but = item2[0].getElementsByClassName('m_btn m_lotteryNumInputFunc_btn m_btn__colorRandom m_btn__block');
    but2 = item2[0].getElementsByClassName('m_lotteryNum_close');
}();

function gnum() {
    ms[size] = [];
    items = item2[0].getElementsByClassName('m_lotteryNumInputNum_btn is_random');
    for (let i = 0; i < items.length; i++) {
        ms[size].push(parseInt(items[i].innerText, 10));
    }
    size += 1;
    return ms[ms.length - 1];
}

function list() {
    let temp2 = new String();
    for (let i = 0; i < ms.length; i++) {
        temp2 = temp2 + ms[i] + '\n';
        // temp2 = temp2 + 'fns6(  [' + ms[i] + ']  )' + '\n';
    }
    let blob = new Blob([temp2], { type: "text/csv" });
    let link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'off_hiro6_list.txt';
    link.click();
}

function fk() {
    but[0].click()
    gnum();
    // list();
}

function fkk(x) {
    var i = 0;
    var tid = setInterval(function () {
        fk();
        i++;
        if (i > x) {
            clearInterval(tid);
            list();
        }
    }, 5);
}

function T_L6ck4(remNums = []) {
    let TAG = 'log_T_ck4->';
    G_L6ck4nums = [];
    G_fnum = [];
    for (let i = 0; i < LMax3743; i++) {
        G_L6ck4nums.push(parseInt(i) + 1);
    }
    if (typeof (WT_ck4) == 'number') {
        clearInterval(WT_ck4);
    }
    if (remNums.length > 0) {
        remNums.forEach(function (e) {
            G_L6ck4nums.splice(G_L6ck4nums.indexOf(e), 1);
        })
    }

    WT_ck4 = setInterval(function () {
        but[0].click()
        let tempnum = gnum();
        let count = 0;
        tempnum.forEach(function (e) {
            if (G_L6ck4nums.indexOf(e) >= 0) {
                count++;
            }
        })
        if (count == 6) {
            tempnum.forEach(function (e) {
                G_L6ck4nums.splice(G_L6ck4nums.indexOf(e), 1);
            });
            G_fnum.push(tempnum);
            tempnum = [];
            console.info(TAG, G_fnum);
            G_fnum.forEach(function (e) {
                console.info(TAG, ' T_cpt2([' + e + ',56,0])  ');
            })
        } else {
            count = 0;
            console.log(TAG, '  clearInterval(WT_ck4)  ');
        }
        if (G_L6ck4nums.length < 6) {
            clearInterval(WT_ck4);
            console.log(TAG, G_fnum);
            console.info(TAG, G_L6ck4nums);
        }
    }, 100)
}

function T_TopSearch(arrayVal) {
    // clearInterval(W_TopSearchSwork);
    let debug = false;
    const TAG = 'log_T_TopSearch->';
    let temp = [];
    let cont = 0;
    let contc = 0;
    if (typeof (W_TopSearchSwork) == 'number') {
        clearInterval(W_TopSearchSwork);
    }
    W_TopSearchSwork = setInterval(function () {
        cont = 0;
        but[0].click();
        let temp = gnum();
        for (let i = 0; i < arrayVal.length; i++) {
            if (temp[i] == arrayVal[i]) {
                cont++;
            }
        }
        console.info(TAG, ' clearInterval(W_TopSearchSwork)  ' + arrayVal.toString());
        if (cont == arrayVal.length) {
            clearInterval(W_TopSearchSwork);
            console.info(TAG, ' T_cpt2([' + temp + ',56,0])  ');
        }
    }, 200)
}

function T_Searchfom(arrayVal) {
    // arrayVal 指定した値が含まれるまで探し
    // clearInterval(W_T_Searchfom);
    const TAG = 'T_Searchfom->';
    let tempArr = arrayVal.concat();
    if (typeof (W_T_Searchfom) == 'number') {
        clearInterval(W_T_Searchfom);
    }
    W_T_Searchfom = setInterval(function () {
        let cont = 0;
        but[0].click();
        var temp = gnum();
        tempArr.forEach(function (e) {
            if (temp.indexOf(e) >= 0) {
                cont++;
            }
        })
        console.info(TAG, ' clearInterval(W_T_Searchfom)  ' + arrayVal.toString());
        if (cont == arrayVal.length) {
            clearInterval(W_T_Searchfom);
            console.info(TAG, ' T_cpt2([' + temp + ',56,0])  ');
        }
    }, 200)
}

function T_tx2() {
    let tag = [
        [12, 15, 26, 34, 35, 38],
        [7, 19, 24, 32, 40, 42],
        [4, 15, 17, 20, 26, 31],
        [1, 12, 25, 27, 39, 42],
        [5, 21, 22, 23, 26, 39],
        [10, 19, 28, 30, 38, 42],
        [2, 8, 17, 23, 24, 27],
        [6, 14, 16, 27, 40, 42],
        [7, 8, 16, 32, 41, 42],
        [5, 9, 15, 30, 32, 39],
        [3, 14, 18, 24, 38, 43]
    ];
    let index = 0;
    let er = [];
    G_tx2list = [];
    tx2_tw = setInterval(function () {
        index++;
        but[0].click()
        er = gnum();
        for (let i = 0; i < tag.length; i++) {
            if (er.toString() == tag[i].toString()) {
                console.log(er);
                G_tx2list.push(er);
            }
        }
        console.log(' clearInterval(tx2_tw) ');
        if (index == 10000) {
            clearInterval(tx2_tw);
            console.log(G_tx2list);
            console.log('tx2_tw_work_end');
        }
    }, 100)
}

function tx1() {
    // call 
    let tag = [[12, 15, 26, 34, 35, 38], [7, 19, 24, 32, 40, 42], [4, 15, 17, 20, 26, 31], [1, 12, 25, 27, 39, 42]];
    for (let i = 0; i < tag.length; i++) {
        (function (i) {
            this.print = function () {
                console.log(tag[i]);
                console.log(tag[i].length);
            };
            this.print();
        }).call(tag, i);
    }
}

window.onbeforeunload = function () {
    return "本当に離れますか？";
}