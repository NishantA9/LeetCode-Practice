import Array "mo:base/Array";
import List "mo:base/List";
import Nat "mo:base/Nat";

persistent actor Program2 {
    // Program 2: Data Structures and Control Structures
    public func showcaseDataStructuresAndControl() : async Text {
        // Array
        let array : [Nat] = [1, 2, 3, 4, 5];
        var arraySum : Nat = 0;
        for (value in array.vals()) {
            arraySum += value; // Summing array elements using a for loop
        };

        // List
        let list = List.fromArray<Nat>([10, 20, 30]);
        var listProduct : Nat = 1;
        List.iterate<Nat>(list, func (x : Nat) {
            listProduct *= x; // Multiplying list elements using iteration
        });

        // If-Else Control Structure
        let largestValue = if (arraySum > listProduct) {
            "Array Sum is larger";
        } else {
            "List Product is larger";
        };

        // Lambda Function
        let lambdaExample = func (x : Nat, y : Nat) : Nat { x + y };
        let lambdaResult = lambdaExample(arraySum, listProduct);

        return "Array Sum: " # Nat.toText(arraySum) # ", List Product: " # Nat.toText(listProduct) # ", " # largestValue # ", Lambda Result: " # Nat.toText(lambdaResult);
    };
};