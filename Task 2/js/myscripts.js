motorcount = 1;
motorname = "Motor";
mid = "csm"+motorcount;
function addRow() {
    var table = document.getElementById("motortable");
    var table1 = document.getElementById("motort");
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    var row1 = table1.insertRow(rowCount);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var c1 = row1.insertCell(0);
    var c2 = row1.insertCell(1);
    var c3 = row1.insertCell(2);
    var ms = document.createElement('div');
  	ms.className = 'currentspeed';
  	ms.id = mid;
    console.log(mid);
  	ms.innerHTML  = '0';
  	cell4.appendChild(ms);
    cell1.innerHTML = motorname+motorcount;
    c1.innerHTML = motorname+motorcount;
    var DivOn = document.createElement('button');
    DivOn.className = 'on';
    DivOn.id=mid+'on';
    DivOn.name=mid+'on';
    DivOn.innerHTML  = 'ON';
    motorcount++;
    mid = "csm"+motorcount;
  	DivOn.setAttribute('onclick',"motoron("+(motorcount-1)+")"); 
  	cell2.appendChild(DivOn);
  	var DivOff = document.createElement('button');
  	DivOff.className = 'off';
  	DivOff.innerHTML  = 'OFF'; 
  	DivOff.setAttribute('onclick',"motoroff("+(motorcount-1)+")");
    cell3.appendChild(DivOff);
  	var up = document.createElement('button');
  	up.className = 'speedchange';
  	up.innerHTML  = 'UP'
    up.setAttribute('onclick',"speedup("+(motorcount-1)+")");
  	var down = document.createElement('button');
  	down.className = 'speedchange';
  	down.innerHTML  = 'Down' 
    down.setAttribute('onclick',"speeddown("+(motorcount-1)+")");
    cell5.appendChild(up);
    cell5.appendChild(down);
    var h = document.createElement('div');
    h.className = 'health';
    h.style.backgroundColor = 'green';
    h.id = "health"+(motorcount-1);
    c2.appendChild(h);
    var fi = document.createElement('button');
    fi.innerHTML = 'Fix Issues';
    fi.id = "f"+(motorcount-1);
    fi.setAttribute('onclick',"fix("+(motorcount-1)+")");
    c3.appendChild(fi);
}
function motoron(x){
  var t = "csm"+x;
  var n = "csm"+x+'on';
  document.getElementById(n).name = "csm"+x+'onn';
	document.getElementById(t).innerHTML="5"; 
}
function motoroff(x){
  var t = "csm"+x;
  var n = "csm"+x+'on';
  document.getElementById(n).name = "csm"+x+'on';
	document.getElementById(t).innerHTML="0"; 
}
function speedup(x){
  var t = "csm"+x;
  var n = "csm"+x+'on';
  var h = "health"+x;
  var s = document.getElementById(t).innerHTML;
  var nn = document.getElementById(n).name;
  if(s>=0 && n!==nn){
    s++;
    document.getElementById(t).innerHTML=s;
  }
  if(s>10){
    document.getElementById(h).style.backgroundColor = "Red";
  }
}
function speeddown(x){
  var t = "csm"+x;
  var n = "csm"+x+'on';
  var h = "health"+x;
  var s = document.getElementById(t).innerHTML;
  var nn = document.getElementById(n).name;
  if(s>0 && n!=nn){
    s--;
    document.getElementById(t).innerHTML=s;
  }
  if(s<=10){
    document.getElementById(h).style.backgroundColor = "green";
  }
}
function fix(x){
  var t = "csm"+x;
  var n = "csm"+x+'on';
  var h = "health"+x;
  var s = document.getElementById(t).innerHTML;
  var nn = document.getElementById(n).name;
  if(n!==nn){
    document.getElementById(t).innerHTML="5"; 
    document.getElementById(h).style.backgroundColor = "green";
  }
}