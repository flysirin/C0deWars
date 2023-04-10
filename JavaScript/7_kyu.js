// (1) 6_kyu
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

// (2) 7_kyu
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

// (3) 7_kyu
// Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4
// positive integers. No floats or non-positive integers will be passed.

// For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
let arr_num = [10, 343445353, 3453445, 3453545353453] // should return 3453455.
// console.log(sumTwoSmallestNumbers(arr_num));
// console.log(sumTwoSmallestNumbers([-3, 5, 8, 12, 19, 22]));
// console.log(sumTwoSmallestNumbers([15, 28, 4, 2, 43]));
// console.log(sumTwoSmallestNumbers([19, 5, 42, 2, 77]));

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
// let [a, b] = [-3, 5, 8, 12, 19, 22];
// console.log(a, b); // -3 5

//----------------------------------------------------------------------------------------------------------------------

// (4) 7_kyu
// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
// Examples
// console.log(highAndLow("1 2 3 4 5"));  // return "5 1"
// console.log(highAndLow("1 2 -3 4 5")); // return "5 -3"
// console.log(highAndLow("1 9 3 4 -5")); // return "9 -5"
// console.log(highAndLow("42")); // return "9 -5"

// my decision ...
// function highAndLow(str_numbers) {
//     if (str_numbers.split(" ").length > 1) {
//         return str_numbers.split(" ").reduce(function (acc, item, index, arr) {
//             return `${Math.max(...arr)} ${Math.min(...arr)}`
//         })
//     } else return str_numbers + ' ' + str_numbers
// }

// by C_W
function highAndLow(numbers) {
    numbers = numbers.split(' ');
    return `${Math.max(...numbers)} ${Math.min(...numbers)}`;
}

//----------------------------------------------------------------------------------------------------------------------

// (5) 7_kyu
// Given the triangle of consecutive odd numbers:
//              1
//           3     5
//        7     9    11
//    13    15    17    19
// 21    23    25    27    29
// ...
// Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
// 1 -->  1
// 2 --> 3 + 5 = 8

// my func
function rowSumOddNumbers(n) {
    let value = 1;
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= i; j++) {
            value += 2
        }
    }
    return value * (n + 1) - 1
}


// from C_W
// function rowSumOddNumbers(n)
// {
//   /* The rows' start numbers are Hogben's centered polygonal numbers:
//      1, 3, 7, 13, 21, 31, 43 = b[n] = n^2 - n + 1.
//      The sum of one row is given by:
//      s[n] = n^2 + n(b[n] - 1).
//      s[n] = n^2 + n(n^2 - n + 1 - 1)
//           = n^2 + n(n^2 - n)
//           = n^2 + n^3 - n^2
//           = n^3
//      ... oh. */
//   return n * n * n;
// }

// console.log(rowSumOddNumbers(42))

//----------------------------------------------------------------------------------------------------------------------

// (6) 7_kyu

// Write a function that takes an array of strings as an argument and returns a sorted array containing
// the same strings, ordered from shortest to longest.
// All of the strings in the array passed to your function will be different lengths, so you will not have to
// decide how to order multiple strings of the same length.

function sortByLength(array) {
    return array.sort((a, b) => a.length - b.length)
}

// console.log(sortByLength(["Telescopes", "Glasses", "Eyes", "Monocles"]))

//----------------------------------------------------------------------------------------------------------------------

// (7) 7_kyu

// Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines
// if a given non-negative integer is a power of two. From the corresponding Wikipedia entry:
// a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with
// number two as the base and integer n as the exponent.
// You may assume the input is always valid.
// Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.
// isPowerOfTwo(1024) // -> true
// isPowerOfTwo(4096) // -> true
// isPowerOfTwo(333)  // -> false

function isPowerOfTwo(n) {
    return Number.isInteger(Math.log2(n))
}

// console.log(isPowerOfTwo(1024));

//----------------------------------------------------------------------------------------------------------------------

// (8) 7_kyu

// Dot Calculator
// You have to write a calculator that receives strings for input. The dots will represent the number in the equation.
// There will be dots on one side, an operator, and dots again after the operator. The dots and the operator
// will be separated by one space.
// Here are the following valid operators :
// + Addition
// - Subtraction
// * Multiplication
// // Integer Division
// You'll have to return a string that contains dots, as many the equation returns. If the result is 0,
// return the empty string. When it comes to subtraction, the first number will always be greater than or equal
// to the second number.
// * "..... // ."              => "....."
// * ". // .."                 => ""
// * ".. - .."                 => ""

// My func
function dotCalculator(equation) {
    let arr = equation.split(' ');
    let res = 0;
    if (arr[1] === '+') {
        res = (arr[0].length + arr[2].length);
    } else if (arr[1] === '-') {
        res = (arr[0].length - arr[2].length);
    } else if (arr[1] === '*') {
        res = (arr[0].length * arr[2].length);
    } else if (arr[1] === '//') {
        res = Math.floor(arr[0].length / arr[2].length);
    }
    return '.'.repeat(res);
}

// from C_W
// const dotCalculator = (equation) => {
//   const operations = {
//     '+' : (a, b) => a + b,
//     '-' : (a, b) => a - b,
//     '*' : (a, b) => a * b,
//     '//': (a, b) => a / b,
//   };
//   const [left, operator, right] = equation.split(' ');
//   return '.'.repeat(operations[operator](left.length, right.length));
// }

// console.log(dotCalculator("..... // .."))

//----------------------------------------------------------------------------------------------------------------------

// (9) 7_kyu

// Write a small function that returns the values of an array that are not odd.
// All values in the array will be integers. Return the good values in the order they are given.

function noOdds( values ){
  return values.filter(value => !(value % 2))
}

//----------------------------------------------------------------------------------------------------------------------

// (10) 7_kyu

// Given an array of numbers, return the difference between the largest and smallest values.
// For example:
// [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
// [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).
// The array will contain a minimum of two elements. Input data range guarantees that max-min will cause no
// integer overflow.

function betweenExtremes(numbers) {
    return Math.max(...numbers) - Math.min(...numbers)
}

// console.log(betweenExtremes([1, 434, 555, 34, 112]))
