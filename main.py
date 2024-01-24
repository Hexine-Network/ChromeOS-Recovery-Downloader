def simplesearch():
    board = input("enter board name *example octopus*")
    crosversion = input("enter chromeos version *example 112*")
    if crosversion == "120":
        crosnumber = "15662.76.0"
    if crosversion == "119":
        crosnumber = "15633.72.0"
    if crosversion == "118":
        crosnumber = "15604.57.0"
    if crosversion == "117":
        crosnumber = "15572.63.0"
    if crosversion == "116":
        crosnumber = "15509.81.0"
    if crosversion == "115":
        crosnumber = "15474.84.0"
    if crosversion == "114":
        crosnumber = "15437.63.0"
    if crosversion == "113":
        crosnumber = "15393.58.0"
    if crosversion == "112":
        crosnumber = "15359.58.0"
    if crosversion == "111":
        crosnumber = "15329.44.2"
    if crosversion == "110":
        crosnumber == "None of the 110 or lower image links work."
        crosversion = input("enter full cros version name *example 112*")
    if board == "octopus":
        boardnum = "32"
    if board == "grunt":
        boardnum = "7"
    if board == "dedede":
        boardnum = "31"
    if board == "coral":
        boardnum = "21"
    if board == "brya":
        if crosversion == "120":
            boardnum = "14"
        if crosversion == "119":
            boardnum = "13"
        if crosversion == "118":
            boardnum = "13"
        if crosversion == "117":
            boardnum = "13"
        if crosversion == "116":
            boardnum = "13"
        if crosversion == "115":
            boardnum = "13"
        if crosversion == "114":
            boardnum = "11"
        if crosversion == "113":
            boardnum = "11"
        if crosversion == "112":
            boardnum = "11"
        if crosversion == "111":
            boardnum = "9"
        print("!For versions above 114 the boardnum for brya is 13 and v120 is 14!")
        #Below is a patch for the number problem
        brya20 = "3"
        brya5 = "2"
        if crosversion == "120":
            boardnum = "14"
        if crosversion == "119":
            boardnum = "13"
        if crosversion == "118":
            boardnum = "13"
        if crosversion == "117":
            boardnum = "13"
        if crosversion == "116":
            boardnum = "13"
        if crosversion == "115":
            boardnum = "13"
        if crosversion == "114":
            boardnum = "11"
        if crosversion == "113":
            boardnum = "11"
        if crosversion == "112":
            boardnum = "11"
        if crosversion == "111":
            boardnum = "9"
    if board == "hana":
        boardnum = "8"
        print("v120 ends with 10 not 8")
    if board == "x86-mario":
        boardnum == "3"
        print("You do know there is only versions 53 and 56 right?")
    if board == "":
        boadnum = ""
    link = "https://dl.google.com/dl/edgedl/chromeos/recovery/"
    cros = "chromeos_"
    under = "_"
    last1 = "_recovery_stable-channel_mp-v"
    last2 = ".bin.zip"
    print("for v120 add one to the last number example v32 = v33 for octopus")
    download = link + cros + crosnumber + under + board + last1 + boardnum + last2
    print("The download url to your recovery image is", download)
    exit()
#functions so its easier for the user to choose a option
def fetcher():
    #This was only tested with Octopus Images 112 and 119
    crosversion = input("enter full cros version name *example 15437.63.0*")
    board = input("enter board name *example octopus*")
    if board == "octopus":
        boardnum = "32"
    if board == "grunt":
        boardnum = "7"
    if board == "dedede":
        boardnum = "31"
    if board == "coral":
        boardnum = "21"
    if board == "brya":
        if crosversion == "15662.76.0":
            boardnum = "14"
        if crosversion == "15474.84.0":
            boardnum = "13"
        if crosversion == "15509.81.0":
            boardnum = "13"
        if crosversion == "15572.63.0":
            boardnum = "13"
        if crosversion == "15604.57.0":
            boardnum = "13"
        if crosversion == "15633.72.0":
            boardnum = "13"
        if crosversion == "15359.58.2":
            boardnum = "11"
        if crosversion == "15393.58.2":
            boardnum = "11"
        if crosversion == "15437.63.0":
            boardnum = "11"
        if crosversion == "15329.44.2":
            boardnum = "9"
        print("!For versions above 114 the boardnum for brya is 13 and v120 is 14!")
        #Below is a patch for the number problem
        brya20 = "3"
        brya5 = "2"
        if crosversion == "15662.76.0":
            boardnum.replace('11', '14')
        if crosversion == "15474.84.0":
            boardnum.replace('11', '13')
        if crosversion == "15509.81.0":
            boardnum.replace('11', '13')
        if crosversion == "15572.63.0":
            boardnum.replace('11', '13')
        if crosversion == "15604.57.0":
            boardnum.replace('11', '13')
        if crosversion == "15633.72.0":
            boardnum.replace('11', '13')
    if board == "hana":
        boardnum = "8"
        print("v120 ends with 10 not 8")
    if board == "x86-mario":
        boardnum == "3"
        print("You do know there is only versions 53 and 56 right?")
    if board == "":
        boadnum = ""
    link = "https://dl.google.com/dl/edgedl/chromeos/recovery/"
    print("for v120 add one to the last number example v32 = v33 for octopus")
    cros = "chromeos_"
    under = "_"
    last1 = "_recovery_stable-channel_mp-v"
    last2 = ".bin.zip"

    download = link + cros + crosversion + under + board + last1 + boardnum + last2
    print("The download url to your recovery image is", download)
    exit()
def boards():
    print("octopus = v32")
    print("grunt = v7")
    print("dedede = v31")
    print("coral = v21")
    print("brya = multiple numbers")
    print("hana = v8")
    print("x86-mario = v3")
    print("That is all the boards I choose to add.")
#Simple python app I made so I can find chromeos recovery files easy instead of going on cros.tech
print("Welcome to ChromeOS Recovery Fetcher v1 or CRF1")
line1 = "█▀▀ █░█ █▀█ █▀█ █▀▄▀█ █▀▀ █▀█ █▀   █▀█ █▀▀ █▀▀ █▀█ █░█ █▀▀ █▀█ █▄█"
line2 = "█▄▄ █▀█ █▀▄ █▄█ █░▀░█ ██▄ █▄█ ▄█   █▀▄ ██▄ █▄▄ █▄█ ▀▄▀ ██▄ █▀▄ ░█░"
print(line1)
print(line2)
print("Please choose an action.")
print("!WARNING! Some v120 boardnumbers are different!")
#Board numbers just in case
print("[1]. board support [2]. Search [3]. Simple Search")
action = input("")
if action == "1":
    boards()
if action == "2":
    fetcher()
if action == "3":
    simplesearch()
#end of code
exit()
#made by slideshowgames
