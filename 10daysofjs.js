'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    if (typeof(s)==="string"){
        console.log(s
        .split("")
        .reverse()
        .join("")
        )
    }
    else{
        console.log("s.split is not a function");
        console.log(s);
    }
    
}

/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    if (a===0){
        throw Error("Zero Error");
    }
    if (a<0){
        throw Error("Negative Error");
    }
    else{
        return "YES";
    }
    
}
class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}
Rectangle.prototype.area = function() {
    return this.w * this.h;
};

class Square extends Rectangle{
    constructor(s) {
        super(s);
        this.h = s;
        this.w = s;
}
}
/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */