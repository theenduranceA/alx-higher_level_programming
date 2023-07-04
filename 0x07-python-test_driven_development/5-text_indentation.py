def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = ['.', '?', ':']
    y = []
    z = ""

    for i in text:
        z = z + i
        if i in x:
            y.append(z.strip())
            z = ""

    if z:
        y.append(z.strip())

    for j in y:
        print(j)
        print()
