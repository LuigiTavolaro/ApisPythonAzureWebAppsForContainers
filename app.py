from flask import Flask,jsonify, request,abort 

app = Flask(__name__)

tarefas = [
    {
        'id': 1,
        'titulo': u'Ir na padaria',
        'descricao': u'trazer leite, pão e manteiga', 
        'done': True
    },
    {
        'id': 2,
        'titulo': u'Ir no mercado',
        'descricao': u'trazer frutas, verduras e legumes', 
        'done': False
    }
]

@app.route('/tarefas', methods=['GET'])
def get_tasks():
    return jsonify({'tarefas': tarefas})


##{
##	"titulo":"Ir na feira",
##	"descricao":"trazer banana, maçã e limão"
##}

@app.route('/new', methods=['POST'])
def new():
    content = request.json
    tit = content['titulo']
    desc = content['descricao']
    tarefas = [
    {
        'id': 3,
        'titulo': tit,
        'descricao': desc, 
        'done': False
    }]
    
    return jsonify({'tarefas': tarefas})

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
