

authors = [
{
"id": 1,
"name": "Justas",
"surname": "Matonis"
},
{
"id": 2,
"name": "Paulius",
"surname": "Davlionis"
},
{
"id": 3,
"name": "Tautvydas",
"surname": "Ravlionis"
}
]

print(authors)

id_counter = 3

print("1. Atvaizduoti visus autorius")
print("2. Itraukti nauja autori")
print("3. Redaguoti autori/us")
print("4. Pasalinti autori/us")
print("5. Sustabdyti programa")


# print(press)

while True:
    print("Pasirinkti: 1. Sarasas. 2. Prideti autori. 3.Redaguoti autori. 4. Pasalinti autori. 5. Sustabdyti programa")
    print("----------Pasirinkite--------")
    press = input()

    match press:
        case "1":
            print("Sarasas")
            for aut in authors:
                print(f"Autoriaus vardas: {aut['name']}. Jo pavarde: {aut["surname"]}, ID numeris: {aut['id']}")
        case "2":
            print("Prideti")
            print("Iveskite nauja varda:")
            name = input()
            print("Iveskite nauja pavarde")
            surname = input()
            id_counter += 1
            authors.append(
                {"id": id_counter,
                 "name": name,
                 "surname": surname, }
            )
        case "3":
            print("Redaguoti")
            print("Iveskite autoriaus ID, kuri redaguosime")
            new_id = input()
            new_id = int(new_id)

            for aut in authors:
                    if aut["id"] == new_id:
                        print("Iveskite nauja varda")
                        new_name = input()
                        print("Iveskite nauja pavarde")
                        new_surname = input()
                        aut["name"] = new_name
                        aut["surname"] = new_surname

        case "4":
            print("Pasalinti")
            print("Iveskite autoriaus ID, kuri pasalinsime:")
            remove_id = input()
            remove_id = int(remove_id)
            autorius_pasalinimui = None

            for aut in authors:
                if aut["id"] == remove_id:
                    print("Pasalinti autori")
                    autorius_pasalinimui = aut
                    break

            if autorius_pasalinimui:
                authors.remove(autorius_pasalinimui)
                print("Autorius pasalintas")
            else:
                print("Autorius nerastas")

        case "5":
            print("Sustabdyti")
            break

#asd##