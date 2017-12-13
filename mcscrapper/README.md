Medical Record Scrapper
Master Branch is the default branch for this Code base.
First clone this code base only then follow the following instrucitons.

1. Clone from git source:
git clone https://github.com/mahfuz110244/medical-record-scrapper.git

2. Get inside medical-record-scrapper folder:
cd medical-record-scrapper/

3. Install Virtual Environment if you don't have previously:
pip install virtualenv

4. Create virtual environment inside odoo for python3.5:
virtualenv -p python3.5 .

5. Activate virtual environment:
source bin/activate

6. Install Re-Vera requirements inside virtual environment:
pip install -r requirements.txt

7. Finally run the scrap file
python scrap.py