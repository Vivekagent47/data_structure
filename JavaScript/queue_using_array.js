class Queue {
  constructor() {
    this.array = []
  }

  isEmpty() {
    return this.array.length === 0;
  }

  enqueue(item) {
    this.array.push(item);
  }

  dequeue() {
    if(this.isEmpty()) {
      return 'Queue is Empty';
    }
    return this.array.shift();
  }

  front() {
    if(this.isEmpty()) {
      return 'Queue is Empty';
    }
    return this.array[0];
  }

  printQueue() {
    let str = '';
    for(let i = 0; i < this.array.length; i++) {
      str += this.array[i] + " ";
    }
    return str;
  }
}

var queue = new Queue();

console.log(queue.dequeue());
console.log(queue.isEmpty());
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.enqueue(50);
queue.enqueue(60);
console.log(queue.front());
console.log(queue.dequeue());
console.log(queue.front());
console.log(queue.dequeue());
console.log(queue.printQueue());