from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Workers ka data
workers_db = [
    {"name": "Ramesh Kumar", "work": "Plumber", "phone": "9876543210"},
    {"name": "Suresh Yadav", "work": "Electrician", "phone": "9123456789"},
    {"name": "Amit Sharma", "work": "Painter", "phone": "9988776655"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kamgar Network</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; text-align: center; }
        .container { max-width: 500px; background: white; margin: auto; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .worker-card { background: #f8f9fa; border-left: 5px solid #3498db; padding: 15px; margin: 15px 0; text-align: left; border-radius: 4px; }
        .call-btn { display: inline-block; background: #2ecc71; color: white; padding: 8px 15px; text-decoration: none; border-radius: 5px; margin-top: 10px; font-weight: bold; }
        .add-form { margin-top: 30px; border-top: 2px dashed #ddd; padding-top: 20px; text-align: left; }
        input, select { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 5px; }
        button { width: 100%; background: #3498db; color: white; padding: 12px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>👷‍♂️ Kamgar Network</h1>
        <p>Bhopal ke Workers ki Shuruaat</p>
        
        {% for worker in workers %}
        <div class="worker-card">
            <strong>{{ worker.name }}</strong><br>
            <span style="color: #e67e22;">🔧 {{ worker.work }}</span><br>
            📞 {{ worker.phone }}<br>
            <a href="tel:{{ worker.phone }}" class="call-btn">📞 Call Now</a>
        </div>
        {% endfor %}

        <div class="add-form">
            <h3>➕ Naya Worker Jodein</h3>
            <form action="/add" method="POST">
                <input type="text" name="name" placeholder="Worker ka Naam" required>
                <select name="work">
                    <option value="Plumber">Plumber</option>
                    <option value="Electrician">Electrician</option>
                    <option value="Painter">Painter</option>
                    <option value="Carpenter">Carpenter</option>
                </select>
                <input type="tel" name="phone" placeholder="Mobile Number" required>
                <button type="submit">Register Karein</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, workers=workers_db)

@app.route('/add', methods=['POST'])
def add_worker():
    name = request.form.get('name')
    work = request.form.get('work')
    phone = request.form.get('phone')
    if name and phone:
        workers_db.append({"name": name, "work": work, "phone": phone})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
