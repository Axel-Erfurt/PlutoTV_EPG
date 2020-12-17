#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from subprocess import Popen


now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
later = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S.000Z')

url = f"http://api.pluto.tv/v2/channels?start={now}&stop={later}"
r = requests.get(url)

chList = ['Pluto TV Kids', 'Pluto TV History+', 'Pluto TV Animals+', 'Pluto TV Inside+', 'World Poker Tour', 'FailArmy', 'Pluto TV Explore', 'Pluto TV Sports', 'IGN', 'MinecrafTV', 'Pluto TV Fight', 'Glory Kickboxing', 'MST3K', 'The Pet Collective', 'Rifftrax', 'Action Sports', 'Fireplace', 'Pluto TV Nature', 'Pluto TV Movies', 'MTV Pluto TV', 'MTV The Shores', 'MTV Dating', 'The Asylum Channel', 'Pluto TV Kids Jr.', 'Pluto TV Sitcoms+', 'Pluto TV Indies', 'Ice Pilots', 'MTV Christmas Songs', 'MTV Teen Mom', 'MTV The Hills', 'SpongeBob Schwammkopf', 'Pluto TV Movies+(DE)', 'Pluto TV Surf', 'CC Pluto TV', 'CC Made in Germany', 'Totally Turtles', 'Slow TV', 'Pluto TV Mistletoe', 'Pluto TV Sitcoms', 'Pluto TV Animals', 'Pluto TV History', 'Pluto TV Inside', 'Pluto TV Dogs', 'Pluto TV Documentaries', 'Pluto TV Lives', 'Pluto TV Cats 24/7', 'MTV Catfish TV Show', 'Inspector Gadget', 'Simsalabim Sabrina', 'Mario vs. Sonic', 'Pluto TV Drama', 'Pluto TV Food', 'Pluto TV Romance', 'Pluto TV Christmas', 'Unbeaten Esports', 'Pluto TV Family', 'Comedy Central+', 'MTV Pluto TV+', 'Pluto TV Drama+', 'Pluto TV Retro Drama', 'Strongman', 'Pluto TV Retro Toons', 'Pluto TV Comedy', 'Pluto TV Thrillers', 'Dora TV', 'Being Human', 'Pluto TV Crime', 'MTV Catfish TV Show+', 'CC Made in Germany+', 'Sanctuary', 'Dark Matter', 'Pluto TV Fitness', 'Pluto TV Yoga', 'Beyblade Burst', "Blue's Clues", 'iCarly', 'Bubble Guppies', 'Sam & Cat', 'Victorious', 'Blaze', 'Pluto TV Chefkoch', 'MTV Teen (OV)', 'MTV Dating (OV)', 'MTV The Hills (OV)', 'MTV Cribs', 'Totally Turtles (OV)', 'People are Awesome', 'Pluto TV Home', 'Wipeout (OV)', 'Nick Rewind', 'Nick Pluto TV', 'Nick Jr. Pluto TV', 'Auction Hunters', 'Storage Wars', 'MTV Cribs+', 'Insight TV', 'Teen Nick', 'InWonder', 'InTrouble', 'Focus TV Reportage', 'Nick Pluto TV+', 'Nick Rewind+', 'Spongebob Schwammkopf+', 'iCarly+', 'Emma, einfach magisch!', 'Auto Motor Sport', 'Nick Christmas', 'Holiday Lights', 'Beat Club', 'Pluto TV Paranormal']

idList = ['5ad9b648e738977e2c312131', '5ad9b6941b95267e225e59c0', '5ad9b6f57ef2767e1846e59f', '5ad9b73efd87eb3a2717ccde', '5ad9b7aae738977e2c312132', '5ad9b7ffe738977e2c312133', '5ad9b8551b95267e225e59c1', '5ad9bb941b95267e225e59c2', '5ad9bc207ef2767e1846e5a0', '5ad9bca67ef2767e1846e5a1', '5ad9bda9fd87eb3a2717cce0', '5ad9be1be738977e2c312134', '5b4f56242d4ec87bdcbbb333', '5b4f5a07694c027be6ed1417', '5b4f5bf8423e067bd6df90ca', '5be1be871843b56328bc3ef1', '5be1c0d81843b56328bc3fba', '5be1c3f9851dd5632e2c91b2', '5c5c3b948002db3c3e0b262e', '5caf325764025859afdd6c4d', '5caf32c2a5068259a32320fc', '5caf330ea5068259a32320fd', '5cc81e793798650e4f7d9fd3', '5cd1495bd9e0ec55c4ecbf52', '5cd149f021cb6c55e258bbe8', '5ce40e59246a395e9758923e', '5ce40f42ba7f7f5ea9518fe1', '5ce40f8aa43c46795e36e8a5', '5cffcf5686dfe15595fb3f56', '5d00e86bf0bac55fe7f75736', '5d00e8adaab96b5635b2a005', '5d0a1f73654db655a9274428', '5d1ce51dbaca4afdb7abfe5f', '5d4947590ba40f75dc29c26b', '5d4948418101147596fd6c5a', '5d6792bd6be2998ad0ccce30', '5d765a05f65029ce2385aa30', '5d767a76367b89cf0032550d', '5d767ab2b456c8cf265ce921', '5d767ae7b456c8cf265ce922', '5d767b1c126c65d0a307355f', '5d767b4889bca2ce7b73ef2e', '5d8dc1d8da13e15d9fce6911', '5db048f9447d6c0009b8f29d', '5db04b360fa2560009deb3de', '5db6a56ce10f0b0009e64037', '5db6a697d5f34a000934cd13', '5dbc2d1ce10f0b0009e6cf9e', '5dbc327d0451770009ed7577', '5dc02ece31f6050009de4b39', '5dc190f7bfed110009d934c3', '5dc280c9aa218c0009724b4b', '5dc287ce3086a20009f5024c', '5dc29179c928a600093a7747', '5dc2a961bac1f70009ca7524', '5dc3fb596262db000923f7e3', '5dcea6bc6fb8890009322ff3', '5dcebe53d352330009e56f5b', '5ddbf866b1862a0009a0648e', '5dde47b63585b500099f74ec', '5e1452156c07b50009d0230e', '5e1c669094e0e80009b22ab8', '5e1efd0dbbe3ba000908b639', '5e1efdbf90ba3e0009d99082', '5e43c344b54fe800093552f4', '5e78f4dd001977000787d7e3', '5e7b6c60fd20c50007910bf5', '5e7b855972c36600076b7ddd', '5e7b8923fc302800079e4f4f', '5e7de99bc5200300072e971a', '5e843d849109b700075d5ada', '5e8b0c92783b3f0007a4c7df', '5e8b0d10e186bf0007e2b100', '5e8b551ddcd25500072c4dad', '5e8b564ff59d130007363823', '5e8b580a233dc90007f0cb9d', '5e8b5a4bb7da5c0007e5c9e9', '5e8b5ba20af628000707cee3', '5e8b5e43f294f8000793c3d7', '5e8b60419becf60008c841fd', '5e8c4c3f141f350007936f7d', '5ea812e0ba6c1f00079d3b7e', '5ea813c04958cd00078e9caf', '5ea8147c6e3dd70007deab3d', '5ea815a515d149000748ee9b', '5ea816a44457070007ffabc7', '5eb95c119dc712000741fa35', '5eb96303f5bb020008e7e44f', '5eb963c98ec06d00077d63cb', '5ed106ce4bf2e80007700bb3', '5ede448d3d50590007a4419e', '5ede45451dce190007ef9ff2', '5ede45d077746000072be0fe', '5ede464e7be0030007c58b73', '5efb54eaa5714d000744b6a0', '5f06bc60e236570007793f31', '5f0d668b872e4400073acc68', '5f1004e0a5714d000745650d', '5f1005f9d5d3cf00074c0395', '5f3bd0e63f793300071574cd', '5f3d2b57d6c60800074cb305', '5f3d2bcd0fadc30007b4863b', '5f3d2c4e501f18000788d8e9', '5f3d2cb9f5b291000773807a', '5f4796368174910007756454', '5f760c3d41aa2d0007bfde19', '5f982a3579d7c00007b54d30', '5f982b9d61dad200071148e8', '5f982c3420de4100070a545e', '5f98487036af340008da1e37']

### to json 
data = r.json() 

def getValues(channel):
    theList = []
    for i in data:
        if i['name'] == channel:
            pr = i['timelines']
            for a in pr:
                title = str(a.get('title'))
                st = a.get('start')
                start = st[11:16]
                desc = a["episode"]["series"].get("description")
                
                theList.append(f"{start} Uhr: {title}\n{desc}\n")
    return theList
    
with open("/tmp/plutoTV.txt", "w") as f:
    for ch in chList:   
        f.write(f"######## {ch.replace('Pluto TV ', '')} ########\n")
        f.write('\n'.join(getValues(ch)))
        f.write('\n\n')
    f.close()
    
Popen(["xdg-open", "/tmp/plutoTV.txt"])
