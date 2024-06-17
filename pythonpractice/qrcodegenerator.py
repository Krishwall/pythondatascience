from flask import Flask,render_template,request
import qrcode
from io import BytesIO
from base64 import b64encode

generator=Flask(__name__)

@generator.route('/')
def home():
    return 'whatever we want'
generator.route('/', methods=['POST'])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')
    img=qrcode.make(data)
    img.save(memory)
    memory.seek(0)

    base64_img="data:image/png;base64,"+b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html',data=base64_img)
if __name__=='__main__':
    generator.run(debug=True)



