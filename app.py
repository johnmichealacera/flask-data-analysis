from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route('/plot')
def plot():
    # create a DataFrame
    data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
    df = pd.DataFrame(data)

    # create a plot
    plt.plot(df['x'], df['y'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('My Plot')
    plt.savefig('plot.png')

    # render a template that displays the plot
    # return render_template('plot.html')
    # render a template that displays the plot and the data
    return render_template('./plot.html', plot_url='/static/plot.png', table=df.to_html())


if __name__ == "__main__":
  app.run(debug=True)

