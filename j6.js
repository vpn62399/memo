//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////
//////////////fns6////////////////////////////////////////////////////
function fns6 (x){
  //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
  if(location.href != 'http://www.ohtashp.com/topics/takarakuji/index_loto6.html'){
    alert("URL 不正 ファンクション不正");
  }
  var colors = ['#FF6666','#99CC66','#33FFCC','#CC66CC','#FFFF00','#FF33CC','#FF6600','#99FF00','#CC66CC'];
  var tb = document.getElementsByTagName('tbody')[0];
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
    if(trs.length < 3){
      break;
    }
    var xc=0;
    for(var i = 1; i< 7; i++){
      for(var j = 0; j < x.length; j++){
        if(trs[i].innerText == x[j]){
          trs[i].style.backgroundColor=colors[j];
          xc++;
        }
      }
    }
    
    if(xc == 3 ){
      trs[0].style.backgroundColor=colors[0];
      xca++;
    }

    if(xc == 4){
      trs[0].style.backgroundColor=colors[1];
      xca++;
    }

    if(xc == 5){
      trs[0].style.backgroundColor=colors[2];
      xca++;
    }
  } while (fc=fc.nextElementSibling);
  
  if(xca > 20 ){
    console.log('fns6(  [' + x + ']  )' + "  d3c = " + xca);
  }
}

function ck(x){
  if(location.href != 'http://www.ohtashp.com/topics/takarakuji/index_loto6.html'){
    alert("URL 不正 ファンクション不正");
    return;
  }
  for(var i=0 ; i<x; i++){
    var temp = l6(6);
    if(x == 1){
      console.log('fns6( [' + temp + '] )');
    }
    fns6(temp);
  }
}

function ad6 (x){
  //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[0].firstElementChild;
  var cc = pf.cloneNode(true);
  cc.getElementsByTagName('th')[0].innerText="ADD";
  var tx = cc.getElementsByClassName('hon')
  for(var i=0; i<6 ; i++){
    tx[i].innerText = x[i];
  }
  tb[0].insertBefore(cc,pf)
}

function rd6 (x){
  //http://www.ohtashp.com/topics/takarakuji/index_loto6.html
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[0].firstElementChild;
  var tx = pf.getElementsByClassName('hon')
  for(var i=0; i<6 ; i++){
    tx[i].innerText = x[i];
  }
}

function rm6(){
  var tb = document.getElementsByTagName('tbody');
  var pf = tb[0].firstElementChild;
  tb[0].removeChild(pf); 
}

function l6(x){
  var j = [];
  do{
    var chk = "OK";
    var c = Math.floor(Math.random()*(1-44)+44);
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
