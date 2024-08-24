# HARMONIA

    #### Video Demo:  <URL HERE>
    #### Description:

Harmony is an extensive subject of music study. It's something I want to learn, at least the basics. That's why I chose this subject for my final project in CS50 python.
This gave me the opportunity to learn object-oriented programming better by creating a class focused on the subject of harmony.
There are probably many libraries on the subject, however, I preferred not to explore this field. I preferred, albeit naively, to create a class with several objects from scratch.
In this case I combined two subjects that I had little knowledge of, so I tried to keep it as simple as possible at first to seek complexity as the two topics became clearer.
Thus, the class created is called "Harmony"
The project then has a "main" function that will allow you to explore the "Harmony" class
The Harmony class is the heart of the project. From the list of chords or major or minor musical notes, the next_note function is responsible for assembling chord progressions or harmonic fields. Receiving the tonic note and the index number of the notes or chords that make up the sequence.
So, given the tonic note, the M_Fields function will trigger the next_note function to discover each of the notes that make up the larger harmonic field. The return of this function are the seven chords that structure the field. The result is given in a dictionary in which the keys are a sequence in Roman numerals and an indication of when they were relative minor or diminished.
The m_fields function performs the same operation whose result will be the chords that make up the minor harmonic field, also presented in a dictionary.
Regarding the chord progression, some of the most popular cadences in music were chosen.
Starting with the I_IV_V cadence, very common in popular, folk, rock music, etc. To obtain a dictionary containing the cadence chords, simply enter the tonic chord. Being valid for any height of the chromatic scale.
The II_III_VI cadence widely used in jazz and blues also requires the tonic chord to present an appropriate list for each key.
Other cadences can be consulted, the tonic chord will always be requested and will result in a dictionary with the respective chord progressions.
It turns out that the tonic chord may have a corresponding enharmonic. In these cases, the "enarmonicos" function handles this issue so that the result in any of the queries is correct. By the way, enharmonics are chords or notes that despite having different names have the same sound.

The "main" function's task is to organize queries made to the "harmony" class. In principle, we sought a library that would produce a menu suitable for dialogue with the user. However, several attempts were unsuccessful. That's why we decided to create a menu. This task was interesting and had a very satisfactory result. The main menu offers the options of consulting the Major or Minor harmonic fields or the chord progressions of the available cadences. The third option is to exit the software.
Exceptions were handled in such a way as to always ask the user to make the correct choice between the options.
Selecting option 1 - Harmonic Fields, go to the submenu that will ask if the user wants the Major or Minor harmonic field.
Once the choice is made, ask what the tonic is and then present the result containing the seven chords in the form of a dictionary.
After presenting the result, you return to the main menu, and you can exit the application or perform a new query.
The query can now be item 2 - Chord progressions. Once this option is selected, a submenu opens with the available cadence options.
1 - I_IV_V
2 - II_III_VI
3 - I_V_vi_IV
4 - vi_IV_I_V
5 - vi_IV_ii_V

Each of these options will request the tonic chord to present the chord sequence as a result. Here too, exceptions are handled in a way that insists that the user makes the correct choice.

Regarding the tonic chord, it must be reported in the notation A-B-C-D-E-F-G, in capital letters.

As said before, this project is the result of a learning process that is still under construction. Therefore, many changes must still occur. Many improvements and additions are expected and are already in sight. Learning music theory will lead to improvement of the application.
