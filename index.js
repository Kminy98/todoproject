// window.onload = async function loadTodo(){
//     const response = await fetch('http://127.0.0.1:8000/todo/', {method:'GET'})

//     response_json = await response.json()

//     console.log(response_json)

//     const todo = document.getElementById("todo")

//     response_json.forEach(element => {
//         const newTodo = document.createElement("div")
//         newTodo.innerText = element.title
//         todo.appendChild(newTodo)
//     });


// }

window.onload= ()=>{
    const payload = localStorage.getItem("payload");
    console.log(payload)
    const payload_parse = JSON.parse(payload)
    console.log(payload_parse)

    const intro = document.getElementById("intro")
    intro.innerText = payload_parse.email
}