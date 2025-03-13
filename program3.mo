import Float "mo:base/Float";
import Error "mo:base/Error";

actor Program3 {
    // Program 3: Exception Handling
    public func showcaseExceptionHandling() : async Text {
        try {
            // Simulate a division by zero error
            let numerator : Float = 10.0;
            let denominator : Float = 0.0;
            if (denominator == 0.0) {
                throw Error.reject("Division by zero is not allowed");
            };
            let result = numerator / denominator;
            return "Division Result: " # Float.toText(result);
        } catch (e) {
            return "Caught an exception: " # Error.message(e);
        };
    };
};

