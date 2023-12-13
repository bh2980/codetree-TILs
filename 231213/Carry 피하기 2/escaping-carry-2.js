const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const print = (...args) => console.log(...args);

let [N, ...arr] = inputAll();
N = Number(N);
arr = arr.map(elm => Number(elm));

let maxNum = 0;

for(let i = 0; i < arr.length; i++){
    for(let j = i + 1; j < arr.length; j++){
        for(let k = j + 1; k < arr.length; k++){
            // 캐리 계산
            let numA = arr[i];
            let numB = arr[j];
            let numC = arr[k];

            let carryFlag = false;

            while(numA !== 0 || numB !== 0 || numC !== 0){
                const leftA = numA % 10;
                const leftB = numB % 10;
                const leftC = numC % 10;

                numA = parseInt(numA / 10);
                numB = parseInt(numB / 10)
                numC = parseInt(numC / 10)

                if(leftA + leftB + leftC >= 10){
                    carryFlag = true;
                    break;
                }
            }

            // 갱신
            if(!carryFlag){
                maxNum = Math.max(maxNum, arr[i] + arr[j] + arr[k]);
            }
        }
    }
}

print(maxNum);