/**
 * This module demonstrates how to process even numbers in an array.
 * It filters out odd numbers, squares the remaining numbers, and logs the results.
 * @module evenNumberProcessor
 */

/**
 * Delays the execution of a callback function by a specified amount of time.
 * @param {function} callback - The function to be executed after the delay.
 * @param {number} delayMilliseconds - The delay in milliseconds.
 */
function delayedCallback(callback, delayMilliseconds) {
    setTimeout(callback, delayMilliseconds);
}

/**
 * Filters out odd numbers from an array and squares the remaining numbers.
 * @param {number[]} inputArray - The array of numbers to be processed.
 * @returns {number[]} An array of squared even numbers.
 */
function processEvenNumbers(inputArray) {
    return inputArray.filter(isEven).map(squareNumber);
}

/**
 * Checks if a number is even.
 * @param {number} number - The number to be checked.
 * @returns {boolean} True if the number is even, false otherwise.
 */
function isEven(number) {
    return number % 2 === 0;
}

/**
 * Squares a number.
 * @param {number} number - The number to be squared.
 * @returns {number} The squared number.
 */
function squareNumber(number) {
    return number * number;
}

/**
 * Logs the results of processing even numbers.
 * @param {string|null} error - An error message if an error occurred, null otherwise.
 * @param {number[]|null} processedResults - The array of squared even numbers, null if an error occurred.
 */
function logResults(error, processedResults) {
    if (error) {
        console.log(`ERROR: ${error}`);
    } else {
        processedResults.forEach((result) => console.log(result));
    }
}

// Define magic numbers as named constants
const DELAY_MILLISECONDS = 1000;
const START_NUMBER = 1;
const END_NUMBER = 10;
const TEST_NUMBERS = [100, 200, 300];

// Generate an array of numbers from START_NUMBER to END_NUMBER
const numbers = Array.from({ length: END_NUMBER - START_NUMBER + 1 }, (_, i) => i + START_NUMBER);

// Process even numbers and log the results
delayedCallback(() => {
    const processedResults = processEvenNumbers(numbers);
    logResults(null, processedResults);

    // Process test numbers and log the results
    delayedCallback(() => {
        const testResults = processEvenNumbers(TEST_NUMBERS);
        logResults(null, testResults);
    }, DELAY_MILLISECONDS);
}, DELAY_MILLISECONDS);