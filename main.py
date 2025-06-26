from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

# Halaman utama
@app.route('/')
def index():
    return """
    <h1>Sistem Voting Dewan Desa Sukamaju</h1>
    <p><a href="/comment">Beri Komentar</a></p>
    """

# Fitur komentar yang rentan SSTI
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment = request.form.get('comment', '')
        
        # Vulnerable template rendering
        template = f"<h2>Komentar Anda:</h2><p>{comment}</p>"
        return render_template_string(template)
    
    return """
    <form method="POST">
        <h2>Beri Komentar</h2>
        <textarea name="comment" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    """

# Halaman admin (tersembunyi)
@app.route('/admin-secret123')
def admin():
    return "Flag: CTF_FLAG{SST1_Fl4sk_J1nj4_Un5afe}"

if __name__ == '__main__':
    app.run(debug=True)