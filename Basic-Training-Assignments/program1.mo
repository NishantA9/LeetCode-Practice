import Nat "mo:base/Nat"; // For integer operations
import Float "mo:base/Float"; // For float operations
import Text "mo:base/Text"; // For string operations
import Bool "mo:base/Bool"; // For boolean operations
import Int "mo:base/Int";

persistent actor Program1 {
    // Program 1: Data Types and Built-in Methods
    public func showcaseDataTypes() : async Text {
        // 1. Integer (Int)
        let intValue : Int = 42;
        let intSum = intValue + 8; // Addition (built-in method 1 for Int)
        let intToString = Int.toText(intValue); // Convert Int to Text (built-in method 2 for Int)

        // 2. Float
        let floatValue : Float = 3.14;
        let floatProduct = floatValue * 2.0; // Multiplication (built-in method 1 for Float)
        let floatToString = Float.toText(floatValue); // Convert Float to Text (built-in method 2 for Float)

        // 3. Text (String)
        let stringValue : Text = "Hello, Motoko!";
        let replacedString = Text.replace(stringValue, #text "Motoko", "World"); // Replace substring (built-in method 1 for Text)
        let stringLength = Text.size(stringValue); // Get length of string (built-in method 2 for Text)

        // 4. Boolean (Bool)
        let boolValue : Bool = true;
        let negatedBool = Bool.lognot(boolValue); // Negate boolean (built-in method 1 for Bool)
        let boolToString = Bool.toText(boolValue); // Convert Bool to Text (built-in method 2 for Bool)

        // Return a summary of the manipulations
        return "Int Sum: " # Int.toText(intSum) # ", Int to String: " # intToString # "\n" #
               "Float Product: " # Float.toText(floatProduct) # ", Float to String: " # floatToString # "\n" #
               "Replaced String: " # replacedString # ", String Length: " # Nat.toText(stringLength) # "\n" #
               "Negated Bool: " # Bool.toText(negatedBool) # ", Bool to String: " # boolToString;
    };
};