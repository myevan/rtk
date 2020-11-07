import ROT from 'rot-js'

let display = new ROT.Display({
    width: 80,
    height: 25,
    layout: "term"
})

display.draw(1, 1, "Hello")
display.draw(1, 2, "World!")
