//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////

var set1 = 0;  //0色の表示をつつける,1色一回のみ
var set2 = 0;  //0色初期化する,1色初期化しない
var set3 = 1;  //連番数
var set4 = 10; //10 ボーナス数字含む、8 ボーナス数字含まない
var set5 = 0;  //0表示 1無表示,ファイルに保存
var set6 = 0;   //0行隠ししない、1行隠しする。

function fns6(tx6, set1 = 0, set2 = 0) {
    //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
    var url = 'http://www.ohtashp.com/topics/takarakuji/index_loto6.html'
    if (location.href != url) {
        window.open(url);
        return;
    }
    // console.log('tx6 =  ' + tx6);
    let colors = ['#FF6666', '#99CC66', '#33FFCC', '#CC66CC', '#FFFF00', '#FF33CC', '#FF6600', '#99FF00', '#CC66CC'];
    let tb = document.getElementsByTagName('tbody')[0];
    let fc = tb.firstElementChild;
    let xca = 0;
    if (set2 == 0) {
        var ns = document.getElementsByClassName('hon');
        for (let i = 0; i < ns.length; i++) {
            ns[i].style = "";
        }
        var ns = document.getElementsByClassName('naka');
        for (let i = 0; i < ns.length; i++) {
            ns[i].style = "";
        }
        var ns = document.getElementsByClassName('bou');
        for (let i = 0; i < ns.length; i++) {
            ns[i].style = "";
        }
    }

    do {
        let trs = fc.getElementsByTagName('td');
        if (trs.length < 3) {
            break;
        }
        let xc = 0;
        for (let i = 1; i < 8; i++) {
            for (let j = 0; j < tx6.length; j++) {
                if (trs[i].innerText == tx6[j]) {
                    trs[i].style.backgroundColor = colors[j];
                    xc++;
                    if (set1 == 1) {
                        tx6.splice(j, 1);
                        master();
                    }
                }
            }
        }

        if (xc == 3) {
            trs[0].style.backgroundColor = colors[0];
            xca++;
        }

        if (xc == 4) {
            trs[0].style.backgroundColor = colors[1];
            xca++;
        }

        if (xc == 5) {
            trs[0].style.backgroundColor = colors[2];
            xca++;
        }
    } while (fc = fc.nextElementSibling);

    if (xca >= set3) {
        console.log('fns6(  [' + tx6 + ']  )' + "  d3c = " + xca);
    }
}

function ck6(tx6) {
    // console.log('tx6 =  ' + tx6);
    if (location.href != 'http://www.ohtashp.com/topics/takarakuji/index_loto6.html') {
        alert("URL 不正 ファンクション不正");
        return;
    }
    ck6_work = setInterval(function () {
        let temp = l6(7);
        if (tx6 == 1) {
            console.log('fns6( [' + temp + '] )');
        }
        fns6(temp);
        if (tx6-- == 0) {
            clearInterval(ck6_work);
            console.log('ck6_work_end');
        }
    }, 1);
}

function ad6kk(tx6) {
    //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
    // console.log('tx6 =  ' + tx6);
    var tb = document.getElementsByTagName('tbody');
    var pf = tb[0].firstElementChild;
    var cc = pf.cloneNode(true);
    cc.getElementsByTagName('th')[0].innerText = "ADD";
    var tt = cc.getElementsByClassName('hon')
    for (var i = 0; i < 6; i++) {
        tt[i].innerText = tx6[i];
    }
    tb[0].insertBefore(cc, pf)
}

function rd6(tx6) {
    //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
    // console.log('tx6 =  ' + tx6);
    var tb = document.getElementsByTagName('tbody');
    var pf = tb[0].firstElementChild;
    var tx6 = pf.getElementsByClassName('hon')
    for (let i = 0; i < 6; i++) {
        tx6[i].innerText = tx6[i];
    }
}

function rm6() {
    let tb = document.getElementsByTagName('tbody');
    let pf = tb[0].firstElementChild;
    let ff = pf.firstElementChild;
    let temp = '';
    do {
        temp = temp + ff.innerText + ', ';
    } while (ff = ff.nextElementSibling);
    tb[0].removeChild(pf);
    return temp;
}

function l6(tx6 = 6) {
    // ランダムの数字を発生
    // console.log('tx6 =  ' + tx6);
    var j = [];
    do {
        var c = Math.floor(Math.random() * (1 - 66) + 66);
        if (c <= 43) {
            if (j.indexOf(c) == -1) {
                j.push(c);
            }
        }
    } while (j.length < tx6);
    return j.sort((a, b) => a - b);
}

function fik(tx6, set6 = 0) {
    //指定の番号の列と一個前の列を表示
    //tx6=0の場合、すべての表示する。
    //set6 = 0;   //0行隠ししない、1行隠しする。
    // console.log('tx6 =  ' + tx6);
    var tb = document.getElementsByTagName('tbody')[0];
    var fc = tb.firstElementChild;
    var pa = [];
    var nol = [];
    var noli = new Array(44);
    for (var i = 1; i < 44; i++) {
        noli[i] = 0;
    }
    if (tx6 == 0) {
        do {
            fc.style = "";
        } while (fc = fc.nextElementSibling);
        return null;
    }
    do {
        var temp = fc.getElementsByTagName('td');
        if (temp.length < 11) {
            break;
        }
        var temp2 = [];
        for (var i = 1; i < 7; i++) {
            temp2.push(parseInt(temp[i].innerText));
        }
        if (temp2.indexOf(tx6) == -1) {
            //set6 = 0;   //0行隠ししない、1行隠しする。
            if (set6 == 1) {
                fc.style.display = "none";
            }
        } else {
            if (fc.previousElementSibling) {
                fc.previousElementSibling.style = " ";
                var t3 = fc.previousElementSibling.getElementsByTagName('td');
                for (var i = 1; i < 7; i++) {
                    nol.push(parseInt(t3[i].innerText));
                    if (pa.indexOf(parseInt(t3[i].innerText)) == -1) {
                        pa.push(parseInt(t3[i].innerText));
                    }
                }
            }
        }
    } while (fc = fc.nextElementSibling);
    console.log('fns( [' + pa.sort((a, b) => a - b) + '] )' + '  tx6 = ' + tx6);
    fns6([tx6]);
    nol = nol.sort((a, b) => a - b)
    do {
        var i = nol.pop();
        noli[i] = noli[i] + 1;
    } while (nol.length != 0)
    console.table(noli);
    // noli.forEach(function(v,i,ar){
    //   console.log(" " + i + "   " + v);
    // })
}

function master() {
    // すべての抽選数字をarrayに取得
    l6ms = [];
    let li = 0;
    let tb = document.getElementsByTagName('tbody')[0];
    let fc = tb.firstElementChild;
    do {
        l6ms[li] = [];
        let da = fc.getElementsByTagName('td');
        if (da.length > 7) {
            for (let i = 1; i < 8; i++) {
                l6ms[li].push(parseInt(da[i].innerText));
            }
            li++;
        }
    } while (fc = fc.nextElementSibling);
    return l6ms;
}
master();

function roolclock() {
    var rolldata = master();
    var tb = document.getElementsByTagName('tbody')[0];
    var th = tb.getElementsByTagName('th');
    for (let i = 0; i < th.length - 1; i++) {
        th[i].setAttribute('id', i);
        th[i].addEventListener('click', function () {
            fns6(rolldata[this.id]);
        })
    }
}
roolclock();

var hiro6_list = [];
function hiro6() {
    // ==t[] までのランダムデータをファイル作成
    console.log(new Date());
    let t = [1, 2, 3, 4, 5, 6];
    var i = 0;
    hiro6_list[i] = [];
    var ix = function () {
        var j = [];
        do {
            var c = Math.floor(Math.random() * (1 - 66) + 66);
            if (c <= 43) {
                j.indexOf(c) == -1 ? j.push(c) : '';
            }
        } while (j.length < 6);
        return j.sort((a, b) => a - b);
    };

    work_hiro6 = setInterval(function () {
        let temp = ix();
        i++;
        hiro6_list[i] = temp;
        if (t.toString() === hiro6_list[i - 1].toString()) {
            console.log(new Date());
            console.log(temp);
            clearInterval(work_hiro6);
            let temp2;
            for (let i = 0; i < hiro6_list.length; i++) {
                temp2 = temp2 + 'fns(  [' + hiro6_list[i] + ']  )' + '\n';
            }
            let blob = new Blob([temp2], { type: "text/csv" });
            let link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'hiro6_list.txt';
            link.click();
        }
    }, 1);
}

function hiro6_view() {
    //== t[] までのランダムデータとまる
    hiro6_item = [5, 8, 20, 21, 27, 43];
    var hiro6_item_string = hiro6_item.toString();
    var i = 0;
    function l6x() {
        let j = [];
        do {
            let c = Math.floor(Math.random() * (1 - 66) + 66);
            if (c <= 43) {
                j.indexOf(c) == -1 ? j.push(c) : '';
            }
        } while (j.length < hiro6_item.length);
        return j.sort((a, b) => a - b);
    }
    var startT = new Date();
    console.log(startT);
    hiro6_view_work = setInterval(() => {
        for (let li = 0; li < 1000; li++) {
            let x = l6x();
            console.log(i++, x);
            if (hiro6_item_string === x.toString()) {
                clearInterval(hiro6_view_work);
                let x = l6x();
                console.log(i++, x);
                console.log(startT);
                console.log(new Date());
                console.log('hiro6_item  ' + hiro6_item);
                console.log("Stop");
                alert("Stoped");
            }
        }
    }, 500);
}

window.onbeforeunload = function () {
    return "本当に離れますか？";
}

//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
///https://www.takarakuji-official.jp/ec/loto6/
//ランダム取得

var ms = [];
var size = 0;
var item2;
var items;
var but;
var xx = function () {
    var url = 'https://www.takarakuji-official.jp/ec/loto6/';
    if (location.href != url) {
        // window.open(url);
        return;
    }
    item2 = document.getElementsByClassName('m_lotteryNumContainer_item2');
    items = item2[0].getElementsByClassName('m_lotteryNumInputNum_btn is_random');
    but = item2[0].getElementsByClassName('m_btn m_lotteryNumInputFunc_btn m_btn__colorRandom m_btn__block');
}();

function gnum() {
    ms[size] = [];
    for (var i = 0; i < items.length; i++) {
        ms[size].push(parseInt(items[i].innerText, 10));
    }
    size += 1;
    // console.log(ms);
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

window.onbeforeunload = function () {
    return "本当に離れますか？";
}

//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////


