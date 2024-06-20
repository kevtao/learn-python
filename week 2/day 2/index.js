let length = 16;
let weight = 7.5;
let color = "Yellow";
// let lastName = "Johnson";
let x = true;
let y = false;
const person = { firstName: "John", lastName: "Doe" };
const cars = ["Saab", "Volvo", "BMW"];
const date = new Date("2022-03-25");

let z = 16 + "Volvo";
console.log(`${z}`);
// prints 16volvo
let a = "Volvo" + 16 + 4;
// turns all into strings when it reaches one
let b = 16 + 4 + "Volvo";
// does not turn into string until it reaches string

let dynamicvar;
dynamicvar = 5;
dynamicvar = "john";

// Single quotes inside double quotes:
let answer1 = "He is called 'Johnny'";

// Double quotes inside single quotes:
let answer2 = 'He is called "Johnny"';

let x1 = 34.0;
let x2 = 34;
let x3 = 3.14;
// ignores float with 0 value at decimal

let expon = 123e5;
console.log(`${expon}`);

let bitint = BigInt("123456789012345678901234567890");
//stores value greater than 64 bit values

let vala = 5;
let valb = 5;
let valc = 6;
// (vala == valb)       Returns true
// (vala == valc)       Returns false

typeof ""; // Returns "string"
typeof "John"; // Returns "string"
typeof "John Doe"; // Returns "string"
typeof 0; // Returns "number"
typeof 314; // Returns "number"
typeof 3.14; // Returns "number"
typeof 3; // Returns "number"
typeof (3 + 4); // Returns "number"

let bob; // Value is undefined, type is undefined
joe = undefined; // Value is undefined, type is undefined
let string = ""; // The value is "", the typeof is "string"

const johndoe = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
const person1 = {};
person1.firstName = "John";
person1.lastName = "Doe";
person1.age = 50;
person1.eyeColor = "blue";
const person2 = new Object();
person2.firstName = "John";
person2.lastName = "Doe";
person2.age = 50;
person2.eyeColor = "blue";

person.lastName;
person["lastName"];
// gets person last name
johndoe.firstName;

// n = person changes to n is a change to person and vice versa
const n = person;
n.age = 10;

delete person.age; // or delete person["age"];

myObj = {
  name: "john",
  myCars: {
    car1: "ford",
    car2: "BMW",
    car3: "Fiat",
  },
};
myObj.myCars.car2;
// or
myObj.myCars["car2"];
// or
myObj["myCars"]["car2"];
// or
let p1 = "myCars";
let p2 = "car2";
myObj[p1][p2];

bob = johndoe.fullName(); // returns persons full name
bob = johndoe.fullName; // returns "person.fullName;"
Doe = johndoe.lastName.toUpperCase;
class people {
  constructor(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
  }
}
const myFather = new people("John", "Doe", 50, "blue");
const myMother = new people("Doe", "John", 48, "green");
const mySelf = new people("Johnny", "Doe", 22, "green");
console.log(myFather.firstName);
myFather.nationality = "English";
myMother.changeName = function (name) {
  this.lastName = name;
};
people.prototype.changeName = function (name) {
  this.lastName = name;
};

myMother.changeName("Doe");

// new Object()   // A new Object object
// new Array()    // A new Array object
// new Map()      // A new Map object
// new Set()      // A new Set object
// new Date()     // A new Date object
// new RegExp()   // A new RegExp object
// new Function() // A new Function object

//   \'	  '	  Single quote
//   \"	  "	  Double quote
//   \\	  \	  Backslash
//   \b	  Backspace
//   \f	  Form Feed
//   \n	  New Line
//   \r	  Carriage Return
//   \t	  Horizontal Tabulator
//   \v	  Vertical Tabulator

let newst = new String("John");

// == regular compare
// === compares and compares type of object

let txt = "Hello World";
let le = txt.length;
let char = txt.charCodeAt(0);
let cha = txt[0];
let letter = txt.charAt(2);
// or
let lette = txt[2];
txt[0] = "A"; // Does not work
let part1 = txt.slice(7, 8);
let part2 = txt.slice(7);
let part3 = txt.slice(-5);
let part4 = txt.slice(-8, -6);
console.log(`${part1}`);
console.log(`${part2}`);
console.log(`${part3}`);
console.log(`${part4}`);

let part = txt.substring(-3, 5); // -3 treated as 0
let tex = txt.toUpperCase();
let texs = txt.toLowerCase();

let bill = "Hello";
let bill2 = "World";
let bill3 = bill.concat(" ", bill2);

tes = "        Hello       ".concat(" ", "World!         ");
let te = tes.trim();
let tx = tes.trimStart();
let ex = tes.trimEnd();
let numb = 5;
let xt = numb.toString();
let padded = xt.padStart(2, "o");
let paddedend = xt.padEnd(4, "O");
let result = tes.repeat(2);
console.log(`${te}`);
console.log(`${tx}`);
console.log(`${ex}`);
console.log(`${padded}`);
console.log(`${paddedend}`);
console.log(`${result}`);

let newtes = tes.replace("Hello", "World!");
let newtes1 = tes.replace(/hello/i, "World!"); // case sensetive
let newtes2 = tes.replace(/o/g, "e"); // global
console.log(`${newtes}`);
console.log(`${newtes1}`);
console.log(`${newtes2}`);

let text = "a,b c,d|e,f";

o = text.split(","); // Split on commas
t = text.split(" "); // Split on spaces
q = text.split("|"); // Split on pipe
console.log(`${o[1]}`);
let index = text.indexOf("a");
let indexl = text.lastIndexOf("b");
let indexx = text.indexOf("c", 7); // 15 is starting position
text.search("d");
text.match("ain");
text.match(/ain/g);
text.match(/ain/gi); // global and case sensitive
const iterator = text.matchAll("c");
const iterators = text.matchAll(/c/g);
text.includes("world");
text.includes("world", 12); // starts at position 12
text.startsWith("a"); // checks for match
text.startsWith("d", 5);
text.endsWith("c");
text.endsWith("d", 11); // checks the word
// does not convert srtings to numbers when adding

let r = 100 / "Apple";
e = isNaN(r); // is not a number NAN is a number so typeof NaN produces number
console.log(`${e}`);
typeof Infinity; // produces number

let myNumber = 32; // equal with == but not ===
let num2 = new Number(123);
myNumber.toString(32);
myNumber.toString(16);
myNumber.toString(12);
myNumber.toString(10);
myNumber.toString(8);
myNumber.toString(2);

// let num3 = 5n;
// let fail = Number(x) / 2;

let num3 = 5n;
let num4 = Number(num3) / 2;
console.log(`${num4}`);
let num5 = 9007199254740992 === 9007199254740993;
console.log(`${num5}`); // true becuase max int limit
let numin = Number.MAX_SAFE_INTEGER;
let numax = Number.MIN_SAFE_INTEGER;
console.log(`${numin}`);
console.log(`${numax}`);
Number.isInteger(10); // checks if integer
Number.isInteger(10.5); // false
Number.isSafeInteger(10); // checks if in min / max
Number.isSafeInteger(12345678901234567890); // false

let nums = 123;
nums.toString();
(123).toString();
(100 + 23).toString(); // adds then converts
let nums1 = 9.656;
nums1.toExponential(2); // 2 and 4 decid chars after decimal point as exponential
nums1.toExponential(4);
nums1.toFixed(0); // rounds to the specified number of decimals
nums1.toFixed(2);
nums1.toPrecision(2); // sets to specified length
nums1.toPrecision(4);
(100 + 23).valueOf(); // returns value of num
Number("John"); // nan   turns string or variable into number
Number("10 33"); // nan
Number("10,33"); // nan
Number("10.33"); // 10.333
let dat = new Date("1970-01-01"); //    this time is base  converts time to miliseconds
parseInt("-10.33"); // converts strings to whole numbers ignores everything after first number
parseInt("10");
parseInt("10.33");
parseInt("10 20 30");
parseInt("10 years");
parseInt("years 10");
parseFloat("10"); // same thing but as integer
parseFloat("10.33");
parseFloat("10 20 30");
parseFloat("10 years");
parseFloat("years 10");

let tiny = Number.EPSILON; // smalest number greater than 1 then take the difference
let A = Number.POSITIVE_INFINITY; // returns infinity
let B = Number.NEGATIVE_INFINITY; // returns -infinity

// 4 ways for an arrray
const cars1 = ["Saab", "Volvo", "BMW"];
const cars2 = ["Saab", "Volvo", "BMW"];
const cars3 = [];
cars3[0] = "Saab";
cars3[1] = "Volvo";
cars3[2] = "BMW";
const cars4 = new Array("Saab", "Volvo", "BMW");

//pulling from arrays
let car = cars1[0];
// changing items
cars1[0] = "Opel";
// creating a string from arrays
cars1.toString();
// or
cars1; // typeof retursn object
// can have funcitons in an array
const myArray = [];
myArray[0] = Date.now;
let lengths = cars1.length; // how many items in an array
cars1[cars1.length - 1]; // last item
cars1[1]; // first item
cars1.push("Ford");
cars1[cars1.length] = "toyota";
cars1[6] = "car"; // creats holes that produce undefined

Array.isArray(cars1); // checks if array
//or
cars1 instanceof Array;

let car2 = cars1[2];

cars1.join(" * "); // joins items with " * "
cars1.pop(); // removes last item   push adds item
cars1.shift(); // removes firs item and shifts other items to front   unshift adds item to begiing
delete cars1[0]; // deltes it and creates a undefined hole

cars1.copyWithin(2, 0); // copies to index mentioned on left to index on right overwriting values
gh = cars2.copyWithin(2, 0, 2);
console.log(`${gh}`);

const fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi", "Papaya"];
result = fruits.copyWithin(2, 0, 4);
console.log(result);

fruits.splice(2, 0, "Lemon", "Kiwi"); // adds items to array splice(start, delete count, item1, item2, ...)
const citrus = fruits.slice(1); // shifts item at (index 1 to end of array) to new array but keeps in regular array as well
const citrus1 = fruits.slice(1, 4); // shifts item at index 1 to index 4 but not index 4 itself to new array keeps in old array

const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction); // finds value
let firstindex = numbers.find(myFunction); // finds index of value

function myFunction(value, index, array) {
  return value > 18;
}
fruits.sort(); // sorts an array
fruits.reverse(); // reverses the elements

const points = [40, 100, 1, 5, 25, 10];
points.sort(function (a, b) {
  return a - b;
}); // sorts so it doesnt get messed up as 4 is bigger than 1 but 100 is bigger than 40
points.sort(function (a, b) {
  return b - a;
}); // decsending order
points.sort(function (a, b) {
  return 0.5 - Math.random();
});

for (let i = points.length - 1; i > 0; i--) {
  let j = Math.floor(Math.random() * (i + 1));
  let k = points[i];
  points[i] = points[j];
  points[j] = k;
}

const myArrayMin = (arr) => {
  let len = arr.length;
  let min = Infinity;
  while (len--) {
    if (arr[len] < min) {
      min = arr[len];
    }
  }
  return min;
};
myArrayMin([3, 1, 6]);
function myArrayMax(arr) {
  let len = arr.length;
  let max = -Infinity;
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}

const carsyear = [
  { type: "volvo", year: 2016 },
  { type: "saab", year: 2001 },
  { type: "mw", year: 2010 },
];
bob = carsyear.sort(function (a, b) {
  let x = a;
  let y = b;
  if (x < y) {
    return -1;
  }
  if (x > y) {
    return 1;
  }
  return 0;
});
console.log(bob);

const numbers1 = [45, 4, 9, 16, 25];
function myFunctionv(value) {
  return value * 2;
}
function myFunctiona(value) {
  return value > 18;
}
function myFunction(total, value) {
  return total + value;
}
function myFunctiono(value) {
  return value > 18;
}
function myFunctions(value) {
  return value > 18;
}
let allOver18 = numbers.every(myFunctiono);
let sums = numbers.reduce(myFunction, -14);
const over18 = numbers.filter(myFunctiona);
const numbers2 = numbers1.map(myFunctionv);
let sumr = numbers.reduceRight(myFunction);
let someOver18 = numbers.some(myFunctions);
console.log(numbers2);
console.log(over18);
console.log(sums);
console.log(sumr);
console.log(allOver18);
console.log(someOver18);

const myArra = [1, 2, 3, 4, 5, 6];
const newArra = myArra.flatMap((x) => x * 2);

df = Array.from("ABCDEFG");
console.log(df);

let tsxt = "";
const keys = fruits.keys();
for (let x of keys) {
  tsxt += x + " ";
}
console.log(tsxt);

const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "May"];

const year = [...q1, ...q2, ...q3, ...q4];
console.log(year);

const d = new Date("2024-06-19");
new Date();
// new Date(year,month)
// new Date(year,month,day)
// new Date(year,month,day,hours)
// new Date(year,month,day,hours,minutes)
// new Date(year,month,day,hours,minutes,seconds)
// new Date(year,month,day,hours,minutes,seconds,ms)
// new Date(milliseconds)

const da = new Date(-100000000000); // jan 01 1970 minus 100000000000 milisecond

const dates = new Date("2015-03-25T12:00:00Z");
const day = new Date("Mar 25 2015"); // month can be written full as well and switch position with day commas ignored names case insenstive

let msec = Date.parse("March 21, 2012");
const dayinms = new Date(msec);

d.getFullYear();
d.getMonth();
d.getDate(); // day of the month
d.getHours();
d.getMinutes();
d.getSeconds();
d.getMilliseconds(); // between 0 and 999
d.getDay(); // day of the week
d.getTime(); // since 1970 jan 1
let ms = Date.now(); // same as get time

let diff = d.getTimezoneOffset(); // diff in minutes between local time and utc

d.setFullYear(2020); // can also set month and day use commas
d.setMonth(11);
d.setDate(d.getDate() + 50);
d.setHours(22);
d.setMinutes(30);
d.setSeconds(30);

let texts = "";
const today = new Date();
const someday = new Date();
someday.setFullYear(2100, 0, 14);

if (someday > today) {
  texts = "Today is before January 14, 2100.";
} else {
  texts = "Today is after January 14, 2100.";
}
console.log(texts);

const hello = (name, msg) => {
  console.log(`hi ${name}, ${msg}`);
};
hello("lan ga", "you suck");

const originalArray = [1, 2, 3];
const copiedArray1 = originalArray;
const copiedArray2 = [...originalArray];
copiedArray1[1] = 4;
console.log(copiedArray1); // [1, 4, 3]
console.log(copiedArray2); // [1, 2, 3]

const originalObject = { name: "lan ba", smarts: "dumb" };
const copiedObject1 = originalObject;
const copiedObject2 = { ...originalObject };
copiedObject1.smarts = "stupid";
console.log(copiedObject1);
console.log(copiedObject2);

const users = [
  { name: "Wenwei", age: 48 },
  { name: "Sean", age: 18 },
  { name: "Kevin", age: 16 },
];
const over20 = users.filter((x) => x.age > 20);
const ages = users.map((x) => x.age);
console.log(ages);
console.log(JSON.stringify(over20));

const vehicles = ["mustang", "f-150", "expedition"];

// old way
const car1 = vehicles[0];
const truck = vehicles[1];
const suv = vehicles[2];

// new way
const [car_1, truck1, suv1] = vehicles;
//or
const [car_2, , suv2] = vehicles;

function calculate(a, b) {
  const add = a + b;
  const subtract = a - b;
  const multiply = a * b;
  const divide = a / b;

  return [add, subtract, multiply, divide];
}

const [add, subtract, multiply, divide] = calculate(4, 7);
