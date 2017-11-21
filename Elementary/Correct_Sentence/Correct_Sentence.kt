fun correct_sentence(text: String): String{
        var temp = text

        if (temp.endsWith(".") == false){
                temp += "."
        }

        return temp.capitalize()
}


fun main(args: Array<String>){
        println(correct_sentence("greetings, friends"))
        println(correct_sentence("Greetings, friends"))
        println(correct_sentence("Greetings, friends."))
        println(correct_sentence("hi"))
}
