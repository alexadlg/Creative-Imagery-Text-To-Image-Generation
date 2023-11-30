from flask import Flask, render_template, request
import your_aws_bedrock_backend_module  # Import your AWS Bedrock backend module here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    
    # Call your AWS Bedrock backend function to generate the image
    generated_image = your_aws_bedrock_backend_module.generate_image(prompt)

    return render_template('result.html', generated_image=generated_image)

if __name__ == '__main__':
    app.run(debug=True)