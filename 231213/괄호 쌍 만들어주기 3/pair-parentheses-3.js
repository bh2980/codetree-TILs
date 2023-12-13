const fs = require('fs');
const input = () => fs.readFileSync('/dev/stdin').toString()

const parString = input();
let answer = 0;

for(let i = 0; i < parString.length; i++){
    const par = parString[i];

    if(par === '('){
        for(let j = i + 1; j < parString.length; j++){
            const par2 = parString[j];

            if(par2 === ')'){
                answer += 1;
            }
        }
    }
}

console.log(answer);