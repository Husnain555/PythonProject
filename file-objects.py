with open('test1.js','w') as file:
    file.write("""const name = [{
        'name':'Husnain',
        'age':20,
    }].map((item)=>{
    return (
    <div>{item.name} {item.age}</div>)})""")
with open('test1.js','r') as file:
  print(    file.read()
)