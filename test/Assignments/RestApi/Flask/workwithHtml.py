from flask import Flask
# from flask_restful import Resource

hey_html = Flask(__name__)

@hey_html.route('/james')
def hello_sir():
   return ("""
           <html>
           <body>
           <h1>Hey, Hello James Bond, Have a nice day with ERRORS!</ha>
           </body>
           </html>""")
if __name__ == "__main__":
    hey_html.run(debug=True)