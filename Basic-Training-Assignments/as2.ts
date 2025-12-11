// // Calculator Interface
// interface Calculator {
//     add(a: number, b: number): number;
//     multiply(a: number, b: number): number;
//   }
  
//   // Implementation of Calculator
//   class BasicCalculator implements Calculator {
//     add(a: number, b: number): number {
//       return a + b;
//     }
  
//     multiply(a: number, b: number): number {
//       return a * b;
//     }
//   }
  
//   // Using the Calculator
//   const calc: Calculator = new BasicCalculator();
//   console.log(calc.add(3, 5)); // Output: 8
//   console.log(calc.multiply(4, 6)); // Output: 24
  
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Shape Interface
interface Shape {
    area(): number;
  }
  
  // Circle Implementation
  class Circle implements Shape {
    constructor(private radius: number) {}
    area(): number {
      return Math.PI * this.radius * this.radius;
    }
  }
  
  // Rectangle Implementation
  class Rectangle implements Shape {
    constructor(private length: number, private width: number) {}
    area(): number {
      return this.length * this.width;
    }
  }
  
  // Using Shapes
  const circle: Shape = new Circle(5);
  const rectangle: Shape = new Rectangle(4, 6);
  
  console.log(circle.area()); // Output: 78.54
  console.log(rectangle.area()); // Output: 24
  
