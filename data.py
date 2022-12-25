def chromaticka_stupnice():
    return ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "h"]

def chromaticka_tabulka(offset):
    stupnice = chromaticka_stupnice()
    return [stupnice[offset    :] + stupnice[:offset    ],          # stupnice s posunem
            stupnice[offset + 4:] + stupnice[:offset + 4],          # tercie
            stupnice[offset + 7:] + stupnice[:offset + 7],          # kvinta
            stupnice[offset +10:] + stupnice[:offset +10]]          # septima

def mod(mod):
    mody = { 1 : [1,0,1,0,1,1,0,1,0,1,0,1],     #[1,3,5,6,8,10,12]  "jonsky"
             2 : [1,0,1,1,0,1,0,1,0,1,1,0],     #[1,3,4,6,8,10,11]  "dorsky"
             3 : [1,1,0,1,0,1,0,1,1,0,1,0],     #[1,2,4,6,8, 9,11]  "frygicky"
             4 : [1,0,1,0,1,0,1,1,0,1,0,1],     #[1,3,5,7,8,10,12]  "lydicky"
             5 : [1,0,1,0,1,1,0,1,0,1,1,0],     #[1,3,5,6,8,10,11]  "mixolydicky"
             6 : [1,0,1,1,0,1,0,1,1,0,1,0],     #[1,3,4,6,8, 9,11]  "aiolsky"
             7 : [1,1,0,1,0,1,1,0,1,0,1,0],     #[1,2,4,6,7, 9,11]  "lokricky"
             8 : [0,0,0,0,0,0,0,0,0,0,0,0]}     #                    Random
    if isinstance(mod, int): 
        return mody[mod]
    elif isinstance(mod, str) & (1 <= int(mod[:1]) <= 8): 
        return mody[int(mod[:1])]    
    else:
        return mody[1]

def maska_tabulky(mod, offset):
    maska_modu = mod(mod)
    return [maska_modu[offset    :] + maska_modu[:offset    ],          # stupnice s posunem
            maska_modu[offset + 4:] + maska_modu[:offset + 4],          # tercie
            maska_modu[offset + 7:] + maska_modu[:offset + 7],          # kvinta
            maska_modu[offset +10:] + maska_modu[:offset +10]]          # septima
 
def tonalita(mod):
    tonalita = {1 : "dur",      #   "jonsky"     
                2 : "moll",     #   "dorsky"     
                3 : "moll",     #   "frygicky"   
                4 : "dur",      #   "lydicky"    
                5 : "dur",      #   "mixolydicky"
                6 : "moll",     #   "aiolsky"    
                7 : "moll"}     #   "lokricky"   
    return tonalita[mod]

def souhrn():
    return ([["1c", "1c#", "1d", "1d#", "1e", "1f", "1f#", "1g", "1g#", "1a", "1a#", "1h"],
             ["2d", "2d#", "2e", "2f", "2f#", "2g", "2g#", "2a", "2a#", "2h", "2c", "2c#"],
             ["3e", "3f", "3f#", "3g", "3g#", "3a", "3a#", "3h", "3c", "3c#", "3d", "3d#"],
             ["4f", "4f#", "4g", "4g#", "4a", "4a#", "4h", "4c", "4c#", "4d", "4d#", "4e"],
             ["5g", "5g#", "5a", "5a#", "5h", "5c", "5c#", "5d", "5d#", "5e", "5f", "5f#"],
             ["6a", "6a#", "6h", "6c", "6c#", "6d", "6d#", "6e", "6f", "6f#", "6g", "6g#"],
             ["7h", "7c", "7c#", "7d", "7d#", "7e", "7f", "7f#", "7g", "7g#", "7a", "7a#"]
            ])

slovnik = {
    "1c":[0,0 ],"1c#":[1,0 ], "1d":[2,0 ],"1d#":[3,0 ], "1e":[4,0 ],"1f" :[5,0 ],"1f#":[6,0 ], "1g":[7,0 ],"1g#":[8,0 ], "1a":[9,0 ],"1a#":[10,0 ], "1h":[11,0 ],
    "2d":[0,2 ],"2d#":[1,2 ], "2e":[2,2 ],"2f" :[3,2 ],"2f#":[4,2 ],"2g" :[5,2 ],"2g#":[6,2 ], "2a":[7,2 ],"2a#":[8,2 ], "2h":[9,2 ],"2c" :[10,2 ],"2c#":[11,2 ],
    "3e":[0,4 ],"3f" :[1,4 ],"3f#":[2,4 ],"3g" :[3,4 ],"3g#":[4,4 ],"3a" :[5,4 ],"3a#":[6,4 ], "3h":[7,4 ],"3c" :[8,4 ],"3c#":[9,4 ],"3d" :[10,4 ],"3d#":[11,4 ],
    "4f":[0,5 ],"4f#":[1,5 ], "4g":[2,5 ],"4g#":[3,5 ], "4a":[4,5 ],"4a#":[5,5 ], "4h":[6,5 ], "4c":[7,5 ],"4c#":[8,5 ], "4d":[9,5 ],"4d#":[10,5 ], "4e":[11,5 ],
    "5g":[0,7 ],"5g#":[1,7 ], "5a":[2,7 ],"5a#":[3,7 ], "5h":[4,7 ],"5c" :[5,7 ],"5c#":[6,7 ], "5d":[7,7 ],"5d#":[8,7 ], "5e":[9,7 ],"5f" :[10,7 ],"5f#":[11,7 ],
    "6a":[0,9 ],"6a#":[1,9 ], "6h":[2,9 ],"6c" :[3,9 ],"6c#":[4,9 ],"6d" :[5,9 ],"6d#":[6,9 ], "6e":[7,9 ],"6f" :[8,9 ],"6f#":[9,9 ],"6g" :[10,9 ],"6g#":[11,9 ],
    "7h":[0,11],"7c" :[1,11],"7c#":[2,11],"7d" :[3,11],"7d#":[4,11],"7e" :[5,11],"7f" :[6,11],"7f#":[7,11],"7g" :[8,11],"7g#":[9,11],"7a" :[10,11],"7a#":[11,11]
    }

def offset(key):
    return (slovnik[key][0] + slovnik[key][1]) % 12



