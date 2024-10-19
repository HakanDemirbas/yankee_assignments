function factorial(num) {
  if (num < 0)
    return "Not a factorial number"
  if(num == 0)
    return 1
  else {
    return num * factorial(num-1)
  }
  
}

// if(num < 0){
//   return "Not a factorial number"
// } else 
module.exports = factorial;
console.log(factorial(5))

/*
-If less than 0 return not a factorial
-If factorial is equal to 0 then return 1
-set a count for every time it iterates to find the factorial
-create a for loop and decrement

Factorial of n = n! = n × (n – 1) × (n – 2) × … × 1


Examples:
0! = 1
1! = 1
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 =  24
*/