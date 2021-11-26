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


// Ways to make an api call with js:
// 1. new XMLHttpRequest()
// 2. jQuery
        $.ajax({
            method: "GET",
            url: ("someUrlOnMyServer.php"),
            data: {
                foo = "someString"
            },

        //GET creates a url like: "url.php?foo=someString"
        //POST just looks like the url b/c no data passed in browser bar
        complete: function(){

        }
    })
    // 3. fetch
    function serverCall(arg){
        return fetch("someUrlOnMyServer.php", {
            data: {foo="someString"}
        });
    };
    result = serverCall("someString").then((someValueFromServer)=>{
        console.log(someValueFromServer);
        return someValueFromServer.json();
    })
    .then((someJsonObject)=>{
        console.log(someJsonObject);
    })
    .then((valueFromSecondHandler)=>{
        console.log(valueFromSecondHandler);
    });

    // 4. use a library! like axios 
    async function(){
        const response = await serverCall();
        const json = response.json();
        const nextValue = json.someKey;
        console.log(nextValue);
    }

    // 5. if you know what errors you want to anticipate, you can add .catch()
    //in your .then chain that will catch the error instead of proceeding to
    //the next step in your chain

    

        
