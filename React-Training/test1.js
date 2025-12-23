// public static int sum(int[] arr) {
//     int total = 0;
//     for (int i = 0; i <= arr.length; i++) {
//         total += arr[i];
//     }
//     return total;
// }

// This code has an error: the loop condition should be i < arr.length, not i <= arr.length.
// Corrected code:

// public static int sum(int[] arr) { 
//     int total = 0;
//     for (int i = 0; i < arr.length; i++) {
//         total += arr[i];
//     }
//     return total;
// }