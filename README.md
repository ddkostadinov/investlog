# InvestLog ⚡️ [![GitHub](https://img.shields.io/github/license/saadpasta/developer-portfolio?color=blue)](https://github.com/saadpasta/developerFolio/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/saadpasta/developerFolio)](https://github.com/saadpasta/developerFolio/stargazers) [![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors)

## A minimalistic, easy-to-use application for logging and managing investments!

<p align="center">
  <kbd>
<img src="https://user-images.githubusercontent.com/53429438/106779355-e9cd9e80-666c-11eb-9417-8a4b54441bc6.gif"></img>
  </kbd>
</p>

Just change `src/portfolio.js` to get your personal portfolio. Customize portfolio theme by using your own color scheme globally in the `src/_globalColor.scss` file. Feel free to use it as-is or personalize it as much as you want.

If you'd like to **contribute** and make this much better for other users, have a look at [Issues](https://github.com/saadpasta/developerFolio/issues).

Created something awesome for your fork of the portfolio and want to share it? Feel free to open a [pull request](https://github.com/saadpasta/developerFolio/pulls).

To view a live example, **[click here](https://developerfolio.js.org/)**.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

You'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/).

```
python@v3.8.10 or higher
git@2.25.1 or higher
```

## How To Use

From your command line, clone InvestLog and create a virtual environment:

```bash
# Clone this repository
git clone https://github.com/ddkostadinov/investlog.git

# Go into the repository
cd investlog

# Create a virtual environment
python3 -m venv .venv

# Activate it
source ./.venv/bin/activate

# Go into the main project folder
cd investlog

# Setup default environment variables

# For Linux
cp env.example .env
# For Windows
copy env.example .env

# Install dependencies
pip install -r requirements.txt

```

Now lets create a new Django secret key:

```bash
# Open the Python shell in Django:
python manage.py shell

# Import the generator function:
from django.core.management.utils import get_random_secret_key

# Create a new secret key:
print(get_random_secret_key())

# Copy and paste the printed key inside the .env file that you created:
#.env
DJANGO_SECRET_KEY = "[new secret key]"
EMAIL_RECEIVER = ""
EMAIL_SENDER = ""
EMAIL_PASSWORD = ""

# You can exit the shell:
exit()

```

To start the application, create the migrations and run it:

```bash
# Create migrations:
python manage.py makemigrations

# Migrate them:
python manage.py migrate

# Run app:
python manage.py runserver

```

Now you can check your application at [localhost](http://localhost:8000).

## Deployment

When you are done with the setup, you should host your website online.
We highly recommend to read through the [Deploying on GitHub Pages](https://create-react-app.dev/docs/deployment/#github-pages) docs for React.

#### Deploying to GitHub Pages

This section guides you to deploy your portfolio on GitHub pages.

- Navigate to `package.json` and enter your domain name instead of `https://developerfolio.js.org/` in `homepage` variable. For example, if you want your site to be `https://<your-username>.github.io/developerFolio`, add the same to the homepage section of `package.json`.

- In short you can also add `/devloperFolio` to `package.json` as both are exactly same. Upon doing so, you tell `create-react-app` to add the path assets accordingly.

- Optionally, configure the domain. You can configure a custom domain with GitHub Pages by adding a `CNAME` file to the `public/` folder.

- Follow through the guide to setup GitHub pages from the official CRA docs [here](https://create-react-app.dev/docs/deployment/#github-pages).

#### Deploying to Netlify

You could also host directly with Netlify by linking your own repository.

[![Deploy To Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/saadpasta/developerFolio)

For more information, read [hosting on Netlify](https://create-react-app.dev/docs/deployment/#netlify).

## Sections

✔️ Summary and About me\
✔️ Skills\
✔️ Education\
✔️ Work Experience\
✔️ Open Source Projects Connected with GitHub\
✔️ Big Projects\
✔️ Achievements And Certifications 🏆\
✔️ Blogs\
✔️ Talks\
✔️ Podcast\
✔️ Contact me\
✔️ Twitter Timeline\
✔️ GitHub Profile

## Technologies Used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Postgres](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

---
