# imports
import requests

while True:  # looping the whole code so it will always go back at end
    clearnum = 1  # for clearing
    while clearnum < 100:  # clearing
        print(" ")
        clearnum += 1      # end of clearing
    print("BTCCalc by xNatok#0442 | Syntetik008")
    print(" ")
    print("What do you want to calculate?")
    print("#####################")
    print("# 1 - USD to BTC #")
    print("# 2 - BTC to USD #")
    print("#####################")
    clearnum = 1   # for clearing
    chose = input("-> ")  # DevNote: I know i could detect if user pressed 1 or 2 in better way but thats the easiest
                          # same for "press enter to go back"

    if chose == "1":  # USD to BTC
        usd = input("How much USD?: ")
        r = requests.get("https://blockchain.info/tobtc?currency=USD&value=" + usd)  # asking api for how much is x$ in BTC
        result = r.text
        print(usd + "$ = " + result + " BTC")
        input("Press enter to go back")
    elif chose == "2":  # BTC to USD
        btc = input("How much BTC?: ")
        r = requests.get("https://blockchain.info/tobtc?currency=USD&value=1")  # asking api for how much is 1$ in BTC
        result = r.text
        # I don't know why, i don't want to know why, I shouldn't have to wonder why, but for whatever reason
        # this stupid float don't want to work. EDIT: ok now it works.
        resultxd = float(btc) / float(result)  # (x btc) / (1$ in btc)
        print(btc + " BTC = " + str(resultxd) + "$")
        input("Press enter to go back")
    else:  # if user put other number than 1 or 2
        while clearnum < 100:  # clearing
            print(" ")
            clearnum += 1  # end of clearing
        input("Wrong number press enter to go back")
        clearnum = 1   # for clearing
else:
    print("")
