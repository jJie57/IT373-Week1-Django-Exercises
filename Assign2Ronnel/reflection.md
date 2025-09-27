Setting up the Django development environment was a good learning experience. At first, I ran into a few problems that slowed me down. One big issue was activating the virtual environment in PowerShell on Windows — it showed a script error. I fixed it by running this command:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass,
which let me activate the .venv without any more issues.

I also forgot to run python -m pip install --upgrade pip inside the virtual environment, so I got a warning about pip being out of date. After upgrading pip, that problem was solved. Installing Django and checking its version worked fine after that.

Another small mistake I made was not adding a dot at the end of the django-admin startproject config . command. Because of that, Django made an extra folder, which I didn’t want. Once I fixed the command, the server ran correctly, and I was able to see the Django welcome page in my browser.

Setting up Git was easy because I’ve used it before. I created a private GitHub repo, started a Git repo in my project, made a commit, and pushed it to GitHub.

Overall, this setup teach me to carefully follow instructions, use the right commands for my system, and solve small setup problems quickly.