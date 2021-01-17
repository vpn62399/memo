//https://www.takarakuji-official.jp/ec/loto7/
//ランダム取得
var ms = [];
var size = 0;
var item2;
var items;
var but;
var LMax3743 = 37;

var xx = function () {
    var url = 'https://www.takarakuji-official.jp/ec/loto7/';
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
    // 取得したデーターをファイルに保存
    let temp2 = new String();
    for (let i = 0; i < ms.length; i++) {
        temp2 = temp2 + ms[i] + '\n';
        // temp2 = temp2 + 'fns(  [' + ms[i] + ']  )' + '\n';
    }
    let blob = new Blob([temp2], { type: "text/csv" });
    let link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'off_hiro7_list.txt';
    link.click();
}

function fk() {
    // ひとつの番号を取得
    but[0].click()
    gnum();
    // list();
}

function fkk(x) {
    // x 回の番号を取得する
    console.log(new Date());
    var i = 0;
    work_fkk = setInterval(function () {
        fk();
        i++;
        if (i > x) {
            clearInterval(work_fkk);
            list();
            console.log(new Date());
            console.log('Work_Stoped');
        }
    }, 5);
}

function T_L6ck4(remNums = []) {
    let TAG = 'log_T_ck4->';
    G_L6ck4nums = [];
    G_fnum = [];
    if (typeof (WT_ck4) == 'number') {
        clearInterval(WT_ck4);
    }
    for (let i = 0; i < LMax3743; i++) {
        G_L6ck4nums.push(parseInt(i) + 1);
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
        if (count == 7) {
            tempnum.forEach(function (e) {
                G_L6ck4nums.splice(G_L6ck4nums.indexOf(e), 1);
            });
            G_fnum.push(tempnum);
            tempnum = [];
            console.info(TAG, G_fnum);
            G_fnum.forEach(function (e) {
                console.info(' T_cpt2([' + e + ',57,0])  ');
            })
        } else {
            count = 0;
            console.log(TAG, '  clearInterval(WT_ck4)  ');
        }
        if (G_L6ck4nums.length < 7) {
            clearInterval(WT_ck4);
            console.log(TAG, G_fnum);
            console.info(TAG, G_L6ck4nums);
        }
    }, 100)
}

function T_TopSearch(arrayVal) {
    // clearInterval(W_TopSearchSwork);
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
            console.info(TAG, temp);
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
            console.info(TAG, temp);
        }
    }, 200)
}

function hiro7_off() {
    // x と一致の番号を探す
    hiro_off_num = [9, 19, 22, 32, 35, 36, 37];  //第386回
    let hiro7_off_num_string = hiro_off_num.toString();
    let i = 0;
    let startT = new Date();
    console.log(startT);
    work_hiro2 = setInterval(function () {
        for (let li = 0; li < 1; li++) {
            but[0].click();
            let temp2 = gnum();
            console.log(i++, temp2)
            if (hiro7_off_num_string === temp2.toString()) {
                clearInterval(work_hiro2);
                but[0].click();
                let temp2 = gnum();
                console.log(i++, temp2);
                console.lot(startT);
                console.log(new Date());
                console.log('hiro7_off_num_string  ' + hiro7_off_num_string);
                console.log('Work_Stoped');
                alert("Work_Stoped");
                list();
            }
        }
    }, 5)
}

window.onbeforeunload = function () {
    return "本当に離れますか？";
}