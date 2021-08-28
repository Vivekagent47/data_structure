function binary(arr, left, right, data) {
  if (left <= right) {
    let mid = left + Math.floor((right - left) / 2);

    if (arr[mid] === data) {
      return mid;
    }
    if (arr[mid] > data) {
      return binary(arr, left, mid - 1, data);
    }
    return binary(arr, mid + 1, right, data);
  }
  return -1;
}

function binarySearch(arr, data) {
  if (arr.length === 0) {
    return -1;
  }
  return binary(arr, 0, arr.length - 1, data);
}

console.log(binarySearch([2, 3, 4, 10, 40], 11));
