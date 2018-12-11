let request = require('request');

let password = [`bla`, `$'2'2'1'<>`, 'fjdjdjss', 'ß∆ß∆œ¨˙≈˜ˆå¨∑¨∂˙∑¨œˆ∂˜∂¨ˆœå', 'iloveu']

for (let i = 0; i < password.length; i++) {
	request({method: "post" ,url: `http://localhost:4000/check_password`, json: true, body: {password: password[i]}}, function(err, httpResponse, body) {
		console.log("password")
		console.log(body)
	})
}

let email = ['bla#.com', 'bla@gmail.com', ".com", "dasdf", "s.s"]

for (let i = 0; i < password.length; i++) {
	request({method: "post" ,url: `http://localhost:4000/login`, json: true, body: {email: email[i], password: password[i]}}, function(err, httpResponse, body) {
		console.log("login")
		console.log(body)
	})
}

let first_name = ['bla', 'd', 'there', 'their', 'that']
let last_name = ['d', 'sdf', 'asdfa', '∂∆∂∆∂∆', 'djdj']

for (let i = 0; i < password.length; i++) {
	request({method: "post" ,url: `http://localhost:4000/login`, json: true, body: {first_name: first_name, last_name: last_name , email: email[i], password: password[i]}}, function(err, httpResponse, body) {
		console.log("login")
		console.log(body)
	})
}