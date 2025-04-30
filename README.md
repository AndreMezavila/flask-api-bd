<h1> Simple student registration API. 🖥️ 📕 ⚒️🖨️ </h1>
<h2> versão com um banco de dados local<h2>

<h3> 📕 required: 📕  </h3>

<p>1 install python </p>
<p>2 install git </p>

<h3>⚒️ how to install:⚒️ </h3>

<p>1 choose a path</p>
	<p><strong>cd ~</strong></p>
	<p><strong>mkdir "yournamepath"</strong></p>
<p>2 clone the repository</p>
	<p><strong>git clone https://github.com/AndreMezavila/simple-flask-api.git</strong></p>
<p>3 create a virtual environment </p>
	<p><strong>python -m venv venv </strong></p>
	<p><strong>source venv/bin/activate (activate) </strong></p>
<p>4 install the requirements from the requirements.txt file </p>
	<p><strong>pip install -i requirements.txt </strong></p>
<p>4 installing the local database </p>
	<p><strong>python setup.py </strong></p>


<h3>🖥️ how to test: 🖥️ </h3>

<p><strong>python3 </strong></p>
<p><strong> >>> import requests </strong></p>

<p>1 list students </p>
	<p><strong> requests.get('http://localhost:5000/students).json() </strong></p>
<p>2 list only one student </p>
	<p><strong> requests.get('http://localhost:5000/students/1').json() </strong></p>
<p>3 register a student </p>
	<p><strong> student = {"email": "yourname@exemple.com","name": "yourname","room": 1} </strong></p>
	<p><strong> requests.post('http://localhost:5000/students/1', json=student).json() </strong></p>
<p>4 delete a student </p>
	<p><strong> requests.delete('http://localhost:5000/students/1').json() </strong></p>
<p>5 edit a student </p>
	<p><strong> student = {"email": "yourname@exemple.com","name": "yourname","room": 1} </strong></p>
	<p><strong> requests.put('http://localhost:5000/students/1', json=student).json() </strong></p>
