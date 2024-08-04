from MenuCreator import CreateMenu


class harmonia():
    def __init__(self):
        self.major = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
        self.minor = ['Am', 'Bbm', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m']
        self.note = 'note'


    def M_Fields(self, note):
        return {
            'tonic' : note,
            'major_third' : self.next_note(note, 4),
            'minor_third' : self.next_note(note, 3),
            'perfect_fifth' : self.next_note(note, 7),
            'augmented_fifth' : self.next_note(note, 8),
            'diminished_fifth' : self.next_note(note, 6),
        }
    
    def m_fields(self, note):        
        return {
            'tonic' : note,
            'major_third' : self.next_note(note, 3),
            'minor_third' : self.next_note(note, 4),
            'perfect_fifth' : self.next_note(note, 5),
            'augmented_fifth' : self.next_note(note, 6),
            'diminished_fifth' : self.next_note(note, 7),
        }
    
    def I_IV_V(self, note):
        note = self.enarmonicos(note)
        return {
            'I' : note,
            'IV' : self.next_note(note, 5),
            'V' : self.next_note(note, 7),
            'Rm:' : self.minor[self.major.index(note)]
        }
    
    def II_III_VI(self, note):
        note = self.enarmonicos(note)
        return {
            'II' : self.next_note(note, 3),
            'III' : self.next_note(note, 4),
            'VI' : self.next_note(note, 6),
            'RMI:' : self.major[self.minor.index(note)]
        }
    
    def I_V_vi_IV(self, note):
        note = self.enarmonicos(note)
        return {
            'I' : note,
            'V' : self.next_note(note, 7),
            'vi' : self.minor[self.major.index(note)],
            'IV' : self.next_note(note, 5),
        }
    
    def vi_IV_I_V(self, note):
        note = self.enarmonicos(note)
        return {
            'vi' : self.minor[self.major.index(note)],
            'IV' : self.next_note(note, 5),
            'I' : note,
            'V' : self.next_note(note, 7),
        }
    
    def vi_IV_ii_V(self, note):
        note = self.enarmonicos(note)
        return {
            'vi' : self.minor[self.major.index(note)],
            'IV' : self.next_note(note, 5),
            'ii' : self.minor[5],
            'V' : self.next_note(note, 7),
        }

   
    def enarmonicos(self, note):
        match note:
            case 'Gb':
                self.note = 'F#'
                return self.note
            case 'Cb':
                self.note = 'B'
                return self.note
            case 'C#':
                self.note = 'Db'
                return self.note
            case _:
                self.note = note
                return self.note
        
    

    def next_note(self, note, number):
        if note in self.major:
            index = self.major.index(note)
            next_index = (index + number) % len(self.major)
            return self.major[next_index]
        else:
            index = self.minor.index(note)
            next_index = (index + number) % len(self.minor)
            return self.minor[next_index]
        


  
def main():

    

    principal = CreateMenu(title="*** Harmony ***", elements=[  
        'Scales',  
        'Chord Progression',  
        'Exit'  
    ])

    principal.load_menu()
    principal.wait()  
    

    if principal.get_selected_item() == 0:
        scales()

    elif principal.get_selected_item() == 1:
        print("Selected second element!")

    else:
        pass

def scales():
    tonic = input('Tonic = ')
    print(tonic)
    
     




if __name__ == "__main__":
    main()

                      
                      
