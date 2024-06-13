# create custom module, dont need export anything

from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def random_fun_fact():
    fun_fact = [
        "Python was named after the British comedy series 'Monty Python's Flying Circus'.",
        "Guido van Rossum, the creator of Python, was inspired to create Python by ABC, a language he had used at Centrum Wiskunde & Informatica (CWI), Netherlands.",
        "Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
        "Python is widely used in web development, data analysis, artificial intelligence, machine learning, automation, and scientific computing.",
        "Python is an interpreted language, which means it does not need to be compiled before execution, making it easier to write and test code quickly.",
        "Python's standard library is vast and includes modules for various tasks such as file I/O, networking, databases, and more.",
        "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.",
        "Python has a strong and active community of developers who contribute to its growth and evolution through open-source development.",
        "Python is known for its simplicity and readability, which makes it an excellent choice for beginners and experienced programmers alike.",
        "Python's popularity has been steadily increasing over the years and consistently ranks among the top programming languages in various indices and surveys."
    ]
    index = choice("0123456789")

    print(fun_fact[int(index)]) 
    


# do this if want use it as module
# this code exist in most of modules
if __name__ == "__main__": # this function will run if this is the main module
    random_fun_fact()