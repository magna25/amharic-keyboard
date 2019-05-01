from amharic_keyboard.keyboard import AmharicKeyboard

def type(str):
    obj = AmharicKeyboard()
    return obj.transform(str)