function serverCall()=>{
return fetch('https://jsonplaceholder.typicode.com/todos/1')
}
response = serverCall().then(response => response.json())
.then(json => console.log(json))
    



function serverCall()=>{
    return fetch('https://jsonplaceholder.typicode.com/todos/1')
}
const fetchResult = serverCall().then(fetchResult => fetchResult.json())
.then(console.log(json))


// {so there's basically three ways to make the request:
// 1. new XMLHttpRequest(), which never fails but no one uses,
// 2. jquery, which you'll see everywhere

// 3.using the fetch method inside the return statement of a function
// serverCall(someString){
//     return fetch("myServer.php", {data: foo="someString"});
// }

// note: you can add .then listeners onto the result variable from a fetch function, or 
// use a wrapper function that assigns a variable to the returned server data from an outer function}

// # Ways to make an ajax request

// 1. Super old way. Never fails. No one uses it anymore: new XMLHttpRequest()

// 2. jQuery

// $.ajax({
// 	method: "GET",
//   url: "/api/pages/on-my-server.php",
//   data: {
//   	foo: 'yes, please',
//   	foo2: 'yes, please'
//   },
//   complete: function() {
  
//   }
// })

// // GET: myserver.com/some/url/on-my-server.php?foo=yes,%20please&foo2=yes,%20please
// // POST: myserver.com/some/url/on-my-server.php

// 3. fetch

// function makeSomeServerCall(arg) {
//   return fetch("/some/url/on-my-server.py", {
//     data: {
//       foo: arg
//     }
//   });
// }


// const response = makeSomeServerCall('yes, please')
// 	.then((someValueFromTheServer) => {
// 		console.log(someValueFromTheServer); // whatever the server gave you
//     return someValueFromTheServer.json();
//   })
//   .then((someJsonObject) => {
// 		console.log(someJsonObject);
//   })
//   .then((someValueFromTheSecondHandler) => {
// 		console.log(someValueFromTheSecondHandler);
//   })
// ;

// console.log(response); // [object Promise]

// 4. use a library!

// - axios

// # Factoids:

// - async/await syntax: syntatic sugar for using promises in a way that makes them seem more synchronous.

// ## syntactic sugar? Wtf is that?
// var x = 1;
// x = x + 1;
// x++; // syntactic sugar over incrementing a value by 1!


// async function() {
//   const response = await makeSomeServerCall();
//   // here, response is a Promise
//   const json = response.json();
//   const nextValue = json.some.key;
//   console.log(nextValue); // whatever the server gave you
// }

// - you can chain .then calls on promises, as many times as you want to,

// - you add .catch() calls to promises
	
// const response = makeSomeServerCall()
// 	.then((someValueFromTheServer) => {
// 		console.log(someValueFromTheServer); // whatever the server gave you
//   })
//   .catch((someError) => {
  
//   	if (someError.status === 404) {
    	
//     }


// 1. new XMLHttpRequest()
// 2. jQuery
// $.ajax({
//     method: "GET",
//     url: ("myServer.php"),
//     data: {foo="someString"},
//     complete: function(){ //this is a callback function
//     }
// })
//with jquery, you just call .ajax and pass it the info it needs, 
//then tell it what to do once it's complete

// 3. fetch()
// function serverCall(arg){
//     return fetch("myServer.php",{
//         data: {foo="someString"}
//     });
// }

// results = serverCall(arg).then((someServerData)=>{
//         console.log(someServerData);
//         return someServerData.json();
//     })
//     .then((someJsonObject)=>{
//         console.log(someJsonObject);
//     })
//     .then((valueSecondHandler)=>{
//         console.log(valueSecondHandler);
//     });
//so with fetch, you call it inside the return statement of a function, passing it the 
//url and the {data} as arguments, then call the function, assigning the result to a variable
//and you can chain ".then" s that take in a value => another function that dones something


// 4. axios library (async await)
// async function(){
//     const response = await serverCall();
//     const json = response.json;
//     const nextValue = json.someKey;
//     console.log(nextValue);
// }
//using the axios library, i create an async function, that calls the serverCall function above, 
//and this is basically an event listener that makes sure that certain things don't run 
//until the data is returned from the server?

//*********************************************** */

// Ways to make an api call with js:
// 1. new XMLHttpRequest()
// 2. jQuery
    //     $.ajax({
    //         method: "GET",
    //         url: ("someUrlOnMyServer.php"),
    //         data: {
    //             foo = "someString"
    //         },

    //     //GET creates a url like: "url.php?foo=someString"
    //     //POST just looks like the url b/c no data passed in browser bar
    //     complete: function(){

    //     }
    // })
    // // 3. fetch
    // function serverCall(arg){
    //     return fetch("someUrlOnMyServer.php", {
    //         data: {foo="someString"}
    //     });
    // };
    // result = serverCall("someString").then((someValueFromServer)=>{
    //     console.log(someValueFromServer);
    //     return someValueFromServer.json();
    // })
    // .then((someJsonObject)=>{
    //     console.log(someJsonObject);
    // })
    // .then((valueFromSecondHandler)=>{
    //     console.log(valueFromSecondHandler);
    // });

    // // 4. use a library! like axios 
    // async function(){
    //     const response = await serverCall();
    //     const json = response.json();
    //     const nextValue = json.someKey;
    //     console.log(nextValue);
    // }

    // 5. if you know what errors you want to anticipate, you can add .catch()
    //in your .then chain that will catch the error instead of proceeding to
    //the next step in your chain

    

        
