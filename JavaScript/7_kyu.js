//6_kyu
// Write a function that takes in a string of one or more words, and returns the same string,
// but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in
// will consist of only letters and spaces. Spaces will be included only when more than one word is present.

// Examples:
// console.log(spinWords("Hey fellow warriors")); //  "Hey wollef sroirraw"
// console.log(spinWords("This is a test")); //  "This is a test"
// console.log(spinWords("This is another test")); //  "This is rehtona test"
// console.log(spinWords("Welcome")); //  "emocleW"

// My function
function spinWords(string) {
    let arr_words = [];
    for (let word of string.split(' ')) {
        if (word.length > 4) {
            word = word.split('').reverse().join('');
        }
        arr_words.push(word)
    }
    return arr_words.join(' ');
}

//from C_W
// function spinWords(str){
//   return str.split(' ').map( w => w.length<5 ? w : w.split('').reverse().join('') ).join(' ');
// }

//----------------------------------------------------------------------------------------------------------------------

//7_kyu
// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function
// that determines whether a string that contains only letters is an isogram. Assume the empty string is
// an isogram. Ignore letter case.
// "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

// console.log(isIsogram("Dermatoglyphics")) // true
// console.log(isIsogram("isogram")) // true
// console.log(isIsogram("aba")) // false
// console.log(isIsogram("moOse")) // false

function isIsogram(str) {
    return str.length === new Set(str.toLowerCase().split('')).size
}

//----------------------------------------------------------------------------------------------------------------------

//7_kyu
// Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4
// positive integers. No floats or non-positive integers will be passed.

// For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
let arr_num = [10, 343445353, 3453445, 3453545353453] // should return 3453455.
console.log(sumTwoSmallestNumbers(arr_num));
console.log(sumTwoSmallestNumbers([-3, 5, 8, 12, 19, 22]));
console.log(sumTwoSmallestNumbers([15, 28, 4, 2, 43]));
console.log(sumTwoSmallestNumbers([19, 5, 42, 2, 77]));

// function sumTwoSmallestNumbers(numbers) {
//     let [a, b] = numbers.slice(0, 2);
//     for (let value of numbers.slice(2)){
//         if (typeof value == 'number' && value >= 0){
//             if (a > value) {
//                 if (b > a) {
//                     b = a;
//                 }
//                 a = value;
//
//             } else if (b > value){
//                 b = value;
//             }
//         }
//     }
//     return  a + b
// }

// my func v2.0
function sumTwoSmallestNumbers(numbers) {
    return numbers.filter(value => typeof value == 'number' && value >= 0)
        .sort((a, b) => a - b)
        .slice(0, 2)
        .reduce((a, b) => a + b)
}

// from C_W
// function sumTwoSmallestNumbers(numbers) {
//   var [ a, b ] = numbers.sort((a, b) => a - b)
//   return a + b
// }

//----------------------------------------------------------------------------------------------------------------------
