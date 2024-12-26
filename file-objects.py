with open('test1.js', 'w') as file:
    file.write("""const name = [{
        'name': 'Husnain',
        'age': 20,
    }].map((item) => {
        return (
            `<div>
                <h1>${item.name}</h1>
                <h1>${item.age}</h1>
            </div>`
        );
    });""")

with open('test1.js', 'r') as file:
    print(file.read())
