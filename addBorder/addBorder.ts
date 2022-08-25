export function addBorder(picture: string[]): string[] {
    for (let i = 0; i < picture.length; i ++) {
        picture[i] = '*'.concat(picture[i], '*')
    }
    picture.unshift('*****')
    picture.push('*****')
    return picture
}

console.log(addBorder(["abc", "ded"]));