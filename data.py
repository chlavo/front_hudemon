def chromaticka_stupnice():
    return ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "h"]

def mod(mod):
    mody = { 1 : [1,0,1,0,1,1,0,1,0,1,0,1],     #[1,3,5,6,8,10,12]  "jonsky"
             2 : [1,0,1,1,0,1,0,1,0,1,1,0],     #[1,3,4,6,8,10,11]  "dorsky"
             3 : [1,1,0,1,0,1,0,1,1,0,1,0],     #[1,2,4,6,8, 9,11]  "frygicky"
             4 : [1,0,1,0,1,0,1,1,0,1,0,1],     #[1,3,5,7,8,10,12]  "lydicky"
             5 : [1,0,1,0,1,1,0,1,0,1,1,0],     #[1,3,5,6,8,10,11]  "mixolydicky"
             6 : [1,0,1,1,0,1,0,1,1,0,1,0],     #[1,3,4,6,8, 9,11]  "aiolsky"
             7 : [1,1,0,1,0,1,1,0,1,0,1,0]}     #[1,2,4,6,7, 9,11]  "lokricky"
    return mody[mod]
 
def tonalita(mod):
    tonalita = {1 : "dur",      #   "jonsky"     
                2 : "moll",     #   "dorsky"     
                3 : "moll",     #   "frygicky"   
                4 : "dur",      #   "lydicky"    
                5 : "dur",      #   "mixolydicky"
                6 : "moll",     #   "aiolsky"    
                7 : "moll"}     #   "lokricky"   
    return tonalita[mod]