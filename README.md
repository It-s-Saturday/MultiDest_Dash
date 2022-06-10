# MultiDest_Dash
### Deployed at [https://multidest.herokuapp.com/](https://multidest.herokuapp.com/)

<br>

## Setup Guide (Windows)
---


## _1) Cloning the project_

This step can be completed as per user preference. Suggested steps are as follows:

Open any CLI (Terminal, Powershell, Git Bash, etc.)


1) `cd ~`
2) `git clone https://github.com/It-s-Saturday/MultiDest_Dash.git multidest`
3) `cd multidest`

## _2) Installing dependencies_
Be sure you're inside your `multidest/` directory.

1) Run the following:
```
pip install -r requirements.txt
```

## _3) Running the web-app_
While still being in the `multidest/` directory,

1) Run `app.py`
```
python app.py
```
You will see an output similar to:

```
Operation App Init took 0.0059967041015625 seconds
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployme
nt.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8050 (Press CTRL+C to quit)
```
## Notes
- If debugging, ensure that in `app.py`, you have debug set to TRUE:
```
if __name__ == "__main__":
    app.run_server(debug=False)
    # Set to true for debugging, false for production
```
