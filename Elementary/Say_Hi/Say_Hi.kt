fun say_hi(name: String,age: Int): String{
    return "Hi. My name is ${name} and I'm ${age} years old"
}

fun main(args: Array<String>){
        println(say_hi("Alex",32))
        println(say_hi("Frank",68))
}
