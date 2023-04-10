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
        let str = "*".repeat(a).padStart((fill + a) / 2, ' ').padEnd(fill, ' ');
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

// (3) 6_kyu

// You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest
// string consisting of k consecutive strings taken in the array.
// Examples:
// strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
//
// Concatenate the consecutive strings of strarr by 2, we get:
//
// treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
// folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
// trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
// blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
// abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
//
// Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
// The first that came is "folingtrashy" so
// longest_consec(strarr, 2) should return "folingtrashy".
//
// In the same way:
// longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
// n being the length of the string array, if n = 0 or k > n or k <= 0 return ""
// (return Nothing in Elm, "nothing" in Erlang).
//
// Note
// consecutive strings : follow one after another without an interruption

function longestConsec(strarr, k) {
    let word = '';
    if (strarr.length && strarr.length >= k && k > 0) {
        for (let i = 0; i < strarr.length - k + 1; i++) {
            let currWord = strarr.slice(i, i + k).join('');
            word = (currWord.length > word.length) ? currWord : word;
        }
    }
    return word
}

let strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2;
let strarr_2 = ["zone", "abigail", "theta", "form", "libe", "zas"]

// console.log(longestConsec(strarr, k));
// console.log(longestConsec(strarr_2, k));
