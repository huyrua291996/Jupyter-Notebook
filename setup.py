from distutils.core import setup
import py2exe


setup(
	console=['webdriver.py'],
	options = {
		'py2exe': {
			'packages': ["os", "linecache"],
			'skip_archive' : True,
			'unbuffered' : True,
			'optimize' : 2
			}
		}
)		
	