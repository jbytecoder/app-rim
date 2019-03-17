import setuptools as st

with open("README.md","r") as f:
  readme = f.read()

st.setup(
  name="app-rim",
  version="0.0.1",
  author="jbytecoder",
  author_email="jbytecoder@gmail.com",
  description="Application Runtime Image Manager",
  long_description=readme,
  long_description_content_type="text/markdown",
  url="https://github.com/jbytecoder/app-rim",
  packages=st.find_packages(),
  classifiers=[
	"Programing Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: Linux",
  ]
)
