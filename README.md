# py-coverLetterMaker

I have developed this application to automate the resume making using a template.

## How to use
- Clone the repo
```
git clone
cd coverLetterMaker
touch letter.docx
```
- edit the template in your root dir and call it letter.docx
- Add the following elements in the template file
```
{{date}}
{{company_name}}
{{location}}
{{positionName}}
{{jobId}}
```
- run the application
 ```
 python generate.py
 ```
