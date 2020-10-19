function generate_first_matrix(){
    let table_container = document.getElementById("first-matrix-table")
    table_container.innerHTML = ""

    let row = parseInt(document.getElementById("first-matrix-row").value)
    let column = parseInt(document.getElementById("first-matrix-column").value)

    for(let i = 0; i < row; i++){
        let tr = document.createElement("tr")
        for (let j = 0; j < column; j++){
            let td = document.createElement("td")
            let entry_field = document.createElement("input")
            entry_field.className = "table-field"
            entry_field.id = "field-first-matrix-" + i + "-" + j
            td.appendChild(entry_field)
            tr.appendChild(td)
        }
        table_container.appendChild(tr);
    }
}

function generate_second_matrix(){
    let table_container = document.getElementById("second-matrix-table")
    table_container.innerHTML = ""

    let row = parseInt(document.getElementById("second-matrix-row").value)
    let column = parseInt(document.getElementById("second-matrix-column").value)

    for(let i = 0; i < row; i++){
        let tr = document.createElement("tr")
        for (let j = 0; j < column; j++){
            let td = document.createElement("td")
            let entry_field = document.createElement("input")
            entry_field.className = "table-field"
            entry_field.id = "field-second-matrix-" + i + "-" + j
            td.appendChild(entry_field)
            tr.appendChild(td)
        }
        table_container.appendChild(tr);
    }
}

function generate_result_matrix(row, column){
    let table_container = document.getElementById("result-matrix-table")
    table_container.innerHTML = ""

    for(let i = 0; i < row; i++){
        let tr = document.createElement("tr")
        for (let j = 0; j < column; j++){
            let td = document.createElement("td")
            let entry_field = document.createElement("input")
            entry_field.className = "table-field"
            entry_field.id = "field-result-matrix-" + i + "-" + j
            td.appendChild(entry_field)
            tr.appendChild(td)
        }
        table_container.appendChild(tr);
    }
}

function generate_value_first_matrix(){
    let row = parseInt(document.getElementById("first-matrix-row").value)
    let column = parseInt(document.getElementById("first-matrix-column").value)

    for(let i = 0; i < row; i++){
        for (let j = 0; j < column; j++){
           let id = "field-first-matrix-" + i + "-" + j
           document.getElementById(id).value = getRandomNumber(1, 50)
        }
    }
}

function generate_value_second_matrix(){
    let row = parseInt(document.getElementById("second-matrix-row").value)
    let column = parseInt(document.getElementById("second-matrix-column").value)

    for(let i = 0; i < row; i++){
        for (let j = 0; j < column; j++){
            let id = "field-second-matrix-" + i + "-" + j
            document.getElementById(id).value = getRandomNumber(1, 50)
        }
    }
}

function return_first_matrix(){
    let first_matrix = []
    let row = parseInt(document.getElementById("first-matrix-row").value)
    let column = parseInt(document.getElementById("first-matrix-column").value)

    for(let i = 0; i < row; i++){
        let tr = []
        for (let j = 0; j < column; j++){
            let id = "field-first-matrix-" + i + "-" + j
            tr.push(document.getElementById(id).value)
        }
        first_matrix.push(tr)
    }
    return first_matrix
}

function return_second_matrix(){
    let second_matrix = []

    let row = parseInt(document.getElementById("second-matrix-row").value)
    let column = parseInt(document.getElementById("second-matrix-column").value)
    for(let i = 0; i < row; i++){
        let tr = []
        for (let j = 0; j < column; j++){
            let id = "field-second-matrix-" + i + "-" + j
            tr.push(document.getElementById(id).value)
        }
        second_matrix.push(tr)
    }
    return second_matrix
}

function multiplay_matrix(){
    let first_matrix = return_first_matrix()
    let second_matrix = return_second_matrix()

    let column_first_matrix = parseInt(document.getElementById("first-matrix-column").value)
    let row_second_matrix = parseInt(document.getElementById("second-matrix-row").value)

    if (column_first_matrix !== row_second_matrix){
        alert("Умножение матриц невозможно")
    }else {
        let row_first = parseInt(document.getElementById("first-matrix-row").value)
        let column_first = parseInt(document.getElementById("first-matrix-column").value)
        let row_second = parseInt(document.getElementById("second-matrix-row").value)
        let column_second = parseInt(document.getElementById("second-matrix-column").value)
        generate_result_matrix(row_first, column_second)

        for(let i = 0; i < row_first; i++){
            for(let k = 0; k < column_second; k++){
                for(let i = 0; i < row_first; i++){
                    let temp = 0
                    for(let j = 0; j < row_second; j++){
                        temp += first_matrix[i][j]*second_matrix[j][k]
                        let id = "field-result-matrix-" + i + "-" + k
                        document.getElementById(id).value = temp
                    }
                }
            }
        }
    }
}

function getRandomNumber(min, max){
    return Math.floor(Math.random() * (max - min)) + min
}


// Шифр Плейфера
class PFEncryption {

    constructor() {
        this.alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        this.matrix = []
    }

    playfir(key, message){

    }
}


