// import Debug "mo:base/Debug";

// // Declare the Calculator interface
// type Calculator = {
//   add : (Int, Int) -> Int;
//   multiply : (Int, Int) -> Int;
// };

// // Implementation of Calculator (hidden inside a module)
// module BasicCalculator = {
//   public func add(a : Int, b : Int) : Int {
//     return a + b; // Simple addition
//   };

//   public func multiply(a : Int, b : Int) : Int {
//     return a * b; // Simple multiplication
//   };
// };

// // Using the Calculator (user interacts only with the interface)
// let calc : Calculator = {
//   add = BasicCalculator.add;
//   multiply = BasicCalculator.multiply;
// };

// Debug.print("Sum: " # debug_show(calc.add(3, 5))); // Output: 8
// Debug.print("Product: " # debug_show(calc.multiply(4, 6))); // Output: 24

// example 2

import Debug "mo:base/Debug";
import Float "mo:base/Float";

// Declare the Shape interface
type Shape = {
  area : () -> Float;
};

// Implementation of Circle (hidden inside a module)
module Circle = {
  public func create(radius : Float) : Shape {
    return {
      area = func() : Float {
        return Float.pi * radius * radius; // Area of a circle
      };
    };
  };
};

// Implementation of Rectangle (hidden inside a module)
module Rectangle = {
  public func create(length : Float, width : Float) : Shape {
    return {
      area = func() : Float {
        return length * width; // Area of a rectangle
      };
    };
  };
};

// Using Shapes (user interacts only with the interface)
let circle : Shape = Circle.create(5.0);
let rectangle : Shape = Rectangle.create(4.0, 6.0);

Debug.print("Circle Area: " # debug_show(circle.area())); // Output: 78.53981633974483
Debug.print("Rectangle Area: " # debug_show(rectangle.area())); // Output: 24.0