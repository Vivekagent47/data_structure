function stackUsingLL() {
  //Node
  let Node = function (elm) {
    this.element = elm;
    this.next = null;
  };
  let length = 0;
  let head = null;

  this.push = function (elm) {
    //Create a new node
    let node = new Node(elm),
      current;

    current = head;
    node.next = current;
    head = node;

    length++;
  };

  this.pop = function () {
    let current = head;

    if (current) {
      let elm = current.element;
      current = current.next;
      head = current;
      length--;
      return elm;
    }

    return null;
  };

  this.peek = function () {
    if (head) {
      return head.element;
    }

    return null;
  };

  this.toArray = function () {
    let arr = [];
    let current = head;
    while (current) {
      arr.push(current.element);
      current = current.next;
    }

    return arr;
  };

  this.isEmpty = function () {
    return length === 0;
  };

  this.size = function () {
    return length;
  };

  this.clear = function () {
    head = null;
    length = 0;
  };
}
