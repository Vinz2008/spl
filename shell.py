import spl
while True:
    text = input("spl > ")
    if text == "exit":
            break
    result, error = spl.run('<stdin>',text)
    if error:
        print(error.as_string())
    else:
        print(result)
    