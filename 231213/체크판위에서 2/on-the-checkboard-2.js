const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().split('\n');
const print = (...arr) => console.log(...arr);

let [mapSize, ...arr] = inputAll()

const [R, C] = mapSize.split(' ').map(elm => Number(elm));
arr = arr.map(line => line.trim().split(' '))

const WHITE = 'W';
const BLACK = 'B';

const reverseTile = (tile) => tile === WHITE ? BLACK : WHITE;

const startTile = arr[0][0];
const endTile = arr[R-1][C-1];

if(startTile === endTile){
    print(0);
    return;
}

let count = 0;

for(let i = 1; i < R - 1; i++){
    for(let j = 1; j < C - 1; j++){
        if(arr[i][j] === reverseTile(startTile)){
            for(let i_2 = i + 1; i_2 < R - 1; i_2++){
                for(let j_2 = j + 1; j_2 < C - 1; j_2++){
                    if(arr[i_2][j_2] === reverseTile(endTile)){
                        count++;
                    }
                }
            }
        }
    }
}

print(count);