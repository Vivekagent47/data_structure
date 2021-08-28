class Stack {
  constructor() {
    this.stack = [];
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  push(data) {
    this.stack.push(data);
  }

  pop() {
    if (this.stack.length === 0) {
      return "Stack is underflow i.e its empty";
    }
    return this.stack.pop();
  }

  print() {
    if (this.stack.length === 0) {
      console.log("Stack is underflow i.e its empty");
    } else {
      console.log(this.stack);
    }
  }
}

let stack = new Stack();
