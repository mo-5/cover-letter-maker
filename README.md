# Cover Letter Maker

I have developed this application to automate the resume making using a template.

## Installation

Clone repo:
```bash
git clone
cd coverLetterMaker
touch letter.docx
```

## Usage
create a python virtuial env
```bash
pip install virtualenv
virtualenv coverLetterMaker
```
acvtivate for windows:
```bash
. coverLetterMaker/Scripts/activate
```
activate for linux or macos:
```bash
. coverLetterMaker/bin/activate
```
edit the template in your root dir and call it letter.docx
Add the following elements in the template file

{{date}}
{{company_name}}
{{location}}
{{positionName}}
{{jobId}}


run the application
 ```
 python generate.py
 ```
 
[More info on virtual env](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
