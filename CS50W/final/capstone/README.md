# Archive

## Estructure

One of the effects of the massive use of software was the abandonment of paper as a means of conveying data. Considering the many advantages of this adoption, a huge volume of paper was saved.
However, a gigantic volume already existed and contained a lot of history and waste.
In Brazil, a discussion became important: what to do with these mountains of paper?
There were already policies related to archiving, but they were restricted to documents that were recognized as historical. The rest, the vast majority, were kept in paper deposits that used to be called archives.
A new policy was created and gradually put into action to deal with this collection.
One of the tasks in this procedure is to distinguish what should be kept from what should be discarded. And if kept, for how long.
It was with these bases that in my project I sought to build an application that would assist in the receipt of archiving objects and control the storage of documents and the elimination of those that should follow this fate.

The Archive application has built-in archiving and deadline control procedures.
First, it is necessary to create the archives, which should be structures to house the documents.

Each archive will have:

* a name: which is freely chosen, but ideally should be an acronym or a short name;
* an address: which is the location of the archive.
Once the archive has been created, it will be necessary to include shelves within it.

The shelves will be distinguished by:

* a type: this could be the model of the shelf or the material from which they are made;
* a location: in this case a code could indicate where within the archive the shelf is. It could also be a free description.
* the capacity will indicate when the shelf is full and thus the need to create another one.
* the shelf will be linked to an archive. In this way, each archive will have several shelves, but each shelf will be in only one archive.
* The boxes are represented by a count that increases or decreases as they are added or removed from the shelf. This makes it possible to compare them with the shelf capacity and indicate whether it is full.

The boxes must be placed on the shelves, which will be identified by their ID and when created they must indicate:

* the shelf where they are located;
* a note of free filling and
* whether they are full.

These boxes are where the objects to be archived will be stored. For this project, I sought to create a solution to a problem at my workplace. Therefore, the object to be archived is court records.

In Brazil, court records receive an identification number following a certain pattern, which results in a 20-digit number, in this pattern:

NNNNNNN-DD.YYYY.I.OO.UUUU
N is the identification number that is reset every year
D is the verification digit created from a specific mathematical formula
Y is the year the records were created
I is the instance of the court
O is the court
U is each of the units of the court

Ideally, information about court records should come from a dedicated system that manages these documents during processing in the courts. However, for this project, it was decided to register the records at the time of archiving.
Therefore, when archiving the records, it will be necessary to provide their identification number, which will be used to fill in the fields:

* code, year and unity
Other available fields are:
* former code: in the case of very old objects that reference systems with other identification formats
* user: which will register the user responsible for receiving the records in the archive.

In addition to this information, it will be necessary to inform the parties to the proceedings, whether plaintiff or defendant.

## The Archive app

The application was created using Django to build the backend and React to build the frontend pages.
The aim was to give the backend the responsibility of carrying out all business interactions. Thus, the data is delivered ready for the frontend, which will only have the task, as far as possible, of presenting and capturing data.
After entering the application, we are presented with the Home page. This page contains a summary of the files we are managing, with information on the archived volume and also the current status of document management.

We have information on the number of objects and also whether they should be analyzed or, perhaps, eliminated.

By clicking on any of the files, we are taken to the details of this file on the Archives page.

These details show the files that should deserve our attention if their storage periods have expired.

With this, we must analyze to decide whether these objects should continue to be stored or should be eliminated.
On the same Archives page, you can create a new file and update the status of each archived object.
When new files are received in these files, they must be registered on the Archiving page.
On this page, you can check if there are shelves available for this procedure. If there are none, you must create them. From the existing shelves, you can find out which file they belong to and their availability to receive boxes.
On the same page, you can find information about the existence of boxes available to store the received files. If there are no boxes, you must create them. In the boxes window, you can see which boxes are available on the shelves and how many volumes there are in them.
With shelves and boxes available, you can receive the files for archiving.
This is done on the same page.
The procedure requires that you register the file number. If these files already exist in the archive, you just need to inform the number of volumes and in which box they will be stored.
When the case numbers are entered, the system returns information about these in the file, indicating in which boxes the other parts already filed are located.
Each box that is filled in must be marked with Full if there is no more space.
If these are new cases in the File, it will be necessary to inform the Plaintiff and Defendant in the process.
Once this is done, the cases are registered for analysis and definition of the storage time in the file.

## Em desenvolvimento

O aplicativo realiza o registro dos Autos, porém, em uma situação ideal deverá existir um sistema de comtrole destes Autos em separado que permita o processamento judicial. Assim, o aplicativo Archivo deve estar conectado a este sistema e dele receber informações dos objetos que venham a ser arquivados.
Assim, por ser parte de um ecosistema os procedimentos de registro de usuários e suas permissões devm ser gerenciadas externamente por um superusuário. Por esta razão este aplicativo não possui uma instancia de registro de usuários, que devem ser autorizados pelo superusuário no Admin do Django.
Outras instancias de relatórios e pesquisa estão entre as ferramentas a serem desenvolvidas.

## Distinctiveness and Complexity

This project aims to meet the need for archival storage records and management in intermediate storage phases for possible elimination after a reasonable period of time or permanent storage if the object has historical or social importance.

As it was created in Django and React, to start it you must go to the back folder and run the command python3 manage.py runserver to start the backend and go to the front folder and type npm start to start the frontend.
