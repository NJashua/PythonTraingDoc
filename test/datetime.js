// 1.)
// <!DOCTYPE html>
// <html>
// <body>

// <h2>Hey</h2>
// <p>for printing the current page</p>
// <button onclick="window.print()">Print this page..</button>
// </body>
// </html>

// 2.)
// function displayDayAndTime(){
//     const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursaday", "Friday", "Saturday"];

//     const today = new Date();
//     const day = days[today.getDay()];
//     let hour = today.getHours();
//     let minute = today.getMinutes();
//     let second = today.getSeconds();

//     const amorpm = hour>=12 ? "PM":"AM";
//     hour = hour % 12;
//     hour = hour ? hour : 12;
//     const minuteStr = minute < 10 ? "0" + minute : minute;
//     const secondStr = second < 10 ? "0" + second : second;
//     const dayStr = `Today is :${day}.`
//     const timeStr = `Current time is : ${hour} ${amorpm} : ${minuteStr} : ${secondStr}`

//     console.log(dayStr)
//     console.log(timeStr)
// }


// displayDayAndTime()
// ////////////////////////////////////////////////////////////
// 3.)
// const today = new Date();

// const day = String(today.getDate())
// const month = String(today.getMonth()+1)
// const year = today.getFullYear();

// const hyphendate = `${month}-${day}-${year}`;
// const slashdate = `${month}/${day}/${year}`;
// const datehypher = `${day}-${month}-${year}`;
// const dateslash = `${day}/${month}/${year}`;

// console.log("mm-dd-yyyy:", hyphendate);
// console.log("mm/dd/yyyy:", slashdate);
// console.log("dd-mm-yyyy:", datehypher);
// console.log("dd/mm/yyyy:", dateslash);


// 4.)
// function get_area_of_triangle(a, b, c){
//     const value= (a+b+c)/2
//     const area = Math.sqrt(value * (value-a) * (value-b) * (value-c))
//     return area
// }

// const a = 7
// const b = 6
// const c = 5

// const get_area = get_area_of_triangle(a,b,c)
// console.log(get_area)

// 5.)

// const array = ["james", "bond"]
// console.log(array.join("*"))

// 6.)