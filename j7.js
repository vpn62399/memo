//////////////fns7////////////////////////////////////////////////////
//////////////fns7////////////////////////////////////////////////////
//////////////fns7////////////////////////////////////////////////////
//////////////fns7////////////////////////////////////////////////////
//////////////fns7////////////////////////////////////////////////////
function fns(x){
  //http://www.ohtashp.com/topics/takarakuji/
  if(location.href != 'http://www.ohtashp.com/topics/takarakuji/'){
    alert("URL 不正 ファンクション不正");
  }
  var colors = ['#FF6666','#99CC66','#33FFCC','#CC66CC','#FFFF00','#FF33CC','#FF6600','#99FF00','#CC66CC'];
	var tb = document.getElementsByTagName('tbody')[1];
	var fc = tb.firstElementChild;
	var xca = 0;
	var ns= document.getElementsByClassName('hon');
  if (x[0] >= 10){
    	document.getElementById('c'+x[0]).click();
  }else{
      document.getElementById('c0'+x[0]).click();
  }
  do{
    var trs = fc.getElementsByTagName('td');
    var xc=0;
    for(var i = 1; i< 8; i++){
      for(var j = 0; j < x.length; j++){
        if(trs[i].innerText == x[j]){
          trs[i].style.backgroundColor=colors[j];
          xc++;
        }
      }
    }
    
    if(xc == 4 ){
      trs[0].style.backgroundColor=colors[0];
      xca++;
    }

    if(xc == 5){
      trs[0].style.backgroundColor=colors[1];
      xca++;
    }

    if(xc == 6){
      trs[0].style.backgroundColor=colors[2];
      xca++;
    }
  } while (fc=fc.nextElementSibling);
	
  if(xca == 0 ){
    console.log('fns(  [' + x + ']  )' + "  d4c = " + xca);
  }
}

function ck(x){
  if(location.href != 'http://www.ohtashp.com/topics/takarakuji/'){
    alert("URL 不正 ファンクション不正");
    return;
  }
  for(var i=0 ; i<x; i++){
    var temp= l7(7);
    if(x==1){
      console.log(temp);
    }
    fns(temp);
  }
}

function ad7 (x){
  //http://www.ohtashp.com/topics/takarakuji/
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[1].firstElementChild;
  var cc = pf.cloneNode(true);
  cc.getElementsByTagName('th')[0].innerText="ADD";
  var ff = cc.firstElementChild.nextElementSibling.nextElementSibling;
  do{
      ff.className="xxx";
  }while(ff=ff.nextElementSibling)
  var ff = cc.firstElementChild.nextElementSibling;
  for(var i=0; i<7; i++){
    ff= ff.nextElementSibling;
    ff.innerText=x[i];
  }
  tb[1].insertBefore(cc,pf)
}

function rd7 (x){
  //http://www.ohtashp.com/topics/takarakuji/
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[1].firstElementChild;
  var tx = pf.getElementsByClassName('xxx')
  for(var i=0; i<7 ; i++){
    tx[i].innerText = x[i];
  }
}

function rm7(){
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[1].firstElementChild;
  tb[1].removeChild(pf); 
}

function l7(x){
  var j = [];
  do{
    var chk = "OK";
    var c = Math.floor(Math.random()*(1-38)+38);
    for (var i=0; i<j.length; i++){
      if(j[i] == c){
        chk = "NG";
      }
    }
    if(chk != "NG"){
      j.push(c);
    }
  }while(j.length < x);
  return j.sort((a, b) => a - b);
}


//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//https://www.takarakuji-official.jp/ec/loto7/
//ランダム取得
var item2 = document.getElementsByClassName('m_lotteryNumContainer_item2');
var items = item2[0].getElementsByClassName('m_lotteryNumInputNum_btn is_random');
var but = item2[0].getElementsByClassName('m_btn m_lotteryNumInputFunc_btn m_btn__colorRandom m_btn__block');
var numitems = [];
var size = 0;

function gnum(){
  numitems[size]=[];
  for( var i=0; i<items.length; i++){
    numitems[size].push(parseInt(items[i].innerText,10));
  }
  size+=1;
  console.log(numitems);
}

function list(){
  var funlink = new String();
  for(var i=0; i< numitems.length; i++){
    funlink = i + '     fns([' + numitems[i] + '])';
    console.log(funlink);
  }
}

function ck(){
   but[0].click()
   gnum();
   list();
}

//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////


