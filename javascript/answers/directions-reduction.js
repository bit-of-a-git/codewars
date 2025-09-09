function dirReduc(arr){
  const opposites = {
    NORTH: "SOUTH",
    SOUTH: "NORTH",
    WEST: "EAST",
    EAST: "WEST",
  }
  const stack = []
  for (let i = 0; i < arr.length; i++) {
    // check if item at i+1 is the opposite of item at i
    // if not, add. If so, delete 
    if (opposites[arr[i]] !== stack[stack.length - 1] ) {
        stack.push(arr[i])
    } else {
      stack.pop()
    }
  }
  return stack
}