export function addTwoDigits(n: any): number {
    n.toString()
    let numbers = n.split("")
    for (let i = 0; i < numbers.length; i ++) {
        parseInt(numbers[i])
    }
    
}

// console.log(addTwoDigits(29));