import csv

class Drama: # drama klass
    def __init__(self,drama_info):
        self.drama_name = drama_info[0]
        self.rating = float(drama_info[1])
        self.actors = drama_info[2]
        self.viewship_rate = float(drama_info[3])
        self.genre = drama_info[4]
        self.director = drama_info[5]
        self.writer = drama_info[6]
        self.year = int(drama_info[7])
        self.no_of_episodes = int(drama_info[8])
        self.network = drama_info[9]

    def __str__(self):
        return(self.drama_name)

    def __lt__(self, other):
        return self.rating < other.rating
    
    def produced_by(self):
        return self.director, self.writer
    
    def years_after_1900(self):
        if self.year<1900:
            return None
        else:
            return self.year-1900


def read_file(filename): # läser in en fil och skriver ut dess innehåll
    with open(filename, mode="r") as file:
        csvfile = csv.reader(file,delimiter="\t")
        for line in csvfile:
            print(line)


def read_drama_from_file(dramafile): # läser in en fil och skapar en lista av drama objekt
    drama_list = list()
    with open(dramafile, mode="r") as file:
        csvfile = csv.reader(file,delimiter=",")
        next(csvfile)
        for line in csvfile:
            new_drama = Drama(line)
            drama_list.append(new_drama)
    return drama_list


def seek_newest(list): # hittar det nyaste dramat i en lista av draman
    newest_year = 0
    newest_drama = None
    for drama in list:
        if drama.year > newest_year:
            newest_year = drama.year
            newest_drama = drama
    
    return newest_drama, newest_year



read_file("/Users/erik/Documents/Tillämpad Datalogi/Labb 1/kdrama.csv")

breaking_bad_info = ["Breaking Bad",9.5,"Bryan Cranstaon, Aaron Paul, Anna Gunn",5.4,"Crime drama, Thriller","Vince Gilligan","Vince Gilligan",2008,62,"AMC"]
chernobyl_info = ["Chernobyl",9.3,"Jared Harris, Jessie Buckley, Stellan Skarsgård",0.5,"Historical drama, Thriller", "Johan Renck", "Craig Mazin",2019,5,"HBO"]

breaking_bad = Drama(breaking_bad_info)
chernobyl = Drama(chernobyl_info)

print(chernobyl)
print(breaking_bad.genre)
print(breaking_bad < chernobyl)

a,b =breaking_bad.produced_by()
print("Director",a,"Writer",b)
print(chernobyl.years_after_1900(),"år efter 1900")


drama_list = read_drama_from_file("/Users/erik/Documents/Tillämpad Datalogi/Labb 1/kdrama.csv")

print(drama_list[1].years_after_1900())

#fett coolt
c,d = seek_newest(drama_list)
print(c,"is the newest drama, it is from",d)