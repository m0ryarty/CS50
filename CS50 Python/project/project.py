import os

class Harmonia():
    def __init__(self):
        self.major = ['C', 'D#', 'D', 'E#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.minor = ['Am', 'B#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m']
        self.note = 'note'


    def M_Fields(self, note):
        return {
            'I' : note,
            'IIm' : self.next_note(note, 2),
            'IIIm' : self.next_note(note, 4),            
            'IV' : self.next_note(note, 5),
            'V' : self.next_note(note, 7),
            'VIm' : self.next_note(note, 9),
            'VIIm7(b5)': self.next_note(note, 11)
        }
    
    def m_fields(self, note):        
        return {
            'Im' : note,
            'IIm(b5)' : self.next_note(note, 2),
            'III' : self.next_note(note, 3),
            'IVm' : self.next_note(note, 5),
            'Vm' : self.next_note(note, 7),
            'VI' : self.next_note(note, 8),
            'VII' : self.next_note(note, 10)
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
            'Rm:' : self.minor[self.major.index(note)]
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
            case 'Db':
                self.note = 'C#'
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
        


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
  
def main():
    
    main_menu()


def fields():       
    fields_options = """

Harmonic Fields Menu:

choose a field:

1 - Major
2 - Minor

"""       
    field = input(fields_options)                    
    fields_choice(field)
    main_menu()
            

def chord_progressions():

    chord_progressions_options = """
Chord Progression Menu:

1 - I_IV_V
2 - II_III_VI
3 - I_V_vi_IV
4 - vi_IV_I_V
5 - vi_IV_ii_V

"""   
    chord = input(chord_progressions_options)                    
    choice_progressions(chord)
    main_menu()   



    
def main_menu():   
    main_options = """
Welcome to Harmony

Chose an option:
 1 - Harmonic Fields
 2 - Chord progressions
 3 - Exit

 """
    
    choice = input(main_options)
    main_choice(choice) 


def main_choice(choice):
    
    if choice == "1":
        clear()
        fields()
    elif choice == "2":
        clear()
        chord_progressions()
    elif choice == "3":
        clear()
        print("""
              Goodbye!
              """)
        exit()
    else:
        clear()
        print("Invalid option. Please try again.")

def fields_choice(choice):
    if choice == "1":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            major = harmony.M_Fields(tonic)
            clear()
            print(major)
            
        except ValueError:
            print("Invalid tonic. Please try again.")

    elif choice == "2":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            minor = harmony.m_fields(tonic)
            clear()
            print(minor)
           
        except ValueError:
                print("Invalid tonic. Please try again.")
    else:
        print("Invalid option. Please try again.")

def choice_progressions(choice):
    if choice == "1":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            progression = harmony.I_IV_V(tonic)
            clear()
            print(progression)
            
        except ValueError:
            print("Invalid tonic. Please try again.")

    elif choice == "2":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            progression = harmony.II_III_VI(tonic)
            clear()
            print(progression)
            
        except ValueError:
            clear()
            print("Invalid tonic. Please try again.")
           

    elif choice == "3":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            progression = harmony.I_V_vi_IV(tonic)
            clear()
            print(progression)
            
        except ValueError:
            clear()
            print("Invalid tonic. Please try again.")

    elif choice == "4":
        try:
            tonic = input('Tonic = ')
            harmony = Harmonia()
            progression = harmony.vi_IV_I_V(tonic)
            clear()
            print(progression)
            
        except ValueError:
            clear()
            print("Invalid tonic. Please try again.")

    elif choice == "5":
        try:
            tonic = input('Tonic = ')
            harmony =Harmonia()
            progression = harmony.vi_IV_ii_V(tonic)
            clear()
            print(progression)
            
        except ValueError:
            clear()
            print("Invalid tonic. Please try again.")
    else:
        clear()
        print("Invalid option. Please try again.")
     


if __name__ == "__main__":
    main()

                      
                      
