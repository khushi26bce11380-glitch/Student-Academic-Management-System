


def isvalidinteger(text):
   
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False
   
    return cleaned.isdigit()


def isvalidfloat(text):
 
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False

   
    if cleaned.count(".") > 1:
        return False

    withoutdot = cleaned.replace(".", "", 1)
    if len(withoutdot) == 0:
        return False

    return withoutdot.isdigit()


def getvalidinteger(prompt, minval=0, maxval=100000):
  
    while True:
        rawval = input(prompt)
        if not isvalidinteger(rawval):
            print("Invalid input! Please enter whole numerical digits only.")
            continue

       
        val = int(rawval)

        if val < minval or val > maxval:
            print(f"Value out of bounds! Must be between {minval} and {maxval}.")
            continue

        return val


def getvalidfloat(prompt, minval=0.0, maxval=100.0):
   
    while True:
        rawval = input(prompt)
        if not isvalidfloat(rawval):
            print("Invalid input! Please enter a valid numerical number.")
            continue

       
        val = float(rawval)

   
        if val < minval or val > maxval:
            print(f"Value out of bounds! Must be between {minval} and {maxval}.")
            continue

        return val


def getnonemptystring(prompt):

    while True:
        text = input(prompt).strip()
        if len(text) == 0:
            print("Input cannot be empty. Please enter valid text.")
            continue
        return text


def getmenuchoice(prompt, validchoices):
   
    while True:
        choice = input(prompt).strip()
        if choice in validchoices:
            return choice
        print("Invalid choice! Please select an option from the menu list.")
