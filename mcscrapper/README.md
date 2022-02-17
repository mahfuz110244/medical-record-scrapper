Medical Record Scrapper
Master Branch is the default branch for this Code base.
First clone this code base only then follow the following instrucitons.

1. Clone from git source:
git clone https://github.com/mahfuz110244/medical-record-scrapper.git

2. Get inside medical-record-scrapper folder:
cd medical-record-scrapper/mscrapper

3. Install Virtual Environment if you don't have previously:
sudo apt install python3-venv

4. Create virtual environment inside project folder for python3:
python3 -m venv venv

5. Activate virtual environment:
source bin/activate

6. Install Re-Vera requirements inside virtual environment:
pip3 install -r requirements.txt

7. Finally run the scrap file
python3 scrap.py
python3 scrap_chaldal.py