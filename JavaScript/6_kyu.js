// (1) 6_kyu

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Additionally, if the number is negative, return 0 (for languages that do have them).
// Note: If the number is a multiple of both 3 and 5, only count it once.

function solution(number) {
    let sum = 0;
    for (let i = 1; i < number; i++) {
        if (!(i % 3) || !(i % 5)) {
            sum += i;
        }
    }
    return sum;
}

// console.log(solution(18));

//----------------------------------------------------------------------------------------------------------------------

// (2) 6_kyu

// Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
// A tower block is represented with "*" character.
// For example, a tower with 3 floors looks like this:
// [
//   "  *  ",
//   " *** ",
//   "*****"
// ]

// My func
function towerBuilder(nFloors) {
    let arr_tower = [];
    let fill = 2 * nFloors - 1;
    for (let i = 1; i <= nFloors; i++) {
        const a = i * 2 - 1;
        let str = "*".repeat(a).padStart((fill + a)/ 2, ' ').padEnd(fill, ' ');
        arr_tower.push(str);
    }
    return arr_tower
}


// from C_W
// function towerBuilder(n) {
//   return Array.from({length: n}, function(v, k) {
//     const spaces = ' '.repeat(n - k - 1);
//     return spaces + '*'.repeat(k + k + 1) + spaces;
//   });
// }
// console.log(towerBuilder(5));

//----------------------------------------------------------------------------------------------------------------------

// (2) 6_kyu

