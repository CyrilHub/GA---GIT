piranah_hungry = True

def swing_vine_river():
    print ("Ahhh! Piranhas got me!.")
    piranah_hungry = False
    global piranah_hungry
    pass

def jump_in_river():
    if piranah_hungry:
        print ("I'm not going in there!")
    else:
        print ("Piranhas are full!")
    pass

print("test")




