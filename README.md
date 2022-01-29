# GRMDS-CrossEntropy
This is a repository containing submissions of team CrossEntropy to the [GRMDS Responsible Investing Dashboard Competition](https://grmds.org/braceImpact)

### Description
This Dashboard display the statistical summary of invested funds and reports for each stock, starting from their usage allocation, type of sustainability investment, and stock growth over time.

### Members
- [Kevin Bennett Haryono](https://github.com/kevinbennetth)
- [Matthew Adrianus Mulyono](https://github.com/Matthew1906)

### Table of Contents:
|Name|Details|
|----|-------|
|[apps](/apps)| Scripts for pages in the dashboard |
|[data-gathering](/data-gathering)| Python scripts used to gather data using [Web Scraping](/data-gathering) with [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)|
|[datasets](/datasets)|Processed datasets used for the dashboard. These datasets are provided by [RMDS](https://grmds.org/)|
|[gathered-dataset](/gathered-dataset)|Datasets scraped using the scripts from [data-gathering](/data-gathering)|
|[dashboard.py](/dashboard.py)| Main code for the dashboard |
|[multiapp.py](/multiapp.py)| Helper code to build the [multi-page](https://github.com/upraneelnihar/streamlit-multiapps) dashboard|
|[requirements.txt](/requirements.txt)|List of required modules to run the dashboard|
|[Working App](https://share.streamlit.io/matthew1906/grmds-crossentropy/main/dashboard.py) | The dashboard, deployed on streamlit |

### Steps of Deployment (in vscode):
1. Clone this repository
2. Set up a virtual environment by typing ```python -m venv env``` in the command line
3. Set your interpreter path to the virtual environment path
4. Download all the dependencies (modules) by typing ```python -m pip install -r requirements.txt```
5. Type ```streamlit run dashboard.py``` in the python (env) command line
6. The application will automatically run by itself, but you can also access them by typing ```localhost:8501``` in your web browser.
