from flask import Flask, request
#import the prediction algorithm
from elections import runprediction

app = Flask(__name__)
app.config["DEBUG"] = True
inputs = []
result = 0

@app.route("/", methods=["GET", "POST"])
def predictions_page():
#    inputs = []

#for this form, I set all the values for the forms to correspond with the values in the prediction algorithm
#that way I could pass the values directly through as 0 or 1 to the prediction algorithm
#and return the percentage probability
    if request.method == "POST":
        if request.form["action"] == "Calculate":
            #inputs.append[request.form["rwb"].astype(int)]
            #inputs.append[request.form["red"].astype(int)]
            #inputs.append[request.form["other1"].astype(int)]
            #inputs.append[request.form["other2"].astype(int)]
            result = runprediction(int(request.form["rwb"]), int(request.form["red"]), int(request.form["other1"]), int(request.form["other2"]))
            #inputs.clear()
            return '''
                <html>
                <head>
                <title>Election Color Success Predictor</title>
                </head>
                <body style="background-color:#F3EDEA; font-family: Arial, Helvetica, sans-serif; text-align: center; color: #3E4244;">
                        <h1>Your color choices have a {result} percent chance of election success!</h1>
                        <p>This calculation comes from comparison of color palettes from elections spanning over 50 years, with a statistical accuracy (also called Accuracy Under the Curve) of up to 75 percent!
                        With more election data, this prediction can and will improve in the future, and is only meant to be a segment of holistic decision making. UpIncoming Political presents this data for
                        informational purposes only and this prediction does not represent any guarantee of election success</p>
                        <p><img src="/static/auc.jpg"></p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
        <head>
        <title>Election Color Success Predictor</title>
        </head>
        <body style="background-color:#F3EDEA; font-family: Arial, Helvetica, sans-serif; text-align: center; color: #3E4244;">
		<h1>Would Your Colors Get You Elected?</h1>
		<p>Choose your color palette for the American Presidential election!</p>
		<form name="elections" action="." method="POST">
		<p>Do you want to use red, white, and blue as the basis for your logo?</p>
		<label for="rwb">Yes</label>
		<input type="radio" id="rwb" name="rwb" value="1" checked>
		<label for="rwb">No</label>
		<input type="radio" id="rwb" name="rwb" value="0">
		<p>If you are not using red, white, and blue, do you want to use red?</p>
		<label for="red">Already Selected Red, White, and Blue</label>
		<input type="radio" id="red" name="red" value="1" checked>
		<label for="red">Yes</label>
		<input type="radio" id="red" name="red" value="1">
		<label for="red">No</label>
		<input type="radio" id="red" name="red" value="0">
		<p>Do you want to use a different color (black, gold, etc.)?</p>
		<label for="other1">Yes</label>
		<input type="radio" id="other1" name="other1" value="1" checked>
		<label for="other1">No</label>
		<input type="radio" id="other1" name="other1" value="0">
		<p>If you answered yes to the last question, do you want to use more than one different color?</p>
		<label for="other2">Yes</label>
        <input type="radio" id="other2" name="other2" value="1" checked>
        <label for="other2">No</label>
        <input type="radio" id="other2" name="other2" value="0">
        <label for="other2">Not Applicable</label>
        <input type="radio" id="other2" name="other2" value="0"><br>

        <input type="submit" name="action" value="Calculate">
        </form>
        <h2>How do your color choices stack up?</h2>
        <p>Our algorithm examined almost 300 color palette combinations for this project. Among those were almost 200 variations of red, over 200 variations of blue, and almost 100 other colors. Using this data,
        we used an averaging process to examine these color values, and generate graphs of the 5 average colors among all the palettes. How do your campaign color choices stack up to over 50 years of color palettes?</p>
        <p><img src="/static/redvalspie.jpg"></p>
        <p>Cluster of average 5 red values</p>
        <p><img src="/static/bluevalspie.jpg"></p>
        <p>Cluster of average 5 blue values</p>
        <p><img src="/static/other1valspie.jpg"></p>
        <p>Cluster of first set of extra color values</p>
        <p><img src="/static/other2valspie.jpg"></p>
        <p>Cluster of second set of extra color values</p>
        </body>
        </html>
    '''.format()
