from setuptools import setup, find_packages

setup(name="prewikka-apps-helloworld",
      version="4.0.0",
      author="Prelude Team",
      author_email="support.prelude@c-s.fr",
      url="https://www.prelude-siem.org",
      packages=find_packages(),
      install_requires=["prewikka >= 4.0.0"],
      entry_points={
          "prewikka.views": [
              "HelloWorld = helloworld:HelloWorld",
          ],
      },
      package_data={
          "helloworld": [
              "templates/*.mak"
          ],
      },
)
