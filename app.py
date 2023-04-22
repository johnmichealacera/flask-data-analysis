from flask import Flask, render_template, jsonify, send_file
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

@app.route('/team/analysis')
def team():
    data = pd.read_json('teams.json')
    df = pd.DataFrame(data)

    # Filter the rows based on the condition rating > 1600
    filtered_df = df[df['rating'] > 1450]

    # Select only the desired columns for display
    selected_columns = ['name', 'rating', 'wins', 'losses']
    display_df = filtered_df[selected_columns]

    # Set the index to 'name' column
    df = display_df.set_index('name')

    # Create the stacked bar chart
    ax = display_df[['rating', 'wins', 'losses']].plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the title and labels
    ax.set_title('Team Performance')
    ax.set_xlabel('Team Name')
    ax.set_ylabel('Number of Games')

    # Set the x-tick labels to be the team names
    ax.set_xticklabels(df.index, rotation=90)

    # render a template that displays the plot
    # return render_template('plot.html')
    # render a template that displays the plot and the data
    # return render_template('./teams.html', plot_url='/static/team.png', table=display_df.to_html())
    # Convert the DataFrame to a JSON object
    return display_df.to_json()
    # Return the DataFrame as JSON
    # return jsonify(json_df)

@app.route("/stacked_bar_chart")
def stacked_bar_chart():
  data = pd.read_json('teams.json')
  # df = pd.DataFrame(data)
  # Filter the rows based on the condition rating > 1600
  filtered_df = data[data['rating'] > 1450]

  # Select only the desired columns for display
  selected_columns = ['name', 'rating', 'wins', 'losses']
  display_df = filtered_df[selected_columns]

  # Set the index to 'name' column
  df = display_df.set_index('name')

  # Create the stacked bar chart
  ax = df[['rating', 'wins', 'losses']].plot(kind='bar', stacked=True, figsize=(10, 6))

  # Set the title and labels
  ax.set_title('Team Performance')
  ax.set_xlabel('Team Name')
  ax.set_ylabel('Number of Games')

  # Set the x-tick labels to be the team names
  ax.set_xticklabels(df.index, rotation=90)

  # Save the figure to a PNG file
  plt.savefig('stacked_bar_chart.png')

  # Return the PNG file as an image
  return send_file('stacked_bar_chart.png', mimetype='image/png')

if __name__ == "__main__":
  app.run(debug=True)

