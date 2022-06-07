let sutjaPan = []

for(var i=1;i<=10000;i++){
    sutjaPan[i-1] = i;
}

//console.log(sutjaPan);
//console.log(arr);

function d(num) {
    let arr = num.toString().split('');
    //인수를 한글자씩 잘라 배열에 저장
    //console.log(arr);

    let resultD = num*1; //저장소
    for(var i=0;i<arr.length;i++){
        resultD += arr[i]*1;
    }
    //console.log(resultD);
    return resultD;
}

function repeatD(nat){

    let resultD = nat;
    while(resultD<=10000){
        resultD = d(resultD);
        //console.log(resultD, sutjaPan.indexOf(resultD));
        if(sutjaPan.indexOf(resultD) > -1){
            sutjaPan.splice(sutjaPan.indexOf(resultD), 1);
        }
    }
}

function main(){
    let j = 1;
    while(j < 10000){
        repeatD(j);
        j++;
    }

    for(var i=0;i<sutjaPan.length;i++){
        console.log(sutjaPan[i]);
    }
}

main();
//d(16);